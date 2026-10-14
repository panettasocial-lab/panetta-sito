// Panetta — comparsa allo scroll + parallasse leggero
(function () {
  var ridotto = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (ridotto) return;

  // comparsa: nasconde solo gli elementi sotto la piega, poi li rivela
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (voci) {
      voci.forEach(function (v) {
        if (v.isIntersecting) { v.target.classList.remove('rv--off'); io.unobserve(v.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    document.querySelectorAll('.rv').forEach(function (el) {
      if (el.getBoundingClientRect().top > window.innerHeight * 0.92) {
        el.classList.add('rv--off');
        io.observe(el);
      }
    });
  }

  // parallasse sulle foto (solo schermi larghi)
  var foto = [].slice.call(document.querySelectorAll('[data-par]'));
  if (!foto.length) return;
  var mq = window.matchMedia('(min-width: 861px)');
  var inCorso = false;
  function aggiorna() {
    inCorso = false;
    var h = window.innerHeight;
    foto.forEach(function (el) {
      if (!mq.matches || el.classList.contains('rv--off')) { el.style.translate = ''; return; }
      var r = el.getBoundingClientRect();
      if (r.bottom < -200 || r.top > h + 200) return;
      var d = (r.top + r.height / 2 - h / 2) * parseFloat(el.dataset.par);
      el.style.translate = '0 ' + (-d).toFixed(1) + 'px';
    });
  }
  function chiedi() { if (!inCorso) { inCorso = true; requestAnimationFrame(aggiorna); } }
  window.addEventListener('scroll', chiedi, { passive: true });
  window.addEventListener('resize', chiedi);
  aggiorna();
})();
