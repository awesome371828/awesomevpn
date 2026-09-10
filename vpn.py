#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Awesome VPN — премиум лендинг + документы + инструкции + партнёрка. relaxdev + Flask."""
import os
from flask import Flask, render_template_string

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
.btn-gold{background:linear-gradient(120deg,#ffd76a,#ffb347);color:#241503}.btn-gold:hover{transform:translateY(-2px);box-shadow:0 8px 26px rgba(255,180,70,.4)}
.hero{text-align:center;padding:9vh 24px 5vh;max-width:880px;margin:0 auto;animation:fadeUp .8s ease}
@keyframes fadeUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.hero h1{font-size:clamp(36px,6.5vw,60px);font-weight:800;line-height:1.06;background:linear-gradient(90deg,#22e0a8,#4f7dff,#8b5cf6,#ffb347,#22e0a8);background-size:300% auto;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;animation:gr 6s linear infinite;filter:drop-shadow(0 4px 30px rgba(34,224,168,.25))}
@keyframes gr{to{background-position:300% center}}
.hero p{color:#98a6b6;font-size:18px;margin:18px auto 30px;max-width:640px;line-height:1.6}
.hero-actions{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.trial{display:inline-block;margin-top:22px;padding:8px 18px;border-radius:999px;background:rgba(255,215,106,.12);border:1px solid rgba(255,215,106,.35);color:#ffd76a;font-weight:600;font-size:14px}
.countries{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:26px}
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
.step::before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#22e0a8,#4f7dff);opacity:0;transition:.3s}.step:hover::before{opacity:1}
.step .num{font-size:52px;font-weight:800;color:rgba(34,224,168,.2);position:absolute;top:16px;right:24px}
.step h3{margin:14px 0 9px;font-size:19px}.step p{color:#98a6b6;font-size:14.5px;line-height:1.65}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:22px}
.card{background:rgba(18,23,32,.55);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.09);border-radius:28px;padding:30px;transition:.25s;position:relative;overflow:hidden}.card:hover{transform:translateY(-6px);border-color:rgba(34,224,168,.5)}
.card::after{content:"";position:absolute;width:120px;height:120px;border-radius:50%;background:radial-gradient(circle,rgba(34,224,168,.15),transparent 70%);top:-30px;right:-30px}
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
/* Активация / инструкция */
.activate{max-width:820px;margin:0 auto;display:grid;gap:16px}
.act-step{display:flex;gap:18px;align-items:flex-start;background:rgba(18,23,32,.55);border:1px solid rgba(255,255,255,.09);border-radius:22px;padding:22px;transition:.2s}.act-step:hover{border-color:rgba(34,224,168,.5);transform:translateX(4px)}
.act-step .an{flex-shrink:0;width:44px;height:44px;border-radius:14px;background:linear-gradient(135deg,#22e0a8,#4f7dff);color:#03140d;font-weight:800;font-size:20px;display:flex;align-items:center;justify-content:center}
.act-step h3{font-size:17px;margin-bottom:5px}.act-step p{color:#98a6b6;font-size:14px;line-height:1.55}
.apps{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;max-width:820px;margin:0 auto}
.app{border:1px solid rgba(255,255,255,.09);background:rgba(18,23,32,.55);border-radius:18px;padding:18px;text-align:center}.app .os{font-size:24px}.app b{display:block;margin:8px 0 6px}.app span{color:#98a6b6;font-size:13px;display:block;line-height:1.5}
/* Партнёрка */
.partner{max-width:820px;margin:0 auto;text-align:center;background:linear-gradient(135deg,rgba(255,215,106,.08),rgba(34,224,168,.08));border:1px solid rgba(255,215,106,.3);border-radius:30px;padding:44px}
.partner h2{font-size:clamp(28px,4vw,38px);font-weight:800;background:linear-gradient(90deg,#ffd76a,#ffb347);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:12px}
.partner p{color:#c6d0dc;font-size:16px;margin-bottom:24px;line-height:1.6}
.partner .pct{font-size:54px;font-weight:800;color:#ffd76a;line-height:1}
.partner .plink{display:inline-block;margin-top:22px;padding:12px 26px;border-radius:999px;background:rgba(255,255,255,.08);border:1px dashed rgba(255,255,255,.25);color:#fff;font-size:14px}
.pstats{display:flex;gap:22px;justify-content:center;flex-wrap:wrap;margin-top:26px}
.pstat{background:rgba(0,0,0,.25);border:1px solid rgba(255,255,255,.1);border-radius:18px;padding:18px 30px}.pstat .n{font-size:30px;font-weight:800;color:#ffd76a}.pstat .l{color:#98a6b6;font-size:13px;margin-top:4px}
.faq{max-width:780px;margin:0 auto}
.faq-item{background:rgba(18,23,32,.55);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.09);border-radius:20px;margin-bottom:14px;overflow:hidden;transition:.2s}
.faq-q{padding:20px 24px;cursor:pointer;font-weight:600;font-size:15.5px;display:flex;justify-content:space-between;align-items:center;gap:12px}
.faq-q .plus{color:#22e0a8;font-size:24px;transition:transform .3s;flex-shrink:0;width:26px;height:26px;border-radius:50%;background:rgba(34,224,168,.12);display:flex;align-items:center;justify-content:center}
.faq-a{max-height:0;overflow:hidden;transition:max-height .35s ease;color:#98a6b6;font-size:14.5px;line-height:1.65}
.faq-item.open .faq-a{max-height:400px;padding:0 24px 22px}
.faq-item.open .plus{transform:rotate(45deg);background:rgba(34,224,168,.25)}
.reviews{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;max-width:900px;margin:0 auto}
.rev{background:rgba(18,23,32,.55);border:1px solid rgba(255,255,255,.09);border-radius:22px;padding:24px}.rev .stars{color:#ffd76a;font-size:16px;margin-bottom:10px}.rev p{color:#c6d0dc;font-size:14px;line-height:1.6;font-style:italic}.rev .who{color:#98a6b6;font-size:13px;margin-top:12px;font-weight:600}
.cta{text-align:center;padding:9vh 24px}
.cta h2{font-size:clamp(30px,4.5vw,44px);font-weight:800;margin-bottom:14px;background:linear-gradient(90deg,#22e0a8,#4f7dff);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.cta p{color:#98a6b6;font-size:17px;margin-bottom:30px}
footer{border-top:1px solid rgba(255,255,255,.08);padding:52px 6vw 28px;max-width:1240px;margin:0 auto}
.foot-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:30px;margin-bottom:36px}
.foot-grid h4{color:#fff;font-size:15px;margin-bottom:16px}
.foot-grid a{display:block;color:#98a6b6;text-decoration:none;font-size:13.5px;margin-bottom:10px;transition:.2s}.foot-grid a:hover{color:#22e0a8;transform:translateX(3px)}
.foot-bottom{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px;color:#6b7684;font-size:13px;border-top:1px solid rgba(255,255,255,.06);padding-top:24px}
.status{display:inline-flex;align-items:center;gap:8px;color:#98a6b6;font-size:13px}
.dot{width:10px;height:10px;border-radius:50%;background:#22e0a8;box-shadow:0 0 12px #22e0a8;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.35}}
.doc{max-width:860px;margin:0 auto;padding:7vh 24px 9vh}
.doc .crumb{color:#98a6b6;font-size:13px;margin-bottom:26px}.doc .crumb a{color:#22e0a8;text-decoration:none}
.doc h1{font-size:clamp(28px,4vw,40px);font-weight:800;margin-bottom:8px}
.doc .upd{color:#6b7684;font-size:13px;margin-bottom:34px}
.doc h2{font-size:20px;font-weight:700;margin:30px 0 12px;color:#22e0a8}
.doc p{color:#c6d0dc;font-size:15px;line-height:1.7;margin-bottom:14px}
.doc .op{background:rgba(34,224,168,.08);border:1px solid rgba(34,224,168,.3);border-radius:18px;padding:16px 20px;color:#22e0a8;font-weight:600;font-size:14px;margin-top:30px}
/* float support */
.float-support{position:fixed;bottom:24px;right:24px;z-index:99;width:60px;height:60px;border-radius:50%;background:linear-gradient(135deg,#22e0a8,#4f7dff);color:#03140d;display:flex;align-items:center;justify-content:center;font-size:26px;box-shadow:0 8px 30px rgba(34,224,168,.5);cursor:pointer;text-decoration:none;transition:.25s}.float-support:hover{transform:scale(1.12)}
@media(max-width:768px){.nav-links{display:none}.hero{padding-top:6vh}}
</style>"""

BG = r"""<div class="scene">
<div class="glow g1"></div><div class="glow g2"></div><div class="glow g3"></div>
<div class="star" style="left:10%;top:15%;animation-delay:0s"></div>
<div class="star" style="left:22%;top:70%;animation-delay:1.2s"></div>
<div class="star" style="left:40%;top:30%;animation-delay:.5s"></div>
<div class="star" style="left:60%;top:80%;animation-delay:2s"></div>
<div class="star" style="left:75%;top:20%;animation-delay:1.5s"></div>
<div class="star" style="left:88%;top:55%;animation-delay:.8s"></div>
<div class="star" style="left:55%;top:10%;animation-delay:2.4s"></div>
<div class="star" style="left:8%;top:45%;animation-delay:1.8s"></div>
<div class="star" style="left:70%;top:65%;animation-delay:.3s"></div>
<div class="star" style="left:30%;top:55%;animation-delay:2.8s"></div>
</div>"""

NAV = r"""<nav>
<div class="brand"><div class="logo"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 2L20 6V12C20 16.4 16.6 20.4 12 22C7.4 20.4 4 16.4 4 12V6L12 2Z" fill="#0a1a14"/><path d="M9 12L11 14L15 10" stroke="#22e0a8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>__SITE_NAME__</div>
<div class="nav-links"><a href="/#how">Как работает</a><a href="/#features">Возможности</a><a href="/#plans">Тарифы</a><a href="/#setup">Подключение</a><a href="/#partner">Партнёрам</a><a href="/#faq">FAQ</a></div>
<a class="btn btn-green" href="__BOT__" target="_blank">Открыть бота</a>
</nav>"""

FOOT = r"""<footer>
<div class="foot-grid">
<div><h4>Продукт</h4><a href="/#how">Как работает</a><a href="/#features">Возможности</a><a href="/#plans">Тарифы</a><a href="/#setup">Подключение</a></div>
<div><h4>Документы</h4><a href="/terms">Пользовательское соглашение</a><a href="/privacy">Политика конфиденциальности</a><a href="/refund">Возврат средств</a><a href="/aup">Допустимое использование</a></div>
<div><h4>Контакты</h4><a href="/contacts">Контакты</a><a href="__BOT__" target="_blank">Telegram-бот</a><a href="__SUPPORT_BOT__" target="_blank">Поддержка @__SUPPORT_USERNAME__</a></div>
</div>
<div class="foot-bottom"><div>© 2026 __SITE_NAME__. Все права защищены.</div><div class="status"><span class="dot"></span>Все системы работают</div></div>
</footer>"""

FLOAT = r"""<a class="float-support" href="__SUPPORT_BOT__" target="_blank" title="Поддержка">💬</a>"""

LANDING = r"""<!DOCTYPE html><html lang="ru"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__SITE_NAME__ — интернет без границ</title>
<meta name="theme-color" content="#07090d">
<meta name="description" content="Быстрый VPN на протоколе VLESS. 8 стран, минимальный пинг для игр, обход блокировок. От 139₽/мес. Тестовый период 3 дня.">
<meta property="og:title" content="__SITE_NAME__ — интернет без границ">
<meta property="og:description" content="Быстрый VPN. От 139₽/мес. Тестовый период 3 дня.">
__HEAD__</head><body>
__BG____NAV__
<section class="hero">
<h1>Интернет без границ</h1>
<p>Быстрый VPN на современном протоколе VLESS. Обход блокировок без снижения скорости, минимальный пинг для игр, безлимит трафика.</p>
<div class="hero-actions">
<a class="btn btn-green" href="__BOT__" target="_blank">🚀 Подключиться за 1 минуту</a>
<a class="btn btn-ghost" href="#plans">Посмотреть тарифы</a>
</div>
<div class="trial">🎁 Тестовый период — 3 дня бесплатно</div>
<div class="countries">
<span class="cflag">🇫🇮 <b>Финляндия</b></span>
<span class="cflag">🇵🇱 <b>Польша</b></span>
<span class="cflag">🇩🇪 <b>Германия</b></span>
<span class="cflag">🇳🇱 <b>Нидерланды</b></span>
<span class="cflag">🇬🇧 <b>Великобритания</b></span>
<span class="cflag">🇺🇸 <b>США</b></span>
<span class="cflag">🇫🇷 <b>Франция</b></span>
<span class="cflag">🇸🇪 <b>Швеция</b></span>
</div>
</section>

<section class="stats">
<div class="stat"><div class="n">8</div><div class="l">стран на выбор</div></div>
<div class="stat"><div class="n">∞</div><div class="l">трафик</div></div>
<div class="stat"><div class="n">0</div><div class="l">логов</div></div>
<div class="stat"><div class="n">1</div><div class="l">минута до защиты</div></div>
<div class="stat"><div class="n">24/7</div><div class="l">поддержка</div></div>
</section>

<section class="section" id="how">
<h2>Как это работает</h2><p class="sub">Три шага — и ты под защитой</p>
<div class="steps">
<div class="step"><div class="num">01</div><h3>Открой бота в Telegram</h3><p>Жми кнопку на странице или ищи @awesomeproxyvpn_bot. Регистрация прямо в чате, за минуту.</p></div>
<div class="step"><div class="num">02</div><h3>Выбери тариф</h3><p>Купи подписку или активируй пробный период на 3 дня. Карта не нужна.</p></div>
<div class="step"><div class="num">03</div><h3>Включи защиту</h3><p>Нажми «📱 Настроить VPN», выбери сервер и подключись. Одна кнопка — и всё.</p></div>
</div>
</section>

<section class="section" id="features">
<h2>Возможности</h2><p class="sub">Всё для приватности — и ничего лишнего</p>
<div class="grid">
<div class="card"><div class="ic">🔒</div><h3>Без логов</h3><p>Не храним историю и не следим за твоим трафиком. Что ты делаешь в сети — знаешь только ты.</p></div>
<div class="card"><div class="ic">⚡</div><h3>Минимальный пинг</h3><p>Оптимальные маршруты до серверов — отлично подходит для игр и стримов.</p></div>
<div class="card"><div class="ic">🛡️</div><h3>Шифрование трафика</h3><p>Современный протокол VLESS. Данные идут через зашифрованный туннель, который не прочитать.</p></div>
<div class="card"><div class="ic">🌍</div><h3>8 стран на выбор</h3><p>Финляндия, Польша, Германия и другие. Быстрые сервера в каждой локации.</p></div>
<div class="card"><div class="ic">📱</div><h3>Работает везде</h3><p>Happ, v2rayTun, Hiddify, Streisand, Shadowrocket, v2rayN и другие клиенты.</p></div>
<div class="card"><div class="ic">🆘</div><h3>Живая поддержка</h3><p>Реальная помощь 24/7. Пиши @__SUPPORT_USERNAME__ — поможем с любым вопросом.</p></div>
</div>
</section>

<section class="section" id="plans">
<h2>Тарифы</h2><p class="sub">Простые цены. Без сюрпризов. Оплата прямо в боте.</p>
<div class="plans">
<div class="plan">
<h3>1 месяц</h3><div class="dur">Гибко, помесячно</div>
<div class="price">139 ₽</div><div class="stars">⭐ 98</div><div class="per">Безлимит трафика · 3 устройства</div>
<ul><li>Полный доступ на месяц</li><li>Безлимит по трафику</li><li>До 3 устройств</li><li>Все 8 локаций</li></ul>
<a class="btn btn-ghost" style="width:100%" href="__BOT__" target="_blank">Выбрать 1 месяц</a>
</div>
<div class="plan popular"><div class="badge">Популярный</div>
<h3>3 месяца</h3><div class="dur">Выгодно</div>
<div class="price">249 ₽</div><div class="stars">⭐ 175</div><div class="per">Безлимит трафика · 3 устройства</div>
<ul><li>Полный доступ на 3 месяца</li><li>Безлимит по трафику</li><li>До 3 устройств</li><li>Все 8 локаций</li></ul>
<a class="btn btn-green" style="width:100%" href="__BOT__" target="_blank">Выбрать 3 месяца</a>
</div>
<div class="plan">
<h3>6 месяцев</h3><div class="dur">Максимум выгоды</div>
<div class="price">519 ₽</div><div class="stars">⭐ 364</div><div class="per">Безлимит трафика · 5 устройств</div>
<ul><li>Полный доступ на 6 месяцев</li><li>Безлимит по трафику</li><li>До 5 устройств</li><li>Все 8 локаций</li></ul>
<a class="btn btn-ghost" style="width:100%" href="__BOT__" target="_blank">Выбрать 6 месяцев</a>
</div>
</div>
</section>

<section class="section" id="setup">
<h2>Как подключиться</h2><p class="sub">4 простых шага — и ты онлайн</p>
<div class="activate">
<div class="act-step"><div class="an">1</div><div><h3>Купи подписку или активируй пробный период</h3><p>Тестовый период — 3 дня бесплатно. Карта не нужна.</p></div></div>
<div class="act-step"><div class="an">2</div><div><h3>Открой свою страницу подписки</h3><p>Нажми кнопку «📱 Настроить VPN» в боте.</p></div></div>
<div class="act-step"><div class="an">3</div><div><h3>Установи приложение и нажми кнопку</h3><p>Подписка добавится автоматически, ничего вводить вручную не нужно.</p></div></div>
<div class="act-step"><div class="an">4</div><div><h3>Выбери сервер и подключись</h3><p>Готово! Ты под защитой ✅</p></div></div>
</div>
<h2 style="margin-top:56px">Рекомендуемые приложения</h2>
<div class="apps">
<div class="app"><div class="os">📱</div><b>iOS</b><span>Happ, Streisand, Shadowrocket</span></div>
<div class="app"><div class="os">🤖</div><b>Android</b><span>Happ, v2rayTun, Hiddify</span></div>
<div class="app"><div class="os">💻</div><b>Windows</b><span>Hiddify, v2rayN</span></div>
<div class="app"><div class="os">🍏</div><b>macOS</b><span>Happ, Hiddify, FoXray</span></div>
<div class="app"><div class="os">📺</div><b>Android TV</b><span>Happ</span></div>
</div>
<p class="sub" style="margin-top:26px">На странице подписки есть кнопки скачивания и пошаговая инструкция для каждой платформы.</p>
</section>

<section class="section" id="partner">
<div class="partner">
<h2>👥 Партнёрская программа</h2>
<p>Приглашайте друзей и получайте <b>20% с каждой их оплаты</b> прямо на свой баланс 💸</p>
<div class="pct">20%</div>
<p style="margin-top:18px">Ваша персональная ссылка генерируется автоматически в Telegram-боте</p>
<div class="plink">🔗 https://t.me/awesomeproxyvpn_bot?start=ваш_код</div>
<div class="pstats">
<div class="pstat"><div class="n">0</div><div class="l">Приглашено друзей</div></div>
<div class="pstat"><div class="n">0 ₽</div><div class="l">Заработано</div></div>
</div>
<div style="margin-top:26px"><a class="btn btn-gold" href="__BOT__" target="_blank">Начать зарабатывать</a></div>
</div>
</section>

<section class="section" id="reviews">
<h2>Что говорят пользователи</h2><p class="sub">Реальные отзывы</p>
<div class="reviews">
<div class="rev"><div class="stars">★★★★★</div><p>«Подключился за минуту, пинг в играх отличный. Лучший VPN из тех, что пробовал!»</p><div class="who">— Игорь</div></div>
<div class="rev"><div class="stars">★★★★★</div><p>«Всё работает стабильно, скорость не падает. Поддержка отвечает быстро.»</p><div class="who">— Мария</div></div>
<div class="rev"><div class="stars">★★★★★</div><p>«Оформил 3 дня бесплатно, понравилось — продлил на полгода. Рекомендую!»</p><div class="who">— Дмитрий</div></div>
</div>
</section>

<section class="section" id="faq">
<h2>FAQ</h2><p class="sub">Частые вопросы</p>
<div class="faq">
<div class="faq-item"><div class="faq-q">Как это защищает меня?<span class="plus">+</span></div><div class="faq-a">Весь твой трафик проходит через зашифрованный туннель. Провайдер и сторонние сервисы не видят, что ты делаешь в сети, а реальный IP скрыт.</div></div>
<div class="faq-item"><div class="faq-q">Вы храните логи?<span class="plus">+</span></div><div class="faq-a">Нет. Мы не ведём логи и не храним историю посещений. Приватность — наш главный принцип.</div></div>
<div class="faq-item"><div class="faq-q">Есть ли бесплатный тестовый период?<span class="plus">+</span></div><div class="faq-a">Да! Первые 3 дня — бесплатно. Карта не нужна, просто открой бота и активируй пробный период.</div></div>
<div class="faq-item"><div class="faq-q">На каких устройствах работает?<span class="plus">+</span></div><div class="faq-a">iOS, Android, Windows, macOS и Android TV. Работает в Happ, v2rayTun, Hiddify, Streisand и других клиентах.</div></div>
<div class="faq-item"><div class="faq-q">Как получить 20% за приглашения?<span class="plus">+</span></div><div class="faq-a">Участвуй в партнёрской программе: твоя ссылка в боте, приглашай друзей и получай 20% с каждой их оплаты на баланс.</div></div>
<div class="faq-item"><div class="faq-q">Можно ли отменить подписку?<span class="plus">+</span></div><div class="faq-a">Да, в любой момент — без звонков и переписок. Доступ останется до конца оплаченного периода.</div></div>
</div>
</section>

<section class="cta">
<h2>Готов попробовать?</h2><p>Подключайся через Telegram — первые 3 дня бесплатно и без карты.</p>
<a class="btn btn-green" href="__BOT__" target="_blank">🚀 Подключиться за 1 минуту</a>
</section>
__FOOT____FLOAT__
<script>document.querySelectorAll('.faq-q').forEach(q=>q.addEventListener('click',()=>q.parentElement.classList.toggle('open')));</script>
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
<div class="op">По вопросам о правовых политиках: __EMAIL__ или Telegram-бот.<br>Оператор: __OPERATOR__.</div>
</div>
__FOOT____FLOAT__
</body></html>"""

TERMS_BODY = r"""<p>Настоящее Пользовательское соглашение (далее — «Соглашение») является публичной офертой и определяет условия использования сервиса __SITE_NAME__ (далее — «Сервис») между Администрацией Сервиса (далее — «Администрация») и пользователем (далее — «Пользователь»).</p>
<h2>1. Предмет соглашения</h2>
<p>1.1. Администрация предоставляет Пользователю доступ к Сервису и его функционалу на условиях, изложенных в настоящем Соглашении.</p>
<p>1.2. Пользователь, используя Telegram-бот @awesomeproxyvpn_bot и сайт __SITE_URL__, подтверждает своё полное и безоговорочное согласие с условиями настоящего Соглашения.</p>
<p>1.3. Настоящее Соглашение является юридически обязательным документом.</p>
<p>1.4. Оператором Сервиса является __OPERATOR__ (__OP_COUNTRY__).</p>
<h2>2. Описание сервиса</h2>
<p>2.1. __SITE_NAME__ предоставляет сервис виртуальной частной сети, обеспечивающий шифрование интернет-соединения и защиту данных Пользователя при передаче через сеть Интернет.</p>
<p>2.2. Регистрация и управление подпиской осуществляются исключительно через Telegram-бот @awesomeproxyvpn_bot. Один Telegram-аккаунт соответствует одной учётной записи.</p>
<p>2.3. Перечень функций Сервиса может быть изменён Администрацией без предварительного уведомления Пользователя.</p>
<h2>3. Правила использования</h2>
<p>3.1. Пользователь обязуется использовать Сервис исключительно в соответствии с его целевым назначением и в рамках применимого законодательства.</p>
<p>3.2. Пользователю запрещается: пытаться получить несанкционированный доступ к информации и инфраструктуре Сервиса; использовать Сервис для распространения вредоносного ПО, спама или иной незаконной информации; вмешиваться в работу Сервиса; нарушать права третьих лиц; передавать доступ к учётной записи третьим лицам.</p>
<p>3.3. Администрация вправе ограничить или прекратить доступ Пользователя в случае нарушения им условий Соглашения без компенсации.</p>
<h2>4. Платные услуги и возврат средств</h2>
<p>4.1. Доступ к Сервису предоставляется на платной основе по подписке.</p>
<p>4.2. Оплата осуществляется через сторонние платёжные системы. __SITE_NAME__ не хранит платёжные реквизиты Пользователей.</p>
<p>4.3. Доступ к оплаченной подписке предоставляется автоматически сразу после подтверждения оплаты, но не позднее 3 (трёх) календарных дней с момента поступления средств.</p>
<p>4.4. Если доступ не был предоставлен в указанный срок, Пользователь вправе потребовать возврата в полном объёме.</p>
<p>4.5. Пользователь вправе отказаться от услуги: до начала её оказания — с возвратом в полном объёме; после активации — с возвратом стоимости неиспользованных дней пропорционально.</p>
<p>4.6. Подробные условия возврата приведены в Политике возврата денежных средств.</p>
<h2>5. Ответственность сторон</h2>
<p>5.1. Сервис предоставляется «как есть». Администрация не несёт ответственности за убытки Пользователя, возникшие в результате использования Сервиса, в том числе за сбои в работе Telegram, действия третьих лиц и временную недоступность Сервиса.</p>
<p>5.2. Пользователь несёт полную ответственность за свои действия при использовании Сервиса.</p>
<h2>6. Обработка персональных данных</h2>
<p>6.1. Администрация обязуется соблюдать конфиденциальность персональных данных Пользователя. Подробная информация содержится в Политике конфиденциальности.</p>
<h2>7. Разрешение споров</h2>
<p>7.1. Настоящее Соглашение регулируется правом страны регистрации Оператора. Все споры разрешаются в порядке, предусмотренном применимым законодательством.</p>
<p>7.2. Настоящее Соглашение не ограничивает права Пользователя как потребителя, предоставленные ему императивными нормами законодательства страны его постоянного проживания.</p>
<h2>8. Контактная информация</h2>
<p>Оператор Сервиса: __OPERATOR__ (__OP_COUNTRY__). Поддержка: __EMAIL__ и через Telegram-бот @__SUPPORT_USERNAME__.</p>"""

PRIVACY_BODY = r"""<h2>1. Общие положения</h2>
<p>Настоящая Политика конфиденциальности определяет порядок сбора, использования, хранения и защиты персональных данных пользователей сервиса __SITE_NAME__ (далее — «Сервис»).</p>
<p>Оператором (контролёром) персональных данных является __OPERATOR__, __OP_COUNTRY__. Контакт по вопросам обработки персональных данных — __EMAIL__.</p>
<p>Факт использования сайта __SITE_URL__ и Telegram-бота @awesomeproxyvpn_bot является полным и безоговорочным согласием с настоящей Политикой. Если Пользователь не согласен с её условиями, ему следует прекратить использование Сервиса.</p>
<h2>2. Источники и состав информации</h2>
<p>2.1. Персональные данные: Telegram ID пользователя; имя пользователя (username); язык интерфейса; дата регистрации; статус подписки.</p>
<p>2.2. Технические данные: тип устройства; версия приложения; IP-адрес; регион подключения (без точного местоположения).</p>
<p>2.3. __SITE_NAME__ не обрабатывает и не хранит: историю посещения сайтов; DNS-запросы; содержимое интернет-трафика.</p>
<h2>3. Цели обработки</h2>
<p>3.1. Персональные данные обрабатываются для: предоставления доступа к Сервису и управления подпиской; технической поддержки; обеспечения стабильной работы и безопасности Сервиса.</p>
<p>3.2. Обработка осуществляется на основании согласия Пользователя, исполнения договора, исполнения правовых обязанностей оператора и законного интереса оператора.</p>
<h2>4. Безопасность и хранение</h2>
<p>4.1. Оператор применяет технические и организационные меры защиты персональных данных.</p>
<p>4.2. Персональные данные хранятся в течение срока использования Сервиса и удаляются по запросу Пользователя, если иное не предусмотрено применимым законодательством.</p>
<h2>5. Передача данных третьим лицам</h2>
<p>Передача данных возможна: платёжным провайдерам; хостинг-провайдерам; аналитическим сервисам (в обезличенном виде). Передача через Telegram осуществляется в соответствии с политикой Telegram.</p>
<h2>6. Права пользователя</h2>
<p>Пользователь имеет право: получить доступ к своим данным; потребовать исправления неточных данных; потребовать удаления данных; потребовать ограничения обработки; получить данные в машиночитаемом формате; возразить против обработки; отозвать ранее данное согласие.</p>
<p>Запросы направляются на __EMAIL__ либо в Telegram-бот поддержки. Ответ предоставляется в течение 30 календарных дней.</p>
<h2>7. Заключительные положения</h2>
<p>Условия Политики могут быть изменены Администрацией в одностороннем порядке. Актуальная версия публикуется на сайте __SITE_URL__.</p>"""

REFUND_BODY = r"""<h2>1. Общие положения</h2>
<p>1.1. Настоящая Политика возврата является неотъемлемой частью Пользовательского соглашения __SITE_NAME__ и определяет условия и порядок возврата средств за подписку.</p>
<p>1.2. Настоящая Политика не ограничивает права Пользователя как потребителя, предоставленные ему императивными нормами законодательства страны его постоянного проживания.</p>
<h2>2. Срок оказания услуги</h2>
<p>2.1. Услугой является предоставление доступа к оплаченной подписке __SITE_NAME__.</p>
<p>2.2. Доступ предоставляется автоматически сразу после подтверждения оплаты, но не позднее 3 (трёх) календарных дней с момента поступления средств. С момента предоставления доступа услуга считается оказанной.</p>
<h2>3. Основания для возврата</h2>
<p>3.1. Неоказание услуги. Если доступ не был предоставлен в срок, Пользователь вправе потребовать возврата в полном объёме.</p>
<p>3.2. Отказ до начала оказания услуги. Если доступ ещё не активирован, возврат производится в полном объёме.</p>
<p>3.3. Отказ после активации доступа. Возвращается стоимость неиспользованных дней подписки пропорционально их количеству.</p>
<h2>4. Срок подачи заявления</h2>
<p>4.1. Заявление по основанию п. 3.1 подаётся в течение 14 (четырнадцати) календарных дней с даты истечения срока оказания услуги.</p>
<p>4.2. Заявление об отказе по основаниям п. 3.2 и п. 3.3 подаётся в течение оплаченного срока подписки.</p>
<h2>5. Форма подачи заявления</h2>
<p>5.1. Заявление направляется: на электронную почту __EMAIL__; в Telegram-бот поддержки @__SUPPORT_USERNAME__.</p>
<p>5.2. В заявлении указываются: данные учётной записи; номер платежа (операции, чека); дата и сумма платежа; причина возврата.</p>
<h2>6. Срок рассмотрения</h2>
<p>6.1. Заявление рассматривается в течение 10 (десяти) рабочих дней с момента его получения. О результате Пользователь уведомляется тем же способом, которым было подано заявление.</p>
<h2>7. Срок и порядок возврата</h2>
<p>7.1. При положительном решении средства возвращаются в течение 10 (десяти) рабочих дней с даты одобрения.</p>
<p>7.2. Возврат производится на те же реквизиты, с которых была совершена оплата.</p>
<p>7.3. По основаниям п. 3.1 и п. 3.2 возврат производится в полном объёме.</p>
<h2>8. Исключения</h2>
<p>8.1. Возврат не осуществляется при нарушении Пользователем Пользовательского соглашения или Политики допустимого использования.</p>"""

AUP_BODY = r"""<p>Настоящая Политика допустимого использования (Acceptable Use Policy) устанавливает правила, которые Пользователь обязан соблюдать при использовании сервиса __SITE_NAME__.</p>
<h2>1. Разрешённое использование</h2>
<p>1.1. Сервис предназначен для законного использования: доступа к сети Интернет, защиты соединения, обхода географических ограничений и обеспечения приватности.</p>
<h2>2. Запрещённое использование</h2>
<p>2.1. Запрещается использовать Сервис для: распространения вредоносного ПО и вирусов; проведения DDoS-атак; незаконного доступа к системам (взлома); распространения спама; торговли незаконными товарами; детской порнографии; террористической деятельности и любых иных противоправных действий.</p>
<p>2.2. Запрещается использовать Сервис для нарушения прав интеллектуальной собственности третьих лиц.</p>
<h2>3. Последствия нарушений</h2>
<p>3.1. При нарушении настоящей Политики Администрация вправе немедленно приостановить или прекратить доступ Пользователя к Сервису без предварительного уведомления и без компенсации.</p>
<p>3.2. Администрация вправе сообщать о противоправной деятельности в правоохранительные органы в соответствии с применимым законодательством.</p>
<h2>4. Прочие условия</h2>
<p>4.1. Настоящая Политика является неотъемлемой частью Пользовательского соглашения.</p>
<p>4.2. Администрация вправе изменять настоящую Политику в одностороннем порядке. Актуальная версия публикуется на сайте __SITE_URL__.</p>"""

CONTACTS_BODY = r"""<h2>Контакты</h2>
<p>Оператор Сервиса: __OPERATOR__ (__OP_COUNTRY__).</p>
<p>Поддержка Пользователей осуществляется по электронной почте и через Telegram-бот поддержки.</p>
<h2>Каналы связи</h2>
<p>• Telegram-бот: <b>@awesomeproxyvpn_bot</b> — покупка и настройка подписки</p>
<p>• Поддержка: <b>@__SUPPORT_USERNAME__</b> — ответим на любые вопросы</p>
<p>• Электронная почта: <b>__EMAIL__</b> — официальные обращения</p>
<h2>Время работы</h2>
<p>Поддержка работает круглосуточно (24/7). Среднее время ответа — до 15 минут.</p>
<h2>Вопросы</h2>
<p>По вопросам работы сервиса, оплаты, подключения и возврата — пишите в поддержку @__SUPPORT_USERNAME__.</p>"""

def build_landing():
    return R(LANDING.replace("__HEAD__", HEAD).replace("__BG__", BG).replace("__NAV__", NAV).replace("__FOOT__", FOOT).replace("__FLOAT__", FLOAT))

def build_doc(title, updated, body):
    t = DOC(title, updated, body)
    t = t.replace("__HEAD__", HEAD).replace("__BG__", BG).replace("__NAV__", NAV).replace("__FOOT__", FOOT).replace("__FLOAT__", FLOAT)
    return R(t)

@app.route('/')
def index(): return build_landing()
@app.route('/terms')
def terms(): return build_doc("Пользовательское соглашение (оферта)", "25 июля 2026", TERMS_BODY)
@app.route('/privacy')
def privacy(): return build_doc("Политика конфиденциальности", "25 июля 2026", PRIVACY_BODY)
@app.route('/refund')
def refund(): return build_doc("Политика возврата денежных средств", "25 июля 2026", REFUND_BODY)
@app.route('/aup')
def aup(): return build_doc("Политика допустимого использования", "25 июля 2026", AUP_BODY)
@app.route('/contacts')
def contacts(): return build_doc("Контакты", "25 июля 2026", CONTACTS_BODY)

@app.route('/favicon.ico')
def favicon():
    svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22e0a8"/><stop offset="1" stop-color="#4f7dff"/></linearGradient></defs><rect width="24" height="24" rx="12" fill="url(#g)"/><path d="M12 4 L19 7 V12 C19 15.3 16.3 18.4 12 19.6 C7.7 18.4 5 15.3 5 12 V7 Z" fill="#0a1a14"/><path d="M9 12 L11 14 L15 10" stroke="#22e0a8" stroke-width="1.6" fill="none" stroke-linecap="round"/></svg>'
    return app.response_class(svg, mimetype='image/svg+xml')

if __name__ == '__main__':
    print("Awesome VPN — лендинг + документы + инструкции + партнёрка")
    app.run(host='0.0.0.0', port=PORT, debug=False)
