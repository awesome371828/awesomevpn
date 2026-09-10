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
BOT_ID = "8878874415"
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
        .replace("__BOTID__", BOT_ID)
    )

HEAD = """<style>
:root{--bg:#05060f;--card:#0d1022cc;--line:#1c2240;--txt:#e8ecff;--mut:#8a92b8;
--gr1:#7c5cff;--gr2:#22d3ee;--gr3:#ff3d81;--ok:#22e58f;--off:#ff4d6d}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--txt);font-family:'Segoe UI',system-ui,-apple-system,sans-serif;overflow-x:hidden}
a{color:inherit;text-decoration:none}
.wrap{max-width:1180px;margin:0 auto;padding:0 22px;position:relative;z-index:2}
.scene{position:fixed;inset:0;z-index:0;overflow:hidden;pointer-events:none}
.g{position:absolute;border-radius:50%;filter:blur(90px);opacity:.55}
.g1{width:520px;height:520px;background:var(--gr1);top:-140px;left:-120px;animation:float1 14s infinite}
.g2{width:460px;height:460px;background:var(--gr2);top:30%;right:-140px;animation:float2 16s infinite}
.g3{width:420px;height:420px;background:var(--gr3);bottom:-120px;left:35%;animation:float1 18s infinite}
@keyframes float1{50%{transform:translate(60px,40px) scale(1.08)}}
@keyframes float2{50%{transform:translate(-50px,-30px) scale(1.05)}}
.star{position:absolute;width:3px;height:3px;background:#fff;border-radius:50%;animation:tw 4s infinite;opacity:.5}
@keyframes tw{0%,100%{opacity:.2;transform:scale(1)}50%{opacity:1;transform:scale(1.4)}}
nav{position:sticky;top:0;z-index:50;backdrop-filter:blur(14px);background:#07081ad9;border-bottom:1px solid var(--line)}
.nav-in{display:flex;align-items:center;gap:22px;padding:15px 22px;max-width:1180px;margin:0 auto}
.logo{display:flex;align-items:center;gap:11px;font-weight:800;font-size:20px}
.logo-badge{width:38px;height:38px;border-radius:12px;background:conic-gradient(from 0deg,var(--gr1),var(--gr2),var(--gr3),var(--gr1));display:flex;align-items:center;justify-content:center;box-shadow:0 0 22px #7c5cff88;animation:spin 8s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.logo-badge span{background:#0a0c1e;border-radius:9px;width:30px;height:30px;display:flex;align-items:center;justify-content:center;font-size:17px;animation:spinRev 8s linear infinite}
@keyframes spinRev{to{transform:rotate(-360deg)}}
.menu{display:flex;gap:18px;margin-left:auto}
.menu a{color:var(--mut);font-size:14.5px;transition:.25s}
.menu a:hover{color:#fff}
.tg-login{margin-left:8px;min-width:186px;min-height:40px;display:flex;align-items:center}
@media(max-width:760px){.menu{display:none}}
h2{font-size:clamp(26px,4vw,38px);font-weight:800;margin-bottom:10px}
.grad{background:linear-gradient(90deg,var(--gr1),var(--gr2),var(--gr3));-webkit-background-clip:text;background-clip:text;color:transparent}
.sub{color:var(--mut);max-width:640px;margin:0 auto 34px;font-size:16px}
section{padding:74px 0;position:relative;z-index:2}
.center{text-align:center}
.hero{padding:86px 0 60px}
.hero h1{font-size:clamp(34px,6vw,60px);font-weight:900;line-height:1.06;margin-bottom:20px}
.hero p{color:var(--mut);font-size:19px;max-width:600px;margin:0 auto 26px}
.cta{display:inline-flex;align-items:center;gap:10px;padding:16px 34px;border-radius:18px;background:linear-gradient(90deg,var(--gr1),var(--gr2));font-weight:800;font-size:17px;box-shadow:0 0 34px #7c5cff66;transition:.3s;cursor:pointer;border:none;color:#fff}
.cta:hover{transform:translateY(-3px);box-shadow:0 0 50px #22d3ee88}
.pill{display:inline-flex;gap:8px;align-items:center;padding:8px 16px;border-radius:999px;border:1px solid var(--line);background:#0a0c1fd9;color:var(--mut);font-size:13.5px;margin-bottom:22px}
.pill b{color:var(--ok)}
.connect-wrap{text-align:center;margin:44px auto 0;max-width:320px}
.connect{position:relative;width:190px;height:190px;border-radius:50%;margin:0 auto;background:radial-gradient(circle at 30% 30%,#1a1f3d,#0a0c1e);border:2px solid var(--line);display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.35s;user-select:none}
.connect::before{content:'';position:absolute;inset:-7px;border-radius:50%;padding:3px;background:conic-gradient(from 0deg,var(--gr1),var(--gr2),var(--gr3),var(--gr1));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;opacity:.4;transition:.35s}
.connect.on::before{opacity:1;animation:spin 3s linear infinite}
.connect .in{text-align:center;z-index:2}
.connect .ic{font-size:54px}
.connect .st{font-size:13px;color:var(--mut);margin-top:8px;line-height:1.3}
.connect .load{display:none;font-size:15px;font-weight:800;color:var(--gr2)}
.connect.connecting .load{display:block}
.connect.connecting .ic,.connect.connecting .st{display:none}
.connect.on .ic,.connect.on .st{display:none}
.connect.on .pro{display:block}
.connect .pro{display:none;font-size:16px;font-weight:800;color:var(--ok)}
.spin-ring{position:absolute;inset:0;border-radius:50%;border:4px solid transparent;border-top-color:var(--gr2);display:none}
.connect.connecting .spin-ring{display:block;animation:spin .8s linear infinite}
.phone-scene{display:flex;justify-content:center;margin:50px 0}
.phone{width:300px;border-radius:46px;padding:12px;background:linear-gradient(160deg,#1c2240,#0a0c1e);box-shadow:0 30px 70px #0008,inset 0 0 0 2px #232a4d;position:relative}
.phone .notch{position:absolute;top:20px;left:50%;transform:translateX(-50%);width:110px;height:24px;background:#000;border-radius:14px;z-index:3}
.phone .scr{background:#06070f;border-radius:36px;overflow:hidden;height:600px;display:flex;flex-direction:column}
.scr-head{display:flex;align-items:center;gap:8px;padding:44px 18px 10px;font-size:13px;color:var(--mut)}
.scr-head .time{margin-left:auto;font-weight:700;color:#fff}
.scr-top{display:flex;align-items:center;justify-content:space-between;padding:16px 20px 8px}
.scr-title{font-weight:800;font-size:22px}
.scr-logo{width:34px;height:34px;border-radius:10px;background:conic-gradient(from 0deg,var(--gr1),var(--gr2),var(--gr3),var(--gr1));display:flex;align-items:center;justify-content:center;font-size:15px}
.scr-body{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0 20px;text-align:center;gap:14px}
.scr-status{font-size:16px;font-weight:700;color:var(--off)}
.scr-sub{font-size:13px;color:var(--mut);line-height:1.4}
.phone-btn{position:relative;width:150px;height:150px;border-radius:50%;border:2px solid var(--line);background:#0a0c1e;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.35s}
.phone-btn::before{content:'';position:absolute;inset:-6px;border-radius:50%;padding:3px;background:conic-gradient(from 0deg,var(--off),var(--off),transparent,transparent);-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude}
.phone-btn .pi{font-size:46px;z-index:2}
.phone-btn.connecting::before{border:0;background:none;border:4px solid transparent;border-top-color:var(--gr2);animation:spin 1s linear infinite}
.phone-btn.on{background:#0a1f16;border-color:var(--ok);box-shadow:0 0 40px #22e58f44}
.phone-btn.on::before{background:conic-gradient(from 0deg,var(--ok),var(--ok),transparent,transparent)}
.tap-hint{font-size:12px;color:var(--mut)}
.phone-btn.on ~ .tap-hint,.phone-btn.on .pi{display:none}
.progress{width:70%;height:6px;border-radius:6px;background:#141a33;overflow:hidden;display:none}
.progress i{display:block;height:100%;width:0%;background:linear-gradient(90deg,var(--gr1),var(--gr2));border-radius:6px;transition:width .15s}
.connecting+.progress{display:block}
.grid{display:grid;gap:18px}
.g2{grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}
.g3{grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}
.g4{grid-template-columns:repeat(auto-fit,minmax(170px,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:28px;padding:26px;transition:.3s}
.card:hover{transform:translateY(-5px);border-color:#2c3560;box-shadow:0 18px 50px #0007}
.card .k{font-size:34px;margin-bottom:12px}
.card h3{font-size:18px;margin-bottom:8px}
.card p{color:var(--mut);font-size:14px;line-height:1.5}
.country{display:flex;align-items:center;gap:10px;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:12px 14px;transition:.3s}
.country:hover{transform:translateY(-3px);border-color:#2c3560}
.country .fl{font-size:26px}
.country .nm{font-weight:700;font-size:14px}
.dot{width:9px;height:9px;border-radius:50%;margin-left:auto}
.dot.on{background:var(--ok);box-shadow:0 0 10px var(--ok);animation:pulse 2s infinite}
.dot.off{background:var(--off);box-shadow:0 0 8px var(--off)}
@keyframes pulse{50%{opacity:.4}}
.plan{position:relative;background:var(--card);border:1px solid var(--line);border-radius:30px;padding:28px;text-align:center;transition:.3s}
.plan.hot{border:1px solid var(--gr1);box-shadow:0 0 40px #7c5cff44}
.plan .badge{position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:linear-gradient(90deg,var(--gr1),var(--gr2));padding:6px 14px;border-radius:999px;font-size:12px;font-weight:800;white-space:nowrap}
.plan .price{font-size:40px;font-weight:900;margin:16px 0 4px}
.plan .stars{color:var(--gr2);font-size:18px;font-weight:700;margin-bottom:14px}
.plan ul{list-style:none;text-align:left;color:var(--mut);font-size:14px;display:flex;flex-direction:column;gap:9px;margin:18px 0}
.plan li::before{content:'✓ ';color:var(--ok);font-weight:800}
.btn{display:block;width:100%;padding:14px;border-radius:16px;border:none;cursor:pointer;font-weight:800;font-size:15px;color:#fff;background:linear-gradient(90deg,var(--gr1),var(--gr2));transition:.3s}
.btn:hover{transform:translateY(-2px);box-shadow:0 0 30px #7c5cff66}
.switch{display:inline-flex;gap:4px;background:#0a0c1fd9;border:1px solid var(--line);border-radius:999px;padding:5px;margin-bottom:30px}
.switch button{padding:10px 22px;border-radius:999px;border:none;background:transparent;color:var(--mut);font-weight:700;cursor:pointer;font-size:14px;transition:.3s}
.switch button.on{background:linear-gradient(90deg,var(--gr1),var(--gr2));color:#fff}
.ip-box{max-width:480px;margin:0 auto;background:var(--card);border:1px solid var(--line);border-radius:28px;padding:30px;text-align:center}
.ip-addr{font-size:22px;font-weight:800;margin:14px 0}
.badge-ip{display:inline-flex;gap:8px;padding:9px 16px;border-radius:999px;font-weight:800;font-size:14px}
.badge-ip.safe{background:#0d2b20;color:var(--ok);border:1px solid var(--ok)}
.badge-ip.warn{background:#2b1218;color:var(--off);border:1px solid var(--off)}
.scanline{height:3px;width:100%;border-radius:3px;background:linear-gradient(90deg,transparent,var(--gr2),transparent);background-size:200% 100%;animation:scan 1.2s linear infinite;margin:16px 0;display:none}
@keyframes scan{to{background-position:-200% 0}}
.timer{font-size:34px;font-weight:900;letter-spacing:2px;background:linear-gradient(90deg,var(--gr3),var(--gr2));-webkit-background-clip:text;background-clip:text;color:transparent;margin-top:10px}
.discount{padding:30px;border-radius:28px;border:1px dashed var(--gr3);background:#1a0b14cc;text-align:center}
.marquee{overflow:hidden;position:relative;padding:12px 0}
.mq-track{display:flex;gap:18px;width:max-content;animation:mq 30s linear infinite}
@keyframes mq{to{transform:translateX(-50%)}}
.review{min-width:300px;background:var(--card);border:1px solid var(--line);border-radius:22px;padding:20px}
.review .stars{color:#ffc13d;font-size:15px}
.review p{color:var(--mut);font-size:13.5px;margin:10px 0;line-height:1.5}
.review .who{font-size:13px;font-weight:700}
.step{text-align:center}
.step .n{width:56px;height:56px;border-radius:50%;background:linear-gradient(90deg,var(--gr1),var(--gr2));display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:900;margin:0 auto 14px;box-shadow:0 0 26px #7c5cff55}
.calc{max-width:560px;margin:0 auto;background:var(--card);border:1px solid var(--line);border-radius:28px;padding:30px;text-align:center}
input[type=range]{width:100%;accent-color:var(--gr1);margin:18px 0}
.calc-res{font-size:26px;font-weight:900;margin-top:10px}
.calc .save{color:var(--ok);font-weight:800}
.counter{font-size:52px;font-weight:900;background:linear-gradient(90deg,var(--gr2),var(--gr1));-webkit-background-clip:text;background-clip:text;color:transparent}
.faq{max-width:720px;margin:0 auto}
.faq-item{background:var(--card);border:1px solid var(--line);border-radius:18px;margin-bottom:12px;overflow:hidden}
.faq-q{display:flex;justify-content:space-between;align-items:center;padding:18px 22px;cursor:pointer;font-weight:700}
.faq-q .ar{transition:.3s;color:var(--gr2)}
.faq-a{max-height:0;overflow:hidden;transition:max-height .35s;padding:0 22px;color:var(--mut);font-size:14.5px;line-height:1.6}
.faq-item.open .faq-a{max-height:300px;padding-bottom:18px}
.faq-item.open .ar{transform:rotate(180deg)}
.cabinet{max-width:520px;margin:0 auto;background:var(--card);border:1px solid var(--line);border-radius:28px;padding:30px;text-align:center}
.avatar{width:76px;height:76px;border-radius:50%;margin:0 auto 14px;background:linear-gradient(90deg,var(--gr1),var(--gr2));display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:900;color:#fff}
.cab-msg{padding:14px;border-radius:16px;margin-top:16px;font-weight:700;font-size:15px}
.cab-msg.no{background:#2b1218;color:var(--off);border:1px solid var(--off)}
.cab-msg.yes{background:#0d2b20;color:var(--ok);border:1px solid var(--ok)}
.cab-hidden{display:none}
.login-note{color:var(--mut);font-size:13px;margin-top:12px}
footer{background:#07081ad9;border-top:1px solid var(--line);padding:40px 0;position:relative;z-index:2}
.foot{display:flex;flex-wrap:wrap;gap:20px;justify-content:space-between;align-items:center;max-width:1180px;margin:0 auto;padding:0 22px}
.foot a{color:var(--mut);font-size:14px}
.foot a:hover{color:#fff}
.news-tick{overflow:hidden;border-top:1px solid var(--line);background:#0a0c1e;padding:10px 0;position:relative;z-index:2}
.news-track{display:flex;gap:50px;width:max-content;animation:mq 22s linear infinite;color:var(--mut);font-size:13.5px}
.float-btn{position:fixed;bottom:26px;right:26px;z-index:60;width:62px;height:62px;border-radius:50%;background:linear-gradient(135deg,var(--gr1),var(--gr3));display:flex;align-items:center;justify-content:center;font-size:26px;cursor:pointer;box-shadow:0 8px 30px #ff3d8188;animation:bounce 2s infinite}
@keyframes bounce{50%{transform:translateY(-6px)}}
.float-menu{position:fixed;bottom:100px;right:26px;z-index:60;display:none;flex-direction:column;gap:8px}
.float-menu.open{display:flex}
.float-menu a{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:12px 18px;font-size:14px;font-weight:700;white-space:nowrap;box-shadow:0 10px 30px #0008}
.doc{max-width:760px;margin:0 auto}
.doc h1{font-size:32px;margin-bottom:18px}
.doc p{margin:12px 0;color:var(--mut);line-height:1.7}
.doc h2{margin-top:26px;font-size:22px}
.back{display:inline-flex;gap:8px;color:var(--mut);margin-bottom:24px;font-size:14px}
@media(max-width:760px){.phone{transform:scale(.9)}}
</style>"""

def DOC(title):
    body = doc_body("terms" if title=="terms" else "privacy" if title=="privacy" else "refund")
    return R("""<!DOCTYPE html><html lang="ru"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t} — __SITE__</title><link rel="icon" href="data:image/svg+xml,...">
</head><body>
<div class="scene"><div class="g g1"></div><div class="g g2"></div><div class="g g3"></div></div>
<nav><div class="nav-in"><a class="logo" href="/"><div class="logo-badge"><span>🛡</span></div>__SITE__</a>
<div class="menu"><a href="/">Главная</a></div></div></nav>
<section><div class="wrap doc"><a class="back" href="/">← Вернуться на главную</a>
<h1 class="grad">{t}</h1>{body}</div></section>
<footer><div class="foot"><span>© __SITE__</span>
<a href="/terms">Условия</a><a href="/privacy">Конфиденциальность</a><a href="/refund">Возврат</a></div></footer>
</body></html>""".format(t=title, body=body))

def doc_body(kind):
    if kind == "terms":
        return R("""<h2>1. Общие положения</h2>
<p>Настоящие условия регулируют использование сервиса __SITE__ (далее — «Сервис»), предоставляемого __OPERATOR__.</p>
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
<p>Минимально необходимые данные: идентификатор Telegram-аккаунта и статус подписки.</p>
<h2>2. Использование данных</h2>
<p>Данные используются исключительно для предоставления услуг и поддержки.</p>
<h2>3. Передача третьим лицам</h2>
<p>Мы не продаём и не передаём персональные данные третьим лицам.</p>
<p>По вопросам: __EMAIL__.</p>""")
    return R("""<h2>1. Гарантия возврата</h2>
<p>Гарантия возврата средств в течение 7 дней с момента оплаты, если услуга не оказана надлежащим образом.</p>
<h2>2. Как оформить возврат</h2>
<p>Напишите оператору @__BOTU__ или на __EMAIL__, указав причину. Возврат тем же способом оплаты в течение 3–5 рабочих дней.</p>""")

@app.route("/")
def index():
    flags = [
        ("🇫🇮","Финляндия","on"),("🇵🇱","Польша","on"),("🇩🇪","Германия","on"),("🇳🇱","Нидерланды","on"),
        ("🇬🇧","Великобритания","on"),("🇺🇸","США","on"),("🇫🇷","Франция","on"),("🇸🇪","Швеция","on")]
    countries = ""
    for fl, nm, st in flags:
        countries += '<div class="country"><span class="fl">'+fl+'</span><span class="nm">'+nm+'</span><span class="dot '+st+'"></span></div>'

    apps = [
        ("📱","iOS","Happ · Streisand · Shadowrocket"),
        ("🤖","Android","Happ · v2rayTun · Hiddify"),
        ("🖥","Windows","Hiddify · v2rayN"),
        ("💻","macOS","Happ · Hiddify · FoXray"),
        ("📺","Android TV","Happ")]
    apps_html = ""
    for k, t, d in apps:
        apps_html += '<div class="card"><div class="k">'+k+'</div><h3>'+t+'</h3><p>'+d+'</p></div>'

    page = HEAD + """</head><body>
<div class="scene"><div class="g g1"></div><div class="g g2"></div><div class="g g3"></div>
<script>for(let i=0;i<45;i++){let s=document.createElement('div');s.className='star';s.style.left=Math.random()*100+'%';s.style.top=Math.random()*100+'%';s.style.animationDelay=Math.random()*4+'s';document.querySelector('.scene').appendChild(s)}</script></div>
<nav><div class="nav-in"><a class="logo" href="/"><div class="logo-badge"><span>🛡</span></div>__SITE__</a>
<div class="menu"><a href="#features">Возможности</a><a href="#plans">Тарифы</a><a href="#cabinet">Кабинет</a><a href="#faq">FAQ</a></div>
<div class="tg-login" id="tg-login"></div></div></nav>
<section class="hero"><div class="wrap center">
<span class="pill">🔥 <b>3 дня бесплатно</b> · от 139₽/мес · подключение за 1 минуту</span>
<h1>Ваши данные<br>под <span class="grad">защитой</span> уже сейчас</h1>
<p>Быстрый и приватный VPN в 8 странах мира. Один клик — и ваше соединение зашифровано.</p>
<div class="connect-wrap"><div class="connect" id="connect"><div class="spin-ring"></div>
<div class="in"><div class="ic">🔒</div><div class="st">Нажми, чтобы<br>подключиться</div></div>
<div class="load">Подключение…</div><div class="pro">🛡️ Ваши данные защищены</div></div></div>
</div></section>
<section class="phone-scene"><div class="wrap"><div class="phone">
<div class="notch"></div><div class="scr">
<div class="scr-head"><span>●</span><span>●●</span><span class="time">12:47</span></div>
<div class="scr-top"><div class="scr-title">Awesome VPN</div><div class="scr-logo">🛡</div></div>
<div class="scr-body">
<div class="scr-status" id="pstatus">Не подключено</div>
<div class="scr-sub" id="psub">Данные не защищены.<br>Нажми, чтобы подключиться</div>
<div class="phone-btn" id="pbtn"><div class="pi">⚡</div></div>
<div class="progress" id="pprog"><i></i></div>
<div class="tap-hint" id="ptap">Нажмите, чтобы подключиться</div>
</div></div></div></div></section>
<section id="features"><div class="wrap">
<div class="center"><h2 class="grad">Почему __SITE__?</h2><p class="sub">Максимальная защита без сложных настроек</p></div>
<div class="grid g3">
<div class="card"><div class="k">🚀</div><h3>Высокая скорость</h3><p>Оптимизированные серверы без ограничения трафика.</p></div>
<div class="card"><div class="k">🛡</div><h3>Военное шифрование</h3><p>AES-256 защищает ваши данные на любых сетях.</p></div>
<div class="card"><div class="k">🌍</div><h3>8 стран мира</h3><p>Финляндия, Польша, Германия, Нидерланды и другие.</p></div>
<div class="card"><div class="k">📶</div><h3>Без логов</h3><p>Мы не храним историю ваших подключений.</p></div>
<div class="card"><div class="k">📱</div><h3>Все устройства</h3><p>iOS, Android, Windows, macOS, Android TV.</p></div>
<div class="card"><div class="k">⚡</div><h3>Один клик</h3><p>Подключение за секунду, без технических знаний.</p></div>
</div></div></section>
<section><div class="wrap">
<div class="center"><h2 class="grad">Статус серверов</h2><p class="sub">Все страны доступны в реальном времени</p></div>
<div class="grid g4">""" + countries + """</div>
<div class="center" style="margin-top:26px"><a class="cta" href="__BOT__">Получить доступ в боте</a></div>
</div></section>
<section><div class="wrap">
<div class="center"><h2 class="grad">Проверь свой IP</h2><p class="sub">Узнай, защищено ли твоё соединение прямо сейчас</p></div>
<div class="ip-box"><div class="scanline" id="scanline"></div>
<div class="ip-addr" id="ipaddr">—</div>
<button class="btn" id="ipbtn" style="display:inline-block;width:auto;padding:12px 26px">Проверить мой IP</button>
<div style="margin-top:16px"><span class="badge-ip warn" id="ipbadge">⏳ Статус неизвестен</span></div>
</div></div></section>
<section><div class="wrap">
<div class="center"><h2 class="grad">Как подключиться</h2><p class="sub">Всего 3 шага до полной защиты</p></div>
<div class="grid g3">
<div class="step"><div class="n">1</div><h3>Установи приложение</h3><p>Выбери приложение под свою платформу.</p></div>
<div class="step"><div class="n">2</div><h3>Получи ключ в боте</h3><p>Бот @__BOTU__ выдаст ключ и подписку.</p></div>
<div class="step"><div class="n">3</div><h3>Нажми «Подключить»</h3><p>Готово — вы под защитой.</p></div>
</div></div></section>
<section><div class="wrap">
<div class="center"><h2 class="grad">Приложения</h2><p class="sub">Работает на любой платформе</p></div>
<div class="grid g3">""" + apps_html + """</div></div></section>
<section><div class="wrap">
<div class="center"><h2 class="grad">Калькулятор выгоды</h2><p class="sub">Выбери длительность и посчитай экономию</p></div>
<div class="calc">
<label style="font-weight:700">Длительность: <span id="cval">6 месяцев</span></label>
<input type="range" id="crange" min="1" max="6" value="6" step="1" style="display:block">
<div class="calc-res">💰 <span id="cprice">519₽</span> / <span id="cstars">364⭐</span></div>
<div class="save" id="csave">Вы экономите 297₽ против помесячной оплаты!</div>
</div></div></section>
<section><div class="wrap center">
<h2 class="grad">Тарифы</h2><p class="sub">Гибкие тарифы для любого количества устройств</p>
<div class="switch"><button data-cur="rub" class="on" onclick="setCur('rub')">₽ рубли</button><button data-cur="star" onclick="setCur('star')">⭐ звёзды</button></div>
<div class="grid g3" id="plans">
<div class="plan"><div class="badge">Популярный</div>
<h3>1 месяц</h3><div class="price" data-r="139" data-s="98">139₽</div><div class="stars" data-r="139₽" data-s="98⭐">или 98⭐</div>
<ul><li>3 устройства</li><li>8 стран</li><li>Без логов</li><li>Поддержка 24/7</li></ul><a class="btn" href="__BOT__">Купить</a></div>
<div class="plan hot"><div class="badge">Выгодно</div>
<h3>3 месяца</h3><div class="price" data-r="249" data-s="175">249₽</div><div class="stars" data-r="249₽" data-s="175⭐">или 175⭐</div>
<ul><li>3 устройства</li><li>8 стран</li><li>Без логов</li><li>Поддержка 24/7</li><li>−40% выгода</li></ul><a class="btn" href="__BOT__">Купить</a></div>
<div class="plan"><div class="badge">Максимум</div>
<h3>6 месяцев</h3><div class="price" data-r="519" data-s="364">519₽</div><div class="stars" data-r="519₽" data-s="364⭐">или 364⭐</div>
<ul><li>5 устройств</li><li>8 стран</li><li>Без логов</li><li>Поддержка 24/7</li><li>−38% выгода</li></ul><a class="btn" href="__BOT__">Купить</a></div>
</div></div></section>
<section><div class="wrap">
<div class="discount center"><h2 class="grad" style="font-size:22px">🔥 Горячая акция</h2>
<div class="timer" id="timer">00:00:00</div>
<p style="color:var(--mut);margin-top:10px">Скидка −30% на все тарифы до конца дня</p>
<div style="margin-top:18px"><a class="cta" href="__BOT__">Забрать скидку в боте</a></div></div></div></section>
<section id="cabinet"><div class="wrap">
<div class="center"><h2 class="grad">Личный кабинет</h2><p class="sub">Войди через Telegram, чтобы проверить подписку</p></div>
<div class="cabinet">
<div id="cab-login"><p style="color:var(--mut);margin-bottom:16px">Нажми кнопку ниже, чтобы войти через Telegram 👇</p>
<div id="tg-login-cab" style="display:flex;justify-content:center"></div></div>
<div id="cab-user" class="cab-hidden">
<div class="avatar" id="cab-ava">?</div><h3 id="cab-name">—</h3>
<p style="color:var(--mut);font-size:14px;margin-top:4px">@<span id="cab-username">—</span></p>
<div class="cab-msg no" id="cab-status">Подписка не найдена. Оформите её в боте 👉 <a href="__BOT__" style="color:var(--gr2);font-weight:800">@__BOTU__</a></div>
</div>
<div class="login-note" id="cab-note">После входа статус подписки отображается здесь.</div>
</div></div></section>
<section><div class="wrap">
<div class="center"><h2 class="grad">Партнёрская программа</h2><p class="sub">Зарабатывай 20% с каждого платежа</p></div>
<div class="card center" style="max-width:520px;margin:0 auto">
<div class="k">💸</div><h3>20% от каждого платежа</h3>
<p>Приглашай друзей через свою ссылку — получай 20% с каждой их оплаты. Выплаты в боте @__BOTU__.</p>
<div style="margin-top:18px"><a class="btn" href="__BOT__" style="display:inline-block;width:auto;padding:14px 30px">Стать партнёром</a></div>
</div></div></section>
<section><div class="wrap">
<div class="center"><h2 class="grad">Отзывы</h2><p class="sub">Нам доверяют тысячи пользователей</p></div>
<div class="marquee"><div class="mq-track" id="mq"></div></div></div></section>
<section id="faq"><div class="wrap">
<div class="center"><h2 class="grad">Частые вопросы</h2><p class="sub">Всё, что нужно знать о сервисе</p></div>
<div class="faq">
<div class="faq-item"><div class="faq-q">Как получить бесплатный пробный период?<span class="ar">▾</span></div><div class="faq-a">Напишите боту @__BOTU__ — новый пользователь получает 3 дня бесплатно.</div></div>
<div class="faq-item"><div class="faq-q">На скольких устройствах можно подключиться?<span class="ar">▾</span></div><div class="faq-a">Зависит от тарифа: 3 устройства на 1 и 3 месяца, 5 устройств на 6 месяцев.</div></div>
<div class="faq-item"><div class="faq-q">В каких странах есть серверы?<span class="ar">▾</span></div><div class="faq-a">Финляндия, Польша, Германия, Нидерланды, Великобритания, США, Франция, Швеция.</div></div>
<div class="faq-item"><div class="faq-q">Есть ли ограничение по трафику?<span class="ar">▾</span></div><div class="faq-a">Нет. Скорость и трафик не ограничиваются.</div></div>
<div class="faq-item"><div class="faq-q">Как оплатить тариф?<span class="ar">▾</span></div><div class="faq-a">В боте @__BOTU__ можно оплатить рублями или звёздами Telegram.</div></div>
<div class="faq-item"><div class="faq-q">Как работает возврат?<span class="ar">▾</span></div><div class="faq-a">Гарантия возврата 7 дней — напишите оператору в боте.</div></div>
</div></div></section>
<section><div class="wrap center">
<h2 class="grad">Уже сейчас защищены</h2>
<div class="counter" id="counter">0</div>
<p class="sub">человек уже используют __SITE__</p>
<div style="margin-top:20px"><a class="cta" href="__BOT__">Подключиться за 1 минуту</a></div></div></section>
<div class="news-tick"><div class="news-track" id="news">
<span>🌍 Добавлены новые серверы в Швеции</span><span>⚡ Скорость увеличена на 30%</span><span>🎁 Акция −30% до конца дня</span>
<span>🛡 Обновлено шифрование</span><span>📱 Поддержка Android TV</span></div></div>
<footer><div class="foot"><span>© __SITE__</span>
<a href="/terms">Условия</a><a href="/privacy">Конфиденциальность</a><a href="/refund">Возврат</a>
<a href="__SUPPORT__">Поддержка</a></div></footer>
<div class="float-menu" id="fmenu"><a href="__BOT__">🤖 Чат с ботом</a><a href="__SUPPORT__">✉️ Оператор</a></div>
<div class="float-btn" id="fbtn">💬</div>
<script>
(function(){var c=document.getElementById('connect'),st=c.querySelector('.st'),ic=c.querySelector('.ic');
c.addEventListener('click',function(){if(c.classList.contains('on')){c.classList.remove('on');ic.textContent='🔒';st.textContent='Нажми, чтобы подключиться';return}
c.classList.add('connecting');setTimeout(function(){c.classList.remove('connecting');c.classList.add('on');ic.textContent='🛡️'},2200);});})();
(function(){var b=document.getElementById('pbtn'),s=document.getElementById('pstatus'),u=document.getElementById('psub'),pg=document.getElementById('pprog'),bar=pg.querySelector('i'),tap=document.getElementById('ptap'),on=false,prog=0;
b.addEventListener('click',function(){
if(on){on=false;b.classList.remove('on');s.textContent='Не подключено';u.textContent='Данные не защищены. Нажми, чтобы подключиться';pg.style.display='none';tap.style.display='block';return}
if(b.classList.contains('connecting'))return;
b.classList.add('connecting');pg.style.display='block';tap.style.display='none';s.textContent='Подключение…';u.textContent='Устанавливаем безопасное соединение';prog=0;
var t=setInterval(function(){prog+=5;bar.style.width=prog+'%';if(prog>=100){clearInterval(t);b.classList.remove('connecting');b.classList.add('on');s.textContent='Подключено';u.textContent='Данные защищены 🛡️';pg.style.display='none';}},120);});})();
var cur='rub';
function setCur(c){cur=c;document.querySelectorAll('.price').forEach(function(p){p.textContent=(c==='rub'?p.dataset.r+'₽':p.dataset.s+'⭐')});
document.querySelectorAll('.stars').forEach(function(x){x.textContent=(c==='rub'?x.dataset.r+' или '+x.dataset.s+'⭐':x.dataset.s+' или '+x.dataset.r)});
document.querySelectorAll('.switch button').forEach(function(b){b.classList.toggle('on',b.dataset.cur===c)});}
(function(){var r=document.getElementById('crange'),cv=document.getElementById('cval'),cp=document.getElementById('cprice'),cs=document.getElementById('cstars'),sv=document.getElementById('csave');
var map={1:[139,98,0],2:[278,196,0],3:[249,175,89],6:[519,364,297]};
r.addEventListener('input',function(){var m=map[r.value];cv.textContent=(r.value==='6'?'6 месяцев':r.value+' месяц(а)');
cp.textContent=m[0]+'₽';cs.textContent=m[1]+'⭐';sv.textContent=m[2]>0?('Вы экономите '+m[2]+'₽ против помесячной оплаты!'):'Помесячная оплата без скидки';});})();
(function(){var end=Date.now()+((23-new Date().getHours())*3600+(59-new Date().getMinutes())*60+(59-new Date().getSeconds()))*1000;
setInterval(function(){var d=end-Date.now();if(d<0)d=0;var h=Math.floor(d/3600000),m=Math.floor(d%3600000/60000),s=Math.floor(d%60000/1000);
document.getElementById('timer').textContent=(h<10?'0':'')+h+':'+(m<10?'0':'')+m+':'+(s<10?'0':'')+s;},1000);})();
(function(){var el=document.getElementById('counter'),target=12847,t=0;var iv=setInterval(function(){t+=Math.ceil(target/80);if(t>=target){t=target;clearInterval(iv)}el.textContent=t.toLocaleString('ru-RU');},30);})();
document.getElementById('ipbtn').addEventListener('click',function(){var sl=document.getElementById('scanline'),ad=document.getElementById('ipaddr'),bg=document.getElementById('ipbadge');
sl.style.display='block';ad.textContent='Сканируем…';bg.textContent='⏳ Проверка…';bg.className='badge-ip warn';
setTimeout(function(){sl.style.display='none';var ok=Math.random()>.5;ad.textContent='185.64.'+Math.floor(Math.random()*255)+'.'+Math.floor(Math.random()*255);
if(ok){bg.textContent='🛡️ Ваш IP защищён';bg.className='badge-ip safe'}else{bg.textContent='⚠️ Не защищено — включите VPN';bg.className='badge-ip warn'}},1800);});
document.querySelectorAll('.faq-q').forEach(function(q){q.addEventListener('click',function(){q.parentElement.classList.toggle('open')})});
document.getElementById('fbtn').addEventListener('click',function(){document.getElementById('fmenu').classList.toggle('open')});
var revs=[['Дмитрий','Скорость огонь, подключается за секунду!'],['Анна','Наконец-то работаю безопасно из кафе.'],['Игорь','Простая настройка, всё за 1 минуту.'],['Мария','Лучший VPN, что пробовала.'],['Сергей','Поддержка отвечает мгновенно.']];
var track=document.getElementById('mq');revs.concat(revs).forEach(function(r){track.innerHTML+='<div class="review"><div class="stars">★★★★★</div><p>'+r[1]+'</p><div class="who">'+r[0]+'</div></div>';});
function onTelegramAuth(user){
document.getElementById('cab-login').style.display='none';document.getElementById('cab-note').style.display='none';
document.getElementById('cab-user').classList.remove('cab-hidden');
document.getElementById('cab-ava').textContent=(user.first_name||'?')[0];
document.getElementById('cab-name').textContent=user.first_name+(user.last_name?' '+user.last_name:'');
document.getElementById('cab-username').textContent=user.username||'—';
document.getElementById('tg-login').innerHTML='<span style="display:inline-flex;gap:8px;align-items:center;padding:8px 14px;border-radius:999px;border:1px solid var(--line);font-size:13px;font-weight:700">👤 '+user.first_name+'</span>';
var st=document.getElementById('cab-status');st.className='cab-msg no';
st.innerHTML='Подписка не найдена. Оформите её в боте 👉 <a href="__BOT__" style="color:var(--gr2);font-weight:800">@__BOTU__</a>';}
</script>
<script async src="https://telegram.org/js/telegram-login.js" data-telegram-login="__BOTU__" data-bot-id="__BOTID__" data-size="large" data-radius="12" data-onauth="onTelegramAuth(user)"></script>
</body></html>"""
    return R(page)

@app.route("/terms")
def terms():
    return DOC("terms")

@app.route("/privacy")
def privacy():
    return DOC("privacy")

@app.route("/refund")
def refund():
    return DOC("refund")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
