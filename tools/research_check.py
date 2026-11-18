"""Frozen public aggregates and real browser regressions; no scientific execution."""
from pathlib import Path
import json,sys,statistics,os
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.local-tools'))
from playwright.sync_api import sync_playwright
D=json.loads((ROOT/'research/results.json').read_text())
assert set(D)=={'schema','date','freeze','sources','studies'}
for s in D['studies']:
 for a in s['arms']:
  assert len(a['seeds'])==10
  for key,mean,sd in [('accuracy','accuracy','sd'),('f1','f1','f1SD')]:
   assert abs(statistics.mean(x[key] for x in a['seeds'])-a[mean])<1e-9
   assert abs(statistics.pstdev(x[key] for x in a['seeds'])-a[sd])<1e-9
pub,cite,cora=D['studies'];arms=lambda s:{a['id']:a for a in s['arms']}
p,c=arms(pub),arms(cite)
assert round(p['D']['accuracy'],4)==81.2576 and round(p['D']['f1'],5)==.80710
assert round(c['D']['accuracy'],4)==68.6725 and round(c['D']['f1'],5)==.65915
assert round(p['D']['accuracy']-p['E']['accuracy'],4)==2.7670
assert round(c['D']['accuracy']-c['E']['accuracy'],4)==-.1663
assert round(c['C']['accuracy'],4)==69.6641
assert [a['train'] for a in pub['arms']]==[60,60,55,58,58]
assert [a['train'] for a in cite['arms']]==[120,120,68,93,93]
assert round(arms(cora)['D']['accuracy'],4)==74.7586
server=None
base=os.environ.get('SITE_QA_URL')
if not base:
 server=ThreadingHTTPServer(('127.0.0.1',0),partial(SimpleHTTPRequestHandler,directory=str(ROOT)))
 Thread(target=server.serve_forever,daemon=True).start();base=f'http://127.0.0.1:{server.server_port}'
errors=[]
with sync_playwright() as pw:
 browser=pw.chromium.launch(channel='chrome',headless=True,args=['--disable-features=BackForwardCache'])
 page=browser.new_page();page.on('pageerror',lambda e:errors.append(str(e)))
 for width in [320,390,560,768,820,1024,1280,1440]:
  page.set_viewport_size({'width':width,'height':900});page.goto(base+'/research/sara.html');page.locator('#evaluation-controls').wait_for(state='visible')
  assert not page.evaluate('document.documentElement.scrollWidth > innerWidth'), page.evaluate('Array.from(document.querySelectorAll("body *")).filter(e=>e.getBoundingClientRect().right>innerWidth+1).slice(0,40).map(e=>[e.tagName,e.className,e.getBoundingClientRect().width,getComputedStyle(e).overflowX])')
  page.locator('#arm').select_option('D');assert '81.2576' in page.locator('#evaluation-output').inner_text()
  page.locator('#study').select_option('CiteSeer120');page.locator('#arm').select_option('D');assert '-0.1663' in page.locator('#evaluation-output').inner_text()
  page.locator('#seed').select_option('7');assert 'Saved seed 7' in page.locator('#evaluation-output').inner_text()
  page.get_by_text('Selected-arm class recall and mean-count confusion',exact=True).click();assert not page.evaluate('document.documentElement.scrollWidth > innerWidth')
  page.locator('#study').select_option('Cora R1');page.locator('#arm').select_option('D');assert '74.7586' in page.locator('#evaluation-output').inner_text();assert page.locator('#arm option').count()==4
  page.reload();page.locator('#evaluation-controls').wait_for(state='visible')
  page.screenshot(path=str(ROOT/'.preview'/f'sara-{width}.png'))
  print('PASS research replay,refresh,class aggregates,no overflow',width)
 nojs=browser.new_context(java_script_enabled=False);pg=nojs.new_page();pg.goto(base+'/research/sara.html');assert pg.locator('table').count()==3;assert pg.locator('h1').is_visible();nojs.close()
 page.goto(base+'/');page.get_by_role('link',name='Full SARA research case study',exact=True).click();assert '/research/sara.html' in page.url;page.go_back(wait_until='domcontentloaded');page.locator('h1').wait_for();page.go_forward(wait_until='domcontentloaded');assert '/research/sara.html' in page.url
 assert not errors,errors
 browser.close()
if server:server.shutdown()
print('PASS scientific aggregates;research browser8widths;noJS;navigation/history;zero page errors')
