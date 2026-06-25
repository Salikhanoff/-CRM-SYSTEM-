#!/usr/bin/env python3
# Выравнивает геометрию index.html (Ученики) под Преподавателей/Расписание:
# одинаковая ширина сайдбара и фиксированный вертикальный скроллбар,
# чтобы при переключении вкладок ничего не «прыгало».
import os, re, sys

f = 'index.html'
if not os.path.exists(f):
    print('ОШИБКА: index.html не найден. Запусти из папки -CRM-SYSTEM-'); sys.exit(1)

h = open(f, encoding='utf-8').read()
orig = h

# 1) Ширина сайдбара 220 -> 280 (как в других разделах)
h = re.sub(r'(\.sidebar\{width:)220px', r'\g<1>280px', h, count=1)

# 2) Фикс вертикального скроллбара на body (убирает горизонтальный сдвиг)
if 'overflow-y:scroll' not in h:
    # добавляем правило прямо в body{...}
    h = re.sub(r'(body\{[^}]*?)\}', r'\1;overflow-y:scroll}', h, count=1)

# 3) Лёгкое выравнивание отступов контента, если используется .content
h = re.sub(r'\.content\{padding:[0-9]+px [0-9]+px;', '.content{padding:36px 44px;', h, count=1)

if h == orig:
    print('Изменений не потребовалось (возможно уже выровнено).')
else:
    open(f, 'w', encoding='utf-8').write(h)
    print('index.html выровнен по геометрии (сайдбар 280px, фикс скролла).')
