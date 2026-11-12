<?php

namespace App\Controllers;

class Pages extends BaseController
{
    public function pillar()
    {
        try {
            return view('pages/mejor-freidora-de-aire');
        } catch (\Throwable $e) {
            return '<pre>Error: ' . esc($e->getMessage()) . "\n" . esc($e->getTraceAsString()) . '</pre>';
        }
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
        return '<h1>Sobre nosotros</h1><p>Página en construcción.</p>';
    }
}
