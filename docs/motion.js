/* Progressive enhancement: content and figures remain visible without JS. */
(() => {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  const items = document.querySelectorAll('.reveal, .section-intro, .privacy-callout, .closing, .feature-grid article');
  let revealObserver;
  if ('IntersectionObserver' in window && !reduced.matches) {
    revealObserver = new IntersectionObserver(entries => {
      for (const entry of entries) if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    }, {threshold: 0.08});
    items.forEach(item => {item.classList.add('motion-ready'); revealObserver.observe(item);});
  }
  const stage = document.querySelector('.story-stage');
  if (!stage) return;
  const steps = [...document.querySelectorAll('.story-step')];
  const buttons = [...document.querySelectorAll('[data-select]')];
  const counters = Object.fromEntries([...stage.querySelectorAll('[data-number]')].map(el => [el.dataset.number, el]));
  const captions = [...stage.querySelectorAll('[data-caption]')];
  const progressDots = [...stage.querySelectorAll('.stage-progress i')];
  const budgetBar = stage.querySelector('[data-bar="budget"]');
  const savedBar = stage.querySelector('[data-bar="saved"]');
  let active = -1;
  let frame = 0;
  const scale = Number(stage.dataset.moneyScale || 1);
  let displayed = {left:1850*scale,spent:3150*scale,saved:18000*scale};
  const formatter = new Intl.NumberFormat(document.documentElement.lang, {maximumFractionDigits:0});
  const digits = n => formatter.format(Math.round(n));
  const paint = values => {
    displayed = values;
    counters.left.textContent = digits(values.left);
    counters.spent.textContent = digits(values.spent);
    counters.saved.textContent = digits(values.saved);
    counters.percent.textContent = `${Math.round(values.spent / (50*scale))}%`;
    budgetBar.style.transform = `scaleX(${values.spent / (5000*scale)})`;
    savedBar.style.transform = `scaleX(${values.saved / (60000*scale)})`;
  };
  function select(index) {
    if (index === active) return;
    active = index;
    stage.dataset.stage = String(index);
    steps.forEach((step,i) => step.classList.toggle('is-active',i === index));
    buttons.forEach((button,i) => button.setAttribute('aria-pressed',String(i === index)));
    captions.forEach((caption,i) => {caption.hidden = i !== index;});
    progressDots.forEach((dot,i) => dot.classList.toggle('is-current',i === index));
    stage.querySelector('.stage-finances').hidden = index === 3;
    stage.querySelector('.stage-visa').hidden = index !== 3;
    const target = {left:(index > 0 ? 1500:1850)*scale,spent:(index > 0 ? 3500:3150)*scale,saved:(index >= 2 ? 19500:18000)*scale};
    cancelAnimationFrame(frame);
    if (reduced.matches || document.hidden) {paint(target); return;}
    const from = {...displayed};
    const start = performance.now();
    function animate(now) {
      const progress = Math.min(1,(now-start)/750);
      const ease = 1-Math.pow(1-progress,3);
      paint(Object.fromEntries(Object.keys(target).map(key => [key,from[key]+(target[key]-from[key])*ease])));
      if (progress < 1) frame = requestAnimationFrame(animate);
    }
    frame = requestAnimationFrame(animate);
  }
  select(0);
  buttons.forEach(button => button.addEventListener('click',() => select(Number(button.dataset.select))));
  // Scroll changes the demo only after the person scrolls. Buttons also work without scrolling.
  let pending = false;
  function update() {
    pending = false;
    const line = innerHeight * (innerWidth <= 760 ? 0.73 : 0.48);
    let next = 0;
    for (let i=0;i<steps.length;i++) if (steps[i].getBoundingClientRect().top <= line) next=i;
    select(next);
  }
  window.addEventListener('scroll',() => {
    if (!pending) {pending=true;requestAnimationFrame(update);}
  }, {passive:true});
  reduced.addEventListener('change',() => {
    if (reduced.matches) {
      revealObserver?.disconnect();
      items.forEach(item => item.classList.remove('motion-ready'));
      const index=active; active=-1; select(index);
    }
  });
})();
