"""Illustrative scroll-driven product demo. No user data, requests or storage."""
STORY = '''
<section class="story" aria-labelledby="story-heading">
  <div class="story-heading reveal"><span class="eyebrow">ОДИН ДЕНЬ. ВСЁ ПОД КОНТРОЛЕМ.</span>
    <h2 id="story-heading">Посмотрите, как<br>становится спокойнее.</h2>
    <p>Прокрутите вниз — пройдём один обычный день вместе.</p>
  </div>
  <div class="story-layout">
    <div class="story-steps">
      <article class="story-step" id="story-plan" data-step="0">
        <button class="step-select" type="button" aria-pressed="true" data-select="0"><span class="step-number">01</span><span>Утро · увидеть главное</span></button>
        <h3>Сегодня уже понятнее.</h3><p>Сколько можно потратить? Когда следующий платёж? Важное собрано рядом — не нужно вспоминать всё самому.</p>
      </article>
      <article class="story-step" id="story-expense" data-step="1">
        <button class="step-select" type="button" aria-pressed="false" data-select="1"><span class="step-number">02</span><span>День · внести расход</span></button>
        <h3>Кофе записали.<br>Остаток обновился.</h3><p>Добавили 350 ₽ за кофе — сразу видите, сколько осталось на сегодня. Понятные цифры вместо догадок.</p>
      </article>
      <article class="story-step" id="story-saving" data-step="2">
        <button class="step-select" type="button" aria-pressed="false" data-select="2"><span class="step-number">03</span><span>Вечер · ближе к цели</span></button>
        <h3>Большая поездка.<br>Маленький шаг сегодня.</h3><p>Отложили 1 500 ₽ — копилка подросла. Это накопление, поэтому сумма расходов от пополнения не меняется.</p>
      </article>
    </div>
    <div class="story-stage" data-stage="0">
      <div class="stage-orbit" aria-hidden="true"></div>
      <div class="stage-top"><span class="stage-dot"></span><span>ПРИМЕР ОДНОГО ДНЯ</span><span class="stage-pagination" aria-hidden="true">01 / 03</span></div>
      <div class="stage-budget">
        <div class="stage-label">Осталось на сегодня</div>
        <div class="stage-amount"><span data-number="left">1 850</span><span> ₽</span></div>
        <div class="stage-track"><i data-bar="budget" style="width:63%"></i></div>
        <div class="stage-budget-foot"><span><span data-number="spent">3 150</span> / 5 000 ₽</span><span data-number="percent">63%</span></div>
      </div>
      <div class="stage-receipt"><span class="receipt-icon" aria-hidden="true">＋</span><div><b>Кофе</b><small>Расход добавлен</small></div><strong>350 ₽</strong><span class="receipt-check" aria-hidden="true">✓</span></div>
      <div class="stage-saving"><div class="stage-saving-title"><span class="saving-icon" aria-hidden="true">↗</span><div><small>Копилка</small><b>На путешествие</b></div><span class="saving-gain">+1 500 ₽</span></div>
        <p><strong data-number="saved">18 000</strong><span> / 60 000 ₽</span></p><div class="stage-track"><i data-bar="saved" style="width:30%"></i></div>
      </div>
      <div class="stage-caption"><span data-caption="0">Важное на виду. Можно заниматься своим днём.</span><span data-caption="1" hidden>Расход учтён. На сегодня осталось 1 500 ₽.</span><span data-caption="2" hidden>Ещё один шаг к путешествию. Без лишней суеты.</span></div>
      <p class="stage-disclaimer">Интерактивный пример · вымышленные суммы</p>
    </div>
  </div>
</section>'''
