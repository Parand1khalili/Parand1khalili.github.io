(() => {
  'use strict';
  document.querySelectorAll('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });
  const toggle = document.querySelector('.menu-toggle');
  const mobile = document.querySelector('.mobile-nav');
  if (toggle && mobile) {
    toggle.addEventListener('click', () => {
      const open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      toggle.setAttribute('aria-label', open ? 'Open menu' : 'Close menu');
      mobile.hidden = open;
    });
    mobile.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
      mobile.hidden = true; toggle.setAttribute('aria-expanded','false'); toggle.setAttribute('aria-label','Open menu');
    }));
  }
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('visible'); observer.unobserve(entry.target); }
    }), { threshold: .08, rootMargin: '0px 0px -30px 0px' });
    revealEls.forEach(el => observer.observe(el));
  } else { revealEls.forEach(el => el.classList.add('visible')); }

  const filterButtons = [...document.querySelectorAll('[data-filter]')];
  const tiles = [...document.querySelectorAll('.project-tile')];
  filterButtons.forEach(button => button.addEventListener('click', () => {
    const filter = button.dataset.filter;
    filterButtons.forEach(b => { b.classList.toggle('active', b === button); b.setAttribute('aria-pressed', String(b === button)); });
    tiles.forEach(tile => { tile.hidden = filter !== 'all' && !tile.dataset.category.split(' ').includes(filter); });
  }));

  const canvas = document.getElementById('network-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  if (!ctx) return;
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let nodes = [], width = 0, height = 0, raf = null, mouse = { x: -10000, y: -10000 };
  const count = 31;
  function resize(){
    const rect = canvas.getBoundingClientRect();
    width = rect.width; height = rect.height;
    const dpr = Math.min(window.devicePixelRatio || 1,2);
    canvas.width = Math.max(1,Math.round(width*dpr)); canvas.height = Math.max(1,Math.round(height*dpr));
    ctx.setTransform(dpr,0,0,dpr,0,0);
    // Stable, evenly distributed pseudo-random points each time we resize.
    nodes = Array.from({length:count},(_,i)=>({x: ((i*73+18)%101)/101*width, y:((i*37+29)%97)/97*height,vx:Math.sin(i*3.5)*.13,vy:Math.cos(i*2.17)*.14, r:i%7===0?4:2}));
  }
  canvas.addEventListener('pointermove',e=>{const r=canvas.getBoundingClientRect(); mouse.x=e.clientX-r.left;mouse.y=e.clientY-r.top;});
  canvas.addEventListener('pointerleave',()=>{mouse.x=-10000;mouse.y=-10000;});
  function draw(){
    ctx.clearRect(0,0,width,height);
    nodes.forEach((n,i)=>{
      if(!reduced){n.x+=n.vx;n.y+=n.vy;if(n.x<0||n.x>width)n.vx*=-1;if(n.y<0||n.y>height)n.vy*=-1;}
      for(let j=i+1;j<nodes.length;j++){
        const t=nodes[j],d=Math.hypot(n.x-t.x,n.y-t.y);
        if(d<120){ctx.beginPath();ctx.strokeStyle=`rgba(65,97,64,${(1-d/120)*.26})`;ctx.lineWidth=1;ctx.moveTo(n.x,n.y);ctx.lineTo(t.x,t.y);ctx.stroke();}
      }
      const proximity=Math.hypot(n.x-mouse.x,n.y-mouse.y);
      ctx.beginPath();ctx.arc(n.x,n.y,proximity<65?n.r+2:n.r,0,Math.PI*2);ctx.fillStyle=proximity<65?'#5a8d2d':'#708c68';ctx.fill();
    });
    if(!reduced)raf=requestAnimationFrame(draw);
  }
  resize();draw();
  window.addEventListener('resize',()=>{if(raf)cancelAnimationFrame(raf);resize();draw();},{passive:true});
  document.addEventListener('visibilitychange',()=>{if(document.hidden){if(raf)cancelAnimationFrame(raf);}else if(!reduced){if(raf)cancelAnimationFrame(raf);draw();}});
})();
