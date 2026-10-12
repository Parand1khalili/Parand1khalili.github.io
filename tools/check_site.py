"""Check static markup, assets, links, metadata and SVGs; standard library only."""
from html.parser import HTMLParser
import json
from pathlib import Path
import struct
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.refs = []
        self.stack = []
        self.elements = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if tag not in VOID:
            self.stack.append(tag)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'{self.path}: duplicate id {attrs["id"]}'
            self.ids.add(attrs['id'])
        for name in ('href', 'src'):
            if name in attrs:
                self.refs.append(attrs[name])
        for entry in attrs.get('srcset', '').split(','):
            if entry.strip():
                self.refs.append(entry.strip().split()[0])
        if tag == 'img':
            assert 'alt' in attrs, f'{self.path}: missing image alt'
            assert 'width' in attrs and 'height' in attrs, f'{self.path}: missing image dimensions'
        if attrs.get('target') == '_blank':
            assert 'noopener' in attrs.get('rel', ''), f'{self.path}: unsafe external target'

    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1] == tag, f'{self.path}: mismatched closing {tag}, stack={self.stack}'
        self.stack.pop()


documents = {}
for path in ROOT.glob('*.html'):
    document = Document(path.name)
    markup = path.read_text(encoding='utf-8')
    assert markup.lower().startswith('<!doctype html>')
    document.feed(markup)
    assert not document.stack, f'{path.name}: unclosed tags {document.stack}'
    assert sum(tag == 'h1' for tag, attrs in document.elements) == 1
    assert sum(tag == 'main' for tag, attrs in document.elements) == 1
    assert any(tag == 'html' and attrs.get('lang') == 'en' for tag, attrs in document.elements)
    for name in ('description', 'viewport', 'twitter:card'):
        assert any(tag == 'meta' and attrs.get('name') == name and attrs.get('content') for tag, attrs in document.elements)
    for name in ('og:title', 'og:description', 'og:url', 'og:image', 'og:type'):
        assert any(tag == 'meta' and attrs.get('property') == name and attrs.get('content') for tag, attrs in document.elements)
    assert any(tag == 'link' and attrs.get('rel') == 'canonical' for tag, attrs in document.elements)
    documents[path.name] = document

checked = 0
for filename, document in documents.items():
    for reference in document.refs:
        url = urlsplit(reference)
        if url.scheme or url.netloc:
            continue
        target = unquote(url.path) or filename
        assert (ROOT / target).is_file(), f'{filename}: missing asset {reference}'
        if url.fragment:
            assert target in documents and unquote(url.fragment) in documents[target].ids, f'{filename}: broken anchor {reference}'
        checked += 1

for asset in ROOT.glob('assets/**/*.svg'):
    ET.parse(asset)
ET.parse(ROOT / 'sitemap.xml')
assert (ROOT / '.nojekyll').is_file()
assert 'Sitemap: https://parand1khalili.github.io/sitemap.xml' in (ROOT / 'robots.txt').read_text()
social_image = (ROOT / 'assets/social-preview.png').read_bytes()
assert social_image.startswith(b'\x89PNG\r\n\x1a\n')
assert struct.unpack('>II', social_image[16:24]) == (1200, 630)
for document in documents.values():
    for tag, attrs in document.elements:
        if tag == 'meta' and attrs.get('property') == 'og:image':
            assert (ROOT / urlsplit(attrs['content']).path.lstrip('/')).is_file()

markup = (ROOT / 'index.html').read_text(encoding='utf-8')
structured = markup.split('<script type="application/ld+json">')[1].split('</script>')[0]
json.loads(structured)
assert (ROOT / 'assets/Parand_Khalili_CV.pdf').read_bytes().startswith(b'%PDF')
print(f'PASS: {len(documents)} pages; balanced HTML, unique IDs, {checked} local references, metadata, JSON-LD, SVGs, social image, sitemap, static hosting and CV.')
