"""Browser regression checks using installed Chrome. Start the static server first.

Install development tools with:
  python -m pip install --target .local-tools playwright tinycss2
Run:
  python tools/browser_check.py
"""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.local-tools'))
from playwright.sync_api import sync_playwright, expect
import tinycss2

BASE = 'http://127.0.0.1:8000'
OUTPUT = ROOT / '.preview'
OUTPUT.mkdir(exist_ok=True)
report = []


def check_css(nodes):
    for node in nodes:
        assert node.type != 'error', f'CSS syntax: {node}'
        if node.type == 'qualified-rule':
            declarations = tinycss2.parse_declaration_list(node.content, skip_comments=True, skip_whitespace=True)
            assert not any(item.type == 'error' for item in declarations), f'Invalid CSS declarations: {declarations}'
        elif node.type == 'at-rule' and node.content is not None:
            check_css(tinycss2.parse_rule_list(node.content, skip_comments=True, skip_whitespace=True))


check_css(tinycss2.parse_stylesheet((ROOT / 'style.css').read_text(), skip_comments=True, skip_whitespace=True))

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    context = browser.new_context()
    page = context.new_page()
    errors = []
    bad_responses = []
    failed_requests = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.on('console', lambda message: errors.append(message.text) if message.type == 'error' else None)
    page.on('response', lambda response: bad_responses.append(f'{response.status} {response.url}') if response.status >= 400 else None)
    page.on('requestfailed', lambda request: failed_requests.append(f'{request.url}: {request.failure}'))

    for route in ('/', '/projects.html'):
        for width, height in ((1440, 1000), (1280, 900), (1024, 900), (820, 1000), (768, 1024), (560, 900), (390, 844), (320, 800)):
            page.set_viewport_size({'width': width, 'height': height})
            response = page.goto(BASE + route, wait_until='networkidle')
            assert response.status == 200
            assert page.locator('h1').is_visible()
            assert page.locator('main').is_visible()
            overflow = page.evaluate('document.documentElement.scrollWidth > innerWidth')
            overflowing = page.evaluate('''() => [...document.querySelectorAll('main *')].filter(el => {
                const r = el.getBoundingClientRect();
                return r.width > 0 && (r.right > innerWidth + 1 || r.left < -1);
            }).map(el => ({tag: el.tagName, class: el.className, text: el.textContent.slice(0, 70)}))''')
            assert not overflow, f'{route} @ {width}: page overflow {overflowing}'
            assert not overflowing, f'{route} @ {width}: element overflow {overflowing}'
            # Exercise native lazy loading by bringing visible artifacts and logos into view.
            for image in page.locator('img:visible').all():
                image.scroll_into_view_if_needed()
                page.wait_for_function('(img) => img.complete && img.naturalWidth > 0', arg=image.element_handle())
            page.evaluate('window.scrollTo({top: 0, behavior: "instant"})')
            if width in (1440, 768, 390):
                name = 'home' if route == '/' else 'projects'
                page.screenshot(path=str(OUTPUT / f'{name}-{width}.png'), full_page=True)
                page.screenshot(path=str(OUTPUT / f'{name}-{width}-top.png'))
            report.append(f'PASS {route} @ {width}px: rendered, no overflow, images loaded')

    # Filter semantics, matching counts and native keyboard activation.
    page.goto(BASE + '/projects.html')
    for label, expected in (('AI & ML', 5), ('Data & BI', 2), ('Systems & Software', 4), ('All projects', 10)):
        button = page.get_by_role('button', name=label, exact=True)
        button.focus()
        button.press('Enter')
        assert button.get_attribute('aria-pressed') == 'true'
        assert page.locator('[data-category]:visible').count() == expected
        assert page.locator('[data-project-count]').inner_text().startswith(f'{expected} projects')
        assert page.locator('.filter-button[aria-pressed="true"]').count() == 1
    report.append('PASS project filters: counts, pressed states, keyboard, live status')

    for label in ('More evaluation figures', 'Learning curve & game visualization'):
        summary = page.get_by_text(label, exact=True)
        summary.click()
        panel = summary.locator('..')
        for image in panel.locator('img').all():
            image.scroll_into_view_if_needed()
            page.wait_for_function('(img) => img.complete && img.naturalWidth > 0', arg=image.element_handle())
    report.append('PASS authentic project evidence disclosures and image loading')

    for route in ('/', '/projects.html'):
        page.set_viewport_size({'width': 390, 'height': 844})
        page.goto(BASE + route)
        menu = page.get_by_role('button', name='Open menu', exact=True)
        menu.focus()
        menu.press('Enter')
        expect(page.locator('#site-navigation')).to_be_visible()
        page.keyboard.press('Tab')
        assert page.evaluate('document.activeElement.getAttribute("href")').endswith('#about')
        page.keyboard.press('Escape')
        expect(page.locator('#site-navigation')).to_be_hidden()
        assert menu.evaluate('(el) => el === document.activeElement')
        menu.click()
        page.locator('#site-navigation a').filter(has_text='Research').click()
        assert page.url.endswith('#research')
        expect(page.locator('#site-navigation')).to_be_hidden()
        # Native smooth-scroll duration varies with distance; wait for the destination.
        page.wait_for_function('''() => {
            const top = document.getElementById('research').getBoundingClientRect().top;
            return top >= 71 && top <= 115;
        }''')
        rect = page.locator('#research').bounding_box()
        assert 71 <= rect['y'] <= 115, f'Anchor did not reach the visible destination: {rect}'
        menu.click()
        page.set_viewport_size({'width': 1440, 'height': 1000})
        expect(page.locator('#site-navigation')).to_be_visible()
        expect(page.locator('.menu-toggle')).to_be_hidden()
        page.set_viewport_size({'width': 390, 'height': 844})
        expect(page.locator('#site-navigation')).to_be_hidden()
    report.append('PASS mobile navigation on both pages: Enter, Tab, Escape, focus return, anchors, resize')

    page.goto(BASE + '/')
    page.keyboard.press('Tab')
    assert page.evaluate('document.activeElement.classList.contains("skip-link")')
    page.keyboard.press('Enter')
    assert page.evaluate('document.activeElement.id') == 'main'
    page.get_by_text('View teaching assistant roles', exact=True).click()
    assert page.locator('.teaching-list').is_visible()
    report.append('PASS skip link and native teaching disclosure')

    response = context.request.get(BASE + '/assets/Parand_Khalili_CV.pdf')
    assert response.status == 200 and response.body().startswith(b'%PDF')
    report.append('PASS CV served as PDF')

    reduced = browser.new_context(reduced_motion='reduce', viewport={'width': 390, 'height': 844})
    reduced_page = reduced.new_page()
    reduced_page.goto(BASE + '/')
    assert reduced_page.evaluate('getComputedStyle(document.documentElement).scrollBehavior') == 'auto'
    assert reduced_page.locator('.button').evaluate_all('(els) => els.every(el => getComputedStyle(el).transitionDuration === "0s")')
    reduced.close()
    report.append('PASS reduced-motion preference')

    nojs = browser.new_context(java_script_enabled=False, viewport={'width': 390, 'height': 844})
    nojs_page = nojs.new_page()
    for route in ('/', '/projects.html'):
        nojs_page.goto(BASE + route)
        assert nojs_page.locator('h1').is_visible()
        assert nojs_page.locator('#site-navigation').is_visible()
        assert nojs_page.locator('.menu-toggle').is_hidden()
        assert not nojs_page.evaluate('document.documentElement.scrollWidth > innerWidth')
    assert nojs_page.locator('[data-category]:visible').count() == 10
    assert nojs_page.locator('[data-project-filters]').is_hidden()
    nojs.close()
    report.append('PASS JavaScript disabled: content, navigation, all projects')

    assert not errors, f'Browser errors: {errors}'
    assert not bad_responses, f'HTTP errors: {bad_responses}'
    assert not failed_requests, f'Failed requests: {failed_requests}'
    report.append('PASS zero console errors, runtime errors, failed requests or HTTP errors')
    browser.close()

(OUTPUT / 'browser-report.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print('\n'.join(report))
