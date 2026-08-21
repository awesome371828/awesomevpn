require('dotenv').config();
const TelegramBot = require('node-telegram-bot-api');
const axios = require('axios');

const bot = new TelegramBot(process.env.BOT_TOKEN, { polling: true });
const PANEL = process.env.PANEL_URL;
const ADMIN = Number(process.env.ADMIN_ID);

// ===== Каталог тарифов =====
const PLANS = {
  '1m':  { name: '1 месяц',  price: 120, days: 30 },
  '3m':  { name: '3 месяца', price: 300, days: 90 },
  '6m':  { name: '6 месяцев',price: 500, days: 180 },
  '12m': { name: '12 месяцев',price: 900, days: 365 }
};

// Хранилище пользователей (в проде - SQLite)
const users = {}; // chatId -> { balance, keys: [{subUrl, expire}] }

// ===== Панель Remnawave: создать клиента =====
async function createPanelClient(username, days) {
  const { data } = await axios.post(`${PANEL}/api/clients`, {
    username,
    days,
    trafficLimitBytes: 0,
    deviceLimit: 0,
    activateImmediately: true
  }, {
    headers: { 'x-api-token': process.env.API_TOKEN }
  });
  return data;
}

// ===== Панель: получить подписку клиента =====
async function getClientSubscription(username) {
  const { data } = await axios.get(`${PANEL}/api/clients/${username}`, {
    headers: { 'x-api-token': process.env.API_TOKEN }
  });
  return data;
}

// ===== Клавиатура тарифов =====
function plansKeyboard() {
  return {
    inline_keyboard: Object.entries(PLANS).map(([id, p]) => [
      { text: `${p.name} — ${p.price}₽`, callback_data: `buy_${id}` }
    ])
  };
}

// ===== /start =====
bot.onText(/\/start/, async (msg) => {
  const chatId = msg.chat.id;
  if (!users[chatId]) users[chatId] = { balance: 0, keys: [] };

  await bot.sendMessage(chatId,
    '👋 Добро пожаловать в Awesome VPN!\n\n' +
    '⚡ Быстрый и стабильный VPN (Германия)\n' +
    '🛡 Обход блокировок: Telegram, Discord, YouTube\n\n' +
    'Выберите тариф:',
    { reply_markup: plansKeyboard() }
  );
});

// ===== Покупка =====
bot.on('callback_query', async (query) => {
  const chatId = query.message.chat.id;
  const data = query.data;

  if (!users[chatId]) users[chatId] = { balance: 0, keys: [] };
  const user = users[chatId];

  // Выбор тарифа
  if (data.startsWith('buy_')) {
    const planId = data.replace('buy_', '');
    const plan = PLANS[planId];

    await bot.answerCallbackQuery(query.id);
    await bot.sendMessage(chatId,
      `🛒 Тариф: ${plan.name}\n` +
      `💰 Цена: ${plan.price}₽\n` +
      `📅 Срок: ${plan.days} дней\n\n` +
      `💳 Переведите ${plan.price}₽ на карту/крипту и нажмите "Я оплатил".\n\n` +
      `Ваш баланс: ${user.balance}₽`,
      {
        reply_markup: {
          inline_keyboard: [
            [{ text: '✅ Я оплатил', callback_data: `pay_${planId}` }],
            [{ text: '🔙 Назад', callback_data: 'back' }]
          ]
        }
      }
    );
  }

  // Подтверждение оплаты
  if (data.startsWith('pay_')) {
    const planId = data.replace('pay_', '');
    const plan = PLANS[planId];

    if (user.balance >= plan.price) {
      user.balance -= plan.price;

      // Автосоздание клиента и ключа
      try {
        const username = `u${chatId}_${Date.now().toString().slice(-6)}`;
        await bot.answerCallbackQuery(query.id, { text: '⏳ Генерирую ключ...' });
        await createPanelClient(username, plan.days);
        const client = await getClientSubscription(username);

        const subUrl = client.subscriptionUrl || `${PANEL}/sub/${client.uuid}`;

        user.keys.push({ name: plan.name, url: subUrl, expires: Date.now() + plan.days*86400000 });

        await bot.sendMessage(chatId,
          '✅ Оплата получена! Ваш ключ готов:\n\n' +
          '📥 <b>Ссылка-подписка:</b>\n' +
          `<code>${subUrl}</code>\n\n` +
          '🗝 Вставьте её в приложение <b>HAPP</b> или <b>v2rayTun</b>\n' +
          `📅 Действует: ${plan.days} дней\n\n` +
          '💡 Добавьте как «Подписку», чтобы обновлять автоматически.',
          { parse_mode: 'HTML' }
        );
      } catch (e) {
        user.balance += plan.price; // вернуть деньги при ошибке
        console.error(e);
        await bot.sendMessage(chatId, '❌ Ошибка при создании ключа. Попробуйте позже.');
      }
    } else {
      await bot.answerCallbackQuery(query.id);
      await bot.sendMessage(chatId, '❌ Недостаточно средств на балансе.');
    }
  }

  // Мои ключи
  if (data === 'my_keys') {
    await bot.answerCallbackQuery(query.id);
    if (user.keys.length === 0) {
      await bot.sendMessage(chatId, 'У вас пока нет ключей. Купите тариф!');
    } else {
      let txt = '🔑 <b>Ваши ключи:</b>\n\n';
      user.keys.forEach((k, i) => {
        txt += `${i+1}. ${k.name}\n<code>${k.url}</code>\n\n`;
      });
      await bot.sendMessage(chatId, txt, { parse_mode: 'HTML' });
    }
  }

  // Баланс / пополнить
  if (data === 'balance') {
    await bot.answerCallbackQuery(query.id);
    await bot.sendMessage(chatId,
      `💰 Ваш баланс: <b>${user.balance}₽</b>\n\n` +
      'Пополнение вручную через поддержку.',
      { parse_mode: 'HTML' }
    );
  }

  // Назад
  if (data === 'back') {
    await bot.answerCallbackQuery(query.id);
    await bot.sendMessage(chatId, 'Выберите тариф:', { reply_markup: plansKeyboard() });
  }
});

// ===== Меню =====
bot.onText(/\/menu/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, '📋 Главное меню:', {
    reply_markup: {
      inline_keyboard: [
        [{ text: '🛒 Купить VPN', callback_data: 'back' }],
        [{ text: '🔑 Мои ключи', callback_data: 'my_keys' }],
        [{ text: '💰 Баланс', callback_data: 'balance' }],
        [{ text: '🆘 Поддержка', url: 'https://t.me/your_support' }]
      ]
    }
  });
});

// ===== Админ: пополнить баланс =====
bot.onText(/\/add (\d+) (\d+)/, async (msg, match) => {
  if (msg.chat.id !== ADMIN) return;
  const [, userId, amount] = match;
  if (!users[userId]) users[userId] = { balance: 0, keys: [] };
  users[userId].balance += Number(amount);
  await bot.sendMessage(msg.chat.id, `✅ Баланс пользователя ${userId}: ${users[userId].balance}₽`);
});

console.log('🔥 Awesome VPN Bot запущен!');
