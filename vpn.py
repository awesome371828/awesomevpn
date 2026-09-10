#!/usr/bin/env python3
"""
Awesome VPN — лендинг.
Запуск:  python3 vpn.py
Открыть: http://localhost:8000
"""

import http.server
import socketserver

BOT_USERNAME = "awesomeproxyvpn_bot"
BOT_URL = f"https://t.me/{BOT_USERNAME}"

PAGE = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Awesome VPN — приватный интернет в один тап</title>
<style>
  :root{
    --bg:#0a0e1a; --bg2:#111730; --card:#151c38;
    --accent:#6c5ce7; --accent2:#00d2ff; --text:#e8ecff; --muted:#9aa3c7;
  }
  *{margin:0;padding:0;box-sizing:border-box;}
  body{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--text);line-height:1.6;}
  a{text-decoration:none;color:inherit;}
  .container{max-width:1140px;margin:0 auto;padding:0 20px;}
  .btn{display:inline-block;background:linear-gradient(135deg,var(--accent),var(--accent2));
    color:#fff;font-weight:700;padding:14px 28px;border-radius:12px;transition:.25s;border:none;cursor:pointer;}
  .btn:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(108,92,231,.45);}
  .btn-outline{background:transparent;border:2px solid var(--accent);}
  /* Header */
  header{position:sticky;top:0;background:rgba(10,14,26,.85);backdrop-filter:blur(10px);z-index:10;border-bottom:1px solid rgba(255,255,255,.06);}
  .nav{display:flex;align-items:center;justify-content:space-between;padding:18px 0;}
  .logo{font-size:22px;font-weight:800;letter-spacing:.5px;}
  .logo span{background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
  .menu{display:flex;gap:26px;font-size:15px;}
  .menu a{color:var(--muted);transition:.2s;}
  .menu a:hover{color:#fff;}
  .nav-actions{display:flex;gap:12px;align-items:center;}
  .hamburger{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;}
  .hamburger span{width:24px;height:2px;background:#fff;}
  /* Hero */
  .hero{text-align:center;padding:90px 0 70px;background:radial-gradient(circle at 50% 0%,rgba(108,92,231,.25),transparent 60%);}
  .badge{display:inline-block;background:rgba(0,210,255,.15);color:var(--accent2);padding:6px 14px;border-radius:20px;font-size:14px;margin-bottom:22px;}
  .hero h1{font-size:52px;line-height:1.15;font-weight:800;margin-bottom:18px;}
  .hero h1 em{font-style:normal;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
  .hero p{font-size:19px;color:var(--muted);max-width:640px;margin:0 auto 34px;}
  .hero-cta{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;}
  .offer{display:flex;justify-content:center;gap:26px;margin-top:50px;flex-wrap:wrap;color:var(--muted);font-size:15px;}
  .offer b{display:block;font-size:26px;color:var(--text);}
  /* Stats */
  .stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:20px;margin:70px auto;}
  .stat{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:16px;padding:28px;text-align:center;}
  .stat b{font-size:32px;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
  .stat span{display:block;margin-top:6px;color:var(--muted);}
  /* Sections */
  section{padding:70px 0;}
  .sec-title{text-align:center;font-size:36px;font-weight:800;margin-bottom:12px;}
  .sec-sub{text-align:center;color:var(--muted);max-width:620px;margin:0 auto 48px;}
  /* How it works */
  .steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px;}
  .step{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:16px;padding:30px;position:relative;}
  .step .num{position:absolute;top:-18px;left:24px;background:linear-gradient(135deg,var(--accent),var(--accent2));width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-weight:800;}
  .step h3{margin-bottom:10px;font-size:18px;}
  .step p{color:var(--muted);}
  /* Features */
  .features{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px;}
  .feat{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:16px;padding:30px;}
  .feat .icon{font-size:32px;margin-bottom:16px;}
  .feat h3{margin-bottom:10px;}
  .feat p{color:var(--muted);}
  /* Pricing */
  .pricing{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;align-items:stretch;}
  .price-card{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:20px;padding:34px;display:flex;flex-direction:column;position:relative;}
  .price-card.popular{border-color:var(--accent);box-shadow:0 0 40px rgba(108,92,231,.25);}
  .pop-tag{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,var(--accent),var(--accent2));padding:6px 16px;border-radius:20px;font-size:13px;font-weight:700;white-space:nowrap;}
  .price-card .period{color:var(--muted);font-size:15px;}
  .price-card .price{font-size:40px;font-weight:800;margin:10px 0 4px;}
  .price-card .price small{font-size:18px;color:var(--muted);font-weight:400;}
  .price-card ul{list-style:none;margin:20px 0 28px;flex:1;}
  .price-card li{padding:8px 0;color:var(--muted);}
  .price-card li::before{content:"✓ ";color:var(--accent2);font-weight:700;}
  .price-card .btn{text-align:center;}
  .note{text-align:center;color:var(--muted);font-size:13px;margin-top:26px;}
  /* FAQ */
  .faq{max-width:760px;margin:0 auto;}
  .faq-item{background:var(--card);border:1px solid rgba(255,255,255,.06);border-radius:14px;margin-bottom:14px;overflow:hidden;}
  .faq-q{width:100%;background:none;border:none;color:var(--text);font-size:17px;font-weight:600;padding:20px 24px;text-align:left;cursor:pointer;display:flex;justify-content:space-between;align-items:center;}
  .faq-q .chev{transition:.3s;color:var(--accent2);}
  .faq-item.open .chev{transform:rotate(180deg);}
  .faq-a{max-height:0;overflow:hidden;transition:.3s;padding:0 24px;color:var(--muted);}
  .faq-item.open .faq-a{max-height:300px;padding:0 24px 20px;}
  /* CTA */
  .cta{text-align:center;background:linear-gradient(135deg,rgba(108,92,231,.2),rgba(0,210,255,.15));border-radius:24px;padding:60px 30px;margin:20px 0 0;}
  .cta h2{font-size:36px;margin-bottom:16px;}
  .cta p{color:var(--muted);max-width:520px;margin:0 auto 30px;}
  /* Footer */
  footer{border-top:1px solid rgba(255,255,255,.06);padding:40px 0;margin-top:70px;}
  .footer-grid{display:flex;justify-content:space-between;flex-wrap:wrap;gap:30px;margin-bottom:26px;}
  .footer-col h4{margin-bottom:14px;font-size:15px;}
  .footer-col a{display:block;color:var(--muted);margin-bottom:8px;font-size:14px;}
  .footer-col a:hover{color:#fff;}
  .footer-bottom{display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;color:var(--muted);font-size:13px;border-top:1px solid rgba(255,255,255,.05);padding-top:20px;}
  .status{display:inline-flex;align-items:center;gap:8px;color:#3ddc84;}
  .status .dot{width:9px;height:9px;border-radius:50%;background:#3ddc84;animation:pulse 1.5s infinite;}
  @keyframes pulse{0%{box-shadow:0 0 0 0 rgba(61,220,132,.6);}70%{box-shadow:0 0 0 8px rgba(61,220,132,0);}100%{box-shadow:0 0 0 0 rgba(61,220,132,0);}}
  @media(max-width:820px){
    .hero h1{font-size:36px;}
    .sec-title{font-size:28px;}
    .menu{display:none;}
    .hamburger{display:flex;}
    .menu.open{display:flex;position:absolute;top:64px;left:0;right:0;background:var(--bg);flex-direction:column;padding:20px;border-bottom:1px solid rgba(255,255,255,.06);}
  }
</style>
</head>
<body>

<header>
  <div class="container nav">
    <div class="logo">Awesome<span>VPN</span></div>
    <nav class="menu" id="menu">
      <a href="#features">Возможности</a>
      <a href="#how">Как работает</a>
      <a href="#pricing">Тарифы</a>
      <a href="#faq">FAQ</a>
    </nav>
    <div class="nav-actions">
      <a class="btn btn-outline" href="__BOT_URL__" target="_blank">Войти на сайте</a>
      <a class="btn" href="__BOT_URL__" target="_blank">Подключиться</a>
      <button class="hamburger" onclick="document.getElementById('menu').classList.toggle('open')">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>

<section class="hero">
  <div class="container">
    <span class="badge">⚡ Современный протокол VLESS</span>
    <h1>Приватный интернет <br>в <em>один тап</em></h1>
    <p>Быстрый VPN на современном протоколе VLESS. Шифруем твой трафик и не ведём логи. Подключаешься за пару минут.</p>
    <div class="hero-cta">
      <a class="btn" href="__BOT_URL__" target="_blank">Открыть Telegram-бота</a>
      <a class="btn btn-outline" href="#pricing">Посмотреть тарифы</a>
    </div>
    <div class="offer">
      <div><b>7 дней</b>бесплатно</div>
      <div><b>iOS / Android</b>уже на подходе</div>
    </div>
  </div>
</section>

<section class="container">
  <div class="stats">
    <div class="stat"><b>1</b><span>тап</span></div>
    <div class="stat"><b>∞</b><span>трафик</span></div>
    <div class="stat"><b>0</b><span>логов</span></div>
    <div class="stat"><b>5</b><span>устройств</span></div>
    <div class="stat"><b>24/7</b><span>поддержка</span></div>
  </div>
</section>

<section id="how">
  <div class="container">
    <h2 class="sec-title">Как это работает</h2>
    <p class="sec-sub">Три шага — и ты под защитой</p>
    <div class="steps">
      <div class="step"><div class="num">01</div><h3>Открой бота в Telegram</h3><p>Жми кнопку на странице или ищи @awesomeproxyvpn_bot. Регистрация прямо в чате, за минуту.</p></div>
      <div class="step"><div class="num">02</div><h3>Выбери тариф</h3><p>Первые дни — бесплатно. Карта не нужна для знакомства с сервисом.</p></div>
      <div class="step"><div class="num">03</div><h3>Включи защиту</h3><p>Одно нажатие — и весь трафик под защитой. Выключается так же просто.</p></div>
    </div>
  </div>
</section>

<section id="features">
  <div class="container">
    <h2 class="sec-title">Возможности</h2>
    <p class="sec-sub">Всё для приватности — и ничего лишнего</p>
    <div class="features">
      <div class="feat"><div class="icon">🚀</div><h3>Высокая скорость</h3><p>Современный протокол VLESS и быстрые сервера — без ограничения скорости.</p></div>
      <div class="feat"><div class="icon">🌍</div><h3>Стабильное соединение</h3><p>Быстрые сервера и устойчивое соединение, чтобы ты всегда оставался онлайн.</p></div>
      <div class="feat"><div class="icon">🔒</div><h3>Без логов</h3><p>Не храним историю и не следим за твоим трафиком. Что ты делаешь — знаешь только ты.</p></div>
      <div class="feat"><div class="icon">📱</div><h3>До 5 устройств</h3><p>Один аккаунт держит под защитой телефон, планшет и компьютер разом.</p></div>
      <div class="feat"><div class="icon">∞</div><h3>Без лимитов</h3><p>Не режем скорость и не считаем гигабайты — ни на одном тарифе.</p></div>
      <div class="feat"><div class="icon">🆘</div><h3>Живая поддержка</h3><p>Поможем, если что-то пойдёт не так — быстро и по делу.</p></div>
    </div>
  </div>
</section>

<section id="pricing">
  <div class="container">
    <h2 class="sec-title">Тарифы</h2>
    <p class="sec-sub">Простые цены. Без сюрпризов. Отмена в любой момент.</p>
    <div class="pricing">
      <div class="price-card">
        <span class="period">1 месяц</span>
        <div class="price">139<small> ₽</small></div>
        <span class="period">Гибко, помесячно</span>
        <ul>
          <li>Безлимит трафика</li>
          <li>До 3 устройств</li>
          <li>Полный доступ ко всему</li>
          <li>Все локации 🌍</li>
        </ul>
        <a class="btn" href="__BOT_URL__" target="_blank">Выбрать месяц</a>
      </div>

      <div class="price-card popular">
        <span class="pop-tag">🔥 Популярный</span>
        <span class="period">3 месяца</span>
        <div class="price">249<small> ₽</small></div>
        <span class="period">Выгоднее, чем помесячно</span>
        <ul>
          <li>Безлимит трафика</li>
          <li>До 3 устройств</li>
          <li>Полный доступ ко всему</li>
          <li>Все локации 🌍</li>
        </ul>
        <a class="btn" href="__BOT_URL__" target="_blank">Выбрать 3 месяца</a>
      </div>

      <div class="price-card">
        <span class="period">6 месяцев</span>
        <div class="price">519<small> ₽</small></div>
        <span class="period">Максимальная выгода</span>
        <ul>
          <li>Безлимит трафика</li>
          <li>До 5 устройств</li>
          <li>Полный доступ ко всему</li>
          <li>Все локации 🌍</li>
        </ul>
        <a class="btn" href="__BOT_URL__" target="_blank">Выбрать 6 месяцев</a>
      </div>
    </div>
    <p class="note">Оплачивая подписку, вы принимаете условия оферты и политики возврата.</p>
  </div>
</section>

<section id="faq">
  <div class="container">
    <h2 class="sec-title">FAQ</h2>
    <p class="sec-sub">Частые вопросы</p>
    <div class="faq">
      <div class="faq-item">
        <button class="faq-q">Как это защищает меня?<span class="chev">▾</span></button>
        <div class="faq-a">Весь трафик идёт через защищённый туннель между твоим устройством и интернетом. Провайдер и сторонние сервисы не видят, что ты делаешь в сети, а реальный IP скрыт.</div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Вы храните логи?<span class="chev">▾</span></button>
        <div class="faq-a">Нет. Мы не храним историю и не следим за твоим трафиком — полная приватность.</div>
      </div>
      <div class="faq-item">
        <button class="faq-q">На скольких устройствах работает?<span class="chev">▾</span></button>
        <div class="faq-a">На тарифе на 1 и 3 месяца — до 3 устройств, на тарифе на 6 месяцев — до 5 устройств одновременно.</div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Есть ли приложения для iOS и Android?<span class="chev">▾</span></button>
        <div class="faq-a">Да, приложения для iOS и Android уже на подходе. А пока ты можешь пользоваться VPN через Telegram-бота.</div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Можно ли отменить подписку?<span class="chev">▾</span></button>
        <div class="faq-a">Да, отмена в любой момент, без сюрпризов.</div>
      </div>
    </div>
  </div>
</section>

<section class="container">
  <div class="cta">
    <h2>Готов попробовать?</h2>
    <p>Подключайся через Telegram — быстро, безопасно и без слежки.</p>
    <a class="btn" href="__BOT_URL__" target="_blank">Открыть Telegram-бота</a>
  </div>
</section>

<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <div class="logo">Awesome<span>VPN</span></div>
        <p style="color:var(--muted);font-size:14px;max-width:260px;margin-top:10px;">Приватный интернет в один тап. Быстро и без слежки.</p>
      </div>
      <div class="footer-col">
        <h4>Продукт</h4>
        <a href="#features">Возможности</a>
        <a href="#how">Как работает</a>
        <a href="#pricing">Тарифы</a>
        <a href="#faq">FAQ</a>
      </div>
      <div class="footer-col">
        <h4>Поддержка</h4>
        <a href="__BOT_URL__" target="_blank">Написать в Telegram</a>
        <a href="__BOT_URL__" target="_blank">Войти на сайте</a>
      </div>
      <div class="footer-col">
        <h4>Документы</h4>
        <a href="#">Пользовательское соглашение</a>
        <a href="#">Политика конфиденциальности</a>
        <a href="#">Возврат средств</a>
        <a href="#">Cookie</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Awesome VPN</span>
      <span class="status"><span class="dot"></span>Все системы работают</span>
    </div>
  </div>
</footer>

<script>
  document.querySelectorAll('.faq-q').forEach(function(q){
    q.addEventListener('click',function(){
      this.parentElement.classList.toggle('open');
    });
  });
</script>

</body>
</html>
"""

# Подставляем ссылку на бота
HTML = PAGE.replace("__BOT_URL__", BOT_URL)


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            body = HTML.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_error(404)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Awesome VPN лендинг запущен: http://localhost:{PORT}")
        print("Для остановки нажмите Ctrl+C")
        httpd.serve_forever()
