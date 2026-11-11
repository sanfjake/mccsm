(() => {
  const year = document.getElementById('copyright-year');
  if (year) year.textContent = new Date().getFullYear();
  const mobile = document.getElementById('mobile-nav');
  if (mobile) {
    mobile.querySelectorAll('a').forEach(link => link.addEventListener('click', () => { mobile.open = false; }));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') mobile.open = false; });
  }
})();
