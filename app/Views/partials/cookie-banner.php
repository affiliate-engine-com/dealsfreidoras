<?php
$gtmId = '';
$configPath = ROOTPATH . 'site.config.json';
if (file_exists($configPath)) {
    $siteConfig = json_decode(file_get_contents($configPath), true) ?? [];
    $gtmId = $siteConfig['gtm_id'] ?? '';
}
?>
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

    function loadGTM() {
        if (window.gtmLoaded) return;
        const gtmId = '<?= esc($gtmId) ?>';
        if (!gtmId) return;
        (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
        new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
        })(window,document,'script','dataLayer', gtmId);
        window.gtmLoaded = true;
    }

    function setConsent(value) {
        localStorage.setItem('cookie_consent', value);
        banner.style.display = 'none';
        if (value === 'accepted') {
            loadGTM();
        }
    }

    acceptBtn.addEventListener('click', function() { setConsent('accepted'); });
    rejectBtn.addEventListener('click', function() { setConsent('rejected'); });
})();
</script>
