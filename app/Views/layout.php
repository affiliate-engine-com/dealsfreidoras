<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= esc($title ?? 'Deals a tu rollo | Freidoras de aire') ?></title>
    <meta name="description" content="<?= esc($meta_description ?? 'Reviews y comparativas de freidoras de aire. Deals a tu rollo.') ?>">
    <link rel="canonical" href="<?= esc($canonical ?? 'https://dealsfreidoras.es' . ($_SERVER['REQUEST_URI'] ?? '/')) ?>">

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
