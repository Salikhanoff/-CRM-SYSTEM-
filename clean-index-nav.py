#!/usr/bin/env python3
# Убирает из сайдбара index.html пункты-заглушки (Зарплаты, Журнал, Настройки),
# оставляя только рабочие: Ученики, Преподаватели, Расписание.
import os, re, sys

f = 'index.html'
if not os.path.exists(f):
    print('ОШИБКА: index.html не найден. Запусти из папки -CRM-SYSTEM-'); sys.exit(1)

h = open(f, encoding='utf-8').read()
orig = h

# Удаляем любые пункты сайдбара (sidebar-item), ведущие в toast-заглушку
h = re.sub(r'\n\s*<a [^>]*onclick="[^"]*toast[^"]*"[^>]*class="sidebar-item"[^>]*>.*?</a>', '', h, flags=re.S)
h = re.sub(r'\n\s*<a [^>]*class="sidebar-item"[^>]*onclick="[^"]*toast[^"]*"[^>]*>.*?</a>', '', h, flags=re.S)
# На случай если заглушки оформлены как <div class="sidebar-item" onclick=...toast...>
h = re.sub(r'\n\s*<div class="sidebar-item"[^>]*onclick="[^"]*toast[^"]*"[^>]*>.*?</div>', '', h, flags=re.S)

if h == orig:
    print('Заглушек в index.html не найдено — меню уже чистое (Ученики, Преподаватели, Расписание).')
else:
    open(f,'w',encoding='utf-8').write(h)
    print('index.html: лишние пункты убраны.')
