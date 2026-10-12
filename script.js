/* Progressive enhancements. All content is readable without JavaScript. */
(() => {
  'use strict';

  document.querySelectorAll('[data-year]').forEach((element) => {
    element.textContent = new Date().getFullYear();
  });

  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.menu-toggle');
  const navigation = document.getElementById('site-navigation');
  const mobileViewport = window.matchMedia('(max-width: 800px)');

  if (header && toggle && navigation) {
    header.classList.add('nav-enhanced');
    toggle.hidden = false;

    function closeMenu(returnFocus = false) {
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Open menu');
      navigation.hidden = mobileViewport.matches;
      if (returnFocus) toggle.focus();
    }

    function syncNavigation() {
      const focusInside = navigation.contains(document.activeElement);
      closeMenu(mobileViewport.matches && focusInside);
    }

    toggle.addEventListener('click', () => {
      const isOpen = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!isOpen));
      toggle.setAttribute('aria-label', isOpen ? 'Open menu' : 'Close menu');
      navigation.hidden = isOpen;
    });

    navigation.addEventListener('click', (event) => {
      if (mobileViewport.matches && event.target.closest('a')) closeMenu(true);
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        closeMenu(true);
      }
    });

    document.addEventListener('click', (event) => {
      if (mobileViewport.matches && !header.contains(event.target)) closeMenu();
    });

    header.addEventListener('focusout', () => {
      // Let Tab leave the disclosure, then close once focus has moved away.
      requestAnimationFrame(() => {
        if (mobileViewport.matches && !header.contains(document.activeElement)) closeMenu();
      });
    });

    mobileViewport.addEventListener('change', syncNavigation);
    syncNavigation();
  }

  const filters = document.querySelector('[data-project-filters]');
  const projects = [...document.querySelectorAll('[data-category]')];
  const count = document.querySelector('[data-project-count]');

  if (filters && projects.length && count) {
    filters.hidden = false;
    const buttons = [...filters.querySelectorAll('[data-filter]')];

    function filterProjects(filter) {
      let visibleCount = 0;
      projects.forEach((project) => {
        const matches = filter === 'all' || project.dataset.category.split(' ').includes(filter);
        project.hidden = !matches;
        if (matches) visibleCount += 1;
      });
      buttons.forEach((button) => {
        button.setAttribute('aria-pressed', String(button.dataset.filter === filter));
      });
      const active = buttons.find((button) => button.dataset.filter === filter);
      count.textContent = `${visibleCount} ${visibleCount === 1 ? 'project' : 'projects'} / ${active.textContent.trim()}`;
    }

    buttons.forEach((button) => {
      button.addEventListener('click', () => filterProjects(button.dataset.filter));
    });
    filterProjects('all');
  }
})();
