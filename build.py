from pathlib import Path
import html, re

root=Path(__file__).parent
out=root/'docs'
out.mkdir(exist_ok=True)
app=Path('C:/AI/Apps/byt-pod-kontrolem')

def inline(s):
    s=html.escape(s)
    s=re.sub(r'\[([^]]+)\]\((https?://[^)]+)\)',r'<a href="\2">\1</a>',s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    return re.sub(r'`([^`]+)`',r'<code>\1</code>',s)

def markdown(s):
    parts=[]; paragraph=[]; listing=False
    def flush():
        if paragraph: parts.append('<p>'+inline(' '.join(paragraph))+'</p>'); paragraph.clear()
    for line in s.splitlines():
        if line.startswith('>'): continue # редакционные заметки исходного документа
        if not line.strip():
            flush()
            if listing: parts.append('</ul>'); listing=False
        elif line.startswith('#'):
            flush(); level=len(line)-len(line.lstrip('#'))
            parts.append(f'<h{level}>'+inline(line[level:].strip())+f'</h{level}>')
        elif line.startswith('- '):
            flush()
            if not listing: parts.append('<ul>'); listing=True
            parts.append('<li>'+inline(line[2:])+'</li>')
        else: paragraph.append(line)
    flush()
    if listing: parts.append('</ul>')
    return '\n'.join(parts)

nav='''<a class="brand" href="./"><span class="logo">Б</span> Быт под контролем</a><nav aria-label="Основное меню"><a href="./#features">Возможности</a><a href="support.html">Поддержка</a></nav>'''
footer='''<footer><a class="brand" href="./">Быт под контролем</a><div><a href="privacy.html">Конфиденциальность</a><a href="terms.html">Условия</a><a href="support.html">Поддержка</a></div><p>© 2026 Tagirov Tagir</p></footer>'''
def page(title,body,cls=''):
    return f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title} — Быт под контролем</title><meta name="description" content="Сроки, расходы, счета и копилка в одном Android-приложении. Официальный сайт «Быт под контролем»."><meta name="theme-color" content="#091424"><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="style.css"></head><body><header>{nav}</header><main class="{cls}">{body}</main>{footer}</body></html>'''

home='''<section class="hero"><div><span class="eyebrow">ДЛЯ ПОВСЕДНЕВНОЙ ЖИЗНИ · ANDROID</span><h1>Меньше держать<br>в голове.<br><em>Больше жить.</em></h1><p class="lead">Аренда, счета, расходы и важные даты — в одном спокойном месте. «Быт под контролем» помогает видеть ближайшее и понимать, куда уходят деньги.</p><div class="actions"><a class="button" href="#features">Посмотреть возможности <span>↗</span></a><span class="release">Готовится к публикации в Google Play</span></div><div class="trust"><span>Без рекламы</span><span>Без регистрации</span><span>Записи на устройстве</span></div></div><div class="phone-wrap"><div class="halo"></div><div class="phone" aria-label="Иллюстрация интерфейса с вымышленными данными"><div class="phone-top"><span>9:41</span><span>● ▰</span></div><h2>Быт под контролем</h2><p class="phone-date">Всё важное — рядом</p><div class="tabs"><b>Сегодня</b><span>Неделя</span><span>Месяц</span></div><div class="balance"><small>Осталось на сегодня</small><strong>1 850 ₽</strong><div class="track"><i></i></div><small>63% потрачено</small><div class="twocol"><span>Потрачено<b>3 150 ₽</b></span><span>Лимит<b>5 000 ₽</b></span></div></div><div class="mini-title">Ближайшее <span>Все ›</span></div><div class="mini-row"><span class="symbol">⌂</span><div><b>Аренда</b><small>До конца договора</small></div><span class="pill">Через 16 дней</span></div><div class="quick"><span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 16a8 8 0 1 1 16 0"></path><path d="M12 16l4-5"></path></svg><small>Показание</small></span><span><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="5" width="16" height="15" rx="2"></rect><path d="M4 10h16M8 3v4M16 3v4"></path></svg><small>Срок</small></span><span><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6" width="18" height="13" rx="2"></rect><path d="M3 10h18M7 15h4"></path></svg><small>Платёж</small></span><span data-only="ru"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"></rect><path d="M6 11a6 6 0 0 0 12 0M12 17v4"></path></svg><small>Голосом</small></span><span><svg viewBox="0 0 24 24" aria-hidden="true"><path class="dots" d="M6 12h.01M12 12h.01M18 12h.01"></path></svg><small>Ещё</small></span></div><div class="mini-title">Копилка <span>Все ›</span></div><div class="saving"><b>На путешествие</b><p>18 000 из 60 000 ₽</p><div class="track"><i style="width:30%"></i></div></div><p class="demo-label">Пример интерфейса · данные вымышлены</p></div></div></section>
<section id="features" class="features"><div class="section-intro"><span class="eyebrow">ОДНО ПРИЛОЖЕНИЕ. ПРИВЫЧНЫЕ ДЕЛА.</span><h2>Чтобы быт занимал<br>меньше вашего внимания.</h2></div><div class="feature-grid"><article><span class="feature-no">СРОКИ</span><h3>Важные даты на виду</h3><p>Виза, страховка, аренда или повторяющееся дело. Отсчёт дней, понятные цвета срочности и напоминания.</p></article><article><span class="feature-no">РАСХОДЫ</span><h3>Понятно, куда ушло</h3><p>Расходы по дням и категориям, поиск и общий итог в основной валюте. Исходная сумма каждой покупки сохраняется.</p></article><article><span class="feature-no">СЧЕТА</span><h3>Платежи без путаницы</h3><p>Регулярные платежи, история оплат и показания счётчиков. Фиксированная сумма, обычный и ступенчатый тариф.</p></article><article><span class="feature-no">БЮДЖЕТ И КОПИЛКА</span><h3>Маленькие шаги к цели</h3><p>Бюджет на месяц и дневной лимит из остатка. Отдельные цели накопления с историей пополнений и снятий.</p></article></div></section>
<section class="privacy-callout"><span class="eyebrow">ВАШИ ЗАПИСИ ОСТАЮТСЯ ВАШИМИ</span><h2>Без аккаунта.<br>Без лишнего шума.</h2><p>Записи хранятся на устройстве. У приложения нет рекламы и аналитики. Для сохранности данных можно создать резервную копию и защитить её паролем.</p><p class="muted">Для обновления курсов используется интернет. Голосовой ввод работает через системную службу распознавания — подробнее в политике.</p><a class="text-link" href="privacy.html">Как обрабатываются данные ↗</a></section>
<section class="closing"><div><h2>Начинаем с простого.</h2><p>Приложение готовится к публикации в Google Play.<br>Здесь появится ссылка на страницу магазина.</p></div><a class="button secondary" href="support.html">Связаться с разработчиком ↗</a></section>'''
from story import STORY
home = home.replace('<section id="features"', STORY + '<section id="features"', 1)
landing = page('Сроки, счета и расходы',home)
landing = landing.replace('</head>', '<link rel="stylesheet" href="motion.css?v=visa1"><script src="motion.js?v=type-only1" defer></script></head>')
(out/'index.html').write_text(landing,encoding='utf-8')
for src,dst,title in [('PRIVACY_POLICY.md','privacy.html','Политика конфиденциальности'),('TERMS_OF_USE.md','terms.html','Условия использования')]:
    text=(app/'docs'/src).read_text(encoding='utf-8')
    (out/dst).write_text(page(title,'<a class="back" href="./">← На главную</a>'+markdown(text),'document'),encoding='utf-8')
support='''<a class="back" href="./">← На главную</a><span class="eyebrow">МЫ НА СВЯЗИ</span><h1>Поддержка</h1><p class="lead">Нашли ошибку или хотите предложить улучшение? Напишите разработчику.</p><a class="button" href="mailto:tagir.tagirov.987@gmail.com">tagir.tagirov.987@gmail.com ↗</a><p>Разработчик: Tagirov Tagir</p><h2>Что указать в сообщении</h2><p>Модель телефона, версию Android и приложения, что вы делали и что произошло. Не присылайте пароли и резервные копии с личными записями.</p><h2>Частые вопросы</h2><details><summary>Как сохранить записи?</summary><p>В настройках приложения создайте резервную копию. Сохраните файл в надёжном месте; при необходимости защитите паролем.</p></details><details><summary>Можно восстановить забытый пароль копии?</summary><p>Нет. Разработчик не имеет доступа к вашим данным и не может восстановить пароль.</p></details><details><summary>Приложение оплачивает счета?</summary><p>Нет. Оно помогает вести учёт. Отметка об оплате не выполняет банковский перевод.</p></details><details><summary>Как удалить данные?</summary><p>В настройках приложения выберите «Удалить все данные». Сохранённые отдельно файлы резервных копий удаляются в месте их хранения.</p></details>'''
(out/'support.html').write_text(page('Поддержка',support,'document'),encoding='utf-8')
(out/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="18" fill="#168bff"/><text x="32" y="46" text-anchor="middle" font-size="44" font-family="Arial" font-weight="bold" fill="white">Б</text></svg>',encoding='utf-8')
(out/'.nojekyll').touch()
print('Built four pages in',out)
from multilingual import build_languages
build_languages(out)
