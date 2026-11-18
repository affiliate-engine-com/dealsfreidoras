<?= $this->extend('layout') ?>

<?php
$this->setVar('title', 'Sobre nosotros | Deals a tu rollo');
$this->setVar('meta_description', 'Comparativas de freidoras de aire de Deals a tu rollo: fichas, especificaciones y opiniones verificadas de Amazon.es, y cómo actualizamos los precios.');
$this->setVar('canonical', 'https://dealsfreidoras.es/sobre-nosotros');
?>

<?= $this->section('content') ?>
<article class="pillar">
    <h1>Sobre nosotros</h1>

    <h2>Quiénes somos</h2>
    <p>Deals Freidoras es el sitio de dealsfreidoras.es y forma parte de <a href="https://dealsatr.com">Deals a tu rollo</a> (dealsatr.com), la marca que reúne comparativas de compra. Este sitio trata las freidoras de aire a la venta en Amazon.es. No fabricamos aparatos ni tenemos tienda: las guías salen de la ficha y cada producto enlaza con su oferta en Amazon.</p>

    <h2>Qué hacemos</h2>
    <p>Hacemos comparativas y guías de freidoras de aire con productos de Amazon.es. En <a href="/mejor-freidora-de-aire">las mejores freidoras de aire</a> cruzamos marcas. Si ya partes de una marca o de un tamaño, hay página propia para <a href="/best-of/freidora-de-aire-cecotec">freidoras Cecotec</a>, <a href="/best-of/freidora-de-aire-cosori">freidoras Cosori</a>, <a href="/best-of/freidora-de-aire-ninja">freidoras Ninja</a> y <a href="/best-of/freidora-de-aire-grande">freidoras grandes</a>. En cada una están la capacidad, la potencia, el precio orientativo de la ficha y la valoración de Amazon.es.</p>
    <p>El material son las fichas públicas de Amazon.es. Analizamos las especificaciones que declara el fabricante y las opiniones verificadas de compradores, con la fecha de la revisión. No cocinamos con las freidoras ni las medimos en un laboratorio, y no añadimos una nota de uso nuestra. Si un dato no está en la ficha, no lo rellenamos.</p>

    <h2>Cómo elegimos y comparamos</h2>
    <p>Un modelo entra si está a la venta en Amazon.es y su ficha da para contrastarlo. Usamos su ASIN y el precio del producto nuevo, no el de segunda mano. Priorizamos buenas valoraciones y reseñas suficientes para leer la media. Un puesto o las compras recientes se anotan con la fecha, como dato de Amazon. El orden sale de la ficha, no de la comisión ni de un acuerdo con la marca.</p>
    <p>Al comparar alineamos lo que la ficha publica. La guía de compra de cada página mira capacidad, potencia, funciones y marca.</p>
    <ul>
        <li><strong>Capacidad.</strong> Los litros dicen el uso de la cubeta: unos 4 litros para una o dos personas, y desde 5,5 o 6 litros un uso más familiar. Es el volumen del cesto, no la comida de una capa.</li>
        <li><strong>Potencia.</strong> Recogemos los vatios declarados. Distinguen un compacto de una cubeta grande y no prometen un resultado de cocina.</li>
        <li><strong>Consumo.</strong> La referencia es esa potencia, cuando la ficha la trae. No medimos kilovatios hora. Si no hay otro dato, no lo estimamos.</li>
        <li><strong>Facilidad de limpieza.</strong> Sale de la descripción: cubeta extraíble, piezas para el lavavajillas y recubrimiento. No la comprobamos fregando el cestillo.</li>
        <li><strong>Valoraciones verificadas.</strong> Usamos la nota media y el número de opiniones de compras verificadas, con la fecha de la consulta.</li>
        <li><strong>Relación calidad-precio.</strong> Cruza capacidad, potencia, funciones y valoración con el importe de ese día. Un precio bajo no adelanta un modelo con pocas opiniones o datos incompletos.</li>
    </ul>
    <p>Si la ficha lo indica, anotamos una segunda zona, una ventana o los programas automáticos. La marca (Cecotec, Cosori, Ninja, Philips u otra) es contexto y no decide sola.</p>

    <h2>Cómo actualizamos los precios</h2>
    <p>El precio de una tabla es el de Amazon.es el día que indica la página, casi siempre el del producto nuevo. Cambia con las ofertas, el vendedor, los cupones y el stock, y puede no coincidir al poco de publicarlo. El enlace abre la ficha vigente: pagas el precio de Amazon en ese momento, sin recargo. Si no había un importe claro, lo decimos y no inventamos uno.</p>

    <h2>Transparencia de afiliación</h2>
    <aside class="affiliate-disclosure">
        <p>Participamos en el Programa de Afiliados de Amazon EU. Si compras desde nuestros enlaces, podemos recibir una comisión sin coste extra para ti. El precio es el de Amazon.</p>
    </aside>
    <p>La comisión no elige los modelos: entran por la ficha y por las opiniones verificadas. El funcionamiento en toda la marca está en la <a href="https://dealsatr.com/afiliados" target="_blank" rel="noopener">divulgación de afiliados</a>.</p>

    <h2>Dónde seguir</h2>
    <p>La <a href="/">portada</a> reúne las categorías. <a href="/mejor-freidora-de-aire">Las mejores freidoras de aire</a> cruzan marcas. Por marca o por cubeta amplia, sigue con Cecotec, Cosori, Ninja o las freidoras grandes.</p>
    <div class="category-grid">
        <a class="category-card" href="/">
            <h3>Inicio</h3>
        </a>
        <a class="category-card" href="/mejor-freidora-de-aire">
            <h3>Mejores freidoras</h3>
        </a>
        <a class="category-card" href="/best-of/freidora-de-aire-cecotec">
            <h3>Freidoras Cecotec</h3>
        </a>
        <a class="category-card" href="/best-of/freidora-de-aire-cosori">
            <h3>Freidoras Cosori</h3>
        </a>
        <a class="category-card" href="/best-of/freidora-de-aire-ninja">
            <h3>Freidoras Ninja</h3>
        </a>
        <a class="category-card" href="/best-of/freidora-de-aire-grande">
            <h3>Freidoras grandes</h3>
        </a>
    </div>

    <aside class="about-callout">
        <h2>Deals a tu rollo</h2>
        <p>Deals Freidoras es uno de los sitios de la marca. Qué es Deals a tu rollo y cómo se organizan el resto de comparativas está en <a href="https://dealsatr.com/sobre-nosotros">Sobre nosotros de Deals a tu rollo</a>.</p>
    </aside>
</article>
<?= $this->endSection() ?>
