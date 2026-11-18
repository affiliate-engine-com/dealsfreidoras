<?php

namespace App\Controllers;

class Home extends BaseController
{
    public function index()
    {
        return view('home');
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
