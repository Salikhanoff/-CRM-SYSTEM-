#!/usr/bin/env python3
# Выравнивает внутренние отступы index.html (Ученики) под Преподавателей/Расписание.
# У Учеников контент в .content с паддингом 24px 28px и есть .topbar.
# Приводим .content и .topbar к единым отступам 36px 44px.
import os, re, sys

f = 'index.html'
if not os.path.exists(f):
    print('ОШИБКА: index.html не найден. Запусти из папки -CRM-SYSTEM-'); sys.exit(1)

h = open(f, encoding='utf-8').read()
orig = h

# 1) .content паддинг -> как в других разделах
h = re.sub(r'\.content\{padding:[0-9]+px [0-9]+px;\}', '.content{padding:36px 44px;max-width:1600px;}', h, count=1)

# 2) .topbar паддинг по горизонтали выровнять под 44px, убрать нижнюю границу/фон,
#    чтобы шапка не выглядела отдельным "этажом", как в Учениках
h = re.sub(r'\.topbar\{background:var\(--white\);border-bottom:1px solid var\(--border\);padding:[0-9]+px [0-9]+px;',
           '.topbar{background:transparent;border-bottom:none;padding:36px 44px 0;', h, count=1)

# 3) max-width контента, если задаётся на .main — оставляем гибким, ограничиваем content
# (сделано в п.1)

if h == orig:
    print('Изменений не потребовалось.')
else:
    open(f, 'w', encoding='utf-8').write(h)
    print('index.html: отступы content/topbar выровнены под другие разделы.')
