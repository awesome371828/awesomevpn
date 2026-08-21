require('dotenv').config();
const TelegramBot = require('node-telegram-bot-api');
const axios = require('axios');
const db = require('./db');

const bot = new TelegramBot(process.env.BOT_TOKEN, { polling: true });
const PANEL = process.env.PANEL_URL;
const ADMIN = Number(process.env.ADMIN_ID);

const MONTH_PRICE = 129;
const PAY_URL = 'https://yoomoney.ru/quickpay/fundraise?billNumber=1JQ48QFUVAK.260821';
const SUPPORT_URL = 'https://t.me/your_support';

function priceFor(m){ return m*MONTH_PRICE; }

// ===== Главная панель =====
async function showPanel(chatId, msgId) {
  const user = await db.getOrCreateUser(chatId);
  const keys = (await db.getKeys(chatId)).filter(k=>k.status==='active'&&k.expires>Date.now());
  let left = '';
  if(keys[0]) left = ` — ещё ${Math.ceil((keys[0].expires-Date.now())/86400000)} дн.`;

  const text =
    `👋 <b>${chatId===ADMIN?'👑 Администратор':'Привет!'}</b>\n\n`+
    `🌐 <b>VPN работает 👌</b>\n`+
    `🔑 Активных ключей: <b>${keys.length}</b>\n`+
    `💰 Баланс: <b>${user.balance}₽</b>${left}\n\n`+
    `📲 <b>Сменил телефон или удалил приложение?</b>\n`+
    `Нажми на ключ ниже или создай новый — пришлём инструкцию заново.`;

  const kb={inline_keyboard:[
    [{text:'🛒 Купить / продлить',callback_data:'buy_menu'}],
    ...keys.map((k,i)=>[{text:`🔑 Ключ ${i+1} · ${k.name}`,callback_data:`key_${k.id}`}]),
    [{text:'➕ Новый ключ',callback_data:'new_key'}],
    [{text:'📥 Мои подписки',callback_data:'my_keys'}],
    [{text:'💰 Баланс',callback_data:'balance'}],
    [{text:'❓ Как подключиться',callback_data:'howto'}],
    [{text:'🆘 Поддержка',url:SUPPORT_URL}],
  ]};
  if(chatId===ADMIN) kb.inline_keyboard.push([{text:'⚙️ Админ-панель',callback_data:'admin'}]);

  if(msgId) return bot.editMessageText(text,{chat_id:chatId,message_id:msgId,parse_mode:'HTML',reply_markup:kb});
  return bot.sendMessage(chatId,text,{parse_mode:'HTML',reply_markup:kb});
}

// ===== Тарифы =====
const monthsKB=()=>({inline_keyboard:[
  [{text:'1 мес · 129₽',callback_data:'buy_1'}],
  [{text:'2 мес · 258₽',callback_data:'buy_2'}],
  [{text:'3 мес · 387₽',callback_data:'buy_3'}],
  [{text:'6 мес · 774₽',callback_data:'buy_6'}],
  [{text:'12 мес · 1548₽',callback_data:'buy_12'}],
  [{text:'🔙 Назад',callback_data:'menu'}]
]});

// ===== Создание клиента в панели =====
async function createClient(username, days){
  const {data}=await axios.post(`${PANEL}/api/clients`,{username,days,trafficLimitBytes:0,deviceLimit:0,activateImmediately:true},{headers:{'x-api-token':process.env.API_TOKEN}});
  return data;
}

bot.onText(/\/start/,async(msg)=>{await db.getOrCreateUser(msg.chat.id);showPanel(msg.chat.id);});
bot.onText(/\/menu/,async(msg)=>{await db.getOrCreateUser(msg.chat.id);showPanel(msg.chat.id);});

bot.on('callback_query',async(q)=>{
  const c=q.message.chat.id,m=q.message.message_id,d=q.data;
  await db.getOrCreateUser(c);

  if(d==='menu')return showPanel(c,m);
  if(d==='buy_menu')return bot.editMessageText(
    '🛒 <b>Выберите на сколько месяцев VPN:</b>\n\nКаждый месяц = +129₽',
    {chat_id:c,message_id:m,parse_mode:'HTML',reply_markup:monthsKB()});

  if(d.startsWith('buy_')){
    const mo=+d.replace('buy_',''),pr=priceFor(mo);
    await db.addPayment(c,pr,mo);
    await bot.answerCallbackQuery(q.id);
    return bot.editMessageText(
      `🛒 <b>${mo} мес. — ${pr}₽</b>\n\n`+
      `💳 Оплатите <b>${pr}₽</b> по кнопке ниже, затем нажмите «Я оплатил».\n\n`+
      `📌 Ключ создастся автоматически после проверки оплаты админом.`,
      {chat_id:c,message_id:m,parse_mode:'HTML',reply_markup:{inline_keyboard:[
        [{text:'💳 Оплатить',url:PAY_URL}],
        [{text:'✅ Я оплатил',callback_data:`paid_${mo}`}],
        [{text:'🔙 Назад',callback_data:'buy_menu'}]
      ]}});
  }

  if(d.startsWith('paid_')){
    const mo=+d.replace('paid_',''),pr=priceFor(mo);
    await bot.answerCallbackQuery(q.id,{text:'⏳ Заявка отправлена админу...'});
    // Уведомляем админа на подтверждение
    await bot.sendMessage(ADMIN,
      `🔔 <b>Новая оплата!</b>\n\n`+
      `👤 Юзер: <code>${c}</code>\n`+
      `🛒 Тариф: ${mo} мес. — ${pr}₽\n\n`+
      `Подтвердить выдачу ключа?`,
      {parse_mode:'HTML',reply_markup:{inline_keyboard:[
        [{text:'✅ Подтвердить',callback_data:`adm_pay_yes_${c}_${mo}`}],
        [{text:'❌ Отклонить',callback_data:`adm_pay_no_${c}`}]
      ]}});
    await bot.sendMessage(c,`📨 Заявка на оплату <b>${pr}₽</b> отправлена. Ожидайте подтверждение.`,{parse_mode:'HTML'});
  }

  // Админ подтверждает оплату
  if(d.startsWith('adm_pay_yes_')){
    if(c!==ADMIN)return;
    const parts=d.split('_'); // adm pay yes <user> <mo>
    const uc=+parts[3], mo=+parts[4];
    await db.addBalance(uc,0);
    // Создаём ключ
    try{
      const uname=`u${uc}_${Date.now().toString().slice(-6)}`;
      const days=mo*30;
      const data=await createClient(uname,days);
      const subUrl=`${PANEL}/sub/${data.uuid}`;
      await db.addKey(uc,`${mo} мес`,subUrl,Date.now()+days*86400000);
      await bot.sendMessage(uc,
        `✅ <b>Оплата подтверждена! Ваш ключ готов</b>\n\n`+
        `📅 ${mo} мес. (${days} дн.)\n\n`+
        `📥 <b>Подписка:</b>\n<code>${subUrl}</code>\n\n`+
        `🗝 Вставьте в <b>HAPP</b>/<b>v2rayTun</b> как «Подписку».`,{parse_mode:'HTML'});
      await bot.answerCallbackQuery(q.id,{text:'Ключ выдан ✅'});
    }catch(e){console.error(e);bot.sendMessage(c,'❌ Ошибка создания ключа');}
  }
  if(d.startsWith('adm_pay_no_')){
    if(c!==ADMIN)return;
    const uc=+d.split('_')[3];
    await bot.sendMessage(uc,'❌ Оплата отклонена. Свяжитесь с поддержкой.');
    await bot.answerCallbackQuery(q.id,{text:'Отклонено'});
  }

  if(d.startsWith('key_')){
    const id=+d.replace('key_','');
    const keys=await db.getKeys(c);
    const k=keys.find(x=>x.id===id);
    if(!k)return bot.answerCallbackQuery(q.id,{text:'Ключ не найден'});
    await bot.answerCallbackQuery(q.id);
    bot.sendMessage(c,
      `🔑 <b>Ключ (${k.name})</b>\n\n`+
      `📥 <b>Подписка:</b>\n<code>${k.url}</code>\n\n`+
      `📅 Истекает: ${new Date(k.expires).toLocaleDateString()}\n`+
      `📌 Статус: ${k.status}\n\nВставьте в HAPP/v2rayTun.`,{parse_mode:'HTML'});
  }

  if(d==='my_keys'){
    const keys=await db.getKeys(c);
    await bot.answerCallbackQuery(q.id);
    if(!keys.length)return bot.sendMessage(c,'У вас пока нет ключей 🛒');
    let t='📥 <b>Ваши подписки:</b>\n\n';
    keys.forEach((k,i)=>t+=`${i+1}. ${k.name} · ${k.status}\n<code>${k.url}</code>\n\n`);
    bot.sendMessage(c,t,{parse_mode:'HTML'});
  }

  if(d==='balance'){
    const u=await db.getUser(c);
    await bot.answerCallbackQuery(q.id);
    bot.sendMessage(c,`💰 <b>Баланс: ${u.balance}₽</b>\n\nПополнение через поддержку.`,{parse_mode:'HTML'});
  }

  if(d==='howto'){
    await bot.answerCallbackQuery(q.id);
    bot.sendMessage(c,
      '❓ <b>Как подключиться:</b>\n\n'+
      '1️⃣ Скачайте <b>HAPP</b> или <b>v2rayTun</b>\n'+
      '2️⃣ «Добавить подписку»\n'+
      '3️⃣ Вставьте ссылку-подписку\n'+
      '4️⃣ Подключитесь 👌',{parse_mode:'HTML'});
  }

  if(d==='new_key'){
    await bot.answerCallbackQuery(q.id);
    bot.sendMessage(c,'Чтобы создать новый ключ — купите тариф 🛒',{reply_markup:{inline_keyboard:[[{text:'🛒 Купить',callback_data:'buy_menu'}]]}});
  }

  // ===== АДМИН =====
  if(d==='admin'){
    if(c!==ADMIN)return;
    await bot.answerCallbackQuery(q.id);
    bot.sendMessage(c,'⚙️ <b>Админ-панель</b>',{parse_mode:'HTML',reply_markup:{inline_keyboard:[
      [{text:'📊 Статистика',callback_data:'ad_stats'}],
      [{text:'💳 Выдать баланс',callback_data:'ad_add'}],
      [{text:'🔻 Забрать баланс',callback_data:'ad_remove'}],
      [{text:'👥 Юзеры',callback_data:'ad_users'}],
      [{text:'🔙 Назад',callback_data:'menu'}]
    ]}});
  }

  if(d==='ad_stats'){
    if(c!==ADMIN)return;
    const users=await db.allUsers();
    let active=0;
    for(const u of users){const k=await db.getKeys(u.chat_id);active+=k.filter(x=>x.status==='active'&&x.expires>Date.now()).length;}
    await bot.answerCallbackQuery(q.id);
    bot.sendMessage(c,`📊 <b>Статистика</b>\n\n👥 Пользователей: ${users.length}\n🔑 Активных ключей: ${active}`,{parse_mode:'HTML'});
  }
  if(d==='ad_add'||d==='ad_remove'){
    if(c!==ADMIN)return;
    await bot.answerCallbackQuery(q.id);
    bot.sendMessage(c,`Используйте команды:\n\n`+
      `💳 Выдать баланс:\n<code>/add &lt;id&gt; &lt;сумма&gt;</code>\n\n`+
      `🔻 Забрать:\n<code>/remove &lt;id&gt; &lt;сумма&gt;</code>\n\n`+
      `🔑 Выдать ключ:\n<code>/givekey &lt;id&gt; &lt;дней&gt;</code>`,{parse_mode:'HTML'});
  }
  if(d==='ad_users'){
    if(c!==ADMIN)return;
    const users=await db.allUsers();
    await bot.answerCallbackQuery(q.id);
    let t='👥 <b>Пользователи:</b>\n\n';
    users.forEach(u=>t+=`<code>${u.chat_id}</code> · ${u.balance}₽\n`);
    bot.sendMessage(c,t,{parse_mode:'HTML'});
  }
});

// ===== Админ текстовые команды =====
bot.onText(/\/add (\d+) (\d+)/,async(msg,match)=>{
  if(msg.chat.id!==ADMIN)return;
  const[,id,amount]=match;
  await db.getOrCreateUser(+id);await db.addBalance(+id,+amount);
  bot.sendMessage(msg.chat.id,`✅ Выдано ${amount}₽ юзеру ${id}`);
});
bot.onText(/\/remove (\d+) (\d+)/,async(msg,match)=>{
  if(msg.chat.id!==ADMIN)return;
  const[,id,amount]=match;
  const u=await db.getUser(+id);const nb=Math.max(0,u.balance-+amount);
  await db.setBalance(+id,nb);
  bot.sendMessage(msg.chat.id,`🔻 Баланс юзера ${id}: ${nb}₽`);
});
bot.onText(/\/givekey (\d+) (\d+)/,async(msg,match)=>{
  if(msg.chat.id!==ADMIN)return;
  const[,id,days]=match;
  await db.getOrCreateUser(+id);
  try{
    const uname=`admin_${Date.now().toString().slice(-6)}`;
    const data=await createClient(uname,+days);
    const sub=`${PANEL}/sub/${data.uuid}`;
    await db.addKey(+id,'выданный',sub,Date.now()+(+days)*86400000);
    bot.sendMessage(msg.chat.id,`🔑 Ключ выдан юзеру ${id} на ${days} дн.\n<code>${sub}</code>`,{parse_mode:'HTML'});
  }catch(e){bot.sendMessage(msg.chat.id,'❌ '+e.message);}
});
bot.onText(/\/stats/,async(msg)=>{
  if(msg.chat.id!==ADMIN)return;
  const users=await db.allUsers();let active=0;
  for(const u of users){const k=await db.getKeys(u.chat_id);active+=k.filter(x=>x.status==='active'&&x.expires>Date.now()).length;}
  bot.sendMessage(msg.chat.id,`📊 Пользователей: ${users.length}\n🔑 Активных ключей: ${active}`);
});

console.log('🔥 Awesome VPN Bot запущен!');
