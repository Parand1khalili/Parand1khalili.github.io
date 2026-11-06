# Parand Khalili — Technical Portfolio

A static portfolio for graph ML research, applied analytics, and software engineering. Semantic HTML, local assets, CSS, and progressive JavaScript; no framework or build step is needed for GitHub Pages.

[Visit the portfolio](https://parand1khalili.github.io/) · [Explore projects](https://parand1khalili.github.io/projects.html)

## November 2026 content update

- Eleven projects, including the CV's retail forecasting work at EMRC.
- Expandable methods, implementation notes, evaluation context, and source links for every project.
- Research descriptions aligned with the supplied CV: Cora/CiteSeer prompt comparisons, downstream GCN behavior, a matched FeatProp evaluation in preparation, and annotation reliability work in progress.
- Current public Tetris code linked through Fundamentals of AI / Project 06.
- Hipka's Audius/Compose/Media3 architecture and collaborative origins; xv6's public syscall/reporting snapshot; JavaFX/TCP/SQLite client/server architecture.
- Larger project image panels, a real recorded xv6 output, and explicitly labeled technical diagrams where a verified screenshot is unavailable.
- User-supplied AUT, EMRC, and YAS logos beside the relevant education or employment entry, with original proportions and colors preserved.
- Updated two-page CV generated from the supplied resume text. `tools/generate_cv.py` contains its content and ReportLab rendering; font paths can be supplied on other operating systems.

Project figures and reported model metrics are historical artifacts, not newly reproduced benchmarks. Professional forecasting information is drawn only from the CV; client data, source code, and private repository contents are not published here. The HR image is an actual report excerpt, not a Power BI dashboard screenshot. [Asset provenance](assets/SOURCES.md) records sources and credits.

## Preview and validation

```powershell
python -m http.server 8000 --bind 127.0.0.1
python tools/check_site.py
node --check script.js
git diff --check
```

Optional browser regression checks use installed Google Chrome and development-only packages:

```powershell
python -m pip install --target .local-tools playwright tinycss2
python tools/browser_check.py --serve
```

`--serve` starts and stops an in-process local server on an available port. Without it, the checker uses a separately running server at port 8000.

The browser suite checks both pages at 320, 390, 560, 768, 820, 1024, 1280, and 1440 CSS pixels; image loading; CSS syntax; filters and counts; native project disclosures with keyboard activation; expanded-content overflow; mobile navigation and focus; teaching disclosure; skip link; reduced motion; CV response; JavaScript-disabled behavior; and browser/network errors. The portrait's deliberately clipped internal image layers are excluded from element-bound checks; document overflow is still checked.

Screenshots, local tools, and temporary reference checkouts stay in ignored `.preview/` and `.local-tools/`. The optional `tools/accessibility_check.py` requires a separately supplied axe-core build; a browser regression pass alone is not a complete accessibility audit.

## Maintenance

The homepage and archive share `style.css` and `script.js`. Keep project summaries and sources consistent between them. Update the stylesheet/script version query in both HTML files when changing either asset; the value is the first 12 characters of its SHA-256 hash. The CV has its own date-based cache version.

Preserve the warm ivory, sunflower, and terracotta identity, local portrait assets, responsive navigation, keyboard focus, reduced-motion support, filters, native disclosures, and no-JavaScript access. Keep diagrams distinct from recorded outputs. Confirm source links and claims before publishing.

The November update also removes decorative link arrows, redundant numbering, faux contact icons, and the rotating typewriter introduction. The opening copy is personal and static; the existing warm palette and portrait remain. The static checker prevents decorative link arrows from being reintroduced.
