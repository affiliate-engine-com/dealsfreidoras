<?= $this->extend('layout') ?>

<?= $this->section('content') ?>
<article>
    <h1>Test Layout</h1>
    <p>If you see the header, footer and CSS, the layout is working.</p>
    <a href="#test">Anchor test</a>
    <div id="test" style="margin-top:400px;">Anchor target</div>
</article>
<?= $this->endSection() ?>
