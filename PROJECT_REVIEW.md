# Project review and visual decisions — working review

Branch: master. Original GraphScope source is now supplied and reused; HR and Hipka alternatives remain awaiting the owner’s choice. No branch or PR was created.

## Evidence and hierarchy

The research thesis remains the primary research project. Its existing portfolio diagram is a prior custom illustration, NOT the original GraphScope workflow; it must not be treated as an accepted scientific figure. The owner subsequently supplied public graphscope; its original workflow pixels are now reused, as recorded below. Publicly accessible deep engineering work (credit scoring, MyTorch, AUJava) receives modest additional emphasis; every other selected project now has a compact visual card on the homepage.

| Project | Material inspected | Working visual / reason |
| --- | --- | --- |
| LLM-GNN / GraphScope | Latest root README; web/graphscope/README.md; sections.tsx; content.ts; Pages workflow | Pending original published workflow URL/asset. Found five exact stages in source, but no standalone original image. Private source is not automatically published. No replacement architecture approved. |
| Credit scoring | README; report-derived figures and existing artifact provenance; notebook and metadata links | Original baseline ROC plot in controlled-height preview, with tuned metrics explicitly distinguished. |
| MyTorch | README; task1/task2 paths and stored notebook accuracy artifact provenance | Saved WDBC learning plot, showing the educational training experiment rather than an invented network diagram. |
| AUJava | README, App.java, demo.aujava | Custom diagram grounded in actual three-pass orchestration, distinct GCC stage; team attribution retained. 27 cases are documented, not claimed freshly executed. |
| Fundamentals of AI | README; public source checkout; six subprojects and original screenshot/learning/GIF artifacts | Actual Sokoban interface; supplementary LunarLander and Isolation outputs retained. |
| Tetris | Public Project 06 Board, constants, saved genome and shape sequence | Actual replay of Board.drop at 8/16/24 placements, rendered as SVG. No new evolution run and no Pygame screenshot claimed. Generator verifies inputs and states. |
| HR | README; report provenance; PBIX/report filenames | Current report excerpt retained temporarily. Asked for real dashboard screenshot or permission for a data-derived analysis view; no fabricated dashboard. |
| Hipka | README; resource tree; docs/VERIFICATION.md | Existing architecture diagram retained temporarily. Device screenshots explicitly not verified in source. Asked for screenshot or approval of documented architecture preview. |
| xv6 | README; selected code responsibilities and original resault.png | Actual recorded terminal output. Collection of changed files, not a complete bootable kernel. |
| Mini-Twitter | README; public source checkout; original diagram.png inspected | Source-based client/server diagram retained. Original diagram.png is largely blank and is a MySQL Workbench capture, so it is unsuitable as a preview of this SQLite application. |
| English learning | Root Django URL configuration and app tree inspected in preceding review; no root README | Module structure diagram, explicitly team work, without an unverified UI screenshot. |
| Retail forecasting | CV; attempted README fetch (unavailable) | Existing CV-based workflow retained temporarily. Asked for shareable README/interface evidence; client data and private repository contents are excluded. |

## Logos

Supplied raster originals are retained. Transparent PNG derivatives have real alpha; website references derivatives and removes white CSS containers. Sematec uses exterior flood fill to retain its intentional white lettering. Alpha assertions check all corners. A local proof sheet was reviewed on ivory and charcoal; the website supports its existing light theme only. No blending-mode workaround or recoloring is used.

## Validation

Static checker passed both pages and 127 local references before the final Tetris preview substitution. Chrome browser regression suite passed both pages at 320, 390, 560, 768, 820, 1024, 1280 and 1440px; filters (12 archive projects), disclosures, keyboard navigation, image loads, no-JS access, reduced motion, certificate responses, and zero runtime/network errors. Subsequent check results are recorded in ignored .preview/browser-report.json. Original GraphScope workflow crop was checked pixel-for-pixel against the supplied public source; external app execution, Android device screenshots, Safari and Firefox are not claimed.

Final local regression pass after adding the Tetris replay: PASS, all 16 route/viewport combinations plus filters, disclosures, keyboard/menu/anchors, no-JS/reduced-motion, images/certificates, zero console/runtime/network errors. `tools/check_site.py`: PASS, 2 pages and 127 local references. `node --check script.js`: exit 0. `git diff --check`: exit 0. Tetris generator: PASS, saved-genome states at placements 8/16/24. Logo generator: PASS, six real-alpha exports with transparent corners.

Modified tracked files: `index.html`, `projects.html`, `style.css`, `tools/browser_check.py`.
New files: `PROJECT_REVIEW.md`, `tools/prepare_logos.py`, `tools/generate_tetris_preview.py`, `assets/projects/compiler-passes.svg`, `assets/projects/tetris-replay.svg`, and six `assets/logos/*-transparent.png` assets (aut, emrc, yaas, quera, sematec, toefl).
Existing branch: `master`. Publication uses a regular forward commit on this branch. Remaining HR/Hipka choices do not authorize fabricated replacement screenshots.

## Resolved by the owner: original GraphScope source and professional confidentiality

Owner supplied https://github.com/Parand1khalili/graphscope. Inspected its public README, tree and original preview.jpg. The README's actual workflow distinguishes the historical B1/Narrative comparison from the separate SARA extension. Reused original screenshot pixels, not the earlier portfolio-authored architecture.

`assets/projects/graphscope-original-preview.jpg` is an unchanged copy of the public preview. `graphscope-workflow.webp` is a lossless crop (40,265,1230,1110) retaining the entire method map, both lanes, dependency paths, conditions and legends. It omits surrounding webpage content only. Both the cropped map and full source capture can be opened at readable size. No private LLM-GNN files are published. Live-demo deployment is marked pending by the source README, so the portfolio links to the verified repository/documentation rather than claiming a verified live deployment.

Owner clarified Retail Forecast is professional/company work and outputs must stay private. Removed its illustrative workflow image from both pages; use a text-only methodology preview. Revised the professional entry and project summary using the supplied client-facing responsibilities, product-specific statistical/CatBoost/blended selection, historical backtesting and WAPE. WAPE below 10% is explicitly restricted to model-selection backtests across evaluated datasets, without suggesting production-wide performance. No company files, data, interface captures or forecast outputs were accessed or published.

Outstanding visual choices: HR dashboard screenshot or approval of a data-derived analytical preview; Hipka device screenshots or approval of the documented architecture preview. Their existing correctly labeled visuals remain pending the owner's answer. All independent changes are implemented on master; no new branch, history rewrite, or PR.
