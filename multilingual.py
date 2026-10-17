"""Build static, separately addressable translations; no JavaScript or cookies."""
from pathlib import Path
from html.parser import HTMLParser
import html
import json
from translations import TEXT

LANGS = {'ru': 'Русский', 'en': 'English', 'vi': 'Tiếng Việt'}
BASE = 'https://evigr.github.io/byt-pod-kontrolem-site/'
PAGES = ['index.html', 'privacy.html', 'terms.html', 'support.html']

def url(lang, name):
    return BASE + ('' if lang == 'ru' else lang + '/') + ('' if name == 'index.html' else name)

def language_links(lang, name):
    label = {'ru': 'Язык сайта', 'en': 'Website language', 'vi': 'Ngôn ngữ trang web'}[lang]
    links = []
    for code, title in LANGS.items():
        prefix = '' if lang == 'ru' else '../'
        href = prefix + ('' if code == 'ru' else code + '/') + name
        current = ' aria-current="page"' if code == lang else ''
        links.append(f'<a href="{href}" lang="{code}" hreflang="{code}"{current}>{title}</a>')
    return f'<nav class="languages" aria-label="{label}">' + ''.join(links) + '</nav>'

def meta(lang, name):
    return '<link rel="canonical" href="'+url(lang,name)+'">' + ''.join(
        f'<link rel="alternate" hreflang="{code}" href="{url(code,name)}">' for code in LANGS
    ) + f'<link rel="alternate" hreflang="x-default" href="{url("ru",name)}">'

class Translate(HTMLParser):
    def __init__(self, lang):
        super().__init__(convert_charrefs=False)
        self.lang = lang
        self.parts = []

    def tr(self, value):
        # Titles combine a page name and brand; translate their two parts independently.
        return ' — '.join(TEXT[self.lang].get(part, part) for part in value.split(' — ')) if value not in TEXT[self.lang] else TEXT[self.lang][value]

    def handle_decl(self, decl): self.parts.append('<!'+decl+'>')
    def handle_starttag(self, tag, attrs):
        result=[]
        for key, value in attrs:
            if tag == 'html' and key == 'lang': value = self.lang
            elif key in ['aria-label', 'content'] and value: value = self.tr(value)
            if tag == 'link' and key == 'href' and value in ['style.css','motion.css','favicon.svg']: value = '../'+value
            if tag == 'script' and key == 'src' and value == 'motion.js': value = '../'+value
            result.append(key if value is None else key+'="'+html.escape(value,quote=True)+'"')
        self.parts.append('<'+tag+(' '+ ' '.join(result) if result else '')+'>')
    def handle_startendtag(self, tag, attrs): self.handle_starttag(tag,attrs)
    def handle_endtag(self, tag): self.parts.append('</'+tag+'>')
    def handle_data(self, data):
        stripped=data.strip()
        translated=self.tr(stripped)
        self.parts.append(html.escape(data.replace(stripped,translated,1)) if stripped else data)
    def handle_entityref(self, name): self.parts.append('&'+name+';')
    def handle_charref(self, name): self.parts.append('&#'+name+';')

def legal_body(document, lang):
    back = TEXT[lang]['← На главную']
    chunks=[f'<a class="back" href="./">{back}</a>', '<h1>'+html.escape(document['title'])+'</h1>']
    def paragraphs(text):
        return ''.join('<p>'+html.escape(p).replace('\n','<br>')+'</p>' for p in text.split('\n\n'))
    for p in document['intro']: chunks.append(paragraphs(p))
    for section in document['sections']:
        chunks.append('<h2>'+html.escape(section['title'])+'</h2>'+paragraphs(section['text']))
    return ''.join(chunks)

def build_languages(out):
    sources = {name:(out/name).read_text(encoding='utf-8') for name in PAGES}
    for lang in LANGS:
        dest=out if lang=='ru' else out/lang
        dest.mkdir(exist_ok=True)
        for name, source in sources.items():
            if lang == 'ru': rendered=source
            else:
                parser=Translate(lang); parser.feed(source); rendered=''.join(parser.parts)
                if name in ['privacy.html','terms.html']:
                    document=json.loads((out.parent/'legal'/f'{lang}.json').read_text(encoding='utf-8'))[
                        'privacy' if name=='privacy.html' else 'terms']
                    a=rendered.index('<main class="document">')+len('<main class="document">')
                    b=rendered.index('</main>',a)
                    rendered=rendered[:a]+legal_body(document,lang)+rendered[b:]
            rendered=rendered.replace('</header>',language_links(lang,name)+'</header>')
            rendered=rendered.replace('</head>',meta(lang,name)+'</head>')
            (dest/name).write_text(rendered,encoding='utf-8')
    print('Built 12 pages: ru, en, vi')
