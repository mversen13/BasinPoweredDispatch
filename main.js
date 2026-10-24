// Basin Powered Dispatch: small site behaviors (kept out of the HTML for a strict CSP)
(function () {
  var btn = document.querySelector('.menu-btn');
  var menu = document.getElementById('menu');
  if (btn && menu) btn.addEventListener('click', function () { menu.classList.toggle('open'); });

  var yr = document.getElementById('yr');
  if (yr) yr.textContent = String(new Date().getFullYear());
})();
