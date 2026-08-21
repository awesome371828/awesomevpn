const TelegramBot = require('node-telegram-bot-api');

const TOKEN = process.env.BOT_TOKEN; // токен из переменной окружения
const bot = new TelegramBot(TOKEN, { polling: true });

// Каталог тарифов
const PLANS = {
  '1_месяц': { price: 120, days: 30 },
  '3_месяца': { price: 300, days: 90 },
  '6_месяцев': { price: 500, days: 180 }
};

// Здесь будут храниться ключи клиентов (в реальности — в БД)
const issuedKeys = {};

bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId,
    '👋 Добро пожаловать в Awesome VPN!\n\n' +
    'Выберите тариф для покупки:',
    {
      reply_markup: {
        inline_keyboard: [
          [{ text: '🌐 1 месяц — 120₽', callback_data: 'plan_1_месяц' }],
          [{ text: '🌐 3 месяца — 300₽', callback_data: 'plan_3_месяца' }],
          [{ text: '🌐 6 месяцев — 500₽', callback_data: 'plan_6_месяцев' }]
        ]
      }
    }
  );
});

bot.on('callback_query', async (query) => {
  const chatId = query.message.chat.id;
  const data = query.data;

  if (data.startsWith('plan_')) {
    const plan = data.replace('plan_', '');
    const info = PLANS[plan];

    await bot.answerCallbackQuery(query.id);
    await bot.sendMessage(chatId,
      `Вы выбрали: ${plan}\n` +
      `Срок: ${info.days} дней\n` +
      `Цена: ${info.price}₽\n\n` +
      `⚠️ Для оплаты переведите ${info.price}₽ и нажмите "Я оплатил".`,
      {
        reply_markup: {
          inline_keyboard: [
            [{ text: '✅ Я оплатил', callback_data: `paid_${plan}` }],
            [{ text: '🔙 Назад', callback_data: 'back' }]
          ]
        }
      }
    );
  }

  if (data.startsWith('paid_')) {
    const plan = data.replace('paid_', '');
    // Здесь должна быть проверка платежа!
    // Пока просто выдаём тестовый ключ

    const key = 'vless://ВАШ_КЛЮЧ_ЗДЕСЬ#' + plan;

    await bot.answerCallbackQuery(query.id);
    await bot.sendMessage(chatId,
      '✅ Оплата получена!\n\n' +
      '🔑 Ваш ключ VPN:\n' +
      '`' + key + '`\n\n' +
      'Вставьте его в приложение HAPP или v2rayTun.\n' +
      `Срок: ${PLANS[plan].days} дней.`,
      { parse_mode: 'Markdown' }
    );
  }

  if (data === 'back') {
    await bot.sendMessage(chatId, 'Выберите тариф:', {
      reply_markup: {
        inline_keyboard: [
          [{ text: '🌐 1 месяц — 120₽', callback_data: 'plan_1_месяц' }],
          [{ text: '🌐 3 месяца — 300₽', callback_data: 'plan_3_месяца' }],
          [{ text: '🌐 6 месяцев — 500₽', callback_data: 'plan_6_месяцев' }]
        ]
      }
    });
  }
});

console.log('Awesome VPN Bot запущен!');
