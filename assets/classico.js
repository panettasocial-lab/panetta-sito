// Panetta — proposta classico: farina che cade nell'hero e si sposta col mouse
(function () {
  var c = document.querySelector('.farina');
  if (!c || (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches)) return;
  var x = c.getContext('2d'), dpr = Math.min(window.devicePixelRatio || 1, 2);
  var W = 0, H = 0, P = [], mx = -1e4, my = -1e4, vis = true, gira = false;

  function misura() {
    var r = c.getBoundingClientRect();
    W = r.width; H = r.height;
    c.width = W * dpr; c.height = H * dpr;
    x.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  function granello(inizio) {
    return { x: Math.random() * W, y: inizio ? Math.random() * H : -6, r: Math.random() * 1.7 + .4,
             v: Math.random() * .22 + .06, f: Math.random() * 6.28, a: Math.random() * .45 + .4, vx: 0 };
  }
  misura();
  var n = Math.round(Math.min(150, W * H / 7000));
  for (var i = 0; i < n; i++) P.push(granello(true));
  window.addEventListener('resize', misura);

  var area = c.parentNode;
  area.addEventListener('pointermove', function (e) {
    var r = c.getBoundingClientRect(); mx = e.clientX - r.left; my = e.clientY - r.top;
  });
  area.addEventListener('pointerleave', function () { mx = my = -1e4; });

  function frame() {
    if (!vis) { gira = false; return; }
    x.clearRect(0, 0, W, H);
    x.fillStyle = '#FFFFFF';
    for (var i = 0; i < P.length; i++) {
      var p = P[i];
      p.f += .012; p.y += p.v; p.x += Math.sin(p.f) * .22 + p.vx; p.vx *= .94;
      var dx = p.x - mx, dy = p.y - my, d = dx * dx + dy * dy;
      if (d < 9000) { var k = (1 - d / 9000) * .7, l = Math.sqrt(d) + 1; p.vx += dx / l * k; p.y += dy / l * k * .5; }
      if (p.y > H + 8 || p.x < -20 || p.x > W + 20) P[i] = granello(false);
      x.globalAlpha = p.a; x.beginPath(); x.arc(p.x, p.y, p.r, 0, 6.283); x.fill();
    }
    requestAnimationFrame(frame);
  }
  new IntersectionObserver(function (e) {
    vis = e[0].isIntersecting;
    if (vis && !gira) { gira = true; requestAnimationFrame(frame); }
  }).observe(c);
})();
