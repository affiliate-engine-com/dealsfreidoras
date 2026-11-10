<?php

use CodeIgniter\Router\RouteCollection;

/**
 * @var RouteCollection $routes
 */
$routes->get('/', 'Home::index');
$routes->get('mejor-freidora-de-aire', 'Pages::bestOf/mejor-freidora-de-aire');
$routes->get('best-of/(:segment)', 'Pages::bestOf/$1');
$routes->get('review/(:segment)', 'Pages::review/$1');
$routes->get('vs/(:segment)', 'Pages::vs/$1');
$routes->get('sobre-nosotros', 'Pages::sobreNosotros');

// Páginas legales
$routes->get('aviso-legal', 'Pages::avisoLegal');
$routes->get('privacidad', 'Pages::privacidad');
$routes->get('cookies', 'Pages::cookies');
$routes->get('afiliados', 'Pages::afiliados');
