<?php

namespace App\Controllers;

class Home extends BaseController
{
    public function index()
    {
        return view('home', [
            'title' => 'Deals a tu rollo | Mejor freidora de aire 2026',
            'meta_description' => 'Comparativas y reviews actualizadas de las mejores freidoras de aire. Encuentra la freidora de aire ideal para ti en Deals a tu rollo.',
            'canonical' => 'https://dealsfreidoras.es/'
        ]);
    }
}
