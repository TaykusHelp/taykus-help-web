/* Centro de ayuda Taykus: buscador, pestañas, vídeos, imágenes y valoración. Sin dependencias. */
(function () {
  'use strict';

  var BASE = (document.querySelector('meta[name="tk-base"]') || {}).content || '';

  // ---------------------------------------------------------------------
  // Texto: normalizar sin tildes conservando la posición de cada letra
  // ---------------------------------------------------------------------
  function fold(s) {
    var out = '';
    s = String(s || '').toLowerCase();
    for (var i = 0; i < s.length; i++) {
      var c = s[i];
      var d = c.normalize('NFD').replace(/[̀-ͯ]/g, '');
      out += d.length === 1 ? d : c;
    }
    return out;
  }

  var STOP = {};
  ('a al ante con contra de del desde el en entre es esta este esto la las le les lo los mas me mi no o para pero por que se si sin sobre su sus te tu un una unas unos y ya como cual cuales donde quiero puedo hacer hago necesito').split(' ')
    .forEach(function (w) { STOP[w] = 1; });

  function tokens(s) {
    return fold(s).split(/[^a-z0-9ñ]+/).filter(function (t) { return t.length > 0; });
  }
  function queryTerms(q) {
    var all = tokens(q);
    var t = all.filter(function (w) { return !STOP[w] && w.length > 1; });
    return t.length ? t : all.filter(function (w) { return w.length > 1; });
  }

  function editDistance(a, b, max) {
    if (Math.abs(a.length - b.length) > max) return max + 1;
    var prev = [], cur = [], i, j;
    for (j = 0; j <= b.length; j++) prev[j] = j;
    for (i = 1; i <= a.length; i++) {
      cur = [i];
      var best = i;
      for (j = 1; j <= b.length; j++) {
        var cost = a[i - 1] === b[j - 1] ? 0 : 1;
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost);
        if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) cur[j] = Math.min(cur[j], prev[j - 2] + 1);
        if (cur[j] < best) best = cur[j];
      }
      if (best > max) return max + 1;
      prev = cur;
    }
    return prev[b.length];
  }

  // ---------------------------------------------------------------------
  // Índice
  // ---------------------------------------------------------------------
  var indexPromise = null;
  function loadIndex() {
    if (!indexPromise) {
      indexPromise = fetch(BASE + '/search-index.json').then(function (r) { return r.json(); }).then(buildIndex);
    }
    return indexPromise;
  }

  function countMap(text) {
    var m = {};
    tokens(text).forEach(function (t) { m[t] = (m[t] || 0) + 1; });
    return m;
  }

  function buildIndex(docs) {
    var vocab = {};
    docs.forEach(function (d) {
      d.ft = countMap(d.t);
      d.fh = countMap(d.h);
      d.fb = countMap(d.b);
      d.fx = countMap(d.x);
      [d.ft, d.fh, d.fb, d.fx].forEach(function (f) {
        for (var k in f) vocab[k] = (vocab[k] || 0) + 1;
      });
    });
    return { docs: docs, vocab: vocab, words: Object.keys(vocab) };
  }

  // Posibles palabras del índice para un término escrito (exacta, empieza por, o con faltas)
  function expand(idx, term) {
    var out = [];
    if (idx.vocab[term]) out.push({ w: term, s: 1, exact: true });
    var maxEd = term.length <= 3 ? 0 : term.length <= 5 ? 1 : 2;
    for (var i = 0; i < idx.words.length; i++) {
      var w = idx.words[i];
      if (w === term) continue;
      if (term.length >= 3 && w.indexOf(term) === 0) { out.push({ w: w, s: 0.75, prefix: true }); continue; }
      if (maxEd && Math.abs(w.length - term.length) <= maxEd) {
        var d = editDistance(term, w, maxEd);
        if (d <= maxEd) out.push({ w: w, s: 0.65 - 0.12 * (d - 1), fuzzy: true, d: d });
      }
    }
    // Con faltas: quedarse solo con las palabras más parecidas
    var minD = Infinity;
    out.forEach(function (e) { if (e.fuzzy && e.d < minD) minD = e.d; });
    return out.filter(function (e) { return !e.fuzzy || e.d === minD; });
  }

  function fieldScore(d, w) {
    var s = 0;
    if (d.ft[w]) s += 10;
    if (d.fh[w]) s += 4;
    if (d.fb[w]) s += 2;
    if (d.fx[w]) s += Math.min(3, 1 + Math.log(1 + d.fx[w]));
    return s;
  }

  function search(idx, q) {
    var terms = queryTerms(q);
    if (!terms.length) return { results: [], terms: [], corrected: null };
    var expansions = terms.map(function (t) { return expand(idx, t); });
    var corrected = null;
    var correctedTerms = terms.map(function (t, i) {
      var ex = expansions[i];
      if (ex.some(function (e) { return e.exact || e.prefix; })) return t;
      var fz = ex.filter(function (e) { return e.fuzzy; }).sort(function (a, b) { return a.d - b.d || idx.vocab[b.w] - idx.vocab[a.w]; });
      if (fz.length) { corrected = true; return fz[0].w; }
      return t;
    });
    if (corrected) corrected = correctedTerms.join(' ');

    function run(requireAll) {
      var res = [];
      idx.docs.forEach(function (d) {
        var total = 0, matched = 0, hit = [];
        expansions.forEach(function (ex) {
          var best = 0, bestW = null;
          ex.forEach(function (e) {
            var fs = fieldScore(d, e.w);
            if (fs && fs * e.s > best) { best = fs * e.s; bestW = e.w; }
          });
          if (best) { matched++; total += best; hit.push(bestW); }
        });
        if (!matched || (requireAll && matched < expansions.length)) return;
        // Bonus si la frase completa aparece en el título
        if (fold(d.t).indexOf(fold(q).trim()) !== -1) total += 15;
        res.push({ d: d, score: total * (matched / expansions.length), hit: hit });
      });
      return res.sort(function (a, b) { return b.score - a.score; });
    }
    var results = run(true);
    var partial = false;
    if (!results.length && expansions.length > 1) { results = run(false); partial = results.length > 0; }
    return { results: results, terms: terms, corrected: corrected, partial: partial };
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; });
  }

  function highlight(text, words) {
    if (!words || !words.length) return esc(text);
    var f = fold(text), marks = [];
    words.forEach(function (w) {
      if (!w || w.length < 2) return;
      var re = new RegExp('(^|[^a-z0-9ñ])(' + w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '[a-z0-9ñ]*)', 'g'), m;
      while ((m = re.exec(f))) marks.push([m.index + m[1].length, m.index + m[0].length]);
    });
    if (!marks.length) return esc(text);
    marks.sort(function (a, b) { return a[0] - b[0]; });
    var out = '', pos = 0;
    marks.forEach(function (r) {
      if (r[0] < pos) return;
      out += esc(text.slice(pos, r[0])) + '<mark class="tk-hl">' + esc(text.slice(r[0], r[1])) + '</mark>';
      pos = r[1];
    });
    return out + esc(text.slice(pos));
  }

  function snippet(text, words) {
    var f = fold(text), at = -1;
    (words || []).forEach(function (w) {
      var re = new RegExp('(^|[^a-z0-9ñ])' + w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
      var m = re.exec(f);
      if (m && (at === -1 || m.index < at)) at = m.index;
    });
    if (at === -1) return text.slice(0, 180) + (text.length > 180 ? '…' : '');
    var start = Math.max(0, at - 70), end = Math.min(text.length, at + 150);
    if (start > 0) { var sp = text.indexOf(' ', start); if (sp !== -1 && sp < at) start = sp + 1; }
    if (end < text.length) { var sp2 = text.lastIndexOf(' ', end); if (sp2 > at) end = sp2; }
    return (start > 0 ? '…' : '') + text.slice(start, end) + (end < text.length ? '…' : '');
  }

  // ---------------------------------------------------------------------
  // Desplegable de resultados mientras se escribe
  // ---------------------------------------------------------------------
  function setupLiveSearch(form) {
    var input = form.querySelector('input[name="q"]');
    var pop = form.querySelector('.tk-search-pop');
    if (!input || !pop) return;
    var sel = -1, timer = null;

    function close() { pop.hidden = true; input.setAttribute('aria-expanded', 'false'); sel = -1; }
    function render() {
      var q = input.value.trim();
      if (q.length < 2) { close(); return; }
      loadIndex().then(function (idx) {
        if (input.value.trim() !== q) return;
        var r = search(idx, q);
        var items = r.results.slice(0, 6);
        var html = '';
        if (!items.length) {
          html = '<div class="tk-pop-empty">No hay resultados para «' + esc(q) + '». Prueba con otras palabras.</div>';
        } else {
          items.forEach(function (it, i) {
            html += '<a class="tk-pop-item" role="option" id="opt' + i + '" href="' + esc(it.d.u) + '"><span class="tk-pop-title">' +
              highlight(it.d.t, it.hit) + '</span><span class="tk-pop-crumb">' + esc(it.d.b) + '</span></a>';
          });
          html += '<a class="tk-pop-foot" href="' + esc(BASE + '/buscar/?q=' + encodeURIComponent(q)) + '">Ver todos los resultados (' + r.results.length + ')</a>';
        }
        pop.innerHTML = html;
        pop.hidden = false;
        input.setAttribute('aria-expanded', 'true');
        sel = -1;
      });
    }
    input.addEventListener('focus', function () { loadIndex(); });
    input.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(render, 120); });
    input.addEventListener('keydown', function (e) {
      var opts = pop.hidden ? [] : pop.querySelectorAll('.tk-pop-item');
      if (e.key === 'ArrowDown' && opts.length) { e.preventDefault(); sel = Math.min(opts.length - 1, sel + 1); }
      else if (e.key === 'ArrowUp' && opts.length) { e.preventDefault(); sel = Math.max(-1, sel - 1); }
      else if (e.key === 'Enter' && sel >= 0 && opts[sel]) { e.preventDefault(); window.location.href = opts[sel].href; return; }
      else if (e.key === 'Escape') { close(); return; }
      else return;
      Array.prototype.forEach.call(opts, function (o, i) { o.setAttribute('aria-selected', i === sel ? 'true' : 'false'); });
      input.setAttribute('aria-activedescendant', sel >= 0 ? 'opt' + sel : '');
    });
    document.addEventListener('click', function (e) { if (!form.contains(e.target)) close(); });
  }

  // ---------------------------------------------------------------------
  // Página de resultados
  // ---------------------------------------------------------------------
  function setupResultsPage() {
    var box = document.querySelector('.tk-results');
    if (!box) return;
    var info = document.querySelector('.tk-results-info');
    var filters = document.querySelector('.tk-filters');
    var form = document.querySelector('.tk-search-page');
    var input = form && form.querySelector('input[name="q"]');
    var params = new URLSearchParams(window.location.search);
    var q = params.get('q') || '';
    var current = 'all';
    if (input) input.value = q;

    function show() {
      if (!q.trim()) {
        info.textContent = 'Escribe lo que necesitas: por ejemplo «festivo», «abrir caja» o «bono».';
        filters.innerHTML = ''; box.innerHTML = '';
        return;
      }
      loadIndex().then(function (idx) {
        var r = search(idx, q);
        var all = r.results;
        var counts = {}, video = 0;
        all.forEach(function (it) { counts[it.d.m] = (counts[it.d.m] || 0) + 1; if (it.d.v) video++; });
        var list = all.filter(function (it) {
          return current === 'all' || (current === 'video' ? it.d.v : it.d.m === current);
        });
        var shown = r.corrected ? r.corrected : q;
        var msg = all.length
          ? (all.length === 1 ? '1 resultado' : all.length + ' resultados') + ' para <strong>' + esc(shown) + '</strong>'
          : 'No hay resultados para <strong>' + esc(q) + '</strong>. Prueba con otras palabras o escríbenos.';
        if (r.corrected && all.length) msg += '. Buscaste «' + esc(q) + '».';
        if (r.partial) msg += ' No hay artículos con todas las palabras; mostramos los más parecidos.';
        info.innerHTML = msg;

        var fhtml = '';
        if (all.length) {
          fhtml += '<button type="button" data-f="all" aria-pressed="' + (current === 'all') + '">Todos · ' + all.length + '</button>';
          Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a]; }).forEach(function (m) {
            fhtml += '<button type="button" data-f="' + esc(m) + '" aria-pressed="' + (current === m) + '">' + esc(m) + ' · ' + counts[m] + '</button>';
          });
          if (video) fhtml += '<button type="button" data-f="video" aria-pressed="' + (current === 'video') + '">Con vídeo · ' + video + '</button>';
        }
        filters.innerHTML = fhtml;

        var html = '';
        list.slice(0, 50).forEach(function (it) {
          html += '<a class="tk-result" href="' + esc(it.d.u) + '"><span class="tk-result-crumb">' + esc(it.d.b) +
            (it.d.v ? '<span class="tk-tag">Vídeo</span>' : '') + '</span><span class="tk-result-title">' + highlight(it.d.t, it.hit) +
            '</span><span class="tk-result-snip">' + highlight(snippet(it.d.x, it.hit), it.hit) + '</span></a>';
        });
        box.innerHTML = html;
        document.title = (q ? q + ' · ' : '') + 'Buscar · Centro de ayuda Taykus';
      });
    }
    filters.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-f]');
      if (!b) return;
      current = b.getAttribute('data-f');
      show();
    });
    if (form) form.addEventListener('submit', function (e) {
      e.preventDefault();
      q = input.value;
      current = 'all';
      var pop = form.querySelector('.tk-search-pop'); if (pop) pop.hidden = true;
      history.replaceState(null, '', '?q=' + encodeURIComponent(q));
      show();
    });
    show();
  }

  // ---------------------------------------------------------------------
  // Contenido de los artículos
  // ---------------------------------------------------------------------
  function setupTabs() {
    document.querySelectorAll('.tk-tabs').forEach(function (tabs, n) {
      var panes = Array.prototype.filter.call(tabs.children, function (c) { return c.classList.contains('tk-tab'); });
      // Las pestañas vacías no se muestran
      panes = panes.filter(function (p) {
        if (p.textContent.trim() || p.querySelector('img, iframe, a')) return true;
        p.remove();
        return false;
      });
      if (!panes.length) return;
      if (panes.length === 1) { tabs.classList.add('is-single'); return; }
      var list = document.createElement('div');
      list.className = 'tk-tablist';
      list.setAttribute('role', 'tablist');
      panes.forEach(function (p, i) {
        var b = document.createElement('button');
        b.type = 'button';
        b.textContent = p.getAttribute('data-title') || 'Pestaña ' + (i + 1);
        b.setAttribute('role', 'tab');
        b.id = 'tab' + n + '-' + i;
        p.setAttribute('role', 'tabpanel');
        p.setAttribute('aria-labelledby', b.id);
        b.addEventListener('click', function () { select(i); });
        list.appendChild(b);
      });
      function select(i) {
        panes.forEach(function (p, j) { p.classList.toggle('is-active', i === j); });
        Array.prototype.forEach.call(list.children, function (b, j) { b.setAttribute('aria-selected', i === j ? 'true' : 'false'); b.tabIndex = i === j ? 0 : -1; });
      }
      list.addEventListener('keydown', function (e) {
        var cur = Array.prototype.indexOf.call(list.children, document.activeElement);
        if (cur < 0) return;
        if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
          e.preventDefault();
          var nx = (cur + (e.key === 'ArrowRight' ? 1 : -1) + panes.length) % panes.length;
          select(nx); list.children[nx].focus();
        }
      });
      tabs.insertBefore(list, tabs.firstChild);
      tabs.classList.add('is-ready');
      select(0);
    });
  }

  function setupVideos() {
    document.addEventListener('click', function (e) {
      var a = e.target.closest('.tk-video-btn');
      if (!a) return;
      e.preventDefault();
      var id = a.getAttribute('data-yt');
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) + '?autoplay=1&rel=0';
      f.title = 'Vídeo tutorial';
      f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
      f.allowFullscreen = true;
      a.replaceWith(f);
    });
  }

  function setupLightbox() {
    var box = document.querySelector('.tk-lightbox');
    if (!box) return;
    document.addEventListener('click', function (e) {
      var img = e.target.closest('.tk-content img');
      if (!img || img.closest('a')) return;
      box.innerHTML = '';
      var big = document.createElement('img');
      big.src = img.currentSrc || img.src;
      big.alt = img.alt || '';
      box.appendChild(big);
      box.hidden = false;
    });
    box.addEventListener('click', function () { box.hidden = true; });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') box.hidden = true; });
  }

  function setupFeedback() {
    document.querySelectorAll('.tk-feedback').forEach(function (fb) {
      fb.addEventListener('click', function (e) {
        var b = e.target.closest('button[data-fb]');
        if (!b) return;
        fb.querySelector('.tk-fb-btns').hidden = true;
        fb.querySelector('.tk-fb-q').hidden = true;
        var t = fb.querySelector('.tk-fb-thanks');
        t.hidden = false;
        if (b.getAttribute('data-fb') === 'no') t.textContent = 'Gracias. Si necesitas ayuda con esto, escríbenos y lo vemos contigo.';
        if (window.gtag) window.gtag('event', 'valoracion', { valor: b.getAttribute('data-fb'), pagina: location.pathname });
      });
    });
  }

  function setupSidebar() {
    var side = document.querySelector('.tk-side');
    if (!side) return;
    var btn = side.querySelector('.tk-side-toggle');
    btn.addEventListener('click', function () {
      var open = side.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    var cur = side.querySelector('[aria-current="page"]');
    if (cur && side.scrollHeight > side.clientHeight) side.scrollTop = Math.max(0, cur.offsetTop - side.clientHeight / 2);
  }

  function setupToc() {
    var links = document.querySelectorAll('.tk-toc a');
    if (!links.length || !('IntersectionObserver' in window)) return;
    var map = {};
    links.forEach(function (l) { map[l.getAttribute('href').slice(1)] = l; });
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          links.forEach(function (l) { l.classList.remove('is-active'); });
          var l = map[en.target.id]; if (l) l.classList.add('is-active');
        }
      });
    }, { rootMargin: '-90px 0px -70% 0px' });
    Object.keys(map).forEach(function (id) { var h = document.getElementById(id); if (h) obs.observe(h); });
  }

  function init() {
    document.querySelectorAll('.tk-search').forEach(function (f) { if (!f.classList.contains('tk-search-page')) setupLiveSearch(f); });
    setupResultsPage();
    setupTabs();
    setupVideos();
    setupLightbox();
    setupFeedback();
    setupSidebar();
    setupToc();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
