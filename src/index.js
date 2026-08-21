require('dotenv').config();
const TelegramBot = require('node-telegram-bot-api');
const axios = require('axios');

const bot = new TelegramBot(process.env.BOT_TOKEN, { polling: true });
const PANEL = process.env.PANEL_URL;
const ADMIN = Number(process.env.ADMIN_ID);

const MONTH_PRICE = 129;
const PAY_URL = 'https://yoomoney.ru/quickpay/fundraise?billNumber=1JQ48QFUVAK.260821';
const SUPPORT_URL = 'https://t.me/flidges';

// ===== База (в проде - SQLite/PostgreSQL) =====
const db = {}; // chatId -> { balance, keys: [{name,url,expires,status}] }

function priceFor(months) { return months * MONTH_PRICE; }

// ===== Панель пользователя =====
async function showPanel(chatId, msgId) {
  const user = db[chatId] || { balance: 0, keys: [] };
  const active = user.keys.filter(k => k.status === 'active' && k.expires > Date.now());
  let firstLeft = '';
  if (active[0]) firstLeft = ` — ещё ${Math.ceil((active[0].expires-Date.now())/86400000)} дней`;

  const text =
    `👋 <b>${chatId === ADMIN ? '👑 Администратор' : 'Привет!'}</b>\n\n` +
    `🌐 <b>VPN работает 👌</b>\n` +
    `🔑 Активных ключей: <b>${active.length}</b>\n` +
    `💰 Баланс: <b>${user.balance}₽</b>${firstLeft}\n\n` +
    `📲 <b>Сменил телефон или удалил приложение?</b>\n` +
    `Нажми на нужный ключ ниже или создай новый — пришлём инструкцию заново.`;

  const kb = {
    inline_keyboard: [
      [{ text: '🛒 Купить / продлить VPN', callback_data: 'buy_menu' }],
      ...active.map((k,i)=>[{ text:`🔑 Ключ ${i+1} · ${k.name}`, callback_data:`key_${i}` }]),
      [{ text:'➕ Создать новый ключ', callback_data:'new_key' }],
      [{ text:'📥 Мои подписки', callback_data:'my_keys' }],
      [{ text:'💰 Пополнить баланс', callback_data:'balance' }],
      [{ text:'❓ Как подключиться', callback_data:'howto' }],
      [{ text:'🆘 Поддержка', url: SUPPORT_URL }]
    ]
  };
  if (chatId === ADMIN) kb.inline_keyboard.push([{ text:'⚙️ Админ-панель', callback_data:'admin' }]);

  if (msgId) return bot.editMessageText(text,{chat_id:chatId,message_id:msgId,parse_mode:'HTML',reply_markup:kb});
  return bot.sendMessage(chatId,text,{parse_mode:'HTML',reply_markup:kb});
}

// ===== Тарифы =====
const monthsKB = () => ({
  inline_keyboard:[
    [{text:'1 мес · 129₽',callback_data:'buy_1'}],
    [{text:'2 мес · 258₽',callback_data:'buy_2'}],
    [{text:'3 мес · 387₽',callback_data:'buy_3'}],
    [{text:'6 мес · 774₽',callback_data:'buy_6'}],
    [{text:'12 мес · 1548₽',callback_data:'buy_12'}],
    [{text:'🔙 Назад',callback_data:'menu'}]
  ]
});

// ===== /start =====
bot.onText(/\/start/, async (msg)=>{ if(!db[msg.chat.id]) db[msg.chat.id]={balance:0,keys:[]}; showPanel(msg.chat.id); });
bot.onText(/\/menu/, (msg)=>showPanel(msg.chat.id));

// ===== Callback =====
bot.on('callback_query', async (q)=>{
  const c=q.message.chat.id, m=q.message.message_id, d=q.data;
  if(!db[c]) db[c]={balance:0,keys:[]};
  const u=db[c];

  if(d==='menu') return showPanel(c,m);
  if(d==='buy_menu') return bot.editMessageText(
    '🛒 <b>Выберите на сколько месяцев:</b>\n\nКаждый месяц +129₽',
    {chat_id:c,message_id:m,parse_mode:'HTML',reply_markup:monthsKB()});

  if(d.startsWith('buy_')){
    const mo=+d.replace('buy_',''), pr=priceFor(mo);
    await bot.answerCallbackQuery(q.id);
    return bot.editMessageText(
      `🛒 <b>${mo} мес. — ${pr}₽</b>\n\n`+
      `💳 Оплатите <b>${pr}₽</b> по кнопке ниже, затем нажмите «Я оплатил».\n\n`+
      `📌 Ключ создастся автоматически после подтверждения.`,
      {chat_id:c,message_id:m,parse_mode:'HTML',reply_markup:{
        inline_keyboard:[
          [{text:'💳 Оплатить',url:PAY_URL}],
          [{text:'✅ Я оплатил',callback_data:`paid_${mo}`}],
          [{text:'🔙 Назад',callback_data:'buy_menu'}]
        ]}});
  }

  if(d.startsWith('paid_')){
    const mo=+d.replace('paid_',''), pr=priceFor(mo);
    await bot.answerCallbackQuery(q.id,{text:'⏳ Создаю ключ...'});
    try{
      const uname=`u${c}_${Date.now().toString().slice(-6)}`;
      const days=mo*30;
      const {data}=await axios.post(`${PANEL}/api/clients`,{username:uname,days,trafficLimitBytes:0,deviceLimit:0,activateImmediately:true},{headers:{'x-api-token':process.env.API_TOKEN}});
      const subUrl=`${PANEL}/sub/${data.uuid}`;
      u.keys.push({name:`${mo} мес`,url:subUrl,expires:Date.now()+days*86400000,status:'active'});
      await bot.sendMessage(c,
        `✅ <b>Оплата получена! Ваш ключ готов</b>\n\n`+
        `📅 <b>${mo} мес. (${days} дн.)</b>\n\n`+
        `📥 <b>Подписка:</b>\n<code>${subUrl}</code>\n\n`+
        `🗝 Вставьте в <b>HAPP</b>/<b>v2rayTun</b> как «Подписку».`,
        {parse_mode:'HTML'});
      showPanel(c);
    }catch(e){console.error(e);bot.sendMessage(c,'❌ Ошибка создания ключа. Напишите поддержке.');}
  }

  if(d.startsWith('key_')){
    const i=+d.replace('key_',''); const k=u.keys[i];
    if(!k) return bot.answerCallbackQuery(q.id,{text:'Ключ не найден'});
    await bot.answerCallbackQuery(q.id);
    bot.sendMessage(c,
      `🔑 <b>Ключ ${i+1} (${k.name})</b>\n\n`+
      `📥 <b>Подписка:</b>\n<code>${k.url}</code>\n\n`+
      `📅 Истекает: ${new Date(k.expires).toLocaleDateString()}\n`+
      `📌 Статус: ${k.status}\n\n`+
      'Вставьте в HAPP / v2rayTun как «Подписку».',{parse_mode:'HTML'});
  }

  if(d==='my_keys'){
    await bot.answerCallbackQuery(q.id);
    if(!u.keys.length) return bot.sendMessage(c,'У вас пока нет ключей. Купите тариф!');
    let t='📥 <b>Ваши подписки:</b>\n\n';
    u.keys.forEach((k,i)=>t+=`${i+1}. ${k.name} · ${k.status}\n<code>${k.url}</code>\n\n`);
    bot.sendMessage(c,t,{parse_mode:'HTML'});
  }

  if(d==='balance'){
    await bot.answerCallbackQuery(q.id);
    bot.sendMessage(c,`💰 <b>Баланс: ${u.balance}₽</b>\n\nПополнение через поддержку.`,{parse_mode:'HTML'});
  }

  if(d==='howto'){
    await bot.answerCallbackQuery(q.id);
    bot.sendMessage(c,
      '❓ <b>Как подключиться:</b>\n\n'+
      '1️⃣ Скачайте приложение <b>HAPP</b> или <b>v2rayTun</b>\n'+
      '2️⃣ Нажмите «Добавить подписку»\n'+
      '3️⃣ Вставьте свою ссылку-подписку\n'+
      '4️⃣ Подключитесь и пользуйтесь 👌',{parse_mode:'HTML'});
  }

  if(d==='new_key'){
    await bot.answerCallbackQuery(q.id);
    bot.sendMessage(c,'Чтобы создать новый ключ — купите тариф 🛒',{reply_markup:{inline_keyboard:[[{text:'🛒 Купить',callback_data:'buy_menu'}]]}});
  }

  // ===== АДМИН ПАНЕЛЬ =====
  if(d==='admin'){
    if(c!==ADMIN) return;
    await bot.answerCallbackQuery(q.id);
    bot.sendMessage(c,'⚙️ <b>Админ-панель</b>',{parse_mode:'HTML',reply_markup:{
      inline_keyboard:[
        [{text:'📊 Статистика',callback_data:'ad_stats'}],
        [{text:'💳 Выдать баланс',callback_data:'ad_add'}],
        [{text:'🔻 Забрать баланс',callback_data:'ad_remove'}],
        [{text:'🔑 Выдать ключ',callback_data:'ad_givekey'}],
        [{text:'👥 Список юзеров',callback_data:'ad_users'}],
        [{text:'🔙 Назад',callback_data:'menu'}]
      ]}});
  }

  if(d==='ad_stats'){
    if(c!==ADMIN)return;
    const total=Object.keys(db).length;
    const active=Object.values(db).reduce((a,u)=>a+u.keys.filter(k=>k.status==='active'&&k.expires>Date.now()).length,0);
    await bot.answerCallbackQuery(q.id);
    bot.sendMessage(c,`📊 <b>Статистика</b>\n\n👥 Пользователей: ${total}\n🔑 Активных ключей: ${active}`,{parse_mode:'HTML'});
  }
});

// ===== Админ команды через текст =====
bot.onText(/\/add (\d+) (\d+)/,async(msg,match)=>{
  if(msg.chat.id!==ADMIN)return;
  const[,id,amount]=match;
  if(!db[id])db[id]={balance:0,keys:[]};
  db[id].balance+=+amount;
  bot.sendMessage(msg.chat.id,`✅ Выдано ${amount}₽ юзеру ${id}. Баланс: ${db[id].balance}₽`);
});
bot.onText(/\/remove (\d+) (\d+)/,async(msg,match)=>{
  if(msg.chat.id!==ADMIN)return;
  const[,id,amount]=match;
  if(!db[id])db[id]={balance:0,keys:[]};
  db[id].balance=Math.max(0,db[id].balance-+amount);
  bot.sendMessage(msg.chat.id,`🔻 У юзера ${id} баланс: ${db[id].balance}₽`);
});
bot.onText(/\/givekey (\d+) (\d+)/,async(msg,match)=>{
  if(msg.chat.id!==ADMIN)return;
  const[,id,days]=match;
  if(!db[id])db[id]={balance:0,keys:[]};
  const uname=`admin_${Date.now().toString().slice(-6)}`;
  try{
    const {data}=await axios.post(`${PANEL}/api/clients`,{username:uname,days:+days,trafficLimitBytes:0,deviceLimit:0,activateImmediately:true},{headers:{'x-api-token':process.env.API_TOKEN}});
    const sub=`${PANEL}/sub/${data.uuid}`;
    db[id].keys.push({name:`выданный`,url:sub,expires:Date.now()+(+days)*86400000,status:'active'});
    bot.sendMessage(msg.chat.id,`🔑 Ключ выдан юзеру ${id} на ${days} дн.\n<code>${sub}</code>`,{parse_mode:'HTML'});
  }catch(e){bot.sendMessage(msg.chat.id,'❌ Ошибка: '+e.message);}
});
bot.onText(/\/stats/,async(msg)=>{
  if(msg.chat.id!==ADMIN)return;
  const total=Object.keys(db).length;
  const active=Object.values(db).reduce((a,u)=>a+u.keys.filter(k=>k.status==='active'&&k.expires>Date.now()).length,0);
  bot.sendMessage(msg.chat.id,`📊 Пользователей: ${total}\n🔑 Активных ключей: ${active}`);
});

console.log('🔥 Awesome VPN Bot запущен!');
