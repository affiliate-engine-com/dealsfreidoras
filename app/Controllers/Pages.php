<?php

namespace App\Controllers;

class Pages extends BaseController
{
    public function pillar()
    {
        helper('amazon');

        return view('pages/mejor-freidora-de-aire', [
            'title' => 'Las 10 mejores freidoras de aire 2026 | Deals a tu rollo',
            'meta_description' => 'Comparativa de las mejores freidoras de aire en 2026: capacidad, precio orientativo y valoración de 10 modelos Cosori, Cecotec, Philips y Ninja en Amazon.es.',
            'canonical' => 'https://dealsfreidoras.es/mejor-freidora-de-aire',
        ]);
    }

    public function bestOf($slug)
    {
        throw \CodeIgniter\Exceptions\PageNotFoundException::forPageNotFound('Best-of page not yet created: ' . $slug);
    }

    public function review($slug)
    {
        throw \CodeIgniter\Exceptions\PageNotFoundException::forPageNotFound();
    }

    public function vs($slug)
    {
        throw \CodeIgniter\Exceptions\PageNotFoundException::forPageNotFound();
    }

    public function sobreNosotros()
    {
        return view('layout', [
            'title' => 'Sobre nosotros | Deals a tu rollo - Freidoras',
            'canonical' => 'https://dealsfreidoras.es/sobre-nosotros',
            'content' => '<h1>Sobre nosotros</h1><p>Página en construcción.</p>'
        ]);
    }
}
