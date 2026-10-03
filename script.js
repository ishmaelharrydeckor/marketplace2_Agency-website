// Reveal on scroll
const io = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
}), { threshold: .15 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Word-by-word highlight in About text
const about = document.querySelector('[data-words]');
if (about) {
  about.innerHTML = about.textContent.trim().split(/\s+/).map(w => `<span class="w">${w}</span>`).join(' ');
  const words = [...about.querySelectorAll('.w')];
  const update = () => {
    const r = about.getBoundingClientRect(), vh = innerHeight;
    const p = Math.min(1, Math.max(0, (vh * .85 - r.top) / (vh * .5 + r.height * .5)));
    words.forEach((w, i) => w.classList.toggle('on', i < p * words.length + 1));
  };
  addEventListener('scroll', update, { passive: true }); update();
}

// Count-up stats
const cio = new IntersectionObserver(es => es.forEach(e => {
  if (!e.isIntersecting) return;
  const el = e.target, to = +el.dataset.count, t0 = performance.now();
  const tick = t => {
    const k = Math.min(1, (t - t0) / 1600);
    el.textContent = Math.round(to * (1 - Math.pow(1 - k, 3))) + '+';
    if (k < 1) requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick); cio.unobserve(el);
}), { threshold: .6 });
document.querySelectorAll('[data-count]').forEach(el => cio.observe(el));

// Team marquee: duplicate for seamless loop
const row = document.querySelector('.team__row');
if (row) row.innerHTML += row.innerHTML;

// FAQ: one open at a time
document.querySelectorAll('.faq details').forEach(d => d.addEventListener('toggle', () => {
  if (d.open) document.querySelectorAll('.faq details').forEach(o => o !== d && (o.open = false));
}));

// Contact form
document.getElementById('form')?.addEventListener('submit', e => {
  e.preventDefault();
  const b = e.target.querySelector('button'); b.textContent = 'Message Sent ✓'; e.target.reset();
  setTimeout(() => b.textContent = 'Send Message', 3000);
});

// Mobile menu: scroll to contact
document.querySelector('.nav__burger')?.addEventListener('click', () => document.getElementById('services').scrollIntoView());
