#!/usr/bin/env python3
# Брендирование index.html — ШАГ 2: перекраска рабочей палитры.
# Файл использует второй :root с --amber/--purple/--blue. Перебиваем его
# значения на фирменные цвета Эхо Гор. Структуру и логику не трогаем.
import os, re, sys

f = 'index.html'
if not os.path.exists(f):
    print('ОШИБКА: index.html не найден. Запусти из папки -CRM-SYSTEM-'); sys.exit(1)

h = open(f, encoding='utf-8').read()
orig = h

# Брендовые значения для переменных, которые реально использует файл.
# Амбер -> золотисто-оливковый, синий/фиолет/оранж -> голубой/золото из логобука.
REPL = {
    '--amber:#C87A00;'        : '--amber:#947C51;',
    '--amber-bg:#FFF4E0;'     : '--amber-bg:#F2EDE2;',
    '--amber-btn:#F5A623;'    : '--amber-btn:#947C51;',
    '--ink:#0A0A0A;'          : '--ink:#1A1A1A;',
    '--bg:#F5F5F7;'           : '--bg:#F4F5F3;',
    '--border:#E5E5EA;'       : '--border:#E7E8E2;',
    '--green:#1B7B3A;'        : '--green:#5C8A5C;',
    '--green-bg:#F0FBF4;'     : '--green-bg:#E9F0E6;',
    '--green-border:#A8D5B5;' : '--green-border:#CFE0C7;',
    '--blue:#1A56DB;'         : '--blue:#5A8499;',
    '--blue-bg:#EFF6FF;'      : '--blue-bg:#EAF1F4;',
    '--blue-border:#BFDBFE;'  : '--blue-border:#BBD3DE;',
    '--purple:#6D28D9;'       : '--purple:#947C51;',
    '--purple-bg:#F5F3FF;'    : '--purple-bg:#F2EDE2;',
    '--purple-border:#DDD6FE;': '--purple-border:#E0D6BF;',
    '--orange:#C2410C;'       : '--orange:#7A6440;',
    '--orange-bg:#FFF7ED;'    : '--orange-bg:#F2EDE2;',
    '--orange-border:#FED7AA;': '--orange-border:#E0D6BF;',
    '--red:#D32F2F;'          : '--red:#C16B4A;',
    '--red-bg:#FFF0F0;'       : '--red-bg:#F6E9E1;',
    '--red-border:#FFCDD2;'   : '--red-border:#EAD2C4;',
}
for a,b in REPL.items():
    h = h.replace(a,b)

# Старый логотип-квадрат (фиолетово-коралловый градиент) -> тёмный бренд-цвет
h = h.replace('background:linear-gradient(135deg,#6D5BD0,#FF6B5B)','background:#1A1A1A')
h = h.replace('.sidebar-logo-text span{color:#6D5BD0;}','.sidebar-logo-text span{color:#87B1C5;}')

# Иконки KPI с жёстко прописанными цветами -> к бренду
h = h.replace('.kpi-icon.orange{background:#FFF3E0;color:#E65100;}','.kpi-icon.orange{background:#F2EDE2;color:#7A6440;}')
h = h.replace('.kpi-icon.green{background:#E8F8EE;color:var(--green);}','.kpi-icon.green{background:#E9F0E6;color:var(--green);}')

if h == orig:
    print('Ничего не заменилось — проверь, запускал ли уже скрипт.')
else:
    open(f,'w',encoding='utf-8').write(h)
    print('index.html ПЕРЕКРАШЕН в бренд-цвета Эхо Гор')
