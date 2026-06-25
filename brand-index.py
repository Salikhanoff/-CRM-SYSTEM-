#!/usr/bin/env python3
# Брендирование index.html (раздел «Ученики») в стиль «Эхо Гор».
# Меняет ТОЛЬКО оформление: цветовые переменные, шрифт заголовков,
# логотип и пункты сайдбара (+ добавляет «Расписание»). Логику не трогает.
import os, re, sys

f = 'index.html'
if not os.path.exists(f):
    print('ОШИБКА: index.html не найден. Запусти из папки -CRM-SYSTEM-'); sys.exit(1)

h = open(f, encoding='utf-8').read()
orig = h

# 1) Подключить брендовые шрифты (Bebas Neue для заголовков)
if 'Bebas+Neue' not in h:
    h = h.replace(
        '<link href="https://fonts.googleapis.com/css2?family=Inter',
        '<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Oswald:wght@400;500;600;700&family=Inter',
        1)
    if 'Bebas+Neue' not in h:
        # запасной вариант — вставить перед </head> ... (head может не иметь Inter-ссылки)
        h = h.replace('</head>',
          '<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Oswald:wght@400;500;600;700&display=swap" rel="stylesheet">\n</head>', 1)

# 2) Брендовые CSS-переменные. Добавляем блок в начало <style> (переопределит дефолты).
BRAND = """
/* ===== ЭХО ГОР brand palette (auto) ===== */
:root{
  --white:#FFFFFF; --bg:#F4F5F3; --ink:#1A1A1A; --muted:#8A8F86;
  --border:#E7E8E2; --gold:#947C51; --gold-soft:#F2EDE2; --gold-ink:#7A6440;
  --blue:#87B1C5; --green:#5C8A5C; --red:#C16B4A;
  --primary:#947C51; --accent:#87B1C5;
}
h1,h2,h3,.topbar-title{font-family:'Bebas Neue','Oswald',sans-serif !important;letter-spacing:.01em;}
.eg-brand{background:var(--ink);border-radius:14px;padding:16px 18px;margin:0 12px 12px;}
.eg-logo{font-family:'Bebas Neue',sans-serif;font-size:30px;line-height:1;display:flex;gap:4px;}
.eg-logo .e{color:#87B1C5;} .eg-logo .g{color:#fff;}
.eg-sub{color:#9aa0a6;font-size:9px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;margin-top:5px;}
.sidebar-item.active{background:var(--gold-soft) !important;color:var(--gold-ink) !important;}
"""
h = h.replace('<style>', '<style>\n'+BRAND, 1)

# 3) Логотип: заменить старый логотип-блок на брендовый, если он есть
h = re.sub(
    r'<div class="sidebar-logo">.*?</div>\s*</div>',
    '<div class="eg-brand"><div class="eg-logo"><span class="e">ЭХО</span><span class="g">ГОР</span></div><div class="eg-sub">Студия кавказского танца</div></div>',
    h, count=1, flags=re.S)

# 4) Сайдбар: единый набор пунктов с активным «Ученики» и ссылками
NAV = '''<div class="sidebar-section">Основное</div>
  <a href="index.html" class="sidebar-item active" style="text-decoration:none">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/></svg> Ученики</a>
  <a href="pages/teachers-echo-gor.html" class="sidebar-item" style="text-decoration:none">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M22 10L12 5 2 10l10 5 10-5zM6 12v5c0 1 3 3 6 3s6-2 6-3v-5"/></svg> Преподаватели</a>
  <a href="pages/schedule-echo-gor.html" class="sidebar-item" style="text-decoration:none">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg> Расписание</a>'''

# вырезаем всё от "Основное" до конца последнего sidebar-item перед </aside>,
# заменяя на наш NAV. Берём диапазон от <div class="sidebar-section">Основное</div>.
m = re.search(r'<div class="sidebar-section">Основное</div>.*?(?=</aside>)', h, flags=re.S)
if m:
    h = h[:m.start()] + NAV + '\n  ' + h[m.end():]
else:
    print('ВНИМАНИЕ: блок навигации не найден по шаблону — логотип и цвета применены, пункты меню проверь вручную.')

if h == orig:
    print('Ничего не изменилось — возможно уже брендировано.')
else:
    open(f, 'w', encoding='utf-8').write(h)
    print('index.html ОБНОВЛЁН: бренд-стиль Эхо Гор + Расписание в меню')
