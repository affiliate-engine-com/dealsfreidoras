<?php

namespace App\Controllers;

class Home extends BaseController
{
    public function index()
    {
        return view('home', [
            'title' => 'Mejor Freidora de Aire 2026 | Deals Freidoras',
            'meta_description' => 'Comparativas y reviews actualizadas de las mejores freidoras de aire. Encuentra la freidora de aire ideal para ti en Deals Freidoras.',
            'canonical' => 'https://dealsfreidoras.es/'
        ]);
    }
}
