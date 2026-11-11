# Prompt: Mejor Freidora de Aire 2026

**URL destino:** `/mejor-freidora-de-aire`  
**Archivo destino:** `app/Views/pages/mejor-freidora-de-aire.php`  
**Tipo:** Best-of / Pillar page  
**Keyword principal:** mejores freidoras de aire  
**Fecha:** 2026-11-11

## Instrucciones para el Bot

Eres un experto en afiliación y SEO. Genera el contenido completo de la página en español de España.

### Requisitos
- Busca **8-10 freidoras de aire reales** actualmente disponibles en Amazon.es (modelos populares de Cecotec, Cosori, Ninja, Philips, etc.).
- Para cada producto incluye:
  - Nombre completo
  - ASIN
  - Capacidad (litros)
  - Precio aproximado
  - 3-4 puntos clave (pros)
  - Enlace usando la función `amazon_link('ASIN')` (no hardcodees el tag)
- Estructura obligatoria:
  1. H1: Las 10 Mejores Freidoras de Aire 2026
  2. Intro (150-200 palabras) con la keyword principal y variantes
  3. Tabla comparativa rápida (modelo, capacidad, precio, valoración)
  4. Listado detallado de cada producto (con imagen placeholder, pros, CTA)
  5. Guía de compra corta (qué mirar: capacidad, potencia, funciones, marca)
  6. FAQ (5 preguntas frecuentes)
  7. Conclusión
- Usa el layout existente (`extend('layout')`).
- Incluye meta description y title adecuados.
- Tono: útil, claro, orientado a conversión, sin hype exagerado.
- Al final, guarda el archivo en la ruta indicada y actualiza `content/README.md` marcando la página como "Generada".

### Notas
- Prioriza productos con buenas valoraciones y volumen de ventas en Amazon.es.
- Si un producto no tiene ASIN claro, omítelo.
- El tag de afiliado se inyecta automáticamente con `amazon_link()`.
