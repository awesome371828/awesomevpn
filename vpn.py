#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Awesome VPN — лендинг + анимация защиты + вход через Telegram + кабинет. relaxdev + Flask."""
import os
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)
PORT = int(os.getenv("PORT", 5000))

# ================== ТВОИ ДАННЫЕ ==================
SITE_NAME   = "Awesome VPN"
BOT         = "https://t.me/awesomeproxyvpn_bot"
SUPPORT_BOT = "https://t.me/flidges"
EMAIL       = "ffdfdfd44242ddd@gmail.com"
SITE_URL    = "awesomevpn.relaxdev.ru"
OPERATOR    = "AWESOME VPN LTE"
OP_COUNTRY  = "Germany"
SUPPORT_USERNAME = SUPPORT_BOT.rstrip("/").split("/")[-1]
# ===================================================

def R(html):
    return (html
        .replace("__SITE_NAME__", SITE_NAME)
        .replace("__BOT__", BOT)
        .replace("__SUPPORT_BOT__", SUPPORT_BOT)
        .replace("__SUPPORT_USERNAME__", SUPPORT_USERNAME)
        .replace("__EMAIL__", EMAIL)
        .replace("__SITE_URL__", SITE_URL)
        .replace("__OPERATOR__", OPERATOR)
        .replace("__OP_COUNTRY__", OP_COUNTRY)
    )

HEAD = r"""<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:'Söhne','Segoe UI',system-ui,sans-serif}
body{background:#07090d;color:#f0f4f8;-webkit-font-smoothing:antialiased;overflow-x:hidden}
::selection{background:rgba(34,224,168,.3)}
.scene{position:fixed;inset:0;z-index:-1;overflow:hidden;background:radial-gradient(120% 120% at 15% 10%,#0d2b24 0%,transparent 50%),radial-gradient(120% 120% at 85% 20%,#141a3d 0%,transparent 50%),radial-gradient(120% 120% at 50% 100%,#1b1030 0%,transparent 55%),#07090d}
.glow{position:absolute;border-radius:50%;filter:blur(85px);mix-blend-mode:screen;will-change:transform;animation:drift 20s ease-in-out infinite alternate}
.g1{width:540px;height:540px;background:radial-gradient(circle,#16d6a4,transparent 65%);top:-140px;left:-100px;opacity:.5}
.g2{width:480px;height:480px;background:radial-gradient(circle,#4f7dff,transparent 65%);bottom:-120px;right:-80px;opacity:.45}
.g3{width:400px;height:400px;background:radial-gradient(circle,#8b5cf6,transparent 65%);top:40%;left:55%;opacity:.35}
@keyframes drift{0%{transform:translate(0,0) scale(1)}100%{transform:translate(60px,40px) scale(1.15)}}
.star{position:absolute;width:3px;height:3px;border-radius:50%;background:#fff;opacity:.6;animation:tw 3s ease-in-out infinite}
@keyframes tw{0%,100%{opacity:.1;transform:scale(1)}50%{opacity:.9;transform:scale(1.5)}}
nav{display:flex;align-items:center;justify-content:space-between;padding:18px 6vw;max-width:1240px;margin:0 auto;position:sticky;top:0;z-index:50;backdrop-filter:blur(14px);background:rgba(7,9,13,.6);border-bottom:1px solid rgba(255,255,255,.07)}
.brand{display:flex;align-items:center;gap:11px;font-weight:800;font-size:19px}
.brand .logo{width:38px;height:38px;border-radius:50%;background:conic-gradient(from 180deg,#22e0a8,#4f7dff,#8b5cf6,#22e0a8);display:flex;align-items:center;justify-content:center;animation:spin 8s linear infinite;box-shadow:0 0 24px rgba(34,224,168,.4)}
@keyframes spin{to{transform:rotate(360deg)}}
.nav-links{display:flex;gap:22px;align-items:center;flex-wrap:wrap}
.nav-links a{color:#98a6b6;text-decoration:none;font-size:14px;transition:.2s}.nav-links a:hover{color:#fff}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 24px;border-radius:999px;border:none;cursor:pointer;font-weight:700;font-size:14px;text-decoration:none;transition:.25s}
.btn-green{background:linear-gradient(135deg,#22e0a8,#0d9d7a);color:#03140d;box-shadow:0 6px 24px rgba(34,224,168,.35)}.btn-green:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(34,224,168,.5)}
.btn-ghost{background:rgba(255,255,255,.07);color:#f0f4f8;border:1px solid rgba(255,255,255,.16)}.btn-ghost:hover{background:rgba(255,255,255,.13);transform:translateY(-2px)}
.hero{text-align:center;padding:8vh 24px 4vh;max-width:900px;margin:0 auto;animation:fadeUp .8s ease}
@keyframes fadeUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.hero h1{font-size:clamp(36px,6.5vw,60px);font-weight:800;line-height:1.06;background:linear-gradient(90deg,#22e0a8,#4f7dff,#8b5cf6,#ffb347,#22e0a8);background-size:300% auto;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;animation:gr 6s linear infinite;filter:drop-shadow(0 4px 30px rgba(34,224,168,.25))}
@keyframes gr{to{background-position:300% center}}
.hero p{color:#98a6b6;font-size:18px;margin:16px auto 26px;max-width:640px;line-height:1.6}
/* === Кнопка ПОДКЛЮЧИТЬ с анимацией === */
.connect-wrap{margin:0 auto 20px;display:flex;flex-direction:column;align-items:center;gap:14px}
.connect-btn{position:relative;width:150px;height:150px;border-radius:50%;border:none;cursor:pointer;background:conic-gradient(from 0deg,#22e0a8,#4f7dff,#8b5cf6,#ffb347,#22e0a8);display:flex;align-items:center;justify-content:center;transition:.3s;box-shadow:0 0 40px rgba(34,224,168,.4)}
.connect-btn::before{content:"";position:absolute;inset:7px;border-radius:50%;background:#0b1116;transition:.3s}
.connect-btn .inner{position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;gap:4px}
.connect-btn .ic{font-size:38px;transition:.3s}
.connect-btn .txt{font-size:13px;font-weight:700;color:#fff}
.connect-btn:hover{transform:scale(1.05);box-shadow:0 0 60px rgba(34,224,168,.6)}
.connect-btn.on{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{box-shadow:0 0 40px rgba(34,224,168,.4)}50%{box-shadow:0 0 70px rgba(34,224,168,.7)}}
.connect-status{font-size:14px;color:#98a6b6;min-height:22px;font-weight:600}
.connect-status.ok{color:#22e0a8}
.connect-status.loading{color:#ffb347}
/* спиннер загрузки */
.spinner{width:20px;height:20px;border:3px solid rgba(34,224,168,.2);border-top-color:#22e0a8;border-radius:50%;animation:spin2 1s linear infinite;display:inline-block;vertical-align:middle;margin-right:6px}
@keyframes spin2{to{transform:rotate(360deg)}}
.protected-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(34,224,168,.12);border:1px solid rgba(34,224,168,.4);color:#22e0a8;padding:8px 18px;border-radius:999px;font-weight:700;font-size:14px;animation:pop .4s ease}
@keyframes pop{from{transform:scale(.6);opacity:0}to{transform:scale(1);opacity:1}}
/* === Кабинет / вход через Telegram === */
.cab{max-width:560px;margin:40px auto 0;background:rgba(18,23,32,.6);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.09);border-radius:28px;padding:32px;text-align:center}
.cab h3{font-size:22px;font-weight:800;margin-bottom:8px}
.cab .sub{color:#98a6b6;font-size:14px;margin-bottom:22px}
.tg-login{display:flex;align-items:center;justify-content:center;gap:10px;background:#229ed9;color:#fff;padding:14px;border-radius:14px;text-decoration:none;font-weight:700;font-size:15px;transition:.2s}.tg-login:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(34,158,217,.4)}
.tg-login svg{width:22px;height:22px}
.sub-status{margin-top:20px;padding:18px;border-radius:16px;background:rgba(0,0,0,.25);border:1px solid rgba(255,255,255,.08);text-align:center}
.sub-status .badge{display:inline-block;padding:6px 16px;border-radius:999px;font-weight:700;font-size:13px;margin-bottom:10px}
.badge.no{background:rgba(255,92,122,.15);color:#ff5c7a;border:1px solid rgba(255,92,122,.4)}
.badge.yes{background:rgba(34,224,168,.15);color:#22e0a8;border:1px solid rgba(34,224,168,.4)}
.sub-status .exp{color:#98a6b6;font-size:14px;line-height:1.6}
.countries{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:22px}
.cflag{background:rgba(18,23,32,.55);border:1px solid rgba(255,255,255,.09);border-radius:14px;padding:8px 14px;font-size:13px;color:#c6d0dc;display:inline-flex;gap:7px;align-items:center}.cflag b{color:#fff}
.stats{display:flex;gap:20px;justify-content:center;flex-wrap:wrap;max-width:940px;margin:0 auto;padding:5vh 24px}
.stat{flex:1;min-width:130px;background:rgba(18,23,32,.55);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.09);border-radius:26px;padding:26px 16px;text-align:center;transition:.25s}.stat:hover{transform:translateY(-6px);border-color:rgba(34,224,168,.5)}
.stat .n{font-size:40px;font-weight:800;background:linear-gradient(90deg,#22e0a8,#4f7dff);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.stat .l{color:#98a6b6;font-size:14px;margin-top:8px}
.section{max-width:1120px;margin:0 auto;padding:7vh 24px}
.section h2{text-align:center;font-size:clamp(30px,4.5vw,42px);font-weight:800;margin-bottom:14px;background:linear-gradient(90deg,#fff,#c6d0dc);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.section .sub{text-align:center;color:#98a6b6;font-size:17px;margin-bottom:40px}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:22px}
.step{background:rgba(18,23,32,.55);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.09);border-radius:28px;padding:30px;position:relative;transition:.25s;overflow:hidden}.step:hover{transform:translateY(-6px);border-color:rgba(34,224,168,.5)}
.step .num{font-size:52px;font-weight:800;color:rgba(34,224,168,.2);position:absolute;top:16px;right:24px}
.step h3{margin:14px 0 9px;font-size:19px}.step p{color:#98a6b6;font-size:14.5px;line-height:1.65}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:22px}
.card{background:rgba(18,23,32,.55);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.09);border-radius:28px;padding:30px;transition:.25s;position:relative;overflow:hidden}.card:hover{transform:translateY(-6px);border-color:rgba(34,224,168,.5)}
.card .ic{font-size:32px;margin-bottom:14px}.card h3{margin-bottom:9px;font-size:18px}.card p{color:#98a6b6;font-size:14.5px;line-height:1.65}
.plans{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:24px;align-items:start}
.plan{background:rgba(18,23,32,.55);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.09);border-radius:30px;padding:34px;text-align:center;position:relative;transition:.28s}.plan:hover{transform:translateY(-8px)}
.plan.popular{border-color:rgba(34,224,168,.6);box-shadow:0 0 50px rgba(34,224,168,.15)}
.badge{position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,#22e0a8,#4f7dff);color:#03140d;font-size:12px;font-weight:800;padding:6px 16px;border-radius:999px;white-space:nowrap}
.plan h3{font-size:21px;margin-bottom:6px}.plan .dur{color:#98a6b6;font-size:14px;margin-bottom:20px}
.plan .price{font-size:46px;font-weight:800;background:linear-gradient(90deg,#22e0a8,#4f7dff);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.plan .stars{color:#ffd76a;font-size:17px;margin:8px 0 4px}.plan .per{color:#98a6b6;font-size:13px;margin-bottom:20px}
.plan ul{list-style:none;text-align:left;margin:0 0 24px;font-size:14px;color:#c6d0dc}
.plan li{padding:8px 0;border-bottom:1px solid rgba(255,255,255,.06)}.plan li::before{content:"✓ ";color:#22e0a8;font-weight:800}
.faq{max-width:780px;margin:0 auto}
.faq-item{background:rgba(18,23,32,.55);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.09);border-radius:20px;margin-bottom:14px;overflow:hidden}
.faq-q{padding:20px 24px;cursor:pointer;font-weight:600;font-size:15.5px;display:flex;justify-content:space-between;align-items:center;gap:12px}
.faq-q .plus{color:#22e0a8;font-size:24px;transition:transform .3s;flex-shrink:0;width:26px;height:26px;border-radius:50%;background:rgba(34,224,168,.12);display:flex;align-items:center;justify-content:center}
.faq-a{max-height:0;overflow:hidden;transition:max-height .35s ease;color:#98a6b6;font-size:14.5px;line-height:1.65}
.faq-item.open .faq-a{max-height:400px;padding:0 24px 22px}
.faq-item.open .plus{transform:rotate(45deg)}
.cta{text-align:center;padding:8vh 24px}
.cta h2{font-size:clamp(30px,4.5vw,44px);font-weight:800;margin-bottom:14px;background:linear-gradient(90deg,#22e0a8,#4f7dff);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.cta p{color:#98a6b6;font-size:17px;margin-bottom:30px}
footer{border-top:1px solid rgba(255,255,255,.08);padding:52px 6vw 28px;max-width:1240px;margin:0 auto}
.foot-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:30px;margin-bottom:36px}
.foot-grid h4{color:#fff;font-size:15px;margin-bottom:16px}
.foot-grid a{display:block;color:#98a6b6;text-decoration:none;font-size:13.5px;margin-bottom:10px;transition:.2s}.foot-grid a:hover{color:#22e0a8}
.foot-bottom{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px;color:#6b7684;font-size:13px;border-top:1px solid rgba(255,255,255,.06);padding-top:24px}
.status{display:inline-flex;align-items:center;gap:8px;color:#98a6b6;font-size:13px}
.dot{width:10px;height:10px;border-radius:50%;background:#22e0a8;box-shadow:0 0 12px #22e0a8;animation:pulse 2s infinite}
.float-support{position:fixed;bottom:24px;right:24px;z-index:99;width:60px;height:60px;border-radius:50%;background:linear-gradient(135deg,#22e0a8,#4f7dff);color:#03140d;display:flex;align-items:center;justify-content:center;font-size:26px;box-shadow:0 8px 30px rgba(34,224,168,.5);cursor:pointer;text-decoration:none;transition:.25s}.float-support:hover{transform:scale(1.12)}
.doc{max-width:860px;margin:0 auto;padding:7vh 24px 9vh}
.doc .crumb{color:#98a6b6;font-size:13px;margin-bottom:26px}.doc .crumb a{color:#22e0a8;text-decoration:none}
.doc h1{font-size:clamp(28px,4vw,40px);font-weight:800;margin-bottom:8px}
.doc .upd{color:#6b7684;font-size:13px;margin-bottom:34px}
.doc h2{font-size:20px;font-weight:700;margin:30px 0 12px;color:#22e0a8}
.doc p{color:#c6d0dc;font-size:15px;line-height:1.7;margin-bottom:14px}
.doc .op{background:rgba(34,224,168,.08);border:1px solid rgba(34,224,168,.3);border-radius:18px;padding:16px 20px;color:#22e0a8;font-weight:600;font-size:14px;margin-top:30px}
@media(max-width:768px){.nav-links{display:none}.hero{padding-top:5vh}}
</style>"""

BG = r"""<div class="scene">
<div class="glow g1"></div><div class="glow g2"></div><div class="glow g3"></div>
<div class="star" style="left:10%;top:15%;animation-delay:0s"></div>
<div class="star" style="left:22%;top:70%;animation-delay:1.2s"></div>
<div class="star" style="left:40%;top:30%;animation-delay:.5s"></div>
<div class="star" style="left:60%;top:80%;animation-delay:2s"></div>
<div class="star" style="left:75%;top:20%;animation-delay:1.5s"></div>
<div class="star" style="left:88%;top:55%;animation-delay:.8s"></div>
</div>"""

NAV = r"""<nav>
<div class="brand"><div class="logo"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 2L20 6V12C20 16.4 16.6 20.4 12 22C7.4 20.4 4 16.4 4 12V6L12 2Z" fill="#0a1a14"/><path d="M9 12L11 14L15 10" stroke="#22e0a8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>__SITE_NAME__</div>
<div class="nav-links"><a href="/#how">Как работает</a><a href="/#plans">Тарифы</a><a href="/#cab">Кабинет</a><a href="/#faq">FAQ</a></div>
<a class="btn btn-green" href="__BOT__" target="_blank">Открыть бота</a>
</nav>"""

FOOT = r"""<footer>
<div class="foot-grid">
<div><h4>Продукт</h4><a href="/#how">Как работает</a><a href="/#plans">Тарифы</a><a href="/#cab">Кабинет</a></div>
<div><h4>Документы</h4><a href="/terms">Соглашение</a><a href="/privacy">Конфиденциальность</a><a href="/refund">Возврат</a></div>
<div><h4>Контакты</h4><a href="__BOT__" target="_blank">Telegram-бот</a><a href="__SUPPORT_BOT__" target="_blank">Поддержка @__SUPPORT_USERNAME__</a></div>
</div>
<div class="foot-bottom"><div>© 2026 __SITE_NAME__. Все права защищены.</div><div class="status"><span class="dot"></span>Все системы работают</div></div>
</footer>"""

FLOAT = r"""<a class="float-support" href="__SUPPORT_BOT__" target="_blank" title="Поддержка">💬</a>"""

LANDING = r"""<!DOCTYPE html><html lang="ru"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__SITE_NAME__ — интернет без границ</title>
<meta name="theme-color" content="#07090d">
<meta name="description" content="Быстрый VPN на протоколе VLESS. 8 стран, минимальный пинг, обход блокировок. От 139₽/мес.">
__HEAD__</head><body>
__BG____NAV__
<section class="hero">
<h1>Интернет без границ</h1>
<p>Шифруем твой трафик и не ведём логи. Подключайся в один тап — и ты под защитой.</p>

<div class="connect-wrap">
<button class="connect-btn" id="connectBtn" onclick="toggleConnect()">
<div class="inner"><span class="ic" id="connIc">🔒</span><span class="txt" id="connTxt">Подключить</span></div>
</button>
<div class="connect-status" id="connStatus">Нажми, чтобы защитить соединение</div>
</div>

<div class="cab" id="cab">
<h3>👤 Личный кабинет</h3>
<p class="sub">Войди через Telegram, чтобы увидеть статус подписки</p>
<a class="tg-login" href="__BOT__" target="_blank">
<svg viewBox="0 0 24 24" fill="#fff"><path d="M9.78 18.65l.28-4.23 7.68-6.92c.34-.31-.07-.46-.52-.19L7.74 13.3 3.64 12c-.88-.25-.89-.86.2-1.3l15.97-6.16c.73-.33 1.43.18 1.15 1.3l-2.72 12.81c-.19.91-.74 1.13-1.5.71L12.6 16.3l-1.99 1.93c-.23.23-.42.42-.83.42z"/></svg>
Войти через Telegram
</a>
<div class="sub-status" id="subStatus">
<div class="badge no" id="subBadge">Подписка не найдена</div>
<div class="exp" id="subExp">Войди в бота @awesomeproxyvpn_bot, чтобы активировать подписку или пробный период.</div>
</div>
</div>

<div class="countries">
<span class="cflag">🇫🇮 <b>Финляндия</b></span><span class="cflag">🇵🇱 <b>Польша</b></span>
<span class="cflag">🇩🇪 <b>Германия</b></span><span class="cflag">🇳🇱 <b>Нидерланды</b></span>
<span class="cflag">🇬🇧 <b>Великобритания</b></span><span class="cflag">🇺🇸 <b>США</b></span>
<span class="cflag">🇫🇷 <b>Франция</b></span><span class="cflag">🇸🇪 <b>Швеция</b></span>
</div>
</section>

<section class="stats">
<div class="stat"><div class="n">8</div><div class="l">стран</div></div>
<div class="stat"><div class="n">∞</div><div class="l">трафик</div></div>
<div class="stat"><div class="n">0</div><div class="l">логов</div></div>
<div class="stat"><div class="n">1</div><div class="l">минута</div></div>
<div class="stat"><div class="n">24/7</div><div class="l">поддержка</div></div>
</section>

<section class="section" id="how">
<h2>Как это работает</h2><p class="sub">Три шага — и ты под защитой</p>
<div class="steps">
<div class="step"><div class="num">01</div><h3>Открой бота</h3><p>Жми кнопку или ищи @awesomeproxyvpn_bot. Регистрация за минуту.</p></div>
<div class="step"><div class="num">02</div><h3>Выбери тариф</h3><p>Купи подписку или активируй пробный период. Без карты.</p></div>
<div class="step"><div class="num">03</div><h3>Подключись</h3><p>Установи приложение, нажми кнопку — и ты под защитой.</p></div>
</div>
</section>

<section class="section" id="plans">
<h2>Тарифы</h2><p class="sub">Простые цены. Оплата прямо в боте.</p>
<div class="plans">
<div class="plan"><h3>1 месяц</h3><div class="dur">Гибко</div><div class="price">139 ₽</div><div class="stars">⭐ 98</div><div class="per">3 устройства</div><ul><li>Безлимит трафика</li><li>Все 8 локаций</li><li>До 3 устройств</li></ul><a class="btn btn-ghost" style="width:100%" href="__BOT__" target="_blank">Выбрать</a></div>
<div class="plan popular"><div class="badge">Популярный</div><h3>3 месяца</h3><div class="dur">Выгодно</div><div class="price">249 ₽</div><div class="stars">⭐ 175</div><div class="per">3 устройства</div><ul><li>Безлимит трафика</li><li>Все 8 локаций</li><li>До 3 устройств</li></ul><a class="btn btn-green" style="width:100%" href="__BOT__" target="_blank">Выбрать</a></div>
<div class="plan"><h3>6 месяцев</h3><div class="dur">Максимум</div><div class="price">519 ₽</div><div class="stars">⭐ 364</div><div class="per">5 устройств</div><ul><li>Безлимит трафика</li><li>Все 8 локаций</li><li>До 5 устройств</li></ul><a class="btn btn-ghost" style="width:100%" href="__BOT__" target="_blank">Выбрать</a></div>
</div>
</section>

<section class="section" id="faq">
<h2>FAQ</h2><p class="sub">Частые вопросы</p>
<div class="faq">
<div class="faq-item"><div class="faq-q">Как это защищает меня?<span class="plus">+</span></div><div class="faq-a">Весь трафик идёт через зашифрованный туннель. Провайдер и сторонние сервисы не видят, что ты делаешь, а IP скрыт.</div></div>
<div class="faq-item"><div class="faq-q">Вы храните логи?<span class="plus">+</span></div><div class="faq-a">Нет. Мы не ведём логи и не храним историю посещений.</div></div>
<div class="faq-item"><div class="faq-q">Есть ли пробный период?<span class="plus">+</span></div><div class="faq-a">Да, первые 3 дня бесплатно. Просто открой бота.</div></div>
<div class="faq-item"><div class="faq-q">На каких устройствах работает?<span class="plus">+</span></div><div class="faq-a">iOS, Android, Windows, macOS, Android TV. Happ, v2rayTun, Hiddify и другие.</div></div>
<div class="faq-item"><div class="faq-q">Можно ли отменить подписку?<span class="plus">+</span></div><div class="faq-a">Да, в любой момент. Доступ останется до конца оплаченного периода.</div></div>
</div>
</section>

<section class="cta">
<h2>Готов попробовать?</h2><p>Первые 3 дня — бесплатно.</p>
<a class="btn btn-green" href="__BOT__" target="_blank">🚀 Открыть Telegram-бота</a>
</section>
__FOOT____FLOAT__
<script>
const connectBtn=$c('connectBtn'),connIc=$c('connIc'),connTxt=$c('connTxt'),connStatus=$c('connStatus');
function $c(id){return document.getElementById(id)}
let on=false;
function toggleConnect(){
  if(on){ off(); return }
  on=true;
  connectBtn.classList.add('on');
  connIc.textContent='🛡️';
  connTxt.textContent='Защита...';
  connStatus.className='connect-status loading';
  connStatus.innerHTML='<span class="spinner"></span>Устанавливаем защищённое соединение...';
  setTimeout(()=>{
    connIc.textContent='✅';
    connTxt.textContent='Подключено';
    connStatus.className='connect-status ok';
    connStatus.innerHTML='<span class="protected-badge">🛡️ Ваши данные защищены</span>';
  },2200);
}
function off(){
  on=false;
  connectBtn.classList.remove('on');
  connIc.textContent='🔒';
  connTxt.textContent='Подключить';
  connStatus.className='connect-status';
  connStatus.textContent='Соединение отключено';
}
document.querySelectorAll('.faq-q').forEach(q=>q.addEventListener('click',()=>q.parentElement.classList.toggle('open')));
</script>
</body></html>"""

def DOC(title, updated, body):
    return r"""<!DOCTYPE html><html lang="ru"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__SITE_NAME__ — """ + title + r"""</title><meta name="theme-color" content="#07090d">__HEAD__</head><body>
__BG____NAV__
<div class="doc">
<div class="crumb">← <a href="/">На главную</a> · Все документы</div>
<h1>""" + title + r"""</h1><div class="upd">Последнее обновление: """ + updated + r"""</div>
""" + body + r"""
<div class="op">По вопросам о правовых политиках: __EMAIL__.<br>Оператор: __OPERATOR__.</div>
</div>
__FOOT____FLOAT__
</body></html>"""

TERMS_BODY = r"""<p>Настоящее Пользовательское соглашение (далее — «Соглашение») является публичной офертой и определяет условия использования сервиса __SITE_NAME__.</p>
<h2>1. Предмет соглашения</h2><p>1.1. Администрация предоставляет доступ к Сервису на условиях настоящего Соглашения.</p><p>1.2. Пользователь, используя Telegram-бот @awesomeproxyvpn_bot и сайт __SITE_URL__, подтверждает согласие с условиями Соглашения.</p><p>1.3. Оператором Сервиса является __OPERATOR__ (__OP_COUNTRY__).</p>
<h2>2. Описание сервиса</h2><p>2.1. __SITE_NAME__ предоставляет сервис виртуальной частной сети.</p><p>2.2. Регистрация и управление подпиской осуществляются через Telegram-бот @awesomeproxyvpn_bot.</p>
<h2>3. Правила использования</h2><p>3.1. Запрещается использование Сервиса для противоправной деятельности.</p><p>3.2. Администрация вправе ограничить доступ при нарушении условий.</p>
<h2>4. Платные услуги и возврат</h2><p>4.1. Доступ предоставляется по подписке.</p><p>4.2. Условия возврата указаны в Политике возврата средств.</p>
<h2>5. Ответственность</h2><p>5.1. Сервис предоставляется «как есть».</p><p>5.2. Пользователь несёт ответственность за свои действия.</p>
<h2>6. Обработка данных</h2><p>6.1. Данные обрабатываются согласно Политике конфиденциальности.</p>
<h2>7. Контакты</h2><p>Оператор: __OPERATOR__ (__OP_COUNTRY__). Поддержка: __EMAIL__ и @__SUPPORT_USERNAME__.</p>"""

PRIVACY_BODY = r"""<h2>1. Общие положения</h2><p>Настоящая Политика определяет порядок обработки персональных данных пользователей __SITE_NAME__.</p><p>Оператор: __OPERATOR__ (__OP_COUNTRY__). Контакт: __EMAIL__.</p>
<h2>2. Состав информации</h2><p>2.1. Telegram ID, имя пользователя, дата регистрации, статус подписки.</p><p>2.2. __SITE_NAME__ не хранит историю посещений, DNS-запросы и содержимое трафика.</p>
<h2>3. Цели обработки</h2><p>3.1. Предоставление доступа, поддержка, безопасность.</p>
<h2>4. Безопасность</h2><p>4.1. Применяются технические меры защиты данных.</p>
<h2>5. Передача третьим лицам</h2><p>5.1. Платёжным и хостинг-провайдерам, аналитике (в обезличенном виде).</p>
<h2>6. Права пользователя</h2><p>6.1. Доступ, исправление, удаление, переносимость данных. Запросы на __EMAIL__.</p>"""

REFUND_BODY = r"""<h2>1. Общие положения</h2><p>1.1. Политика определяет условия возврата средств за подписку __SITE_NAME__.</p>
<h2>2. Срок оказания услуги</h2><p>2.1. Доступ предоставляется после оплаты, не позднее 3 календарных дней.</p>
<h2>3. Основания для возврата</h2><p>3.1. Неоказание услуги — возврат в полном объёме.</p><p>3.2. Отказ до активации — возврат в полном объёме.</p><p>3.3. Отказ после активации — возврат за неиспользованные дни.</p>
<h2>4. Срок подачи</h2><p>4.1. Заявление подаётся в течение оплаченного срока подписки.</p>
<h2>5. Форма подачи</h2><p>5.1. Заявление на __EMAIL__ или в поддержку @__SUPPORT_USERNAME__.</p>
<h2>6. Срок рассмотрения</h2><p>6.1. 10 рабочих дней.</p>
<h2>7. Возврат средств</h2><p>7.1. В течение 10 рабочих дней на те же реквизиты.</p>
<h2>8. Исключения</h2><p>8.1. Возврат не производится при нарушении Соглашения.</p>"""

def build_landing():
    return R(LANDING.replace("__HEAD__", HEAD).replace("__BG__", BG).replace("__NAV__", NAV).replace("__FOOT__", FOOT).replace("__FLOAT__", FLOAT))

def build_doc(title, updated, body):
    t = DOC(title, updated, body)
    return R(t.replace("__HEAD__", HEAD).replace("__BG__", BG).replace("__NAV__", NAV).replace("__FOOT__", FOOT).replace("__FLOAT__", FLOAT))

@app.route('/')
def index(): return build_landing()
@app.route('/terms')
def terms(): return build_doc("Пользовательское соглашение (оферта)", "25 июля 2026", TERMS_BODY)
@app.route('/privacy')
def privacy(): return build_doc("Политика конфиденциальности", "25 июля 2026", PRIVACY_BODY)
@app.route('/refund')
def refund(): return build_doc("Политика возврата денежных средств", "25 июля 2026", REFUND_BODY)

@app.route('/favicon.ico')
def favicon():
    svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22e0a8"/><stop offset="1" stop-color="#4f7dff"/></linearGradient></defs><rect width="24" height="24" rx="12" fill="url(#g)"/><path d="M12 4 L19 7 V12 C19 15.3 16.3 18.4 12 19.6 C7.7 18.4 5 15.3 5 12 V7 Z" fill="#0a1a14"/><path d="M9 12 L11 14 L15 10" stroke="#22e0a8" stroke-width="1.6" fill="none" stroke-linecap="round"/></svg>'
    return app.response_class(svg, mimetype='image/svg+xml')

if __name__ == '__main__':
    print("Awesome VPN — лендинг + защита + кабинет")
    app.run(host='0.0.0.0', port=PORT, debug=False)
