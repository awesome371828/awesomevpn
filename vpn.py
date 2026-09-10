#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Awesome VPN — Безопасный интернет"""
import os
from flask import Flask, render_template_string

app = Flask(__name__)
PORT = int(os.getenv("PORT", 5000))

INDEX = r"""<!DOCTYPE html><html lang="ru"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Awesome VPN — приватный интернет в один тап</title>
<meta name="theme-color" content="#07090d">
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:'Söhne','Segoe UI',system-ui,sans-serif}
body{background:#07090d;color:#f0f4f8;-webkit-font-smoothing:antialiased;overflow-x:hidden}
.scene{position:fixed;inset:0;z-index:-1;overflow:hidden;background:radial-gradient(120% 120% at 15% 10%,#0d2b24 0%,transparent 50%),radial-gradient(120% 120% at 85% 20%,#141a3d 0%,transparent 50%),radial-gradient(120% 120% at 50% 100%,#1b1030 0%,transparent 55%),#07090d}
.glow{position:absolute;border-radius:50%;filter:blur(80px);mix-blend-mode:screen;animation:drift 20s ease-in-out infinite alternate}
.g1{width:520px;height:520px;background:radial-gradient(circle,#16d6a4,transparent 65%);top:-140px;left:-100px;opacity:.5}
.g2{width:460px;height:460px;background:radial-gradient(circle,#4f7dff,transparent 65%);bottom:-120px;right:-80px;opacity:.45}
.g3{width:380px;height:380px;background:radial-gradient(circle,#8b5cf6,transparent 65%);top:40%;left:55%;opacity:.35}
@keyframes drift{0%{transform:translate(0,0) scale(1)}100%{transform:translate(60px,40px) scale(1.15)}}
nav{display:flex;align-items:center;justify-content:space-between;padding:18px 6vw;max-width:1240px;margin:0 auto}
.brand{display:flex;align-items:center;gap:10px;font-weight:800;font-size:19px}
.brand .logo{width:36px;height:36px;border-radius:10px;background:conic-gradient(from 180deg,#22e0a8,#4f7dff,#8b5cf6,#22e0a8);display:flex;align-items:center;justify-content:center;animation:spin 8s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.nav-links{display:flex;gap:26px;align-items:center}
.nav-links a{color:#98a6b6;text-decoration:none;font-size:14px}.nav-links a:hover{color:#fff}
.btn{display:inline-flex;align-items:center;gap:8px;padding:11px 22px;border-radius:12px;border:none;cursor:pointer;font-weight:700;font-size:14px;text-decoration:none;transition:.2s}
.btn-green{background:linear-gradient(135deg,#22e0a8,#0d9d7a);color:#03140d}.btn-green:hover{transform:translateY(-2px);box-shadow:0 8px 26px rgba(34,224,168,.4)}
.btn-ghost{background:rgba(255,255,255,.07);color:#f0f4f8;border:1px solid rgba(255,255,255,.15)}.btn-ghost:hover{background:rgba(255,255,255,.12)}
.hero{text-align:center;padding:9vh 24px 6vh;max-width:880px;margin:0 auto}
.hero h1{font-size:clamp(34px,6vw,56px);font-weight:800;line-height:1.08;background:linear-gradient(90deg,#22e0a8,#4f7dff,#8b5cf6,#ffb347,#22e0a8);background-size:300% auto;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;animation:gr 6s linear infinite;filter:drop-shadow(0 4px 30px rgba(34,224,168,.25))}
@keyframes gr{to{background-position:300% center}}
.hero p{color:#98a6b6;font-size:19px;margin:20px auto 34px;max-width:620px}
.hero-actions{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.stats{display:flex;gap:20px;justify-content:center;flex-wrap:wrap;max-width:900px;margin:0 auto;padding:6vh 24px}
.stat{flex:1;min-width:130px;background:rgba(18,23,32,.6);backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,.09);border-radius:18px;padding:24px;text-align:center;transition:.2s}.stat:hover{transform:translateY(-4px);border-color:rgba(34,224,168,.5)}
.stat .n{font-size:38px;font-weight:800;background:linear-gradient(90deg,#22e0a8,#4f7dff);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.stat .l{color:#98a6b6;font-size:14px;margin-top:6px}
.section{max-width:1120px;margin:0 auto;padding:7vh 24px}
.section h2{text-align:center;font-size:clamp(28px,4vw,40px);font-weight:800;margin-bottom:12px}
.section .sub{text-align:center;color:#98a6b6;font-size:17px;margin-bottom:44px}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:22px}
.step{background:rgba(18,23,32,.6);backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,.09);border-radius:20px;padding:28px;position:relative;transition:.2s}.step:hover{transform:translateY(-5px);border-color:rgba(34,224,168,.5)}
.step .num{font-size:46px;font-weight:800;color:rgba(34,224,168,.25);position:absolute;top:18px;right:22px}
.step h3{margin:12px 0 8px;font-size:19px}.step p{color:#98a6b6;font-size:14.5px;line-height:1.6}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:22px}
.card{background:rgba(18,23,32,.6);backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,.09);border-radius:20px;padding:28px;transition:.2s}.card:hover{transform:translateY(-5px);border-color:rgba(34,224,168,.5)}
.card .ic{font-size:30px;margin-bottom:12px}.card h3{margin-bottom:8px;font-size:18px}.card p{color:#98a6b6;font-size:14.5px;line-height:1.6}
.plans{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:22px}
.plan{background:rgba(18,23,32,.6);backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,.09);border-radius:22px;padding:30px;text-align:center;position:relative;transition:.25s}.plan:hover{transform:translateY(-6px)}
.plan.popular{border-color:rgba(34,224,168,.6);box-shadow:0 0 40px rgba(34,224,168,.15)}
.badge{position:absolute;top:-12px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,#22e0a8,#4f7dff);color:#03140d;font-size:12px;font-weight:800;padding:5px 14px;border-radius:20px}
.plan h3{font-size:20px;margin-bottom:6px}.plan .dur{color:#98a6b6;font-size:14px;margin-bottom:18px}
.plan .price{font-size:42px;font-weight:800;background:linear-gradient(90deg,#22e0a8,#4f7dff);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.plan .stars{color:#ffd76a;font-size:16px;margin:6px 0 4px}.plan .per{color:#98a6b6;font-size:13px;margin-bottom:18px}
.plan ul{list-style:none;text-align:left;margin:0 0 22px;font-size:14px;color:#c6d0dc}
.plan li{padding:7px 0;border-bottom:1px solid rgba(255,255,255,.06)}.plan li::before{content:"✓ ";color:#22e0a8;font-weight:800}
.faq{max-width:780px;margin:0 auto}
.faq-item{background:rgba(18,23,32,.6);border:1px solid rgba(255,255,255,.09);border-radius:14px;margin-bottom:12px;overflow:hidden}
.faq-q{padding:18px 22px;cursor:pointer;font-weight:600;font-size:15.5px;display:flex;justify-content:space-between;align-items:center}
.faq-q .plus{color:#22e0a8;font-size:22px;transition:.3s}
.faq-a{max-height:0;overflow:hidden;transition:max-height .3s;color:#98a6b6;font-size:14.5px;line-height:1.6}
.faq-item.open .faq-a{max-height:400px;padding:0 22px 18px}
.faq-item.open .plus{transform:rotate(45deg)}
.cta{text-align:center;padding:9vh 24px}
.cta h2{font-size:clamp(28px,4vw,42px);font-weight:800;margin-bottom:12px}
.cta p{color:#98a6b6;font-size:17px;margin-bottom:30px}
footer{border-top:1px solid rgba(255,255,255,.08);padding:48px 6vw 28px;max-width:1240px;margin:0 auto}
.foot-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:30px;margin-bottom:34px}
.foot-grid h4{color:#fff;font-size:15px;margin-bottom:14px}
.foot-grid a{display:block;color:#98a6b6;text-decoration:none;font-size:13.5px;margin-bottom:9px}.foot-grid a:hover{color:#22e0a8}
.foot-bottom{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px;color:#6b7684;font-size:13px;border-top:1px solid rgba(255,255,255,.06);padding-top:22px}
.status{display:inline-flex;align-items:center;gap:7px;color:#98a6b6;font-size:13px}
.dot{width:9px;height:9px;border-radius:50%;background:#22e0a8;box-shadow:0 0 10px #22e0a8;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
@media(max-width:768px){.nav-links{display:none}.hero{padding-top:6vh}}
</style></head><body>
<div class="scene"><div class="glow g1"></div><div class="glow g2"></div><div class="glow g3"></div></div>

<nav>
<div class="brand"><div class="logo"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 2L20 6V12C20 16.4 16.6 20.4 12 22C7.4 20.4 4 16.4 4 12V6L12 2Z" fill="#0a1a14"/><path d="M9 12L11 14L15 10" stroke="#22e0a8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>Awesome VPN</div>
<div class="nav-links"><a href="#how">Как работает</a><a href="#features">Возможности</a><a href="#plans">Тарифы</a><a href="#faq">FAQ</a></div>
<a class="btn btn-green" href="https://t.me/awesomeproxyvpn_bot" target="_blank">Открыть бота</a>
</nav>

<section class="hero">
<h1>Приватный интернет в один тап</h1>
<p>Шифруем трафик и не ведём логи. Никаких настроек — подключаешься за пару минут через Telegram.</p>
<div class="hero-actions">
<a class="btn btn-green" href="https://t.me/awesomeproxyvpn_bot" target="_blank">🚀 Открыть Telegram-бота</a>
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
<a class="btn btn-ghost" style="width:100%" href="https://t.me/awesomeproxyvpn_bot" target="_blank">Выбрать 1 месяц</a>
</div>
<div class="plan popular"><div class="badge">Популярный</div>
<h3>3 месяца</h3><div class="dur">Выгодно</div>
<div class="price">249 ₽</div><div class="stars">⭐ 175</div><div class="per">Безлимит трафика · 3 устройства</div>
<ul><li>Полный доступ на 3 месяца</li><li>Безлимит по трафику</li><li>До 3 устройств</li><li>Все локации</li></ul>
<a class="btn btn-green" style="width:100%" href="https://t.me/awesomeproxyvpn_bot" target="_blank">Выбрать 3 месяца</a>
</div>
<div class="plan">
<h3>6 месяцев</h3><div class="dur">Максимум выгоды</div>
<div class="price">519 ₽</div><div class="stars">⭐ 364</div><div class="per">Безлимит трафика · 5 устройств</div>
<ul><li>Полный доступ на 6 месяцев</li><li>Безлимит по трафику</li><li>До 5 устройств</li><li>Все локации</li></ul>
<a class="btn btn-ghost" style="width:100%" href="https://t.me/awesomeproxyvpn_bot" target="_blank">Выбрать 6 месяцев</a>
</div>
</div>
</section>

<section class="section" id="faq">
<h2>FAQ</h2><p class="sub">Частые вопросы</p>
<div class="faq">
<div class="faq-item"><div class="faq-q">Как это защищает меня?<span class="plus">+</span></div><div class="faq-a">Весь твой трафик проходит через зашифрованный туннель. Провайдер и посторонние не видят, какие сайты ты посещаешь.</div></div>
<div class="faq-item"><div class="faq-q">Вы храните логи?<span class="plus">+</span></div><div class="faq-a">Нет. Мы не ведём логи и не храним историю. Приватность — наш главный принцип.</div></div>
<div class="faq-item"><div class="faq-q">На скольких устройствах работает?<span class="plus">+</span></div><div class="faq-a">До 3 на тарифах 1 и 3 месяца, до 5 — на полугодовом. Всё зависит от выбранного тарифа.</div></div>
<div class="faq-item"><div class="faq-q">Есть ли приложения для iOS и Android?<span class="plus">+</span></div><div class="faq-a">Да, подключение работает через Telegram-бота с готовыми конфигами для любых устройств.</div></div>
<div class="faq-item"><div class="faq-q">Можно ли отменить подписку?<span class="plus">+</span></div><div class="faq-a">Да, в любой момент — без звонков и переписок. Доступ останется до конца оплаченного периода.</div></div>
</div>
</section>

<section class="cta">
<h2>Готов попробовать?</h2><p>Подключайся через Telegram — быстро и без слежки.</p>
<a class="btn btn-green" href="https://t.me/awesomeproxyvpn_bot" target="_blank">🚀 Открыть Telegram-бота</a>
</section>

<footer>
<div class="foot-grid">
<div><h4>Продукт</h4><a href="#how">Как работает</a><a href="#features">Возможности</a><a href="#plans">Тарифы</a><a href="#faq">FAQ</a></div>
<div><h4>Документы</h4><a href="#">Пользовательское соглашение</a><a href="#">Политика конфиденциальности</a><a href="#">Возврат средств</a></div>
<div><h4>Контакты</h4><a href="https://t.me/awesomeproxyvpn_bot" target="_blank">Telegram-бот</a><a href="#">Написать в поддержку</a></div>
</div>
<div class="foot-bottom">
<div>© 2026 Awesome VPN. Все права защищены.</div>
<div class="status"><span class="dot"></span>Все системы работают</div>
</div>
</footer>

<script>
document.querySelectorAll('.faq-q').forEach(q=>{q.addEventListener('click',()=>{q.parentElement.classList.toggle('open')})});
</script>
</body></html>"""

@app.route('/')
def index(): return render_template_string(INDEX)

@app.route('/favicon.ico')
def favicon():
    svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22e0a8"/><stop offset="1" stop-color="#4f7dff"/></linearGradient></defs><rect width="24" height="24" rx="6" fill="url(#g)"/><path d="M12 4 L19 7 V12 C19 15.3 16.3 18.4 12 19.6 C7.7 18.4 5 15.3 5 12 V7 Z" fill="#0a1a14"/><path d="M9 12 L11 14 L15 10" stroke="#22e0a8" stroke-width="1.6" fill="none" stroke-linecap="round"/></svg>'
    return app.response_class(svg, mimetype='image/svg+xml')

if __name__ == '__main__':
    print("Awesome VPN — лендинг")
    app.run(host='0.0.0.0', port=PORT, debug=False)
