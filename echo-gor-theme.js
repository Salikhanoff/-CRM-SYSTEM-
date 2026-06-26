/* ЭХО ГОР — переключатель темы день/ночь.
   Подключите в конце <body>:  <script src="echo-gor-theme.js"></script>
   и добавьте куда угодно кнопку:  <button id="eg-theme-toggle">🌙 / ☀</button>
   Если кнопки нет — тема всё равно восстановится из памяти. */
(function () {
  var KEY = 'eg-theme';
  var saved = localStorage.getItem(KEY) || 'night';      // 'night' (по умолч.) или 'day'
  apply(saved);

  function apply(mode) {
    if (mode === 'day') document.documentElement.setAttribute('data-theme', 'day');
    else document.documentElement.removeAttribute('data-theme');
    localStorage.setItem(KEY, mode);
    var btn = document.getElementById('eg-theme-toggle');
    if (btn) btn.textContent = mode === 'day' ? '☀' : '☾';
  }

  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest('#eg-theme-toggle');
    if (!btn) return;
    var now = localStorage.getItem(KEY) === 'day' ? 'night' : 'day';
    apply(now);
  });

  // на случай раннего запуска — выставим иконку после загрузки DOM
  document.addEventListener('DOMContentLoaded', function () { apply(localStorage.getItem(KEY) || 'night'); });
})();
