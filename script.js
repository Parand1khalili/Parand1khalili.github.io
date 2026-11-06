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

  // Hysteresis prevents repeated mode switches near the top; fixed header avoids layout jumps.
  if (header) {
    let scrollFrame = 0;
    let glassMode = window.scrollY >= 72;
    const syncHeader = () => {
      const y = Math.max(0, window.scrollY);
      if (!glassMode && y >= 72) glassMode = true;
      else if (glassMode && y <= 24) glassMode = false;
      header.classList.toggle('is-scrolled', glassMode);
      scrollFrame = 0;
    };
    window.addEventListener('scroll', () => {
      if (!scrollFrame) scrollFrame = requestAnimationFrame(syncHeader);
    }, { passive: true });
    window.addEventListener('pageshow', syncHeader);
    syncHeader();
  }

  // A static viewport dot grid; only a soft highlight around a fine pointer changes.
  if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    const root = document.documentElement;
    let pointerFrame = 0;
    let pointX = -400;
    let pointY = -400;
    window.addEventListener('pointermove', (event) => {
      if (event.pointerType !== 'mouse' && event.pointerType !== 'pen') return;
      pointX = event.clientX;
      pointY = event.clientY;
      if (!pointerFrame) {
        pointerFrame = requestAnimationFrame(() => {
          root.style.setProperty('--dot-x', pointX + 'px');
          root.style.setProperty('--dot-y', pointY + 'px');
          root.classList.add('has-pointer');
          pointerFrame = 0;
        });
      }
    }, { passive: true });
    const hideHighlight = () => root.classList.remove('has-pointer');
    root.addEventListener('pointerleave', hideHighlight);
    window.addEventListener('blur', hideHighlight);
  }

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

  // Frame-rate independent from pointer event frequency: one eased rAF loop, no idle work.
  const heroParallax = document.querySelector('[data-hero-parallax]');
  if (heroParallax) {
    const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let frame = 0;
    let lastFrameTime = 0;
    let x = 0, y = 0, targetX = 0, targetY = 0;

    function writeLayers() {
      const shift = (value) => value.toFixed(2) + 'px';
      heroParallax.style.setProperty('--bg-x', shift(-x * 6));
      heroParallax.style.setProperty('--bg-y', shift(-y * 6));
      heroParallax.style.setProperty('--lemon-x', shift(x * 15));
      heroParallax.style.setProperty('--lemon-y', shift(y * 13));
      heroParallax.style.setProperty('--navy-x', shift(-x * 10));
      heroParallax.style.setProperty('--navy-y', shift(-y * 11));
      heroParallax.style.setProperty('--lilac-x', shift(x * 18));
      heroParallax.style.setProperty('--lilac-y', shift(-y * 13));
      heroParallax.style.setProperty('--portrait-x', shift(x * 7));
      heroParallax.style.setProperty('--portrait-y', shift(y * 5));
    }

    function tick(now) {
      frame = 0;
      const elapsed = lastFrameTime ? Math.min(48, now - lastFrameTime) : 16.7;
      lastFrameTime = now;
      const ease = 1 - Math.exp(-elapsed / 115);
      x += (targetX - x) * ease;
      y += (targetY - y) * ease;
      writeLayers();
      if (Math.abs(targetX - x) + Math.abs(targetY - y) > .0015) schedule();
      else lastFrameTime = 0;
    }

    function schedule() {
      if (!frame && finePointer.matches && !reducedMotion.matches && !document.hidden) {
        frame = requestAnimationFrame(tick);
      }
    }

    function reset() {
      targetX = 0;
      targetY = 0;
      schedule();
    }

    function syncMotion() {
      if (reducedMotion.matches || !finePointer.matches) {
        cancelAnimationFrame(frame);
        frame = 0;
        lastFrameTime = 0;
        x = y = targetX = targetY = 0;
        writeLayers();
      }
    }

    heroParallax.addEventListener('pointermove', (event) => {
      if (!finePointer.matches || reducedMotion.matches ||
          (event.pointerType !== 'mouse' && event.pointerType !== 'pen')) return;
      const rect = heroParallax.getBoundingClientRect();
      targetX = Math.max(-1, Math.min(1, ((event.clientX - rect.left) / rect.width) * 2 - 1));
      targetY = Math.max(-1, Math.min(1, ((event.clientY - rect.top) / rect.height) * 2 - 1));
      schedule();
    }, { passive: true });
    heroParallax.addEventListener('pointerleave', reset);
    window.addEventListener('blur', reset);
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        cancelAnimationFrame(frame);
        frame = 0;
        lastFrameTime = 0;
      } else schedule();
    });
    finePointer.addEventListener('change', syncMotion);
    reducedMotion.addEventListener('change', syncMotion);
    syncMotion();
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
