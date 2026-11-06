# Asset sources and credits

## Portrait

The homepage foreground (`portrait/parand-portrait-cutout.webp`) is an optimized transparent WebP derivative of the user's supplied cutout PNG. It was resized and compressed without generating a new face or changing the subject. The circular-stage background (`portrait/hero-rooftop.jpg`) is a grayscale, 720px square display crop from the user's rooftop-garden photograph supplied on October 23, 2026; the source image is not overwritten. Colored shapes and the outline remain individually editable HTML/CSS layers, moved with an optional reduced-motion-aware pointer effect. Neither original upload is published.

The photograph was supplied by Parand Khalili for this website. The original stays untouched outside the public source. The local 480px and 768px WebP images and JPEG fallback are editorial crops and resized exports only. No face generation, background replacement, filters, or retouching was used. EXIF metadata is omitted from web exports.

## Authentic project artifacts

Retrieved from the owner's public repositories on October 12, 2026. Project reports and notebooks are retained only in the ignored local review directory; the website includes selected optimized figures.

| Local image | Source | What it shows |
| --- | --- | --- |
| `projects/credit-roc.webp` | [Credit-scoring report, page 8](https://github.com/Parand1khalili/credit-scoring-risk-mitigation/blob/main/docs/report.pdf) | Embedded baseline-model ROC comparison; extracted image xref 94 |
| `projects/credit-pr.webp` | Same report, page 8 | Embedded baseline precision–recall comparison; xref 95 |
| `projects/credit-feature-importance.webp` | Same report, page 10 | Random Forest feature importance; xref 99 |
| `projects/hr-report-excerpt.webp` | [HR project report, page 7](https://github.com/Parand1khalili/PowerBI_HR_Analysis/blob/main/PowerBI_Project_Report.pdf) | Rendered analysis excerpt in Persian, PDF crop `(65, 65, 532, 420)` points |
| `projects/mytorch-accuracy.webp` | [MyTorch task2 notebook](https://github.com/Parand1khalili/MLP-Classifier-MyTorch-Framework/blob/main/task2.ipynb) | Stored training/testing accuracy output on WDBC; cell 5, output 1 |
| `projects/sokoban.webp` | [Original screenshot](https://github.com/Parand1khalili/Fundamentals-of-AI/blob/main/01-Sokoban-AI-Solver/screenshot.png) | Actual Sokoban solver interface |
| `projects/lunarlander-learning.webp` | [Original learning curve](https://github.com/Parand1khalili/Fundamentals-of-AI/blob/main/04-RL-LunarLander/learning_curve.png) | Saved LunarLander learning curve |
| `projects/isolation-state.webp` | [Original recorded animation](https://github.com/Parand1khalili/Fundamentals-of-AI/blob/main/03-Isolation-Game-Agent/viz.gif) | Frame 20 from the saved game animation; displayed as a still to avoid unsolicited motion |

Image conversion preserves the source axes, labels, and plotted values. These are previously saved project artifacts, not newly reproduced experiments. The credit report's baseline curves are distinct from its reported tuned-model metrics.

The HR report has no dashboard screenshot. The `.pbix` archive contains a decorative embedded icon, not a dashboard thumbnail, and Power BI Desktop was unavailable for a reliable export. The website therefore shows the authentic report excerpt and links to the source project instead of fabricating a dashboard.

## Thesis diagram

`thesis-pipeline.svg` is a website-authored, clearly labeled methodology illustration based on the supplied educational CV. It depicts the ongoing investigation into graph-aware prompts, node selection, LLM annotations, confidence filtering, and GNN classification. It is not an experimental output, publication, or validated result.

## Technology logos

Python, PyTorch, NumPy, Pandas, scikit-learn, Git, Linux, and Docker logos come from [DEVICON](https://github.com/devicons/devicon/tree/master/icons), distributed under the [MIT license](logos/LICENSE-DEVICON.txt), copyright 2015 konpa. The official logo shapes and proportions are preserved. Linux uses DEVICON's plain variant to keep the asset small.

The Power BI logo comes from [Microsoft / PowerBI-Icons](https://github.com/microsoft/PowerBI-Icons/blob/main/SVG/Power-BI.svg), under [CC BY 4.0](logos/LICENSE-POWERBI.txt). Attribution: Microsoft, PowerBI-Icons. The SVG is unchanged and displayed at a smaller size. This does not imply Microsoft endorsement.

Brand names and marks identify the technologies used in the portfolio. They remain the property of their respective owners.

## November 2026 additions

- `logos/aut.png`, `logos/emrc.jpg`, `logos/yaas.jpg`: original image files supplied by the user on November 6, 2026 for the education and employment sections. Copied without cropping, recoloring, or redrawing. The organizations retain their marks; placement identifies education/employment and does not claim endorsement.
- `projects/xv6-result.webp`: optimized derivative of [the public xv6 recorded output](https://github.com/Parand1khalili/xv6_syscall/blob/main/resault.png), retrieved November 6, 2026. Original 739 × 577 dimensions and full content retained; WebP quality 88. This is a historical run, not a newly verified kernel build.
- `projects/retail-workflow.svg`: CV-based method diagram only. No internal source, client data, measurements, or private repository content is included.
- `projects/tetris-process.svg`: method diagram derived from [the public Tetris documentation](https://github.com/Parand1khalili/Fundamentals-of-AI/tree/main/06-Tetris-Genetic-Algorithm).
- `projects/hipka-architecture.svg`: implementation diagram derived from [Hipka's README](https://github.com/Parand1khalili/Hipka_Music/blob/main/README.md).
- `projects/twitjava-architecture.svg`: architecture diagram derived from [Mini-Twitter's README](https://github.com/Parand1khalili/twitterFinal/blob/master/README.md).
- `projects/english-architecture.svg`: source-structure diagram based on [the Django root URL configuration](https://github.com/Parand1khalili/Software-Engineering-1403-01_G1/blob/master/src/english_website/urls.py) and its app modules. This collaborative project is not represented as solely authored work.

The five new SVGs are geometric technical diagrams, not app screenshots or experimental results. Existing project evidence is preserved. The thesis diagram's prompt-context and evaluation notes were aligned with the supplied November CV; node selection/filtering remain research directions.

`Parand_Khalili_CV.pdf` was refreshed from the user's supplied resume text on November 6, 2026, using `tools/generate_cv.py`. The two rendered PDF pages were visually reviewed. The source claims and ongoing-work status are preserved; website/project links point to known public destinations.
