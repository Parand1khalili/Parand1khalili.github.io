"""Audit with development-only axe-core; never loaded by the website.

Requires the optional Playwright installation and .local-tools/axe.min.js,
or a supplied --axe-js path. The library used for this review was axe-core 4.14.0.
"""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.local-tools'))
from playwright.sync_api import sync_playwright

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--axe-js', type=Path, default=ROOT / '.local-tools/axe.min.js')
args = parser.parse_args()
if not args.axe_js.is_file():
    parser.error('Provide a local axe-core JavaScript build with --axe-js.')

reports = []
with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page()
    for route in ('/', '/projects.html'):
        for width in (1440, 390):
            page.set_viewport_size({'width': width, 'height': 1000})
            page.goto('http://127.0.0.1:8000' + route, wait_until='networkidle')
            page.add_script_tag(path=str(args.axe_js))
            result = page.evaluate('''async () => await axe.run(document, {
                runOnly: {type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa']}
            })''')
            report = {
                'route': route,
                'width': width,
                'passes': len(result['passes']),
                'violations': result['violations'],
                'incomplete': result['incomplete'],
            }
            reports.append(report)
            print(f'{route} @ {width}px: {len(result["violations"])} violations; '
                  f'{len(result["incomplete"])} categories need manual review.')
    browser.close()

output = ROOT / '.preview'
output.mkdir(exist_ok=True)
(output / 'accessibility-report.json').write_text(json.dumps(reports, indent=2), encoding='utf-8')
assert not any(report['violations'] for report in reports), 'Review accessibility-report.json.'
