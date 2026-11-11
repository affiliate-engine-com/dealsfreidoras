<div id="cookie-banner" class="cookie-banner" style="display:none;">
    <div class="cookie-banner-content">
        <p>Usamos cookies propias y de terceros (incluida Amazon) para mejorar la experiencia y analizar el tráfico. Puedes aceptarlas o configurarlas. <a href="https://dealsatr.com/cookies" target="_blank" rel="noopener">Más información</a>.</p>
        <div class="cookie-banner-actions">
            <button id="cookie-accept" class="cta">Aceptar</button>
            <button id="cookie-reject" class="cta-secondary cta">Rechazar</button>
        </div>
    </div>
</div>

<script>
(function() {
    const banner = document.getElementById('cookie-banner');
    const acceptBtn = document.getElementById('cookie-accept');
    const rejectBtn = document.getElementById('cookie-reject');
    const consent = localStorage.getItem('cookie_consent');

    if (!consent) {
        banner.style.display = 'block';
    }

    function setConsent(value) {
        localStorage.setItem('cookie_consent', value);
        banner.style.display = 'none';
    }

    acceptBtn.addEventListener('click', function() { setConsent('accepted'); });
    rejectBtn.addEventListener('click', function() { setConsent('rejected'); });
})();
</script>
