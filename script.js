/* Agenciy – interactions measured from the original site */
(() => {
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const smooth = t => t * t * (3 - 2 * t);
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ---- scroll reveals: play once when the element's top reaches ~76% of the viewport ---- */
const revealIO = new IntersectionObserver(es => es.forEach(e => {
  if (!e.isIntersecting) return;
  e.target.classList.add('in');
  revealIO.unobserve(e.target);
  const b = $('[data-count]', e.target);
  if (b) countUp(b);
}), { rootMargin: '0px 0px -24% 0px', threshold: 0 });
$$('[data-reveal]').forEach(el => {
  el.style.setProperty('--ry', (el.dataset.y ?? 60) + 'px');
  if (el.dataset.x) el.style.setProperty('--rx', el.dataset.x + 'px');
  if (el.dataset.scale) el.style.setProperty('--rs', '.8');
  if (el.dataset.scale) el.style.setProperty('--ry', '30px');
  revealIO.observe(el);
});

/* project covers: 1.15 -> 1 zoom, once, a bit earlier than other reveals */
const coverIO = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('in'); coverIO.unobserve(e.target); }
}), { rootMargin: '0px 0px -27% 0px' });
$$('.project').forEach(p => coverIO.observe(p));

/* ---- stat counters (~1.1s, fast start then settle) ---- */
function countUp(el) {
  const to = +el.dataset.count;
  if (reduce) { el.textContent = to + '+'; return; }
  const t0 = performance.now(), D = 1300;
  const step = t => {
    const k = clamp((t - t0) / D);
    el.textContent = Math.round(to * (k === 1 ? 1 : 1 - Math.pow(2, -10 * k))) + '+';
    if (k < 1) requestAnimationFrame(step);
  };
  el.textContent = '0+';
  requestAnimationFrame(step);
}

/* ---- per-character text reveals driven by scroll ---- */
function splitChars(el) {
  const text = el.textContent.trim();
  el.innerHTML = '';
  const chars = [];
  text.split(' ').forEach((w, i, a) => {
    const word = document.createElement('span');
    word.style.whiteSpace = 'nowrap'; word.style.display = 'inline-block'; word.style.textIndent = '0';
    [...w].forEach(ch => { const s = document.createElement('span'); s.className = 'c'; s.textContent = ch; word.appendChild(s); chars.push(s); });
    el.appendChild(word);
    if (i < a.length - 1) el.appendChild(document.createTextNode(' '));
  });
  return chars;
}
const heroP = $('[data-hero-reveal]');
const heroChars = heroP ? splitChars(heroP) : [];
const aboutP = $('[data-about]');
const aboutChars = aboutP ? splitChars(aboutP) : [];
const light = (chars, f) => { const n = Math.round(chars.length * f); chars.forEach((c, i) => c.classList.toggle('on', i < n)); };

/* ---- testimonial cards: scale .5 -> 1 and fade, scrubbed by scroll position ---- */
const tcards = $$('[data-tcard]').map(el => ({ el, s: .5, o: 0 }));
const testi = $('.testi');
const wideTesti = () => innerWidth > 1100;
function testiTarget(vp) {            // vp: card top relative to a 900px-tall viewport
  const enter = smooth(clamp((820 - vp) / 310));
  const exit = 1 - smooth(clamp((-90 - vp) / 310));
  return Math.min(enter, exit);
}

/* ---- team carousel: drag, wraps around, centre cards full size ---- */
const view = $('[data-team]');
let team = null;
if (view) {
  const track = $('.team__track', view);
  const orig = $$('figure', track);
  for (let i = 0; i < 2; i++) orig.forEach(f => track.appendChild(f.cloneNode(true)));
  const figs = $$('figure', track);
  const gap = 24;
  const setW = () => orig.length * (orig[0].offsetWidth + gap);
  team = { off: 0, vel: 0, drag: false, lastX: 0 };
  team.off = setW() - 24;                       // first card sits 24px from the left, like the original
  const apply = () => {
    const W = setW();
    while (team.off < W / 2) team.off += W;
    while (team.off >= 1.5 * W) team.off -= W;
    track.style.transform = `translate3d(${-team.off}px,0,0)`;
    const vw = view.clientWidth;
    figs.forEach(f => {
      const x = f.offsetLeft - team.off;
      f.classList.toggle('on', x >= -2 && x + f.offsetWidth <= vw + 2);
    });
  };
  const frame = () => {
    if (!team.drag && Math.abs(team.vel) > .05) { team.off += team.vel; team.vel *= .9; apply(); }
    requestAnimationFrame(frame);
  };
  view.addEventListener('pointerdown', e => { team.drag = true; team.lastX = e.clientX; team.vel = 0; view.classList.add('drag'); view.setPointerCapture(e.pointerId); });
  view.addEventListener('pointermove', e => { if (!team.drag) return; const dx = e.clientX - team.lastX; team.lastX = e.clientX; team.off -= dx; team.vel = -dx * .12; apply(); });
  const end = () => { team.drag = false; view.classList.remove('drag'); };
  view.addEventListener('pointerup', end); view.addEventListener('pointercancel', end);
  view.addEventListener('dragstart', e => e.preventDefault());
  addEventListener('resize', apply);
  apply(); frame();
}

/* ---- one scroll loop for the scrubbed effects ---- */
let ticking = false;
function onScroll() {
  const vh = innerHeight;
  if (heroChars.length) light(heroChars, .6 + .4 * clamp(scrollY / 150));
  if (aboutChars.length) {
    const top = aboutP.getBoundingClientRect().top;
    light(aboutChars, .56 + .44 * clamp((.43 * vh - top) / (.333 * vh)));
  }
  ticking = false;
}
addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
onScroll();

function loop() {
  if (testi && wideTesti()) {
    const r = testi.getBoundingClientRect();
    if (r.bottom > -400 && r.top < innerHeight + 400) {
      const k = 900 / innerHeight;
      tcards.forEach(c => {
        const top = (r.top + c.el.offsetTop) * k;
        const tgt = reduce ? 1 : testiTarget(top);
        c.o += (tgt - c.o) * .16;
        c.el.style.opacity = c.o.toFixed(3);
        c.el.style.transform = `scale(${(.5 + .5 * c.o).toFixed(3)})`;
      });
    }
  }
  requestAnimationFrame(loop);
}
loop();

/* ---- hero video: keep it still when the visitor prefers reduced motion; recover if autoplay was blocked ---- */
const heroVideo = $('.hero__video');
if (heroVideo) {
  if (reduce) heroVideo.pause();
  else { const go = () => heroVideo.play().catch(() => {}); go(); document.addEventListener('visibilitychange', () => { if (!document.hidden) go(); }); }
}

/* ---- FAQ: each question toggles on its own, several can stay open ---- */
$$('.qa__q').forEach(q => q.addEventListener('click', () => {
  const qa = q.parentElement;
  qa.classList.toggle('open');
  q.setAttribute('aria-expanded', qa.classList.contains('open'));
}));

/* ---- project hover: circular cursor with arrow ---- */
const cursor = $('.cursor');
if (cursor && matchMedia('(hover:hover)').matches) {
  let tx = 0, ty = 0, cx = 0, cy = 0, on = false;
  addEventListener('mousemove', e => { tx = e.clientX; ty = e.clientY; if (!on) { cx = tx; cy = ty; } });
  $$('.project').forEach(p => {
    p.addEventListener('mouseenter', () => { on = true; cursor.classList.add('on'); });
    p.addEventListener('mouseleave', () => { on = false; cursor.classList.remove('on'); });
  });
  const follow = () => { cx += (tx - cx) * .25; cy += (ty - cy) * .25; cursor.style.transform = `translate(${cx}px,${cy}px)`; requestAnimationFrame(follow); };
  follow();
}

/* ---- contact form: opens the visitor's email app (set the address below) ---- */
const CONTACT_EMAIL = 'hello@truecraft.dev';
const form = $('#form');
if (form) form.addEventListener('submit', e => {
  e.preventDefault();
  const d = new FormData(form);
  const body = `Name: ${d.get('name')}\nEmail: ${d.get('email')}\n\n${d.get('message') || ''}`;
  location.href = `mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent('New project enquiry')}&body=${encodeURIComponent(body)}`;
});

const nav = $('.nav');
/* ---- nav: reappears when scrolling up after the hero ---- */
let lastY = scrollY;
function navFloat() {
  const y = scrollY;
  if (y > 700) { nav.classList.add('float'); nav.classList.toggle('show', y < lastY - 2 || nav.classList.contains('open')); }
  else if (y < 40) { nav.classList.remove('float', 'show'); }
  lastY = y;
}
addEventListener('scroll', navFloat, { passive: true });
$$('.nav__pill a').forEach(a => a.addEventListener('click', () => nav.classList.remove('open')));

/* ---- mobile menu ---- */
$('.nav__burger')?.addEventListener('click', () => nav.classList.toggle('open'));
})();
