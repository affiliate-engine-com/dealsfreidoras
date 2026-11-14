<?php

if (! function_exists('amazon_link')) {
    /**
     * Generate an Amazon affiliate link.
     *
     * The tag comes from site.config.json. A fallback applies only when that file has no tag.
     *
     * @param string $asin
     * @param string|null $tag Override tag (optional)
     * @return string
     */
    function amazon_link(string $asin, ?string $tag = null): string
    {
        $configPath = ROOTPATH . 'site.config.json';
        $config = [];

        if (file_exists($configPath)) {
            $config = json_decode(file_get_contents($configPath), true) ?? [];
        }

        $tag = $tag ?? ($config['affiliate_tag'] ?? 'dealsatr-21');

        return 'https://www.amazon.es/dp/' . rawurlencode($asin) . '?tag=' . rawurlencode($tag);
    }
}
