/* Native details works without JS; these are dismissal conveniences. */
(() => {
  const picker = document.querySelector('.language-picker');
  if (!picker) return;
  document.addEventListener('pointerdown', event => {
    if (!picker.contains(event.target)) picker.open = false;
  });
  picker.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      picker.open = false;
      picker.querySelector('summary').focus();
    }
  });
})();
