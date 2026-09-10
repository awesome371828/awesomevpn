import os
from flask import Flask

app = Flask(__name__)

# ================== ТВОИ ДАННЫЕ ==================
SITE_NAME = "Awesome VPN"
BOT = "https://t.me/awesomeproxyvpn_bot"
SUPPORT_BOT = "https://t.me/flidges"
EMAIL = "ffdfdfd44242ddd@gmail.com"
SITE_URL = "awesomevpn.relaxdev.ru"
OPERATOR = "AWESOME VPN LTE"
OP_COUNTRY = "Germany"
BOT_USERNAME = "awesomeproxyvpn_bot"
# ================================================

def R(t):
    return (t
        .replace("__SITE__", SITE_NAME)
        .replace("__BOT__", BOT)
        .replace("__SUPPORT__", SUPPORT_BOT)
        .replace("__EMAIL__", EMAIL)
        .replace("__URL__", SITE_URL)
        .replace("__OPERATOR__", OPERATOR)
        .replace("__OPC__", OP_COUNTRY)
        .replace("__BOTU__", BOT_USERNAME)
    )

def countries_html():
    items = [
        ("🇫🇮","Финляндия"),("🇵🇱","Польша"),("🇩🇪","Германия"),
        ("🇳🇱","Нидерланды"),("🇬🇧","Великобритания"),("🇺🇸","США"),
        ("🇫🇷","Франция"),("🇸🇪","Швеция")]
    out = ""
    for fl, nm in items:
        out += '<div class="country"><span class="fl">'+fl+'</span><span class="nm">'+nm+'</span><span class="dot"></span></div>'
    return out

def apps_html():
    items = [
        ("📱","iOS","Happ · Streisand · Shadowrocket"),
        ("🤖","Android","Happ · v2rayTun · Hiddify"),
        ("🖥","Windows","Hiddify · v2rayN"),
        ("💻","macOS","Happ · Hiddify · FoXray"),
        ("📺","Android TV","Happ")]
    out = ""
    for k, t, d in items:
        out += '<div class="card"><div class="k">'+k+'</div><h3>'+t+'</h3><p>'+d+'</p></div>'
    return out

def guarantee_html():
    out = ""
    items = [
        ("🚀","Высокая скорость","Оптимизированные серверы без ограничений по трафику."),
        ("🛡","Военное шифрование","AES-256 защищает данные на любых сетях."),
        ("🌍","8 стран мира","Финляндия, Польша, Германия, Нидерланды и другие."),
        ("🔒","Без логов","Мы не храним историю ваших подключений."),
        ("📱","Все устройства","iOS, Android, Windows, macOS, Android TV."),
        ("⚡","Один клик","Подключение за секунду без сложных настроек."),
        ("📶","Безлимит трафика","Нет лимитов на скорость и объём данных."),
        ("🔄","Автопереключение","При обрыве соединение восстанавливается автоматически.")]
    for k, t, d in items:
        out += '<div class="card"><div class="k">'+k+'</div><h3>'+t+'</h3><p>'+d+'</p></div>'
    return out

HEAD = """<style>
:root{--bg:#0a0c1e;--card:#121430;--line:#2a2f56;--txt:#f0f2ff;--mut:#9ba2cf;
--gr1:#7c5cff;--gr2:#22d3ee;--ok:#25e08a}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
/* анимированный градиентный фон (без наложений) */
body{color:var(--txt);font-family:Arial,Helvetica,sans-serif;overflow-x:hidden;
background:linear-gradient(120deg,#0a0c1e,#131a3a,#0d1026,#1a1033,#0a0c1e);
background-size:400% 400%;animation:bgMove 20s ease infinite}
@keyframes bgMove{50%{background-position:100% 50%}}
a{color:inherit;text-decoration:none}
.wrap{max-width:1160px;margin:0 auto;padding:0 22px}

/* nav */
nav{position:sticky;top:0;z-index:50;background:#0a0c1e;border-bottom:1px solid var(--line)}
.nav-in{display:flex;align-items:center;gap:22px;padding:15px 22px;max-width:1160px;margin:0 auto}
.logo{display:flex;align-items:center;gap:11px;font-weight:800;font-size:20px}
.logo-badge{width:38px;height:38px;border-radius:12px;background:linear-gradient(135deg,var(--gr1),var(--gr2));display:flex;align-items:center;justify-content:center;box-shadow:0 0 18px #7c5cff66;animation:pulse 2.5s infinite}
.logo-badge span{background:#0a0c1e;border-radius:9px;width:30px;height:30px;display:flex;align-items:center;justify-content:center;font-size:17px}
@keyframes pulse{50%{box-shadow:0 0 34px #22d3ee88}}
.menu{display:flex;gap:20px;margin-left:auto}
.menu a{color:var(--mut);font-size:14.5px;transition:.2s}
.menu a:hover{color:#fff}
@media(max-width:760px){.menu{display:none}}

h2{font-size:clamp(26px,4vw,38px);font-weight:800;margin-bottom:12px;color:#fff}
.hl{color:var(--gr2)}
.sub{color:var(--mut);max-width:640px;margin:0 auto 36px;font-size:16px}
section{padding:72px 0}
.center{text-align:center}

/* hero */
.hero{padding:100px 0 80px}
.hero h1{font-size:clamp(36px,6vw,62px);font-weight:900;line-height:1.08;margin-bottom:22px;color:#fff}
.hero p{color:var(--mut);font-size:19px;max-width:620px;margin:0 auto 32px}
.hero-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.cta{display:inline-flex;align-items:center;gap:10px;padding:16px 36px;border-radius:16px;background:linear-gradient(90deg,var(--gr1),var(--gr2));font-weight:800;font-size:17px;box-shadow:0 0 26px #7c5cff66;transition:.25s;cursor:pointer;border:none;color:#fff}
.cta:hover{transform:translateY(-4px) scale(1.03);box-shadow:0 0 44px #22d3ee99}
.cta.ghost{background:transparent;border:1px solid var(--line)}
.cta.ghost:hover{border-color:var(--gr2)}
.pill{display:inline-flex;gap:8px;align-items:center;padding:9px 18px;border-radius:999px;border:1px solid var(--line);background:#121430cc;color:var(--mut);font-size:13.5px;margin-bottom:24px}
.pill b{color:var(--ok)}

.grid{display:grid;gap:18px}
.g3{grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}
.g4{grid-template-columns:repeat(auto-fit,minmax(170px,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:24px;padding:26px;transition:.3s}
.card:hover{transform:translateY(-6px) scale(1.02);border-color:#454f96;box-shadow:0 18px 48px #0008}
.card .k{font-size:38px;margin-bottom:14px;display:inline-block;transition:.3s}
.card:hover .k{transform:scale(1.15)}
.card h3{font-size:18px;margin-bottom:8px;color:#fff}
.card p{color:var(--mut);font-size:14px;line-height:1.5}

.country{display:flex;align-items:center;gap:10px;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:12px 14px;transition:.25s}
.country:hover{transform:translateY(-3px);border-color:#454f96}
.country .fl{font-size:26px}
.country .nm{font-weight:700;font-size:14px;color:#fff}
.dot{width:9px;height:9px;border-radius:50%;margin-left:auto;background:var(--ok);box-shadow:0 0 8px var(--ok);animation:blink 2s infinite}
@keyframes blink{50%{opacity:.35}}

/* plans */
.plan{background:var(--card);border:1px solid var(--line);border-radius:26px;padding:26px 28px 30px;text-align:center;transition:.3s}
.plan:hover{transform:translateY(-8px) scale(1.02);box-shadow:0 22px 55px #000a}
.plan.hot{border:1px solid var(--gr1)}
.plan .badge{display:inline-block;background:linear-gradient(90deg,var(--gr1),var(--gr2));padding:5px 16px;border-radius:999px;font-size:12px;font-weight:800;color:#fff;margin-bottom:14px}
.plan .price{font-size:42px;font-weight:900;margin:14px 0 4px;color:#fff}
.plan .stars{color:var(--gr2);font-size:17px;font-weight:700;margin-bottom:14px}
.plan ul{list-style:none;text-align:left;color:var(--mut);font-size:14px;display:flex;flex-direction:column;gap:10px;margin:18px 0}
.plan li::before{content:'✓ ';color:var(--ok);font-weight:800}
.btn{display:block;width:100%;padding:15px;border-radius:16px;border:none;cursor:pointer;font-weight:800;font-size:15px;color:#fff;background:linear-gradient(90deg,var(--gr1),var(--gr2));transition:.25s}
.btn:hover{transform:translateY(-3px);box-shadow:0 0 28px #7c5cff88}
.switch{display:inline-flex;gap:4px;background:#121430cc;border:1px solid var(--line);border-radius:999px;padding:5px;margin-bottom:32px}
.switch button{padding:10px 24px;border-radius:999px;border:none;background:transparent;color:var(--mut);font-weight:700;cursor:pointer;font-size:14px;transition:.25s}
.switch button.on{background:linear-gradient(90deg,var(--gr1),var(--gr2));color:#fff}

/* отзывы */
.marquee{overflow:hidden;position:relative;padding:12px 0}
.mq-track{display:flex;gap:18px;width:max-content;animation:mq 30s linear infinite}
@keyframes mq{to{transform:translateX(-50%)}}
.review{min-width:300px;background:var(--card);border:1px solid var(--line);border-radius:20px;padding:22px}
.review .stars{color:#ffc13d;font-size:16px}
.review p{color:var(--mut);font-size:13.5px;margin:12px 0;line-height:1.5}
.review .who{font-size:13px;font-weight:700;color:#fff}

.step{text-align:center}
.step .n{width:60px;height:60px;border-radius:50%;background:linear-gradient(135deg,var(--gr1),var(--gr2));display:flex;align-items:center;justify-content:center;font-size:23px;font-weight:900;margin:0 auto 16px;color:#fff;box-shadow:0 0 22px #7c5cff66;animation:stepPulse 3s infinite}
@keyframes stepPulse{50%{box-shadow:0 0 40px #22d3ee88}}

.calc{max-width:560px;margin:0 auto;background:var(--card);border:1px solid var(--line);border-radius:24px;padding:32px;text-align:center}
input[type=range]{width:100%;accent-color:var(--gr1);margin:20px 0;height:6px}
.calc-res{font-size:28px;font-weight:900;margin-top:12px;color:#fff}
.calc .save{color:var(--ok);font-weight:800}
.counter{font-size:58px;font-weight:900;color:var(--gr2)}
.faq{max-width:720px;margin:0 auto}
.faq-item{background:var(--card);border:1px solid var(--line);border-radius:16px;margin-bottom:12px;overflow:hidden}
.faq-q{display:flex;justify-content:space-between;align-items:center;padding:18px 22px;cursor:pointer;font-weight:700;color:#fff}
.faq-q .ar{transition:.25s;color:var(--gr2)}
.faq-a{max-height:0;overflow:hidden;transition:max-height .35s;padding:0 22px;color:var(--mut);font-size:14.5px;line-height:1.6}
.faq-item.open .faq-a{max-height:300px;padding-bottom:18px}
.faq-item.open .ar{transform:rotate(180deg)}

footer{background:#0a0c1e;border-top:1px solid var(--line);padding:40px 0}
.foot{display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;align-items:center;max-width:1160px;margin:0 auto;padding:0 22px}
.foot a{color:var(--mut);font-size:14px;transition:.2s}
.foot a:hover{color:#fff}
.doc{max-width:760px;margin:0 auto}
.doc h1{font-size:32px;margin-bottom:18px;color:#fff}
.doc p{margin:12px 0;color:var(--mut);line-height:1.7}
.doc h2{margin-top:26px;font-size:22px;color:#fff}
.back{display:inline-flex;gap:8px;color:var(--mut);margin-bottom:24px;font-size:14px}
</style>"""

def DOC(title, body_key):
    body = doc_body(body_key)
    return R("""<!DOCTYPE html><html lang="ru"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>"""+title+""" — __SITE__</title></head><body>
<nav><div class="nav-in"><a class="logo" href="/"><div class="logo-badge"><span>🛡</span></div>__SITE__</a>
<div class="menu"><a href="/">Главная</a></div></div></nav>
<section><div class="wrap doc"><a class="back" href="/">← Вернуться на главную</a>
<h1>"""+title+"""</h1>
"""+body+"""
</div></section>
<footer><div class="foot"><span>© __SITE__</span>
<a href="/terms">Условия</a><a href="/privacy">Конфиденциальность</a><a href="/refund">Возврат</a></div></footer>
</body></html>""")

def doc_body(kind):
    if kind == "terms":
        return R("""<h2>1. Общие положения</h2>
<p>Настоящие условия регулируют использование сервиса __SITE__, предоставляемого __OPERATOR__.</p>
<h2>2. Услуги</h2>
<p>Сервис предоставляет защищённое подключение к сети Интернет через серверы в 8 странах.</p>
<h2>3. Пробный период</h2>
<p>Новым пользователям предоставляется бесплатный пробный доступ на 3 дня.</p>
<h2>4. Тарифы</h2>
<p>1 месяц — 139₽ / 98⭐ (3 устройства); 3 месяца — 249₽ / 175⭐ (3 устройства); 6 месяцев — 519₽ / 364⭐ (5 устройств).</p>
<h2>5. Партнёрская программа</h2>
<p>Партнёры получают 20% от каждого платежа привлечённого пользователя.</p>
<p>По вопросам: __EMAIL__ или @__BOTU__.</p>""")
    if kind == "privacy":
        return R("""<h2>1. Какие данные мы обрабатываем</h2>
<p>Минимально необходимые данные для предоставления услуг.</p>
<h2>2. Использование данных</h2>
<p>Данные используются исключительно для предоставления услуг и поддержки.</p>
<h2>3. Передача третьим лицам</h2>
<p>Мы не продаём и не передаём персональные данные третьим лицам.</p>
<p>По вопросам: __EMAIL__.</p>""")
    return R("""<h2>1. Гарантия возврата</h2>
<p>Гарантия возврата средств в течение 7 дней с момента оплаты, если услуга не оказана надлежащим образом.</p>
<h2>2. Как оформить возврат</h2>
<p>Напишите оператору @__BOTU__ или на __EMAIL__, указав причину. Возврат тем же способом оплаты в течение 3–5 рабочих дней.</p>""")

def index_html():
    return R("""<!DOCTYPE html><html lang="ru"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__SITE__ — защита за 1 минуту</title>"""+HEAD+"""</head><body>
<nav><div class="nav-in"><a class="logo" href="/"><div class="logo-badge"><span>🛡</span></div>__SITE__</a>
<div class="menu"><a href="#features">Возможности</a><a href="#countries">Страны</a><a href="#plans">Тарифы</a><a href="#faq">FAQ</a></div></div></nav>

<!-- HERO -->
<section class="hero"><div class="wrap center">
<span class="pill">🔥 <b>3 дня бесплатно</b> · от 139₽/мес · подключение за 1 минуту</span>
<h1>Ваши данные под <span class="hl">защитой</span> уже сейчас</h1>
<p>Быстрый и приватный VPN в 8 странах мира. Один клик — и ваше соединение зашифровано. Без логов, без лимитов, на всех устройствах.</p>
<div class="hero-btns">
<a class="cta" href="__BOT__">🚀 Подключиться</a>
<a class="cta ghost" href="#plans">💰 Смотреть тарифы</a>
</div>
<div style="display:flex;gap:28px;justify-content:center;flex-wrap:wrap;margin-top:44px">
<div><div style="font-size:30px;font-weight:900" class="hl">8</div><div style="color:var(--mut);font-size:13px">стран мира</div></div>
<div><div style="font-size:30px;font-weight:900" class="hl">∞</div><div style="color:var(--mut);font-size:13px">трафика</div></div>
<div><div style="font-size:30px;font-weight:900" class="hl">24/7</div><div style="color:var(--mut);font-size:13px">поддержка</div></div>
<div><div style="font-size:30px;font-weight:900" class="hl">1 мин</div><div style="color:var(--mut);font-size:13px">до защиты</div></div>
</div>
</div></section>

<!-- ПРЕИМУЩЕСТВА -->
<section id="features"><div class="wrap">
<div class="center"><h2>Почему <span class="hl">__SITE__</span>?</h2><p class="sub">Максимальная защита без сложных настроек</p></div>
<div class="grid g3">"""+guarantee_html()+"""</div></div></section>

<!-- СТРАНЫ -->
<section id="countries"><div class="wrap">
<div class="center"><h2>Статус <span class="hl">серверов</span></h2><p class="sub">Все страны доступны в реальном времени</p></div>
<div class="grid g4">"""+countries_html()+"""</div>
<div class="center" style="margin-top:28px"><a class="cta" href="__BOT__">Получить доступ в боте</a></div>
</div></section>

<!-- КАК ПОДКЛЮЧИТЬСЯ -->
<section><div class="wrap">
<div class="center"><h2>Как <span class="hl">подключиться</span></h2><p class="sub">Всего 3 шага до полной защиты</p></div>
<div class="grid g3">
<div class="step"><div class="n">1</div><h3>Установи приложение</h3><p>Выбери приложение под свою платформу.</p></div>
<div class="step"><div class="n">2</div><h3>Получи ключ в боте</h3><p>Бот @__BOTU__ выдаст ключ и подписку.</p></div>
<div class="step"><div class="n">3</div><h3>Нажми «Подключить»</h3><p>Готово — вы под защитой.</p></div>
</div></div></section>

<!-- ПРИЛОЖЕНИЯ -->
<section><div class="wrap">
<div class="center"><h2>Приложения</h2><p class="sub">Работает на любой платформе</p></div>
<div class="grid g3">"""+apps_html()+"""</div></div></section>

<!-- КАЛЬКУЛЯТОР -->
<section><div class="wrap">
<div class="center"><h2>Калькулятор <span class="hl">выгоды</span></h2><p class="sub">Выбери длительность и посчитай экономию</p></div>
<div class="calc">
<label style="font-weight:700">Длительность: <span id="cval">6 месяцев</span></label>
<input type="range" id="crange" min="1" max="6" value="6" step="1" style="display:block">
<div class="calc-res">💰 <span id="cprice">519₽</span> / <span id="cstars">364⭐</span></div>
<div class="save" id="csave">Вы экономите 297₽ против помесячной оплаты!</div>
</div></div></section>

<!-- ТАРИФЫ -->
<section id="plans"><div class="wrap center">
<h2>Тарифы</h2><p class="sub">Гибкие тарифы для любого количества устройств</p>
<div class="switch"><button data-cur="rub" class="on" onclick="setCur('rub')">₽ рубли</button><button data-cur="star" onclick="setCur('star')">⭐ звёзды</button></div>
<div class="grid g3">
<div class="plan"><span class="badge">Популярный</span>
<h3>1 месяц</h3><div class="price" data-r="139" data-s="98">139₽</div><div class="stars" data-r="139₽" data-s="98⭐">или 98⭐</div>
<ul><li>3 устройства</li><li>8 стран</li><li>Без логов</li><li>Поддержка 24/7</li></ul><a class="btn" href="__BOT__">Купить</a></div>
<div class="plan hot"><span class="badge">Выгодно</span>
<h3>3 месяца</h3><div class="price" data-r="249" data-s="175">249₽</div><div class="stars" data-r="249₽" data-s="175⭐">или 175⭐</div>
<ul><li>3 устройства</li><li>8 стран</li><li>Без логов</li><li>Поддержка 24/7</li><li>−40% выгода</li></ul><a class="btn" href="__BOT__">Купить</a></div>
<div class="plan"><span class="badge">Максимум</span>
<h3>6 месяцев</h3><div class="price" data-r="519" data-s="364">519₽</div><div class="stars" data-r="519₽" data-s="364⭐">или 364⭐</div>
<ul><li>5 устройств</li><li>8 стран</li><li>Без логов</li><li>Поддержка 24/7</li><li>−38% выгода</li></ul><a class="btn" href="__BOT__">Купить</a></div>
</div></div></section>

<!-- ПАРТНЁРКА -->
<section><div class="wrap">
<div class="center"><h2>Партнёрская <span class="hl">программа</span></h2><p class="sub">Зарабатывай 20% с каждого платежа</p></div>
<div class="card center" style="max-width:540px;margin:0 auto">
<div class="k">💸</div><h3>20% от каждого платежа</h3>
<p>Приглашай друзей через свою ссылку — получай 20% с каждой их оплаты. Выплаты в боте @__BOTU__.</p>
<div style="margin-top:20px"><a class="btn" href="__BOT__" style="display:inline-block;width:auto;padding:14px 32px">Стать партнёром</a></div>
</div></div></section>

<!-- ОТЗЫВЫ -->
<section><div class="wrap">
<div class="center"><h2>Отзывы</h2><p class="sub">Нам доверяют тысячи пользователей</p></div>
<div class="marquee"><div class="mq-track" id="mq"></div></div></div></section>

<!-- FAQ -->
<section id="faq"><div class="wrap">
<div class="center"><h2>Частые <span class="hl">вопросы</span></h2><p class="sub">Всё, что нужно знать о сервисе</p></div>
<div class="faq">
<div class="faq-item"><div class="faq-q">Как получить бесплатный пробный период?<span class="ar">▾</span></div><div class="faq-a">Напишите боту @__BOTU__ — новый пользователь получает 3 дня бесплатно.</div></div>
<div class="faq-item"><div class="faq-q">На скольких устройствах можно подключиться?<span class="ar">▾</span></div><div class="faq-a">Зависит от тарифа: 3 устройства на 1 и 3 месяца, 5 устройств на 6 месяцев.</div></div>
<div class="faq-item"><div class="faq-q">В каких странах есть серверы?<span class="ar">▾</span></div><div class="faq-a">Финляндия, Польша, Германия, Нидерланды, Великобритания, США, Франция, Швеция.</div></div>
<div class="faq-item"><div class="faq-q">Есть ли ограничение по трафику?<span class="ar">▾</span></div><div class="faq-a">Нет. Скорость и трафик не ограничиваются.</div></div>
<div class="faq-item"><div class="faq-q">Как оплатить тариф?<span class="ar">▾</span></div><div class="faq-a">В боте @__BOTU__ можно оплатить рублями или звёздами Telegram.</div></div>
<div class="faq-item"><div class="faq-q">Как работает возврат?<span class="ar">▾</span></div><div class="faq-a">Гарантия возврата 7 дней — напишите оператору в боте.</div></div>
</div></div></section>

<!-- СЧЁТЧИК -->
<section><div class="wrap center">
<h2>Уже сейчас <span class="hl">защищены</span></h2>
<div class="counter" id="counter">0</div>
<p class="sub">человек уже используют __SITE__</p>
<div style="margin-top:22px"><a class="cta" href="__BOT__">Подключиться за 1 минуту</a></div></div></section>

<footer><div class="foot"><span>© __SITE__</span>
<a href="/terms">Условия</a><a href="/privacy">Конфиденциальность</a><a href="/refund">Возврат</a>
<a href="__SUPPORT__">Поддержка</a></div></footer>

<script>
var cur='rub';
function setCur(c){cur=c;document.querySelectorAll('.price').forEach(function(p){p.textContent=(c==='rub'?p.dataset.r+'₽':p.dataset.s+'⭐')});
document.querySelectorAll('.stars').forEach(function(x){x.textContent=(c==='rub'?x.dataset.r+' или '+x.dataset.s+'⭐':x.dataset.s+' или '+x.dataset.r)});
document.querySelectorAll('.switch button').forEach(function(b){b.classList.toggle('on',b.dataset.cur===c)});}
(function(){var r=document.getElementById('crange'),cv=document.getElementById('cval'),cp=document.getElementById('cprice'),cs=document.getElementById('cstars'),sv=document.getElementById('csave');
var map={1:[139,98,0],2:[278,196,0],3:[249,175,89],6:[519,364,297]};
r.addEventListener('input',function(){var m=map[r.value];cv.textContent=(r.value==='6'?'6 месяцев':r.value+' месяц(а)');
cp.textContent=m[0]+'₽';cs.textContent=m[1]+'⭐';sv.textContent=m[2]>0?('Вы экономите '+m[2]+'₽ против помесячной оплаты!'):'Помесячная оплата без скидки';});})();
(function(){var el=document.getElementById('counter'),target=12847,t=0;var iv=setInterval(function(){t+=Math.ceil(target/80);if(t>=target){t=target;clearInterval(iv)}el.textContent=t.toLocaleString('ru-RU');},30);})();
document.querySelectorAll('.faq-q').forEach(function(q){q.addEventListener('click',function(){q.parentElement.classList.toggle('open')})});
var revs=[['Дмитрий','Скорость огонь, подключается за секунду!'],['Анна','Наконец-то работаю безопасно из кафе.'],['Игорь','Простая настройка, всё за 1 минуту.'],['Мария','Лучший VPN, что пробовала.'],['Сергей','Поддержка отвечает мгновенно.']];
var track=document.getElementById('mq');revs.concat(revs).forEach(function(r){track.innerHTML+='<div class="review"><div class="stars">★★★★★</div><p>'+r[1]+'</p><div class="who">'+r[0]+'</div></div>';});
</script>
</body></html>""")

@app.route("/")
def index():
    return index_html()

@app.route("/terms")
def terms():
    return DOC("Условия использования", "terms")

@app.route("/privacy")
def privacy():
    return DOC("Политика конфиденциальности", "privacy")

@app.route("/refund")
def refund():
    return DOC("Политика возврата", "refund")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
