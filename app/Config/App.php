<?php

namespace Config;

use CodeIgniter\Config\BaseConfig;

/**
 * Replaces ci4-base v1.1.0 App.php on overlay. The rest matches that tag;
 * the site value is baseURL, so the logo does not depend on .env.
 */
class App extends BaseConfig
{
    public string $baseURL = 'https://dealsfreidoras.es/';
    public array $allowedHostnames = [];
    public string $indexPage = '';
    public string $uriProtocol = 'REQUEST_URI';
    public string $permittedURIChars = 'a-z 0-9~%.:_\-';
    public string $defaultLocale = 'es';
    public bool $negotiateLocale = false;
    public array $supportedLocales = ['es'];
    public string $appTimezone = 'Europe/Madrid';
    public string $charset = 'UTF-8';
    public bool $forceGlobalSecureRequests = false;
    public array $proxyIPs = [];
    public bool $CSPEnabled = false;
}
