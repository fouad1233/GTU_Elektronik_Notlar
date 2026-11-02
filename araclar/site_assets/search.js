/* Basit, bağımlılıksız site içi arama (Türkçe karakter duyarsız). search-index.json dosyasını okur. */
(function () {
  var input = document.getElementById('q'), list = document.getElementById('results');
  var me = document.currentScript;
  if (!input || !list || !me) return;
  var url = me.getAttribute('data-index'), root = me.getAttribute('data-root') || '';
  var empty = me.getAttribute('data-empty') || 'Sonuç bulunamadı';
  var data = null, loading = false;
  function fold(s) {
    return String(s).replace(/İ/g, 'i').replace(/I/g, 'i').toLowerCase().replace(/ı/g, 'i')
      .replace(/ç/g, 'c').replace(/ğ/g, 'g').replace(/ö/g, 'o').replace(/ş/g, 's').replace(/ü/g, 'u');
  }
  function load(cb) {
    if (data) return cb();
    if (loading) return;
    loading = true;
    fetch(url).then(function (r) { return r.json(); }).then(function (j) {
      data = j.map(function (e) { e.f = fold(e.t); e.g = fold(e.k || ''); return e; });
      cb();
    }).catch(function () { loading = false; });
  }
  function run() {
    var q = fold(input.value).trim();
    list.textContent = '';
    if (q.length < 2) return;
    var toks = q.split(/\s+/), res = [];
    data.forEach(function (e) {
      var s = 0;
      for (var i = 0; i < toks.length; i++) {
        if (e.f.indexOf(toks[i]) > -1) s += 3;
        else if (e.g.indexOf(toks[i]) > -1) s += 1;
        else return;
      }
      if (e.y === 'Ders') s += 2;
      res.push([s, e]);
    });
    res.sort(function (a, b) { return b[0] - a[0]; });
    if (!res.length) {
      var li = document.createElement('li'); li.className = 'muted'; li.style.padding = '9px 14px';
      li.textContent = empty; list.appendChild(li); return;
    }
    res.slice(0, 25).forEach(function (r) {
      var e = r[1], li = document.createElement('li'), a = document.createElement('a');
      var st = document.createElement('strong'), sm = document.createElement('small');
      a.href = root + e.u; st.textContent = e.t; sm.textContent = e.y + (e.c ? ' · ' + e.c : '');
      a.appendChild(st); a.appendChild(sm); li.appendChild(a); list.appendChild(li);
    });
  }
  input.addEventListener('input', function () { load(run); });
  input.addEventListener('focus', function () { load(function () {}); });
})();
