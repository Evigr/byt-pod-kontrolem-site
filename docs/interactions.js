/* Small, local-only interactions. Native language disclosure works without JS. */
(() => {
  const picker = document.querySelector('.language-picker');
  document.addEventListener('click', event => {
    if (picker && !picker.contains(event.target)) picker.open = false;
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && picker?.open) {
      picker.open = false;
      picker.querySelector('summary').focus();
    }
  });
  const lang = document.documentElement.lang;
  const featureCards = [...document.querySelectorAll('.feature-grid article')];
  if (featureCards.length && typeof HTMLDialogElement !== 'undefined') {
    const labels = {
      ru: ['Что умеет Шуршик', 'Закрыть', 'Дальше', 'Пример интерфейса · вымышленные данные', 'дней до окончания', 'Виза', 'Аренда', 'Отмечено как оплачено', 'На путешествие', 'из', 'Осталось на сегодня', 'Добавить кофе', 'Расход учтён'],
      en: ['Explore Shurshik', 'Close', 'Next', 'Interface example · fictional data', 'days remaining', 'Visa', 'Rent', 'Marked as paid', 'For a trip', 'of', 'Left for today', 'Add coffee', 'Expense recorded'],
      vi: ['Khám phá Shurshik', 'Đóng', 'Tiếp theo', 'Ví dụ giao diện · dữ liệu giả định', 'ngày còn lại', 'Visa', 'Thuê nhà', 'Đã đánh dấu thanh toán', 'Cho chuyến đi', 'trên', 'Còn lại hôm nay', 'Thêm cà phê', 'Đã ghi chi tiêu']
    }[lang];
    const scale = lang === 'vi' ? 200 : lang === 'en' ? .02 : 1;
    const fmt = new Intl.NumberFormat(lang, {style:'currency', currency:lang === 'vi' ? 'VND' : lang === 'en' ? 'USD' : 'RUB', maximumFractionDigits:0});
    const cash = n => fmt.format(n * scale);
    const dialog = document.createElement('dialog');
    dialog.className = 'feature-explorer';
    dialog.setAttribute('aria-labelledby', 'explorer-heading');
    dialog.innerHTML = `<div class="explorer-top"><span id="explorer-heading"></span><button class="explorer-close" type="button">×</button></div><div class="explorer-options"></div><div class="explorer-body"><div class="explorer-copy"><h2></h2><p></p></div><div class="explorer-preview" aria-live="polite"></div></div><div class="explorer-foot"><small></small><button class="hello-button explorer-next" type="button"></button></div>`;
    dialog.querySelector('#explorer-heading').textContent = labels[0];
    const close = dialog.querySelector('.explorer-close');
    close.setAttribute('aria-label', labels[1]);
    dialog.querySelector('.explorer-foot small').textContent = labels[3];
    dialog.querySelector('.explorer-next').textContent = labels[2] + ' →';
    const options = dialog.querySelector('.explorer-options');
    const preview = dialog.querySelector('.explorer-preview');
    let current = 0;
    let opener;
    const buttons = featureCards.map((card, index) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.textContent = card.querySelector('.feature-no').textContent;
      button.addEventListener('click', () => selectFeature(index));
      options.append(button);
      return button;
    });
    const examples = {
      ru: {
        titles: ['Страховка не закончится неожиданно', 'Из чего складываются расходы?', 'Показания — в понятную сумму', 'Новый ноутбук становится ближе'],
        descriptions: ['До окончания страховки ещё три недели. Важная дата на виду, а напоминание можно настроить заранее.', 'Посмотрите, сколько ушло на продукты и транспорт. Переключите категорию — сумма сразу изменится.', 'Разница между прошлым и текущим показанием помогает рассчитать платёж по вашему тарифу.', 'Добавьте небольшую сумму к цели и посмотрите, как растёт прогресс. Накопления учитываются отдельно от расходов.'],
        insurance: 'Страховка', days: 'день до окончания', food: 'Продукты', transport: 'Транспорт', period: 'Расходы за неделю', power: 'Электричество', previous: 'Предыдущее', now: 'Текущее', usage: 'Расход', unit: 'кВт·ч', tariff: 'Тариф за кВт·ч', laptop: 'На ноутбук', add: 'Отложить', done: 'Ближе к цели'
      },
      en: {
        titles: ['Know when your insurance expires', 'See where your money goes', 'Turn meter readings into a clear amount', 'A new laptop is getting closer'],
        descriptions: ['Your insurance has three weeks left. Keep the date in view and set a reminder ahead of time.', 'Explore spending on groceries and transport. Choose a category to see its total.', 'The difference between your previous and current reading helps calculate a bill using your tariff.', 'Add a small amount to your goal and watch your progress grow. Savings are tracked separately from expenses.'],
        insurance: 'Insurance', days: 'days remaining', food: 'Groceries', transport: 'Transport', period: 'Spending this week', power: 'Electricity', previous: 'Previous', now: 'Current', usage: 'Usage', unit: 'kWh', tariff: 'Rate per kWh', laptop: 'For a laptop', add: 'Set aside', done: 'Closer to your goal'
      },
      vi: {
        titles: ['Biết trước ngày hết hạn bảo hiểm', 'Tiền đã chi vào đâu?', 'Từ chỉ số công tơ đến số tiền rõ ràng', 'Chiếc laptop mới đang đến gần hơn'],
        descriptions: ['Bảo hiểm còn ba tuần. Theo dõi ngày quan trọng và đặt lời nhắc trước.', 'Xem chi tiêu cho thực phẩm và đi lại. Chọn danh mục để xem tổng tiền.', 'Chênh lệch giữa chỉ số cũ và mới giúp tính tiền điện theo đơn giá của bạn.', 'Thêm một khoản nhỏ vào mục tiêu và xem tiến độ tăng lên. Tiền tiết kiệm được theo dõi riêng với chi tiêu.'],
        insurance: 'Bảo hiểm', days: 'ngày còn lại', food: 'Thực phẩm', transport: 'Đi lại', period: 'Chi tiêu tuần này', power: 'Điện', previous: 'Chỉ số cũ', now: 'Chỉ số mới', usage: 'Tiêu thụ', unit: 'kWh', tariff: 'Đơn giá mỗi kWh', laptop: 'Mua laptop', add: 'Tiết kiệm thêm', done: 'Gần mục tiêu hơn'
      }
    }[lang];
    function selectFeature(index) {
      current = index;
      buttons.forEach((button, i) => button.setAttribute('aria-pressed', String(index === i)));
      dialog.querySelector('.explorer-copy h2').textContent = examples.titles[index];
      dialog.querySelector('.explorer-copy p').textContent = examples.descriptions[index];
      preview.dataset.feature = String(index);
      if (index === 0) {
        preview.innerHTML = `<span class="explorer-mini-label">${examples.insurance}</span><strong class="explorer-big">21</strong><span>${examples.days}</span><div class="explorer-dots" aria-hidden="true">● ● ●</div>`;
      } else if (index === 1) {
        preview.innerHTML = `<span class="explorer-mini-label">${examples.period}</span><strong class="explorer-big">${cash(680)}</strong><div class="category-bars" aria-hidden="true"><i></i><i></i></div><div class="category-options"><button type="button" class="hello-button" aria-pressed="true">${examples.food}</button><button type="button" class="hello-button" aria-pressed="false">${examples.transport}</button></div>`;
        preview.querySelectorAll('button').forEach((button, i) => button.addEventListener('click', () => {
          preview.querySelector('strong').textContent = cash(i ? 320 : 680);
          preview.querySelectorAll('button').forEach((choice, j) => choice.setAttribute('aria-pressed', String(i === j)));
          preview.querySelector('.category-bars').classList.toggle('transport-selected', i === 1);
        }));
      } else if (index === 2) {
        const tariff = lang === 'en' ? '$0.06' : lang === 'vi' ? '600 ₫' : '3 ₽';
        const total = lang === 'en' ? '$8.40' : cash(420);
        preview.innerHTML = `<span class="explorer-mini-label">${examples.power}</span><div class="meter-readings"><span>${examples.previous}<b>12 540</b></span><span aria-hidden="true">→</span><span>${examples.now}<b>12 680</b></span></div><span>${examples.usage}: 140 ${examples.unit}</span><span class="meter-tariff">${examples.tariff}: ${tariff}</span><strong class="explorer-big">${total}</strong>`;
      } else {
        preview.innerHTML = `<span class="explorer-mini-label">${examples.laptop}</span><div class="explorer-ring" style="background:conic-gradient(#8dc5ff 60%,#ffffff15 60%)"><strong>60%</strong></div><span class="goal-amount">${cash(24000)} ${labels[9]} ${cash(40000)}</span><button type="button" class="hello-button">＋ ${examples.add} ${cash(2000)}</button>`;
        preview.querySelector('button').addEventListener('click', event => {
          preview.querySelector('.explorer-ring strong').textContent = '65%';
          preview.querySelector('.explorer-ring').style.background = 'conic-gradient(#8dc5ff 65%,#ffffff15 65%)';
          preview.querySelector('.goal-amount').textContent = `${cash(26000)} ${labels[9]} ${cash(40000)}`;
          event.currentTarget.textContent = '✓ ' + examples.done;
          event.currentTarget.disabled = true;
        });
      }
    }
    document.body.append(dialog);
    document.querySelectorAll('a[href="#features"], a[href="./#features"]').forEach(link => {
      link.setAttribute('aria-haspopup', 'dialog');
      link.addEventListener('click', event => {
        event.preventDefault();
        opener = link;
        selectFeature(0);
        dialog.showModal();
        document.documentElement.classList.add('explorer-open');
      });
    });
    close.addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', event => {
      if (event.target !== dialog) return;
      const box = dialog.getBoundingClientRect();
      if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) dialog.close();
    });
    dialog.addEventListener('close', () => {
      document.documentElement.classList.remove('explorer-open');
      opener?.focus({preventScroll:true});
    });
    dialog.querySelector('.explorer-next').addEventListener('click', () => selectFeature((current + 1) % featureCards.length));
  }
  const copy = {
    ru: ['Привет! Я Шуршик. Рад знакомству!', 'Расход записан. Всё по порядку!', 'На сегодня осталось', 'Пример сброшен. Можно попробовать снова.'],
    en: ['Hi! I’m Shurshik. Nice to meet you!', 'Expense recorded. All in order!', 'Left for today', 'Example reset. Try again whenever you like.'],
    vi: ['Chào bạn! Mình là Shurshik. Rất vui được gặp bạn!', 'Đã ghi chi tiêu. Mọi thứ đã rõ ràng!', 'Còn lại hôm nay', 'Đã đặt lại ví dụ. Bạn có thể thử lại.']
  }[lang] || [];
  const greeting = document.querySelector('[data-greeting]');
  const mascot = document.querySelector('.companion-picture img');
  document.querySelector('[data-say-hello]')?.addEventListener('click', () => {
    greeting.textContent = copy[0];
    mascot.classList.remove('mascot-wave');
    void mascot.offsetWidth;
    mascot.classList.add('mascot-wave');
  });
  const demo = document.querySelector('.try-budget');
  if (!demo) return;
  demo.hidden = false;
  const scale = lang === 'vi' ? 200 : lang === 'en' ? .02 : 1;
  const currency = lang === 'vi' ? 'VND' : lang === 'en' ? 'USD' : 'RUB';
  const money = new Intl.NumberFormat(lang, {style:'currency', currency, maximumFractionDigits:0});
  const output = demo.querySelector('output');
  const status = demo.querySelector('[role="status"]');
  const choices = [...demo.querySelectorAll('[data-expense]')];
  function paint(amount) {
    output.textContent = money.format((1850 - amount) * scale);
    demo.querySelector('.try-fill').style.width = `${(1850-amount)/1850*100}%`;
    choices.forEach(button => button.setAttribute('aria-pressed', String(Number(button.dataset.expense) === amount)));
  }
  choices.forEach(button => button.addEventListener('click', () => {
    paint(Number(button.dataset.expense));
    status.textContent = copy[1];
  }));
  demo.querySelector('[data-reset]').addEventListener('click', () => {
    paint(0);
    status.textContent = copy[3];
  });
  paint(0);
})();
