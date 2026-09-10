#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Awesome VPN — премиум лендинг + юридические документы. relaxdev + Flask."""
import os
from flask import Flask, render_template_string, request

app = Flask(__name__)
PORT = int(os.getenv("PORT", 5000))

# ================== РЕДАКТИРУЙ ЭТО ==================
SITE_NAME   = "Awesome VPN"
BOT         = "https://t.me/awesomeproxyvpn_bot"      # главный бот
SUPPORT_BOT = "https://t.me/awesomeproxyvpn_support"  # бот поддержки (замени)
EMAIL       = "support@awesomevpn.site"               # почта поддержки (замени)
SITE_URL    = "https://awesomevpn.site"               # твой домен (замени)
OPERATOR    = "AWESOME VPN LTD"                       # название оператора (замени)
OP_COUNTRY  = "Великобритания"                        # юрисдикция оператора
# =====================================================

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
.nav-links{display:flex;gap:26px;align-items:center}
.nav-links a{color:#98a6b6;text-decoration:none;font-size:14px;transition:.2s}.nav-links a:hover{color:#fff}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 24px;border-radius:999px;border:none;cursor:pointer;font-weight:700;font-size:14px;text-decoration:none;transition:.25s}
.btn-green{background:linear-gradient(135deg,#22e0a8,#0d9d7a);color:#03140d;box-shadow:0 6px 24px rgba(34,224,168,.35)}.btn-green:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(34,224,168,.5)}
.btn-ghost{background:rgba(255,255,255,.07);color:#f0f4f8;border:1px solid rgba(255,255,255,.16)}.btn-ghost:hover{background:rgba(255,255,255,.13);transform:translateY(-2px)}
.hero{text-align:center;padding:10vh 24px 6vh;max-width:880px;margin:0 auto;animation:fadeUp .8s ease}
@keyframes fadeUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
.hero h1{font-size:clamp(36px,6.5vw,60px);font-weight:800;line-height:1.06;background:linear-gradient(90deg,#22e0a8,#4f7dff,#8b5cf6,#ffb347,#22e0a8);background-size:300% auto;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;animation:gr 6s linear infinite;filter:drop-shadow(0 4px 30px rgba(34,224,168,.25))}
@keyframes gr{to{background-position:300% center}}
.hero p{color:#98a6b6;font-size:19px;margin:22px auto 36px;max-width:620px;line-height:1.6}
.hero-actions{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.stats{display:flex;gap:20px;justify-content:center;flex-wrap:wrap;max-width:940px;margin:0 auto;padding:6vh 24px;animation:fadeUp 1s ease}
.stat{flex:1;min-width:130px;background:rgba(18,23,32,.55);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.09);border-radius:26px;padding:26px 16px;text-align:center;transition:.25s}.stat:hover{transform:translateY(-6px);border-color:rgba(34,224,168,.5);box-shadow:0 12px 40px rgba(34,224,168,.12)}
.stat .n{font-size:40px;font-weight:800;background:linear-gradient(90deg,#22e0a8,#4f7dff);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.stat .l{color:#98a6b6;font-size:14px;margin-top:8px}
.section{max-width:1120px;margin:0 auto;padding:8vh 24px}
.section h2{text-align:center;font-size:clamp(30px,4.5vw,42px);font-weight:800;margin-bottom:14px;background:linear-gradient(90deg,#fff,#c6d0dc);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.section .sub{text-align:center;color:#98a6b6;font-size:17px;margin-bottom:46px}
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
.faq{max-width:780px;margin:0 auto}
.faq-item{background:rgba(18,23,32,.55);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.09);border-radius:20px;margin-bottom:14px;overflow:hidden;transition:.2s}
.faq-q{padding:20px 24px;cursor:pointer;font-weight:600;font-size:15.5px;display:flex;justify-content:space-between;align-items:center;gap:12px}
.faq-q .plus{color:#22e0a8;font-size:24px;transition:transform .3s;flex-shrink:0;width:26px;height:26px;border-radius:50%;background:rgba(34,224,168,.12);display:flex;align-items:center;justify-content:center}
.faq-a{max-height:0;overflow:hidden;transition:max-height .35s ease;color:#98a6b6;font-size:14.5px;line-height:1.65}
.faq-item.open .faq-a{max-height:400px;padding:0 24px 22px}
.faq-item.open .plus{transform:rotate(45deg);background:rgba(34,224,168,.25)}
.cta{text-align:center;padding:10vh 24px;animation:fadeUp .8s ease}
.cta h2{font-size:clamp(30px,4.5vw,44px);font-weight:800;margin-bottom:14px;background:linear-gradient(90deg,#22e0a8,#4f7dff);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.cta p{color:#98a6b6;font-size:17px;margin-bottom:32px}
footer{border-top:1px solid rgba(255,255,255,.08);padding:52px 6vw 28px;max-width:1240px;margin:0 auto}
.foot-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:30px;margin-bottom:36px}
.foot-grid h4{color:#fff;font-size:15px;margin-bottom:16px}
.foot-grid a{display:block;color:#98a6b6;text-decoration:none;font-size:13.5px;margin-bottom:10px;transition:.2s}.foot-grid a:hover{color:#22e0a8;transform:translateX(3px)}
.foot-bottom{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px;color:#6b7684;font-size:13px;border-top:1px solid rgba(255,255,255,.06);padding-top:24px}
.status{display:inline-flex;align-items:center;gap:8px;color:#98a6b6;font-size:13px}
.dot{width:10px;height:10px;border-radius:50%;background:#22e0a8;box-shadow:0 0 12px #22e0a8;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.35}}
/* === Документы === */
.doc{max-width:860px;margin:0 auto;padding:7vh 24px 9vh;animation:fadeUp .6s ease}
.doc .crumb{color:#98a6b6;font-size:13px;margin-bottom:26px}.doc .crumb a{color:#22e0a8;text-decoration:none}
.doc h1{font-size:clamp(28px,4vw,40px);font-weight:800;margin-bottom:8px}
.doc .upd{color:#6b7684;font-size:13px;margin-bottom:34px}
.doc h2{font-size:20px;font-weight:700;margin:30px 0 12px;color:#22e0a8}
.doc p{color:#c6d0dc;font-size:15px;line-height:1.7;margin-bottom:14px}
.doc .op{background:rgba(34,224,168,.08);border:1px solid rgba(34,224,168,.3);border-radius:18px;padding:16px 20px;color:#22e0a8;font-weight:600;font-size:14px;margin-top:30px}
@media(max-width:768px){.nav-links{display:none}.hero{padding-top:7vh}}
</style>"""

NAV = """<nav>
<div class="brand"><div class="logo"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 2L20 6V12C20 16.4 16.6 20.4 12 22C7.4 20.4 4 16.4 4 12V6L12 2Z" fill="#0a1a14"/><path d="M9 12L11 14L15 10" stroke="#22e0a8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>""" + SITE_NAME + """</div>
<div class="nav-links"><a href="/#how">Как работает</a><a href="/#features">Возможности</a><a href="/#plans">Тарифы</a><a href="/#faq">FAQ</a><a href="/terms">Оферта</a></div>
<a class="btn btn-green" href=\"""" + BOT + """" target="_blank">Открыть бота</a>
</nav>"""

FOOT = """<footer>
<div class="foot-grid">
<div><h4>Продукт</h4><a href="/#how">Как работает</a><a href="/#features">Возможности</a><a href="/#plans">Тарифы</a><a href="/#faq">FAQ</a></div>
<div><h4>Документы</h4><a href="/terms">Пользовательское соглашение</a><a href="/privacy">Политика конфиденциальности</a><a href="/refund">Возврат средств</a></div>
<div><h4>Контакты</h4><a href=\"""" + BOT + """" target="_blank">Telegram-бот</a><a href=\"""" + SUPPORT_BOT + """" target="_blank">Поддержка в Telegram</a></div>
</div>
<div class="foot-bottom"><div>© 2026 """ + SITE_NAME + """. Все права защищены.</div><div class="status"><span class="dot"></span>Все системы работают</div></div>
</footer>"""

LANDING = """<!DOCTYPE html><html lang="ru"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>"""+SITE_NAME+""" — приватный интернет в один тап</title>
<meta name="theme-color" content="#07090d">"""+HEAD+"""</head><body>
"""+BG+NAV+"""
<section class="hero">
<h1>Приватный интернет<br>в один тап</h1>
<p>Шифруем твой трафик и не ведём логи. Никакой рекламы и настроек — подключаешься за пару минут через Telegram.</p>
<div class="hero-actions">
<a class="btn btn-green" href=\""""+BOT+"""" target="_blank">🚀 Открыть Telegram-бота</a>
<a class="btn btn-ghost" href="#plans">Посмотреть тарифы</a>
</div>
</section>

<section class="stats">
<div class="stat"><div class="n">1</div><div class="l">тап до защиты</div></div>
<div class="stat"><div class="n">∞</div><div class="l">трафик</div></div>
<div class="stat"><div class="n">0</div><div class="l">логов</div></div>
<div class="stat"><div class="n">7</div><div class="l">устройств</div></div>
<div class="stat"><div class="n">24/7</div><div class="l">поддержка</div></div>
</section>

<section class="section" id="how">
<h2>Как это работает</h2><p class="sub">Три шага — и ты под защитой</p>
<div class="steps">
<div class="step"><div class="num">01</div><h3>Открой бота в Telegram</h3><p>Жми кнопку на странице или ищи @awesomeproxyvpn_bot. Регистрация прямо в чате, за минуту.</p></div>
<div class="step"><div class="num">02</div><h3>Выбери тариф</h3><p>Любой удобный срок — без привязки карты и лишних настроек.</p></div>
<div class="step"><div class="num">03</div><h3>Включи защиту</h3><p>Одно нажатие — и весь трафик под защитой. Выключается так же просто.</p></div>
</div>
</section>

<section class="section" id="features">
<h2>Возможности</h2><p class="sub">Всё для приватности — и ничего лишнего</p>
<div class="grid">
<div class="card"><div class="ic">🔒</div><h3>Без логов</h3><p>Не храним историю и не следим за твоим трафиком. Что ты делаешь в сети — знаешь только ты.</p></div>
<div class="card"><div class="ic">⚡</div><h3>Высокая скорость</h3><p>Современный протокол VLESS. Не режем скорость и не считаем гигабайты.</p></div>
<div class="card"><div class="ic">🛡️</div><h3>Шифрование трафика</h3><p>Данные идут через зашифрованный туннель. Ни провайдер, ни чужой Wi-Fi их не прочитают.</p></div>
<div class="card"><div class="ic">📱</div><h3>До 7 устройств</h3><p>Один аккаунт держит под защитой телефон, планшет и компьютер разом.</p></div>
<div class="card"><div class="ic">🌍</div><h3>Все локации</h3><p>Быстрые сервера по всему миру и стабильное соединение в любой точке.</p></div>
<div class="card"><div class="ic">🆘</div><h3>Живая поддержка</h3><p>Реальная помощь 24/7, если что-то пойдёт не так.</p></div>
</div>
</section>

<section class="section" id="plans">
<h2>Тарифы</h2><p class="sub">Простые цены. Без сюрпризов. Оплата прямо в боте.</p>
<div class="plans">
<div class="plan">
<h3>1 месяц</h3><div class="dur">Гибко, помесячно</div>
<div class="price">139 ₽</div><div class="stars">⭐ 98</div><div class="per">Безлимит трафика · 3 устройства</div>
<ul><li>Полный доступ на месяц</li><li>Безлимит по трафику</li><li>До 3 устройств</li><li>Все локации</li></ul>
<a class="btn btn-ghost" style="width:100%" href=\""""+BOT+"""" target="_blank">Выбрать 1 месяц</a>
</div>
<div class="plan popular"><div class="badge">Популярный</div>
<h3>3 месяца</h3><div class="dur">Выгодно</div>
<div class="price">249 ₽</div><div class="stars">⭐ 175</div><div class="per">Безлимит трафика · 3 устройства</div>
<ul><li>Полный доступ на 3 месяца</li><li>Безлимит по трафику</li><li>До 3 устройств</li><li>Все локации</li></ul>
<a class="btn btn-green" style="width:100%" href=\""""+BOT+"""" target="_blank">Выбрать 3 месяца</a>
</div>
<div class="plan">
<h3>6 месяцев</h3><div class="dur">Максимум выгоды</div>
<div class="price">519 ₽</div><div class="stars">⭐ 364</div><div class="per">Безлимит трафика · 5 устройств</div>
<ul><li>Полный доступ на 6 месяцев</li><li>Безлимит по трафику</li><li>До 5 устройств</li><li>Все локации</li></ul>
<a class="btn btn-ghost" style="width:100%" href=\""""+BOT+"""" target="_blank">Выбрать 6 месяцев</a>
</div>
</div>
</section>

<section class="section" id="faq">
<h2>FAQ</h2><p class="sub">Частые вопросы</p>
<div class="faq">
<div class="faq-item"><div class="faq-q">Как это защищает меня?<span class="plus">+</span></div><div class="faq-a">Весь твой трафик проходит через зашифрованный туннель между твоим устройством и интернетом. Провайдер и сторонние сервисы не видят, что ты делаешь в сети, а реальный IP скрыт.</div></div>
<div class="faq-item"><div class="faq-q">Вы храните логи?<span class="plus">+</span></div><div class="faq-a">Нет. Мы не ведём логи и не храним историю посещений. Приватность — наш главный принцип.</div></div>
<div class="faq-item"><div class="faq-q">На скольких устройствах работает?<span class="plus">+</span></div><div class="faq-a">До 3 на тарифах 1 и 3 месяца, до 5 — на полугодовом. Один аккаунт держит под защитой телефон, планшет и компьютер разом.</div></div>
<div class="faq-item"><div class="faq-q">Есть ли приложения для iOS и Android?<span class="plus">+</span></div><div class="faq-a">Да, подключение работает через Telegram-бота с готовыми конфигами для любых устройств.</div></div>
<div class="faq-item"><div class="faq-q">Можно ли отменить подписку?<span class="plus">+</span></div><div class="faq-a">Да, в любой момент — без звонков и переписок. Доступ останется до конца оплаченного периода.</div></div>
</div>
</section>

<section class="cta">
<h2>Готов попробовать?</h2><p>Подключайся через Telegram — быстро и без слежки.</p>
<a class="btn btn-green" href=\""""+BOT+"""" target="_blank">🚀 Открыть Telegram-бота</a>
</section>
"""+FOOT+"""
<script>document.querySelectorAll('.faq-q').forEach(q=>q.addEventListener('click',()=>q.parentElement.classList.toggle('open')));</script>
</body></html>"""

def doc_page(title, updated, body, crumb_label):
    return """<!DOCTYPE html><html lang="ru"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>"""+SITE_NAME+" — "+title+"""</title><meta name="theme-color" content="#07090d">"""+HEAD+"""</head><body>
"""+BG+NAV+"""
<div class="doc">
<div class="crumb">← <a href="/">На главную</a> · Все документы</div>
<h1>"""+title+"""</h1><div class="upd">Последнее обновление: """+updated+"""</div>
"""+body+"""
<div class="op">По вопросам о правовых политиках: """+EMAIL+" или Telegram-бот.<br>Оператор: "+OPERATOR+""".</div>
</div>
"""+FOOT+"""
</body></html>"""

TERMS = doc_page("Пользовательское соглашение (оферта)", "25 июля 2026", """
<p>Настоящее Пользовательское соглашение (далее — «Соглашение») является публичной офертой и определяет условия использования сервиса """+SITE_NAME+""" (далее — «Сервис») между Администрацией Сервиса (далее — «Администрация») и пользователем (далее — «Пользователь»).</p>

<h2>1. Предмет соглашения</h2>
<p>1.1. Администрация предоставляет Пользователю доступ к Сервису и его функционалу на условиях, изложенных в настоящем Соглашении.</p>
<p>1.2. Пользователь, используя Telegram-бот @awesomeproxyvpn_bot и сайт """+SITE_URL+""", подтверждает своё полное и безоговорочное согласие с условиями настоящего Соглашения.</p>
<p>1.3. Настоящее Соглашение является юридически обязательным документом.</p>
<p>1.4. Оператором Сервиса является """+OPERATOR+""" ("""+OP_COUNTRY+""").</p>

<h2>2. Описание сервиса</h2>
<p>2.1. """+SITE_NAME+""" предоставляет сервис виртуальной частной сети, обеспечивающий шифрование интернет-соединения и защиту данных Пользователя при передаче через сеть Интернет.</p>
<p>2.2. Регистрация и управление подпиской осуществляются исключительно через Telegram-бот @awesomeproxyvpn_bot. Один Telegram-аккаунт соответствует одной учётной записи.</p>
<p>2.3. Перечень функций Сервиса может быть изменён Администрацией без предварительного уведомления Пользователя.</p>

<h2>3. Правила использования</h2>
<p>3.1. Пользователь обязуется использовать Сервис исключительно в соответствии с его целевым назначением и в рамках применимого законодательства.</p>
<p>3.2. Пользователю запрещается: пытаться получить несанкционированный доступ к информации и инфраструктуре Сервиса; использовать Сервис для распространения вредоносного ПО, спама или иной незаконной информации; вмешиваться в работу Сервиса; нарушать права третьих лиц; передавать доступ к учётной записи третьим лицам.</p>
<p>3.3. Администрация вправе ограничить или прекратить доступ Пользователя в случае нарушения им условий Соглашения без компенсации.</p>

<h2>4. Платные услуги и возврат средств</h2>
<p>4.1. Доступ к Сервису предоставляется на платной основе по подписке.</p>
<p>4.2. Оплата осуществляется через сторонние платёжные системы. """+SITE_NAME+""" не хранит платёжные реквизиты Пользователей.</p>
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
<p>Оператор Сервиса: """+OPERATOR+""" ("""+OP_COUNTRY+"""). Поддержка: """+EMAIL+" и через Telegram-бот @"+SUPPORT_BOT.rstrip('/').split('/')[-1]+""".</p>
""", "Пользовательское соглашение")

PRIVACY = doc_page("Политика конфиденциальности", "25 июля 2026", """
<h2>1. Общие положения</h2>
<p>Настоящая Политика конфиденциальности определяет порядок сбора, использования, хранения и защиты персональных данных пользователей сервиса """+SITE_NAME+""" (далее — «Сервис»).</p>
<p>Оператором (контролёром) персональных данных является """+OPERATOR+""", """+OP_COUNTRY+""". Контакт по вопросам обработки персональных данных — """+EMAIL+""".</p>
<p>Факт использования сайта """+SITE_URL+""" и Telegram-бота @awesomeproxyvpn_bot является полным и безоговорочным согласием с настоящей Политикой. Если Пользователь не согласен с её условиями, ему следует прекратить использование Сервиса.</p>

<h2>2. Источники и состав информации</h2>
<p>2.1. Персональные данные: Telegram ID пользователя; имя пользователя (username); язык интерфейса; дата регистрации; статус подписки.</p>
<p>2.2. Технические данные: тип устройства; версия приложения; IP-адрес; регион подключения (без точного местоположения).</p>
<p>2.3. """+SITE_NAME+""" не обрабатывает и не хранит: историю посещения сайтов; DNS-запросы; содержимое интернет-трафика.</p>

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
<p>Запросы направляются на """+EMAIL+""" либо в Telegram-бот поддержки. Ответ предоставляется в течение 30 календарных дней.</p>

<h2>7. Заключительные положения</h2>
<p>Условия Политики могут быть изменены Администрацией в одностороннем порядке. Актуальная версия публикуется на сайте """+SITE_URL+""".</p>
""", "Политика конфиденциальности")

REFUND = doc_page("Политика возврата денежных средств", "25 июля 2026", """
<h2>1. Общие положения</h2>
<p>1.1. Настоящая Политика возврата является неотъемлемой частью Пользовательского соглашения """+SITE_NAME+""" и определяет условия и порядок возврата средств за подписку.</p>
<p>1.2. Настоящая Политика не ограничивает права Пользователя как потребителя, предоставленные ему императивными нормами законодательства страны его постоянного проживания.</p>

<h2>2. Срок оказания услуги</h2>
<p>2.1. Услугой является предоставление доступа к оплаченной подписке """+SITE_NAME+""".</p>
<p>2.2. Доступ предоставляется автоматически сразу после подтверждения оплаты, но не позднее 3 (трёх) календарных дней с момента поступления средств. С момента предоставления доступа услуга считается оказанной.</p>

<h2>3. Основания для возврата</h2>
<p>3.1. Неоказание услуги. Если доступ не был предоставлен в срок, Пользователь вправе потребовать возврата в полном объёме.</p>
<p>3.2. Отказ до начала оказания услуги. Если доступ ещё не активирован, возврат производится в полном объёме.</p>
<p>3.3. Отказ после активации доступа. Возвращается стоимость неиспользованных дней подписки пропорционально их количеству.</p>

<h2>4. Срок подачи заявления</h2>
<p>4.1. Заявление по основанию п. 3.1 подаётся в течение 14 (четырнадцати) календарных дней с даты истечения срока оказания услуги.</p>
<p>4.2. Заявление об отказе по основаниям п. 3.2 и п. 3.3 подаётся в течение оплаченного срока подписки.</p>

<h2>5. Форма подачи заявления</h2>
<p>5.1. Заявление направляется: на электронную почту """+EMAIL+"""; в Telegram-бот поддержки @"+SUPPORT_BOT.rstrip('/').split('/')[-1]+""".</p>
<p>5.2. В заявлении указываются: данные учётной записи; номер платежа (операции, чека); дата и сумма платежа; причина возврата.</p>

<h2>6. Срок рассмотрения</h2>
<p>6.1. Заявление рассматривается в течение 10 (десяти) рабочих дней с момента его получения. О результате Пользователь уведомляется тем же способом, которым было подано заявление.</p>

<h2>7. Срок и порядок возврата</h2>
<p>7.1. При положительном решении средства возвращаются в течение 10 (десяти) рабочих дней с даты одобрения.</p>
<p>7.2. Возврат производится на те же реквизиты, с которых была совершена оплата.</p>
<p>7.3. По основаниям п. 3.1 и п. 3.2 возврат производится в полном объёме.</p>

<h2>8. Исключения</h2>
<p>8.1. Возврат не осуществляется при нарушении Пользователем Пользовательского соглашения или Политики допустимого использования.</p>
""", "Политика возврата")

@app.route('/')
def index(): return render_template_string(LANDING)
@app.route('/terms')
def terms(): return render_template_string(TERMS)
@app.route('/privacy')
def privacy(): return render_template_string(PRIVACY)
@app.route('/refund')
def refund(): return render_template_string(REFUND)

@app.route('/favicon.ico')
def favicon():
    svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22e0a8"/><stop offset="1" stop-color="#4f7dff"/></linearGradient></defs><rect width="24" height="24" rx="12" fill="url(#g)"/><path d="M12 4 L19 7 V12 C19 15.3 16.3 18.4 12 19.6 C7.7 18.4 5 15.3 5 12 V7 Z" fill="#0a1a14"/><path d="M9 12 L11 14 L15 10" stroke="#22e0a8" stroke-width="1.6" fill="none" stroke-linecap="round"/></svg>'
    return app.response_class(svg, mimetype='image/svg+xml')

if __name__ == '__main__':
    print("Awesome VPN — лендинг + документы")
    app.run(host='0.0.0.0', port=PORT, debug=False)
