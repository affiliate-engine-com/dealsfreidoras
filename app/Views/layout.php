<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <?php helper('site'); ?>
    <title><?= esc($title ?? 'Deals Freidoras') ?></title>
    <meta name="description" content="<?= esc($meta_description ?? 'Reviews y comparativas de freidoras de aire. Deals Freidoras.') ?>">
    <link rel="canonical" href="<?= esc($canonical ?? seo_canonical_url()) ?>">
    <?= seo_verification_meta() ?>
    <?= seo_social_meta($title ?? 'Deals Freidoras', $meta_description ?? '', $canonical ?? null) ?>
    <?= seo_jsonld([
        'title' => $title ?? 'Deals Freidoras',
        'description' => $meta_description ?? '',
        'canonical' => $canonical ?? null,
        'type' => $jsonld_type ?? '',
        'products' => $jsonld_products ?? [],
        'faqs' => $jsonld_faqs ?? [],
        'breadcrumbs' => $breadcrumbs ?? [],
    ]) ?>

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="<?= esc($title ?? 'Deals Freidoras') ?>">
    <meta name="twitter:description" content="<?= esc($meta_description ?? '') ?>">

    <?= seo_icon_links() ?>
    <meta name="theme-color" content="#0D6EFD">

    <link rel="stylesheet" href="/assets/css/style.css?v=20261127-110">

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
