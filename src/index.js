require('dotenv').config();
const TelegramBot = require('node-telegram-bot-api');
const axios = require('axios');

const bot = new TelegramBot(process.env.BOT_TOKEN, { polling: true });
const PANEL = process.env.PANEL_URL;
const ADMIN = Number(process.env.ADMIN_ID);

// ===== Цена за месяц =====
const MONTH_PRICE = 129;

// ===== Тарифы (авто-рост цены) =====
function getPlanPrice(months) {
  return months * MONTH_PRICE;
}

// ===== База данных (в проде - SQLite/PostgreSQL) =====
const db = {}; // chatId -> { balance, keys: [{url, expires}] }

// ===== Клавиатура выбора месяцев =====
function monthsKeyboard() {
  return {
    inline_keyboard: [
      [{ text: '1 месяц — 129₽', callback_data: 'buy_1' }],
      [{ text: '2 месяца — 258₽', callback_data: 'buy_2' }],
      [{ text: '3 месяца — 387₽', callback_data: 'buy_3' }],
      [{ text: '6 месяцев — 774₽', callback_data: 'buy_6' }],
      [{ text: '12 месяцев — 1548₽', callback_data: 'buy_12' }],
      [{ text: '🔙 В меню', callback_data: 'menu' }]
    ]
  };
}

// ===== Панель пользователя (главный экран) =====
async function showUserPanel(chatId, msgId) {
  const user = db[chatId] || { balance: 0, keys: [] };
  const activeKeys = user.keys.filter(k => k.expires > Date.now());

  let text =
    `👋 <b>${/* имя пользователя */ 'Добро пожаловать'}</b>\n\n` +
    `🌐 VPN работает 👌\n` +
    `🔑 Активных ключей: <b>${activeKeys.length}</b>\n` +
    `💰 Баланс: <b>${user.balance}₽</b>` +
    (activeKeys[0] ? ` — ещё ${Math.ceil((activeKeys[0].expires-Date.now())/86400000)} дней` : '') +
    `\n\n` +
    `📲 <b>Сменил телефон или удалил приложение?</b>\n` +
    `Нажми на нужный ключ ниже или создай новый — пришлём инструкцию заново.`;

  const keyboard = {
    inline_keyboard: [
      [{ text: '🛒 Купить / продлить VPN', callback_data: 'buy_menu' }],
      ...activeKeys.map((k, i) => [
        { text: `🔑 Ключ ${i+1} (${k.name})`, callback_data: `key_${i}` }
      ]),
      [{ text: '➕ Создать новый ключ', callback_data: 'new_key' }],
      [{ text: '📥 Мои подписки', callback_data: 'my_keys' }],
      [{ text: '💰 Пополнить баланс', callback_data: 'balance' }],
      [{ text: '🆘 Поддержка', url: 'https://t.me/your_support' }]
    ]
  };

  if (msgId) await bot.editMessageText(text, { chat_id: chatId, message_id: msgId, parse_mode: 'HTML', reply_markup: keyboard });
  else await bot.sendMessage(chatId, text, { parse_mode: 'HTML', reply_markup: keyboard });
}

// ===== /start =====
bot.onText(/\/start/, async (msg) => {
  const chatId = msg.chat.id;
  if (!db[chatId]) db[chatId] = { balance: 0, keys: [] };
  await showUserPanel(chatId);
});

// ===== /menu =====
bot.onText(/\/menu/, (msg) => showUserPanel(msg.chat.id));

// ===== Callback =====
bot.on('callback_query', async (query) => {
  const chatId = query.message.chat.id;
  const msgId = query.message.message_id;
  const data = query.data;

  if (!db[chatId]) db[chatId] = { balance: 0, keys: [] };
  const user = db[chatId];

  // Меню
  if (data === 'menu') return showUserPanel(chatId, msgId);

  // Меню покупки
  if (data === 'buy_menu') {
    await bot.answerCallbackQuery(query.id);
    return bot.editMessageText(
      '🛒 <b>Выберите на сколько месяцев хотите VPN:</b>\n\n' +
      'Каждый месяц = +129₽',
      { chat_id: chatId, message_id: msgId, parse_mode: 'HTML', reply_markup: monthsKeyboard() }
    );
  }

  // Покупка
  if (data.startsWith('buy_')) {
    const months = Number(data.replace('buy_', ''));
    const price = getPlanPrice(months);
    await bot.answerCallbackQuery(query.id);
    return bot.editMessageText(
      `🛒 <b>Тариф: ${months} мес. — ${price}₽</b>\n\n` +
      `💳 Оплата на карту: переведите <b>${price}₽</b>\n` +
      `по ссылке ниже, затем нажмите «Я оплатил».\n\n` +
      `📌 После оплаты ключ создастся автоматически.`,
      {
        chat_id: chatId, message_id: msgId, parse_mode: 'HTML',
        reply_markup: {
          inline_keyboard: [
            [{ text: '💳 Оплатить', url: 'https://yoomoney.ru/to/ВАШ_КОШЕЛЕК' }],
            [{ text: '✅ Я оплатил', callback_data: `paid_${months}` }],
            [{ text: '🔙 Назад', callback_data: 'buy_menu' }]
          ]
        }
      }
    );
  }

  // Подтверждение оплаты
  if (data.startsWith('paid_')) {
    const months = Number(data.replace('paid_', ''));
    const price = getPlanPrice(months);

    await bot.answerCallbackQuery(query.id, { text: '⏳ Проверяю и создаю ключ...' });

    // Здесь должна быть реальная проверка оплаты!
    // Пока имитируем успех и выдаём ключ
    try {
      const username = `u${chatId}_${Date.now().toString().slice(-6)}`;
      const days = months * 30;

      // Создание клиента в панели Remnawave
      const { data } = await axios.post(`${PANEL}/api/clients`, {
        username, days, trafficLimitBytes: 0, deviceLimit: 0, activateImmediately: true
      }, { headers: { 'x-api-token': process.env.API_TOKEN } });

      const subUrl = `${PANEL}/sub/${data.uuid}`;

      user.keys.push({ name: `${months} мес`, url: subUrl, expires: Date.now() + days*86400000 });

      await bot.sendMessage(chatId,
        '✅ <b>Оплата получена! Ваш ключ готов</b>\n\n' +
        `📅 <b>${months} мес. (${days} дней)</b>\n\n` +
        `📥 <b>Подписка:</b>\n<code>${subUrl}</code>\n\n` +
        '🗝 Вставьте в приложение <b>HAPP</b> или <b>v2rayTun</b> как «Подписку».\n\n' +
        '💡 В главном меню вы всегда сможете вернуть свой ключ.',
        { parse_mode: 'HTML' }
      );
      await showUserPanel(chatId);
    } catch (e) {
      console.error(e);
      await bot.sendMessage(chatId, '❌ Ошибка при создании ключа. Напишите поддержке.');
    }
  }

  // Показать конкретный ключ
  if (data.startsWith('key_')) {
    const idx = Number(data.replace('key_', ''));
    const key = user.keys[idx];
    if (!key) return bot.answerCallbackQuery(query.id, { text: 'Ключ не найден' });
    await bot.answerCallbackQuery(query.id);
    await bot.sendMessage(chatId,
      `🔑 <b>Ключ ${idx+1} (${key.name})</b>\n\n` +
      `📥 <b>Подписка:</b>\n<code>${key.url}</code>\n\n` +
      `📅 Истекает: ${new Date(key.expires).toLocaleDateString()}\n\n` +
      'Вставьте в HAPP / v2rayTun как «Подписку».',
      { parse_mode: 'HTML' }
    );
  }

  // Мои подписки
  if (data === 'my_keys') {
    await bot.answerCallbackQuery(query.id);
    if (user.keys.length === 0) {
      return bot.sendMessage(chatId, 'У вас пока нет ключей. Купите тариф!');
    }
    let txt = '📥 <b>Ваши подписки:</b>\n\n';
    user.keys.forEach((k, i) => {
      txt += `${i+1}. ${k.name}\n<code>${k.url}</code>\n\n`;
    });
    await bot.sendMessage(chatId, txt, { parse_mode: 'HTML' });
  }

  // Баланс
  if (data === 'balance') {
    await bot.answerCallbackQuery(query.id);
    await bot.sendMessage(chatId,
      `💰 <b>Баланс: ${user.balance}₽</b>\n\n` +
      'Пополнение через поддержку или перевод на карту.',
      { parse_mode: 'HTML' }
    );
  }
});

// ===== Админ: пополнение баланса /add <id> <сумма> =====
bot.onText(/\/add (\d+) (\d+)/, async (msg, match) => {
  if (msg.chat.id !== ADMIN) return;
  const [, userId, amount] = match;
  if (!db[userId]) db[userId] = { balance: 0, keys: [] };
  db[userId].balance += Number(amount);
  await bot.sendMessage(msg.chat.id, `✅ Баланс ${userId}: ${db[userId].balance}₽`);
});

// ===== Админ: статистика =====
bot.onText(/\/stats/, async (msg) => {
  if (msg.chat.id !== ADMIN) return;
  const totalUsers = Object.keys(db).length;
  const activeKeys = Object.values(db).reduce((a,u) => a + u.keys.filter(k=>k.expires>Date.now()).length, 0);
  await bot.sendMessage(msg.chat.id, `📊 Всего пользователей: ${totalUsers}\n🔑 Активных ключей: ${activeKeys}`);
});

console.log('🔥 Awesome VPN Bot запущен!');
