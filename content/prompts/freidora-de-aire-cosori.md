# Prompt: Mejores Freidoras de Aire Cosori

**URL destino:** `/best-of/freidora-de-aire-cosori`  
**Archivo destino:** `app/Views/pages/best-of/freidora-de-aire-cosori.php`  
**Tipo:** Best-of (marca)  
**Keyword principal:** freidora de aire cosori  
**Fecha:** 2026-11-14

## Instrucciones para el Bot

Eres un experto en afiliación y SEO. Genera el contenido completo de la página en español de España.

### Requisitos
- Busca **5-7 freidoras de aire Cosori** reales y actualmente disponibles en Amazon.es (Turbo Blaze, CP158-AF, Dual Blaze, etc.).
- Para cada producto incluye:
  - Nombre completo
  - ASIN
  - Capacidad (litros)
  - Precio aproximado
  - 3-4 puntos clave (pros)
  - Enlace usando la función `amazon_link('ASIN')` (no hardcodees el tag)
- Estructura obligatoria:
  1. H1: Las Mejores Freidoras de Aire Cosori 2026
  2. Intro (150-180 palabras) con la keyword principal y variantes
  3. Tabla comparativa rápida (modelo, capacidad, precio, valoración)
  4. Listado detallado de cada producto (con imagen placeholder, pros, CTA)
  5. Guía de compra corta enfocada en la gama Cosori (diferencias entre modelos, cuál elegir)
  6. FAQ (4-5 preguntas frecuentes sobre freidoras Cosori)
  7. Conclusión + enlace a la pillar page `/mejor-freidora-de-aire`
- Usa el layout existente (`extend('layout')`).
- Incluye meta description y title adecuados.
- Tono: útil, claro, orientado a conversión, sin hype exagerado.
- Al final, guarda el archivo en la ruta indicada y actualiza `content/README.md` marcando la página como "Generada".

### Notas
- Prioriza productos con buenas valoraciones y volumen de ventas en Amazon.es.
- Si un producto no tiene ASIN claro, omítelo.
- El tag de afiliado se inyecta automáticamente con `amazon_link()`.
