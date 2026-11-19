<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= esc($title ?? 'Deals a tu rollo | Freidoras de aire') ?></title>
    <meta name="description" content="<?= esc($meta_description ?? 'Reviews y comparativas de freidoras de aire. Deals a tu rollo.') ?>">
    <link rel="canonical" href="<?= esc($canonical ?? 'https://dealsfreidoras.es' . ($_SERVER['REQUEST_URI'] ?? '/')) ?>">
    <?php helper('site'); ?>
    <?= seo_verification_meta() ?>

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="<?= esc($title ?? 'Deals a tu rollo | Freidoras de aire') ?>">
    <meta property="og:description" content="<?= esc($meta_description ?? '') ?>">
    <meta property="og:url" content="<?= esc($canonical ?? 'https://dealsfreidoras.es') ?>">
    <meta property="og:site_name" content="Deals a tu rollo">
    <meta property="og:locale" content="es_ES">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="<?= esc($title ?? 'Deals a tu rollo | Freidoras de aire') ?>">
    <meta name="twitter:description" content="<?= esc($meta_description ?? '') ?>">

    <!-- Favicons -->
    <link rel="icon" href="/favicon.svg" type="image/svg+xml">
    <link rel="icon" href="/favicon.ico" sizes="any">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="manifest" href="/site.webmanifest">
    <meta name="theme-color" content="#0D6EFD">

    <link rel="stylesheet" href="/assets/css/style.css">

    <?= $this->renderSection('head') ?>

    <?php
    $gtmId = '';
    $configPath = ROOTPATH . 'site.config.json';
    if (file_exists($configPath)) {
        $siteConfig = json_decode(file_get_contents($configPath), true) ?? [];
        $gtmId = $siteConfig['gtm_id'] ?? '';
    }
    ?>
    <?php if ($gtmId): ?>
    <script>
    (function() {
        if (localStorage.getItem('cookie_consent') === 'accepted') {
            (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
            new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
            j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
            'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
            })(window,document,'script','dataLayer','<?= esc($gtmId) ?>');
        }
    })();
    </script>
    <?php endif; ?>
</head>
<body>
    <?= $this->include('partials/header') ?>
    <main>
        <?= $this->renderSection('content') ?>
        <?= $content ?? '' ?>
    </main>
    <?= $this->include('partials/footer') ?>
    <?= $this->include('partials/cookie-banner') ?>
</body>
</html>
