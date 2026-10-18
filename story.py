"""Illustrative scroll-driven product demo. No user data, requests or storage."""
STORY = '''
<section class="story" aria-labelledby="story-heading">
  <div class="story-heading reveal"><span class="eyebrow">ОДИН ДЕНЬ. ВСЁ ПОД КОНТРОЛЕМ.</span>
    <h2 id="story-heading">Обычный день<br>с приложением.</h2>
    <p>Листайте или выбирайте ситуацию. Цифры в примере будут меняться.</p>
  </div>
  <div class="story-layout">
    <div class="story-steps">
      <article class="story-step" id="story-plan" data-step="0">
        <button class="step-select" type="button" aria-pressed="true" data-select="0"><span>Утро · увидеть главное</span></button>
        <h3>Сколько осталось на сегодня?</h3><p>Откройте приложение утром: остаток бюджета, ближайшие платежи и сроки уже перед вами.</p>
      </article>
      <article class="story-step" id="story-expense" data-step="1">
        <button class="step-select" type="button" aria-pressed="false" data-select="1"><span>День · внести расход</span></button>
        <h3>Кофе записали.<br>Остаток обновился.</h3><p>Запишите 350 ₽ за кофе. Приложение учтёт покупку и покажет остаток дневного бюджета.</p>
      </article>
      <article class="story-step" id="story-saving" data-step="2">
        <button class="step-select" type="button" aria-pressed="false" data-select="2"><span>Вечер · ближе к цели</span></button>
        <h3>Отложили на поездку.<br>Видно, сколько накопили.</h3><p>Внесите 1 500 ₽ в копилку на путешествие. Пополнение сохранится в истории и не попадёт в расходы.</p>
      </article>
      <article class="story-step" id="story-visa" data-step="3">
        <button class="step-select" type="button" aria-pressed="false" data-select="3"><span>Виза · вспомнить заранее</span></button>
        <h3>Срок визы на виду.<br>Можно подготовиться.</h3><p>Укажите дату окончания визы и выберите, за сколько дней напомнить. Приложение покажет, сколько дней осталось, и пришлёт уведомление заранее, если уведомления разрешены.</p>
      </article>
    </div>
    <div class="story-stage" data-stage="0">
      <div class="stage-orbit" aria-hidden="true"></div>
      <div class="stage-top"><span class="stage-dot"></span><span>ПРИМЕР ОДНОГО ДНЯ</span><span class="stage-progress" aria-hidden="true"><i class="is-current"></i><i></i><i></i><i></i></span></div>
      <div class="stage-finances">
      <div class="stage-budget">
        <div class="stage-label">Осталось на сегодня</div>
        <div class="stage-amount"><span data-number="left">1 850</span><span> ₽</span></div>
        <div class="stage-track"><i data-bar="budget" style="width:63%"></i></div>
        <div class="stage-budget-foot"><span><span data-number="spent">3 150</span> / 5 000 ₽</span><span data-number="percent">63%</span></div>
      </div>
      <div class="stage-receipt"><span class="receipt-icon" aria-hidden="true">＋</span><div><b>Кофе</b><small>Расход добавлен</small></div><strong>350 ₽</strong><span class="receipt-check" aria-hidden="true">✓</span></div>
      <div class="travel-scene" aria-hidden="true"><model-viewer class="car-model" src="assets/models/car-road.glb" camera-orbit="35deg 62deg 78%" field-of-view="30deg" exposure="1.2" shadow-intensity="1" interaction-prompt="none" loading="lazy" tabindex="-1"></model-viewer><div class="travel-horizon"></div></div>
      <div class="stage-saving"><div class="stage-saving-title"><span class="saving-icon" aria-hidden="true">↗</span><div><small>Копилка</small><b>На путешествие</b></div><span class="saving-gain">+1 500 ₽</span></div>
        <p><strong data-number="saved">18 000</strong><span> / 60 000 ₽</span></p><div class="stage-track"><i data-bar="saved" style="width:30%"></i></div>
      </div>
      </div>
      <div class="stage-visa" hidden>
        <div class="visa-card"><div class="flight-scene" aria-hidden="true"><div class="flight-route"></div><model-viewer class="plane-model" src="assets/models/airplane.glb" camera-orbit="35deg 68deg 72%" field-of-view="28deg" exposure="1.1" shadow-intensity="0" interaction-prompt="none" loading="lazy" tabindex="-1"></model-viewer></div><div class="visa-information"><div class="stage-label">До окончания визы</div><div class="visa-count">7 <span>дней</span></div><div class="visa-rule"></div><div class="visa-setting"><span>Напомнить за</span><b>7 дней</b></div><p>Вы выбираете срок напоминания</p></div></div>
        <div class="visa-notification"><svg class="visa-bell" viewBox="0 0 24 24" aria-hidden="true"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9M10 21h4M12 2V1"/></svg><div><b>Пора проверить визу</b><p>До окончания осталось 7 дней.</p></div></div>
        <small class="model-credit">3D: <a href="https://poly.pizza/m/8ciDd9k8wha">Poly by Google</a> · <a href="https://creativecommons.org/licenses/by/3.0/">CC BY 3.0</a></small>
      </div>
      <div class="stage-caption"><span data-caption="0">Важное на виду. Можно заниматься своим днём.</span><span data-caption="1" hidden>Расход учтён. На сегодня осталось 1 500 ₽.</span><span data-caption="2" hidden>Ещё один шаг к путешествию. Без лишней суеты.</span><span data-caption="3" hidden>Важная дата под контролем. Есть время подготовиться.</span></div>
      <p class="stage-disclaimer">Интерактивный пример · вымышленные суммы</p>
    </div>
  </div>
</section>'''
