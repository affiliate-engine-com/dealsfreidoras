<?php

use CodeIgniter\Router\RouteCollection;

/**
 * @var RouteCollection $routes
 */
$routes->get('/', 'Home::index');
$routes->get('mejor-freidora-de-aire', 'Pages::pillar');
$routes->get('best-of/(:segment)', 'Pages::bestOf/$1');
$routes->get('review/(:segment)', 'Pages::review/$1');
$routes->get('vs/(:segment)', 'Pages::vs/$1');
$routes->get('sobre-nosotros', 'Pages::sobreNosotros');

// Páginas legales centralizadas en dealsatr.com
$routes->get('aviso-legal', static function () {
    return redirect()->to('https://dealsatr.com/aviso-legal');
});
$routes->get('privacidad', static function () {
    return redirect()->to('https://dealsatr.com/privacidad');
});
$routes->get('cookies', static function () {
    return redirect()->to('https://dealsatr.com/cookies');
});
$routes->get('afiliados', static function () {
    return redirect()->to('https://dealsatr.com/afiliados');
});
