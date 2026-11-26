# Plan long-tail — dealsfreidoras.es

Una página por semana, con intención de compra o de comparación, enlazada desde la pillar `/mejor-freidora-de-aire` y desde las páginas de marca. La semana planificada es la del lunes.

El estado vive en la tabla. Debajo, cada URL tiene su checklist. Marca la casilla en el commit en el que el paso queda hecho. Search Console y el correo se hacen fuera del repo: déjalos sin marcar hasta entonces.

IndexNow (Bing) lo envía el deploy, no a mano. El script `bin/indexnow.py` publica `https://<dominio>/<indexnow_key>.txt` y, tras un deploy correcto, manda a `https://api.indexnow.org/indexnow` las URLs cuyo view o cuyo JSON de producto cambió respecto al commit anterior. Si `noindex` es `true`, o si el sitio es `amazon-high-ticket`, no escribe la clave y no envía nada. Un fallo del ping queda en el log y no tumba el deploy.

## Tabla

| Semana planificada | Slug / URL | Keyword objetivo | Intención | Estado | Fecha publicación | Commit |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-11-23 | [/mejor-freidora-de-aire-barata](https://dealsfreidoras.es/mejor-freidora-de-aire-barata) | mejor freidora de aire barata | compra | publicada | 2026-11-25 | `f23c3b97828d262592c28b7c525554352dd45a74` |
| 2026-11-30 | `/mejor-freidora-de-aire-4-litros` | mejor freidora de aire 4 litros | compra | pendiente | | |
| 2026-12-07 | `/mejor-freidora-de-aire-dos-cestas` | mejor freidora de aire dos cestas | compra | pendiente | | |
| 2026-12-14 | `/vs/cosori-vs-cecotec` | Cosori vs Cecotec | comparación | pendiente | | |
| 2026-12-21 | `/freidora-de-aire-con-ventana` | freidora de aire con ventana | compra | pendiente | | |
| 2026-12-28 | `/mejor-freidora-de-aire-6-litros` | mejor freidora de aire 6 litros | compra | pendiente | | |
| 2027-01-04 | `/mejor-freidora-de-aire-para-2-personas` | mejor freidora de aire para 2 personas | compra | pendiente | | |
| 2027-01-11 | `/mejor-freidora-de-aire-pequena` | freidora de aire pequeña | compra | pendiente | | |
| 2027-01-18 | `/mejor-freidora-de-aire-para-4-personas` | mejor freidora de aire para 4 personas | compra | pendiente | | |
| 2027-01-25 | `/freidora-de-aire-inoxidable` | freidora de aire inoxidable | compra | pendiente | | |

Estados: `pendiente` o `publicada`. Añade filas al final. No borres las publicadas.

## Checklist

### 2026-11-23 — /mejor-freidora-de-aire-barata

- [x] generada
- [x] merge a main
- [x] deploy OK
- [x] verificada en vivo
- [x] IndexNow (Bing) enviado
- [ ] indexación solicitada en Google Search Console
- [ ] correo enviado

### 2026-11-30 — /mejor-freidora-de-aire-4-litros

- [ ] generada
- [ ] merge a main
- [ ] deploy OK
- [ ] verificada en vivo
- [ ] IndexNow (Bing) enviado
- [ ] indexación solicitada en Google Search Console
- [ ] correo enviado

### 2026-12-07 — /mejor-freidora-de-aire-dos-cestas

- [ ] generada
- [ ] merge a main
- [ ] deploy OK
- [ ] verificada en vivo
- [ ] IndexNow (Bing) enviado
- [ ] indexación solicitada en Google Search Console
- [ ] correo enviado

### 2026-12-14 — /vs/cosori-vs-cecotec

- [ ] generada
- [ ] merge a main
- [ ] deploy OK
- [ ] verificada en vivo
- [ ] IndexNow (Bing) enviado
- [ ] indexación solicitada en Google Search Console
- [ ] correo enviado

### 2026-12-21 — /freidora-de-aire-con-ventana

- [ ] generada
- [ ] merge a main
- [ ] deploy OK
- [ ] verificada en vivo
- [ ] IndexNow (Bing) enviado
- [ ] indexación solicitada en Google Search Console
- [ ] correo enviado

### 2026-12-28 — /mejor-freidora-de-aire-6-litros

- [ ] generada
- [ ] merge a main
- [ ] deploy OK
- [ ] verificada en vivo
- [ ] IndexNow (Bing) enviado
- [ ] indexación solicitada en Google Search Console
- [ ] correo enviado

### 2027-01-04 — /mejor-freidora-de-aire-para-2-personas

- [ ] generada
- [ ] merge a main
- [ ] deploy OK
- [ ] verificada en vivo
- [ ] IndexNow (Bing) enviado
- [ ] indexación solicitada en Google Search Console
- [ ] correo enviado

### 2027-01-11 — /mejor-freidora-de-aire-pequena

- [ ] generada
- [ ] merge a main
- [ ] deploy OK
- [ ] verificada en vivo
- [ ] IndexNow (Bing) enviado
- [ ] indexación solicitada en Google Search Console
- [ ] correo enviado

### 2027-01-18 — /mejor-freidora-de-aire-para-4-personas

- [ ] generada
- [ ] merge a main
- [ ] deploy OK
- [ ] verificada en vivo
- [ ] IndexNow (Bing) enviado
- [ ] indexación solicitada en Google Search Console
- [ ] correo enviado

### 2027-01-25 — /freidora-de-aire-inoxidable

- [ ] generada
- [ ] merge a main
- [ ] deploy OK
- [ ] verificada en vivo
- [ ] IndexNow (Bing) enviado
- [ ] indexación solicitada en Google Search Console
- [ ] correo enviado

## Cómo añadir una página

1. Elige un slug en minúsculas y guiones, el de la keyword. Una página por semana. Copia la última fila de la tabla y el bloque de checklist, suma siete días a la semana y déjalo en `pendiente`, con la fecha y el commit vacíos y todas las casillas sin marcar.
2. Crea la vista con la misma estructura que `/mejor-freidora-de-aire` y las páginas `/best-of/`: caja «Respuesta rápida», navegación `related`, fecha de actualización, introducción, `{{compare:ASIN,ASIN}}`, una ficha por modelo con pros y contras, guía, FAQ y conclusión.
   - Slug de primer nivel: `app/Views/pages/<slug>.php` y una ruta explícita en `app/Config/Routes.php`, igual que la pillar: `$routes->get('<slug>', 'Pages::bestOf/<slug>');`.
   - Comparativa de marca o de uso: `app/Views/pages/best-of/<slug>.php`. La ruta `best-of/(:segment)` ya existe.
   - Cara a cara: `app/Views/pages/vs/<slug>.php`. La ruta `vs/(:segment)` ya existe.
3. Los datos de producto salen solo de `content/products/<ASIN>.json`. En la vista usa `{{product:ASIN.full_name}}`, `{{product:ASIN.specs.capacity}}` y el resto de campos, `{{product:ASIN.pros}}`, `{{product:ASIN.cta}}` y `{{compare:...}}`. El build (`base/bin/build-pages.py`) los resuelve. Un ASIN nuevo solo se añade con ficha real y comprobable. No inventes litros, vatios ni programas.
4. No publiques precios. El botón es «Ver precio en Amazon». Los enlaces de Amazon llevan `tag=dealsatr-21` y `rel="sponsored nofollow"`: el placeholder `cta` ya lo hace, y un enlace manual usa `amazon_link('ASIN')` con ese `rel`.
5. JSON-LD: `jsonld_type` = `article`, más `jsonld_products`, `jsonld_faqs` y `breadcrumbs`. El layout emite Article, BreadcrumbList, ItemList y FAQPage, sin precios, ofertas ni valoraciones en el schema.
6. Enlaza la página nueva desde la pillar y desde las páginas de marca (nav `related` y una frase en el cuerpo), y desde la nueva hacia ellas. No enlaces URLs que sigan en `pendiente`.
7. Al hacer merge a `main`, el deploy incluye la URL en `sitemap.xml` y en `llms.txt` (las rutas concretas y las vistas que encajan en `best-of/`, `review/` y `vs/`). IndexNow manda las URLs cambiadas cuando el sitio no tiene `noindex`.
8. Marca `generada` y `merge a main` al subirla. `deploy OK`, `verificada en vivo` e `IndexNow (Bing) enviado` se marcan cuando el workflow queda en verde, la URL responde 200 y el log del ping es 200 o 202. Search Console y el correo se marcan después, en otro commit.

No toques el repo `amazon-high-ticket`.
