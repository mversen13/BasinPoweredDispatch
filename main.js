// Basin Powered Dispatch: small site behaviors (kept out of the HTML for a strict CSP)
(function () {
  var btn = document.querySelector('.menu-btn');
  var menu = document.getElementById('menu');
  if (btn && menu) btn.addEventListener('click', function () { menu.classList.toggle('open'); });

  var yr = document.getElementById('yr');
  if (yr) yr.textContent = String(new Date().getFullYear());

  // Pre-select carrier/operator on the join form from ?type=
  var sel = document.getElementById('jtype');
  if (sel) {
    var t = new URLSearchParams(location.search).get('type');
    if (t === 'carrier') sel.value = 'Carrier';
    if (t === 'operator') sel.value = 'Operator';
  }

  // Redirect pages (e.g. demo-ready) declare their target in data-redirect
  var r = document.querySelector('[data-redirect]');
  if (r) {
    var url = r.getAttribute('data-redirect');
    if (/^https:\/\/([a-z0-9-]+\.)*basinpowereddispatch\.com\//.test(url)) {
      setTimeout(function () { location.href = url; }, 2500);
    }
  }
})();
