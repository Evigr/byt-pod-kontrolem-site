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
  const pagination = stage.querySelector('.stage-pagination');
  const budgetBar = stage.querySelector('[data-bar="budget"]');
  const savedBar = stage.querySelector('[data-bar="saved"]');
  let active = -1;
  let frame = 0;
  let displayed = {left:1850,spent:3150,saved:18000};
  const digits = n => Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ' ');
  const paint = values => {
    displayed = values;
    counters.left.textContent = digits(values.left);
    counters.spent.textContent = digits(values.spent);
    counters.saved.textContent = digits(values.saved);
    counters.percent.textContent = `${Math.round(values.spent / 50)}%`;
    budgetBar.style.width = `${values.spent / 50}%`;
    savedBar.style.width = `${values.saved / 600}%`;
  };
  function select(index) {
    if (index === active) return;
    active = index;
    stage.dataset.stage = String(index);
    steps.forEach((step,i) => step.classList.toggle('is-active',i === index));
    buttons.forEach((button,i) => button.setAttribute('aria-pressed',String(i === index)));
    captions.forEach((caption,i) => {caption.hidden = i !== index;});
    pagination.textContent = `0${index + 1} / 0${steps.length}`;
    stage.querySelector('.stage-finances').hidden = index === 3;
    stage.querySelector('.stage-visa').hidden = index !== 3;
    const target = {left:index > 0 ? 1500:1850,spent:index > 0 ? 3500:3150,saved:index >= 2 ? 19500:18000};
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
