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
:root{--bg:#05061a;--card:rgba(18,20,48,.85);--line:rgba(90,100,190,.25);--txt:#f0f2ff;--mut:#9aa1cf;
--gr1:#7c5cff;--gr2:#22d3ee;--gr3:#ff5c8a;--ok:#25e08a}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{color:var(--txt);font-family:'Segoe UI',system-ui,Arial,sans-serif;overflow-x:hidden;min-height:100vh;
background:linear-gradient(120deg,#05061a,#101540,#0a0e30,#1a0f3d,#05061a);
background-size:600% 600%;animation:bgMove 22s ease infinite}
@keyframes bgMove{50%{background-position:100% 50%}}
a{color:inherit;text-decoration:none}
img,svg{max-width:100%}

/* плавающие партиклы */
.part{position:fixed;width:6px;height:6px;border-radius:50%;pointer-events:none;z-index:1;filter:blur(1px);opacity:.6}
@keyframes floaty{0%{transform:translateY(100vh) scale(1)}100%{transform:translateY(-10vh) scale(.4)}}

.wrap{max-width:1600px;margin:0 auto;padding:0 30px;position:relative;z-index:2}
@media(max-width:760px){.wrap{padding:0 18px}}

/* NAV */
nav{position:sticky;top:0;z-index:50;background:rgba(6,8,26,.75);backdrop-filter:blur(16px);border-bottom:1px solid var(--line)}
.nav-in{display:flex;align-items:center;gap:26px;padding:16px 30px;max-width:1600px;margin:0 auto}
.logo{display:flex;align-items:center;gap:12px;font-weight:800;font-size:21px}
.logo-badge{width:40px;height:40px;border-radius:13px;background:conic-gradient(from 0deg,var(--gr1),var(--gr2),var(--gr3),var(--gr1));display:flex;align-items:center;justify-content:center;box-shadow:0 0 26px #7c5cff88;animation:spin 6s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.logo-badge span{background:#05061a;border-radius:10px;width:32px;height:32px;display:flex;align-items:center;justify-content:center;font-size:18px;animation:spinRev 6s linear infinite}
@keyframes spinRev{to{transform:rotate(-360deg)}}
.menu{display:flex;gap:24px;margin-left:auto}
.menu a{color:var(--mut);font-size:15px;font-weight:600;position:relative;transition:.25s}
.menu a::after{content:'';position:absolute;left:0;bottom:-5px;width:0;height:2px;background:linear-gradient(90deg,var(--gr1),var(--gr2));transition:.3s;border-radius:2px}
.menu a:hover{color:#fff}
.menu a:hover::after{width:100%}
@media(max-width:820px){.menu{display:none}}

h2{font-size:clamp(28px,4vw,44px);font-weight:900;margin-bottom:14px}
.hl{background:linear-gradient(90deg,var(--gr1),var(--gr2),var(--gr3));-webkit-background-clip:text;background-clip:text;color:transparent}
.sub{color:var(--mut);max-width:680px;margin:0 auto 40px;font-size:17px}
section{padding:90px 0;position:relative;z-index:2}
.center{text-align:center}

/* появление при скролле */
.reveal{opacity:0;transform:translateY(40px);transition:opacity .8s,transform .8s}
.reveal.show{opacity:1;transform:translateY(0)}

/* HERO */
.hero{padding:130px 0 90px;text-align:center}
.hero h1{font-size:clamp(42px,7vw,76px);font-weight:900;line-height:1.05;margin-bottom:26px;letter-spacing:-1px}
.hero p{color:var(--mut);font-size:21px;max-width:680px;margin:0 auto 36px}
.pill{display:inline-flex;gap:9px;align-items:center;padding:10px 22px;border-radius:999px;border:1px solid var(--line);background:rgba(10,12,40,.6);color:var(--mut);font-size:14px;margin-bottom:30px;animation:floatIn 2s infinite}
@keyframes floatIn{50%{transform:translateY(-4px)}}
.pill b{color:var(--ok)}
.hero-btns{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.cta{display:inline-flex;align-items:center;gap:11px;padding:18px 44px;border-radius:18px;background:linear-gradient(90deg,var(--gr1),var(--gr2));background-size:200% 200%;font-weight:800;font-size:18px;box-shadow:0 0 36px #7c5cff77;transition:.3s;cursor:pointer;border:none;color:#fff;animation:gradShift 3s ease infinite;position:relative;overflow:hidden}
@keyframes gradShift{50%{background-position:100% 0}}
.cta:hover{transform:translateY(-5px) scale(1.04);box-shadow:0 0 60px #22d3eeaa}
.cta.ghost{background:rgba(124,92,255,.1);border:1px solid var(--line);animation:none}
.cta.ghost:hover{border-color:var(--gr2)}
.shine{position:absolute;top:0;left:-70%;width:50%;height:100%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.4),transparent);transform:skewX(-20deg);animation:shine 2.6s infinite}
@keyframes shine{to{left:140%}}
.stats{display:flex;gap:60px;justify-content:center;flex-wrap:wrap;margin-top:54px}
.stat{text-align:center}
.stat .num{font-size:40px;font-weight:900;background:linear-gradient(90deg,var(--gr2),var(--gr1),var(--gr3));-webkit-background-clip:text;background-clip:text;color:transparent}
.stat .lab{color:var(--mut);font-size:14px;margin-top:4px}

/* CARDS */
.grid{display:grid;gap:22px}
.g3{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.g4{grid-template-columns:repeat(auto-fit,minmax(190px,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:26px;padding:30px;transition:.4s;position:relative;overflow:hidden;backdrop-filter:blur(10px)}
.card::before{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:radial-gradient(circle,rgba(124,92,255,.15),transparent 50%);opacity:0;transition:.4s}
.card:hover{transform:translateY(-10px) scale(1.02);border-color:#5a66c0;box-shadow:0 28px 70px #000a}
.card:hover::before{opacity:1}
.card .k{font-size:44px;margin-bottom:16px;display:inline-block;transition:.4s}
.card:hover .k{transform:scale(1.2) rotate(-6deg)}
.card h3{font-size:19px;margin-bottom:10px}
.card p{color:var(--mut);font-size:14.5px;line-height:1.6;position:relative;z-index:1}

.country{display:flex;align-items:center;gap:12px;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:14px 16px;transition:.3s;backdrop-filter:blur(8px)}
.country:hover{transform:translateY(-5px);border-color:#5a66c0;box-shadow:0 16px 40px #0008}
.country .fl{font-size:30px;animation:float 3s ease-in-out infinite}
@keyframes float{50%{transform:translateY(-5px)}}
.country .nm{font-weight:700;font-size:15px}
.dot{width:10px;height:10px;border-radius:50%;margin-left:auto;background:var(--ok);box-shadow:0 0 12px var(--ok);animation:blink 1.8s infinite}
@keyframes blink{50%{opacity:.3}}

/* PLANS */
.plan{background:var(--card);border:1px solid var(--line);border-radius:30px;padding:34px 30px;text-align:center;transition:.4s;position:relative;backdrop-filter:blur(12px)}
.plan:hover{transform:translateY(-12px) scale(1.02);box-shadow:0 30px 70px #000c}
.plan.hot{border:1px solid var(--gr1);background:linear-gradient(160deg,rgba(124,92,255,.15),rgba(18,20,48,.9));box-shadow:0 0 50px #7c5cff33}
.plan .badge{display:inline-block;background:linear-gradient(90deg,var(--gr1),var(--gr2));padding:6px 18px;border-radius:999px;font-size:12px;font-weight:800;color:#fff;margin-bottom:16px;box-shadow:0 4px 24px #7c5cff66}
.plan .price{font-size:48px;font-weight:900;margin:16px 0 6px;letter-spacing:-1px}
.plan .stars{color:var(--gr2);font-size:18px;font-weight:700;margin-bottom:16px}
.plan ul{list-style:none;text-align:left;color:var(--mut);font-size:14.5px;display:flex;flex-direction:column;gap:12px;margin:22px 0}
.plan li::before{content:'✓ ';color:var(--ok);font-weight:900}
.btn{display:block;width:100%;padding:16px;border-radius:16px;border:none;cursor:pointer;font-weight:800;font-size:15.5px;color:#fff;background:linear-gradient(90deg,var(--gr1),var(--gr2));background-size:200% 200%;transition:.3s;animation:gradShift 3s ease infinite}
.btn:hover{transform:translateY(-4px);box-shadow:0 0 34px #7c5cff99}
.switch{display:inline-flex;gap:4px;background:rgba(10,12,40,.6);border:1px solid var(--line);border-radius:999px;padding:6px;margin-bottom:36px}
.switch button{padding:11px 26px;border-radius:999px;border:none;background:transparent;color:var(--mut);font-weight:700;cursor:pointer;font-size:14.5px;transition:.3s}
.switch button.on{background:linear-gradient(90deg,var(--gr1),var(--gr2));color:#fff}

/* steps */
.step{text-align:center}
.step .n{width:68px;height:68px;border-radius:50%;background:linear-gradient(135deg,var(--gr1),var(--gr3));display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:900;margin:0 auto 18px;color:#fff;box-shadow:0 0 30px #7c5cff88;animation:stepPulse 3s infinite}
@keyframes stepPulse{50%{box-shadow:0 0 55px #ff5c8aaa}}
.step p{color:var(--mut);font-size:14.5px}

/* calc */
.calc{max-width:600px;margin:0 auto;background:var(--card);border:1px solid var(--line);border-radius:28px;padding:36px;text-align:center;backdrop-filter:blur(12px)}
input[type=range]{width:100%;accent-color:var(--gr1);margin:22px 0;height:7px;cursor:pointer}
.calc-res{font-size:30px;font-weight:900;margin-top:14px}
.calc .save{color:var(--ok);font-weight:800}
.counter{font-size:64px;font-weight:900;background:linear-gradient(90deg,var(--gr2),var(--gr1),var(--gr3));-webkit-background-clip:text;background-clip:text;color:transparent}

/* reviews marquee */
.marquee{overflow:hidden;padding:14px 0;position:relative;mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}
.mq-track{display:flex;gap:22px;width:max-content;animation:mq 34s linear infinite}
.mq-track:hover{animation-play-state:paused}
@keyframes mq{to{transform:translateX(-50%)}}
.review{min-width:320px;background:var(--card);border:1px solid var(--line);border-radius:24px;padding:26px;backdrop-filter:blur(8px);transition:.3s}
.review:hover{border-color:#5a66c0;transform:translateY(-4px)}
.review .stars{color:#ffc13d;font-size:17px;letter-spacing:3px}
.review p{color:var(--mut);font-size:14px;margin:14px 0;line-height:1.6}
.review .who{font-size:14px;font-weight:800}

/* faq */
.faq{max-width:760px;margin:0 auto}
.faq-item{background:var(--card);border:1px solid var(--line);border-radius:20px;margin-bottom:14px;overflow:hidden;transition:.3s;backdrop-filter:blur(8px)}
.faq-item:hover{border-color:#5a66c0}
.faq-q{display:flex;justify-content:space-between;align-items:center;padding:20px 26px;cursor:pointer;font-weight:700;font-size:16px}
.faq-q .ar{transition:.3s;color:var(--gr2);font-size:18px}
.faq-a{max-height:0;overflow:hidden;transition:max-height .4s;padding:0 26px;color:var(--mut);font-size:15px;line-height:1.6}
.faq-item.open .faq-a{max-height:400px;padding-bottom:22px}
.faq-item.open .ar{transform:rotate(180deg)}

footer{background:rgba(5,6,26,.9);border-top:1px solid var(--line);padding:44px 0;position:relative;z-index:2}
.foot{display:flex;flex-wrap:wrap;gap:22px;justify-content:space-between;align-items:center;max-width:1600px;margin:0 auto;padding:0 30px}
.foot a{color:var(--mut);font-size:14px;transition:.2s}
.foot a:hover{color:#fff}
.doc{max-width:780px;margin:0 auto}
.doc h1{font-size:36px;margin-bottom:20px}
.doc p{margin:12px 0;color:var(--mut);line-height:1.7}
.doc h2{margin-top:28px;font-size:24px}
.back{display:inline-flex;gap:8px;color:var(--mut);margin-bottom:24px;font-size:14px;transition:.2s}
.back:hover{color:#fff}
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
<section class="hero center"><div class="wrap">
<span class="pill reveal show">🔥 <b>3 дня бесплатно</b> · от 139₽/мес · подключение за 1 минуту</span>
<h1 class="reveal show">Ваши данные под<br><span class="hl">молниеносной защитой</span></h1>
<p class="reveal show">Быстрый и приватный VPN в 8 странах мира. Один клик — и ваше соединение зашифровано. Без логов, без лимитов, на всех устройствах.</p>
<div class="hero-btns reveal show">
<a class="cta" href="__BOT__"><span class="shine"></span>🚀 Подключиться</a>
<a class="cta ghost" href="#plans">💰 Смотреть тарифы</a>
</div>
<div class="stats reveal show">
<div class="stat"><div class="num">8</div><div class="lab">стран мира</div></div>
<div class="stat"><div class="num">∞</div><div class="lab">безлимит</div></div>
<div class="stat"><div class="num">24/7</div><div class="lab">поддержка</div></div>
<div class="stat"><div class="num">1 мин</div><div class="lab">до защиты</div></div>
</div>
</div></section>

<!-- ПРЕИМУЩЕСТВА -->
<section id="features"><div class="wrap">
<div class="center"><h2 class="reveal">Почему <span class="hl">__SITE__</span>?</h2><p class="sub reveal">Максимальная защита без сложных настроек</p></div>
<div class="grid g3">"""+guarantee_html()+"""</div></div></section>

<!-- СТРАНЫ -->
<section id="countries"><div class="wrap">
<div class="center"><h2 class="reveal">Статус <span class="hl">серверов</span></h2><p class="sub reveal">Все страны доступны в реальном времени</p></div>
<div class="grid g4">"""+countries_html()+"""</div>
<div class="center" style="margin-top:32px"><a class="cta reveal" href="__BOT__">Получить доступ в боте</a></div>
</div></section>

<!-- КАК ПОДКЛЮЧИТЬСЯ -->
<section><div class="wrap">
<div class="center"><h2 class="reveal">Как <span class="hl">подключиться</span></h2><p class="sub reveal">Всего 3 шага до полной защиты</p></div>
<div class="grid g3">
<div class="step reveal"><div class="n">1</div><h3>Установи приложение</h3><p>Выбери приложение под свою платформу.</p></div>
<div class="step reveal"><div class="n">2</div><h3>Получи ключ в боте</h3><p>Бот @__BOTU__ выдаст ключ и подписку.</p></div>
<div class="step reveal"><div class="n">3</div><h3>Нажми «Подключить»</h3><p>Готово — вы под защитой.</p></div>
</div></div></section>

<!-- ПРИЛОЖЕНИЯ -->
<section><div class="wrap">
<div class="center"><h2 class="reveal">Приложения</h2><p class="sub reveal">Работает на любой платформе</p></div>
<div class="grid g3">"""+apps_html()+"""</div></div></section>

<!-- КАЛЬКУЛЯТОР -->
<section><div class="wrap">
<div class="center"><h2 class="reveal">Калькулятор <span class="hl">выгоды</span></h2><p class="sub reveal">Выбери длительность и посчитай экономию</p></div>
<div class="calc reveal">
<label style="font-weight:700">Длительность: <span id="cval">6 месяцев</span></label>
<input type="range" id="crange" min="1" max="6" value="6" step="1" style="display:block">
<div class="calc-res">💰 <span id="cprice">519₽</span> / <span id="cstars">364⭐</span></div>
<div class="save" id="csave">Вы экономите 297₽ против помесячной оплаты!</div>
</div></div></section>

<!-- ТАРИФЫ -->
<section id="plans"><div class="wrap center">
<h2 class="reveal">Тарифы</h2><p class="sub reveal">Гибкие тарифы для любого количества устройств</p>
<div class="switch reveal"><button data-cur="rub" class="on" onclick="setCur('rub')">₽ рубли</button><button data-cur="star" onclick="setCur('star')">⭐ звёзды</button></div>
<div class="grid g3">
<div class="plan reveal"><span class="badge">Популярный</span>
<h3>1 месяц</h3><div class="price" data-r="139" data-s="98">139₽</div><div class="stars" data-r="139₽" data-s="98⭐">или 98⭐</div>
<ul><li>3 устройства</li><li>8 стран</li><li>Без логов</li><li>Поддержка 24/7</li></ul><a class="btn" href="__BOT__">Купить</a></div>
<div class="plan hot reveal"><span class="badge">Выгодно</span>
<h3>3 месяца</h3><div class="price" data-r="249" data-s="175">249₽</div><div class="stars" data-r="249₽" data-s="175⭐">или 175⭐</div>
<ul><li>3 устройства</li><li>8 стран</li><li>Без логов</li><li>Поддержка 24/7</li><li>−40% выгода</li></ul><a class="btn" href="__BOT__">Купить</a></div>
<div class="plan reveal"><span class="badge">Максимум</span>
<h3>6 месяцев</h3><div class="price" data-r="519" data-s="364">519₽</div><div class="stars" data-r="519₽" data-s="364⭐">или 364⭐</div>
<ul><li>5 устройств</li><li>8 стран</li><li>Без логов</li><li>Поддержка 24/7</li><li>−38% выгода</li></ul><a class="btn" href="__BOT__">Купить</a></div>
</div></div></section>

<!-- ПАРТНЁРКА -->
<section><div class="wrap">
<div class="center"><h2 class="reveal">Партнёрская <span class="hl">программа</span></h2><p class="sub reveal">Зарабатывай 20% с каждого платежа</p></div>
<div class="card center reveal" style="max-width:560px;margin:0 auto">
<div class="k">💸</div><h3>20% от каждого платежа</h3>
<p>Приглашай друзей через свою ссылку — получай 20% с каждой их оплаты. Выплаты в боте @__BOTU__.</p>
<div style="margin-top:22px"><a class="btn" href="__BOT__" style="display:inline-block;width:auto;padding:15px 36px">Стать партнёром</a></div>
</div></div></section>

<!-- ОТЗЫВЫ -->
<section><div class="wrap">
<div class="center"><h2 class="reveal">Отзывы</h2><p class="sub reveal">Нам доверяют тысячи пользователей</p></div>
<div class="marquee reveal"><div class="mq-track" id="mq"></div></div></div></section>

<!-- FAQ -->
<section id="faq"><div class="wrap">
<div class="center"><h2 class="reveal">Частые <span class="hl">вопросы</span></h2><p class="sub reveal">Всё, что нужно знать о сервисе</p></div>
<div class="faq">
<div class="faq-item reveal"><div class="faq-q">Как получить бесплатный пробный период?<span class="ar">▾</span></div><div class="faq-a">Напишите боту @__BOTU__ — новый пользователь получает 3 дня бесплатно.</div></div>
<div class="faq-item reveal"><div class="faq-q">На скольких устройствах можно подключиться?<span class="ar">▾</span></div><div class="faq-a">Зависит от тарифа: 3 устройства на 1 и 3 месяца, 5 устройств на 6 месяцев.</div></div>
<div class="faq-item reveal"><div class="faq-q">В каких странах есть серверы?<span class="ar">▾</span></div><div class="faq-a">Финляндия, Польша, Германия, Нидерланды, Великобритания, США, Франция, Швеция.</div></div>
<div class="faq-item reveal"><div class="faq-q">Есть ли ограничение по трафику?<span class="ar">▾</span></div><div class="faq-a">Нет. Скорость и трафик не ограничиваются.</div></div>
<div class="faq-item reveal"><div class="faq-q">Как оплатить тариф?<span class="ar">▾</span></div><div class="faq-a">В боте @__BOTU__ можно оплатить рублями или звёздами Telegram.</div></div>
<div class="faq-item reveal"><div class="faq-q">Как работает возврат?<span class="ar">▾</span></div><div class="faq-a">Гарантия возврата 7 дней — напишите оператору в боте.</div></div>
</div></div></section>

<!-- СЧЁТЧИК -->
<section class="center"><div class="wrap">
<h2 class="reveal">Уже сейчас <span class="hl">защищены</span></h2>
<div class="counter reveal" id="counter">0</div>
<p class="sub reveal">человек уже используют __SITE__</p>
<div style="margin-top:24px" class="reveal"><a class="cta" href="__BOT__">Подключиться за 1 минуту</a></div></div></section>

<footer><div class="foot"><span>© __SITE__</span>
<a href="/terms">Условия</a><a href="/privacy">Конфиденциальность</a><a href="/refund">Возврат</a>
<a href="__SUPPORT__">Поддержка</a></div></footer>

<script>
/* партиклы */
(function(){var c=['#7c5cff','#22d3ee','#ff5c8a'];for(var i=0;i<35;i++){var p=document.createElement('div');p.className='part';p.style.left=Math.random()*100+'%';p.style.background=c[Math.floor(Math.random()*c.length)];p.style.animation='floaty '+(8+Math.random()*10)+'s linear infinite';p.style.animationDelay=Math.random()*10+'s';document.body.appendChild(p)}})();

/* появление при скролле */
(function(){var els=document.querySelectorAll('.reveal');if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('show')});return}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('show');io.unobserve(e.target)}})},{threshold:.1});
els.forEach(function(e){io.observe(e)})})();

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
