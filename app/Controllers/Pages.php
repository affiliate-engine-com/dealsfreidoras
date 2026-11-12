<?php

namespace App\Controllers;

class Pages extends BaseController
{
    public function pillar()
    {
        return view('pages/mejor-freidora-de-aire');
    }

    public function bestOf($slug)
    {
        $view = 'pages/best-of/' . $slug;
        if (!view_exists($view)) {
            $view = 'pages/best-of'; // fallback if exists, or handle 404
            // For now, try specific or show a simple message
            if (!view_exists($view)) {
                throw \CodeIgniter\Exceptions\PageNotFoundException::forPageNotFound();
            }
        }
        return view($view, [
            'title' => 'Mejores ' . str_replace('-', ' ', $slug) . ' | Deals a tu rollo',
            'canonical' => 'https://dealsfreidoras.es/best-of/' . $slug
        ]);
    }

    public function review($slug)
    {
        $view = 'pages/review/' . $slug;
        if (!view_exists($view)) {
            throw \CodeIgniter\Exceptions\PageNotFoundException::forPageNotFound();
        }
        return view($view);
    }

    public function vs($slug)
    {
        $view = 'pages/vs/' . $slug;
        if (!view_exists($view)) {
            throw \CodeIgniter\Exceptions\PageNotFoundException::forPageNotFound();
        }
        return view($view);
    }

    public function sobreNosotros()
    {
        return view('pages/sobre-nosotros', [
            'title' => 'Sobre nosotros | Deals a tu rollo - Freidoras',
            'canonical' => 'https://dealsfreidoras.es/sobre-nosotros'
        ]);
    }
}
