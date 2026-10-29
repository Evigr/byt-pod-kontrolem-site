"""Presentation for the Shurshik landing page; legal copy is left intact."""

HERO = '''<section class="hero shurshik-hero"><div class="hero-copy"><span class="eyebrow">ШУРШИК · ПОМОЩНИК ДЛЯ ПОВСЕДНЕВНЫХ ДЕЛ</span><h1>Быт под контролем.<br><em>С заботой о вас.</em></h1><p class="lead">Расходы, счета и важные даты — в одном приложении. Шуршик помогает навести порядок в делах и освободить голову для жизни.</p><div class="actions"><a class="button" href="#features">Посмотреть возможности <span aria-hidden="true">↗</span></a><a class="text-link" href="#try-heading">Попробовать на примере ↓</a></div><p class="release">Готовится к публикации в Google Play</p><div class="trust"><span>Без рекламы</span><span>Без регистрации</span><span>Записи на устройстве</span></div></div><div class="mascot-scene"><div class="mascot-glow" aria-hidden="true"></div><span class="scene-label">ВАШ ДОМАШНИЙ ПОМОЩНИК</span><img class="hero-mascot" src="images/shurshik-house.webp" width="740" height="800" alt="Шуршик в синем колпаке обнимает игрушечный домик" fetchpriority="high"><div class="scene-note"><span aria-hidden="true">✓</span><div><strong>Важное рядом.</strong><small>Остальному — ваше время.</small></div></div></div></section>'''

COMPANION = '''<section class="companion" aria-labelledby="companion-heading"><div class="companion-picture"><img src="images/shurshik-hello.webp" width="480" height="480" alt="Шуршик приветственно машет лапкой" loading="lazy"><p class="greeting speech-bubble" data-greeting role="status" aria-live="polite"></p><button class="hello-button" type="button" data-say-hello>Поздороваться с Шуршиком <span aria-hidden="true">✦</span></button></div><div><span class="eyebrow">ПОЗНАКОМЬТЕСЬ С ШУРШИКОМ</span><h2 id="companion-heading">Маленький друг.<br>Для привычных дел.</h2><p class="lead">Пушистый домовёнок делает ежедневный учёт немного теплее. Записывайте расходы в своём темпе — Шуршик порадуется вместе с вами.</p><p class="muted">Предпочитаете только цифры? Питомца можно скрыть в настройках.</p><a class="text-link" href="#features">Что умеет приложение ↗</a></div></section>'''

TRY_BUDGET = '''<section class="try-budget" aria-labelledby="try-heading" hidden><div><span class="eyebrow">ПОПРОБУЙТЕ САМИ</span><h2 id="try-heading">Одна запись.<br>И уже понятнее.</h2><p class="muted">Выберите расход и посмотрите, как меняется остаток. Это пример, данные не сохраняются.</p></div><div class="try-card"><span>Осталось на сегодня</span><output aria-live="polite"></output><div class="try-track"><i class="try-fill"></i></div><div class="try-choices"><button type="button" data-expense="350" aria-pressed="false">Кофе · 350 ₽</button><button type="button" data-expense="700" aria-pressed="false">Продукты · 700 ₽</button></div><div class="try-bottom"><span role="status" aria-live="polite"></span><button type="button" data-reset>Сбросить</button></div></div></section>'''

def refresh_home(home):
    end = home.index('</section>') + len('</section>')
    return HERO + TRY_BUDGET + COMPANION + home[end:]

def refresh_shell(markup):
    markup = markup.replace('</head>', '<script src="interactions.js?v=3" defer></script></head>')
    markup = markup.replace('<span class="logo">Б</span> Быт под контролем', '<img class="brand-icon" src="images/icon.png" width="40" height="40" alt=""> Шуршик')
    markup = markup.replace('<a class="brand" href="./">Быт под контролем</a>', '<a class="brand" href="./">Шуршик</a>')
    markup = markup.replace(' — Быт под контролем</title>', ' — Шуршик</title>')
    markup = markup.replace('Официальный сайт «Быт под контролем».', 'Официальный сайт приложения «Шуршик».')
    markup = markup.replace('href="favicon.svg" type="image/svg+xml"', 'href="images/favicon.png" type="image/png"')
    return markup

