#!/usr/bin/env python3
# Добавляет пункт «Бухгалтерия» в сайдбар во ВСЕХ разделах:
# index.html (путь pages/accounting...), teachers и schedule (путь accounting...).
# Если пункт уже есть — пропускает. Ничего другого не трогает.
import os, re

# (файл, ссылка на schedule в этом файле, ссылка на бухгалтерию, формат пункта)
TARGETS = [
    # index.html: пункты вида <a href="pages/..." class="sidebar-item">
    {
        'file': 'index.html',
        'after': r'(<a href="pages/schedule-echo-gor\.html"[^>]*>.*?Расписание</a>)',
        'html': '\n  <a href="pages/accounting-echo-gor.html" class="sidebar-item" style="text-decoration:none">\n'
                '    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><path d="M12 6v12M9 9h4a2 2 0 0 1 0 4H9"/></svg> Бухгалтерия</a>',
    },
    # teachers / schedule: пункты вида <a href="schedule-echo-gor.html">...
    {
        'file': 'pages/teachers-echo-gor.html',
        'after': r'(<a href="schedule-echo-gor\.html"[^>]*>.*?Расписание</a>)',
        'html': '\n      <a href="accounting-echo-gor.html"><svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v12M9 9h4a2 2 0 0 1 0 4H9"/></svg>Бухгалтерия</a>',
    },
    {
        'file': 'pages/schedule-echo-gor.html',
        'after': r'(<a href="schedule-echo-gor\.html"[^>]*>.*?Расписание</a>)',
        'html': '\n      <a href="accounting-echo-gor.html"><svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v12M9 9h4a2 2 0 0 1 0 4H9"/></svg>Бухгалтерия</a>',
    },
]

for t in TARGETS:
    f = t['file']
    if not os.path.exists(f):
        print(f'— {f}: не найден, пропуск'); continue
    h = open(f, encoding='utf-8').read()
    if 'accounting-echo-gor.html' in h:
        print(f'— {f}: пункт уже есть'); continue
    new = re.sub(t['after'], r'\1' + t['html'], h, count=1, flags=re.S)
    if new == h:
        print(f'! {f}: не нашёл ссылку на «Расписание» — проверь вручную')
    else:
        open(f, 'w', encoding='utf-8').write(new)
        print(f'✓ {f}: добавлена «Бухгалтерия»')
