# Parand Khalili — Technical Portfolio

A static personal website for Computer Engineering, Data Analytics, AI, and Graph Machine Learning. It uses semantic HTML, local assets, maintained CSS, and progressive JavaScript enhancements. No framework, package installation, or build step is required to serve it on GitHub Pages.

## Local preview

From the repository root:

```powershell
python -m http.server 8000 --bind 127.0.0.1
```

Open [the homepage](http://127.0.0.1:8000/) and [projects](http://127.0.0.1:8000/projects.html). Stop the server with `Ctrl+C`.

Work remains local on the existing `master` branch. No branch, commit, pull request, push, or deployment was created.

## Visual direction and retained behavior

Warm ivory (`#FAF9F3`) is the primary background, charcoal the text color, and soft lemon (`#F3F5A1`) the principal accent. Blue, lilac, and butter-yellow tints distinguish selected project artifacts. Direct, moderate-sized headings replace the previous oversized editorial slogans. There are no dark-green sections, animated canvas, marketing marquee, remote fonts, or animation libraries.

The working static architecture, project descriptions, verified repository links, mobile disclosure navigation, project filters, teaching disclosure, keyboard support, and no-JavaScript behavior are retained. Accessible names were improved after an automated audit: menu labels and repository link labels now include the visible control text, and labeled groups have explicit semantics.

Employment and education/teaching are separate. Research is explicitly ongoing. The photograph establishes personal identity while real figures and reports provide project evidence.

## Files

| File or folder | Purpose |
| --- | --- |
| `index.html` | Introduction, about, selected projects, research, employment, education/teaching, skills, contact and structured metadata |
| `projects.html` | Filterable ten-project index, evidence captions, report links and supplementary figures |
| `style.css` | Shared palette and components, responsive layouts, focus states, reduced motion and print rules |
| `script.js` | Navigation disclosure, keyboard/focus behavior, filtering and live result counts |
| `assets/portrait/` | Two optimized WebP portrait sizes and JPEG fallback |
| `assets/projects/` | Authentic figures, screenshots, report excerpt and a recorded-animation still |
| `assets/thesis-pipeline.svg` | Clearly labeled methodology illustration, not experimental output |
| `assets/logos/` | Reliable technology SVGs and their license notices |
| `assets/SOURCES.md` | Per-image provenance, source URLs, export details and logo attribution |
| `assets/favicon.svg`, PNG icons and `assets/social-preview.png` | Lemon/ivory identity and 1200×630 sharing image with the actual portrait |
| `assets/Parand_Khalili_CV.pdf` | Supplied CV, preserved unchanged |
| `robots.txt`, `sitemap.xml`, `.nojekyll` | Crawl discovery and direct static hosting |
| `tools/` | Optional validation and deterministic asset preparation scripts |
| `.gitignore` | Excludes `.preview/`, `.local-tools/` and Python caches |

## Photograph and project evidence

The supplied original photograph remains unchanged. `tools/prepare_portrait.py` creates an editorial crop, resizes it, and exports WebP/JPEG derivatives without EXIF. It performs no segmentation, background replacement, facial generation, filtering or retouching. The resulting crop preserves natural hair edges, facial features, clothing and proportions. WebP exports are approximately 75 KB (480px) and 174 KB (768px), versus the 3.6 MB original.

Real project images include credit-scoring ROC and precision–recall curves and feature importance, the MyTorch notebook's saved WDBC accuracy plot, the Sokoban interface, a LunarLander learning curve, and a frame from the recorded Isolation animation. Captions distinguish stored project output from the illustrative thesis workflow. Opening an image shows its original aspect ratio at full resolution.

The HR report contains analysis but **no dashboard screenshot**. The `.pbix` has an embedded decorative icon rather than a dashboard thumbnail, and Power BI Desktop was unavailable for export. The website uses a genuine report excerpt (Persian, page 7) and links to the source report and repository. It does not reconstruct or simulate a dashboard.

Technology logos come from DEVICON (MIT) and Microsoft's PowerBI-Icons (CC BY 4.0). They remain local, retain their original proportions, and appear beside text in categorized skills. Attribution and license notices are included under `assets/` and linked from the footer.

Public source reports and notebooks are stored only in ignored `.preview/references/`, not added as public reference documents. The website includes only the necessary image derivatives.

## Content accuracy

The educational CV is the source for degree, GPA, professional dates, TA roles, thesis scope, skills, certifications and the email/LinkedIn URLs. Software projects from the prior site are preserved with descriptions grounded in the public codebases. Credit-scoring figures are labeled as baseline-model curves, distinct from the project's reported tuned-model evaluation metrics.

No publications, research outcomes, employer metrics or new affiliations were invented. The thesis remains **ongoing**. The CV's Tetris repository URL returned 404 during the earlier review, so its project description is retained without an unavailable public code link.

## Validation

Standard-library static checks:

```powershell
python tools/check_site.py
git diff --check
```

Optional browser checks use installed Google Chrome. Start the preview server in another terminal, then:

```powershell
python -m pip install --target .local-tools playwright tinycss2
python tools/browser_check.py
```

The checks cover both pages at 320, 390, 560, 768, 820, 1024, 1280 and 1440 CSS pixels; element overflow; native lazy image loading; project filters and result counts; artifact disclosures; mobile menu keyboard/focus/resize behavior; anchor navigation; skip link; teaching disclosure; CV response; reduced motion; JavaScript-disabled behavior; CSS syntax; console errors and failed requests.

An additional development-only axe-core 4.14.0 check ran at 1440px and 390px on both pages with WCAG A/AA tags. It reported **zero violations**. The remaining manual contrast-review entries contain only decorative arrows, which were checked separately. This is automated evidence, not a claim of complete WCAG conformance or a screen-reader audit.

To repeat that check, provide a local axe-core build in `.local-tools/axe.min.js`, or pass another local build with `--axe-js`:

```powershell
python tools/accessibility_check.py
```

All final checks passed in Chrome. Desktop, tablet and mobile screenshots were inspected. Reports and screenshots are saved under ignored `.preview/`. Firefox, Safari, physical devices, logged-in LinkedIn behavior, email delivery and the deployed site were not tested.

## Asset maintenance

Optional development commands (Pillow required):

```powershell
python tools/prepare_portrait.py "path/to/original.jpg"
python tools/generate_assets.py
```

The portrait crop is specifically reviewed for the supplied photograph; review the crop before using a different source. The social-card generator currently uses Windows system fonts. Adjust development font paths on other operating systems. Serving the generated files requires no Python dependencies.

Keep project descriptions consistent between pages, preserve source captions, and verify links before adding them. The original CV and photograph should not be overwritten by asset preparation. Publishing remains a separate manual action after local review.
