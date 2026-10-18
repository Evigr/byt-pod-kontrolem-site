"""Check the generated pages, links and copied legal text without third-party dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
import re

ROOT=Path(__file__).parent
DOCS=ROOT/'docs'
class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(); self.links=[]; self.ids=set(); self.text=[]; self.lang=None
        self.feed(source)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag=='html': self.lang=a.get('lang')
        if tag=='a': self.links.append(a)
    def handle_data(self,data): self.text.append(data)

pages={p:Page(p.read_text(encoding='utf-8')) for p in DOCS.rglob('*.html')}
assert len(pages)==12
for path,page in pages.items():
    source=path.read_text(encoding='utf-8')
    assert '—' not in source and '&mdash;' not in source and '&#8212;' not in source, path
    if path.name=='index.html':
        assert 'step-number' not in source and 'stage-pagination' not in source, path
        assert not re.search(r'0[1-4] / ', source), path
    lang=path.parent.name if path.parent!=DOCS else 'ru'
    assert page.lang==lang, path
    switches=[a for a in page.links if 'hreflang' in a]
    assert {a['hreflang'] for a in switches}=={'ru','en','vi'}, path
    for link in page.links:
        target=urlsplit(link.get('href',''))
        if target.scheme or target.netloc: continue
        dest=(path.parent/unquote(target.path)).resolve() if target.path else path.resolve()
        if dest.is_dir(): dest=dest/'index.html'
        assert dest.is_file(), (path,link)
        if target.fragment: assert target.fragment in pages[dest].ids,(path,link)
        if 'hreflang' in link: assert dest.name==path.name,(path,link)
    if lang in ['en','vi']:
        text=' '.join(page.text)
        assert not re.search('[А-Яа-яЁё]',text.replace('Русский','').replace('Б','')),path
        if path.name in ['terms.html','privacy.html']:
            key='terms' if path.name=='terms.html' else 'privacy'
            doc=json.loads((ROOT/'legal'/f'{lang}.json').read_text(encoding='utf-8'))[key]
            normalized=' '.join(text.split())
            for item in doc['intro']+[s['text'] for s in doc['sections']]:
                assert ' '.join(item.replace('—','-').split()) in normalized,(path,item[:40])
print('OK: 12 pages; links and language switches; complete legal translations; no untranslated Russian text.')
