# Prompt: Mejorar Home de dealsfreidoras.es

**URL destino:** `/`  
**Archivo destino:** `app/Views/home.php`  
**Tipo:** Home / Landing  
**Fecha:** 2026-11-18

## Instrucciones para el Bot

Reescribe la home para que deje de ser un esqueleto básico y tenga más cuerpo, mejor jerarquía visual y más puntos de entrada al contenido.

### Requisitos
- Mantén el branding: logo de Deals a tu rollo en el header (ya está en el partial), claim "Deals a tu rollo – Freidoras de aire".
- Estructura obligatoria de la home:
  1. **Hero**
     - H1: Deals a tu rollo – Freidoras de aire
     - Párrafo introductorio corto (2-3 líneas)
     - CTA principal a `/mejor-freidora-de-aire`
  2. **Categorías principales** (en cards, no bullets simples)
     - Freidoras Cecotec → `/best-of/freidora-de-aire-cecotec`
     - Freidoras Cosori → `/best-of/freidora-de-aire-cosori`
     - Freidoras Ninja → `/best-of/freidora-de-aire-ninja`
     - Freidoras grandes (5-8L) → `/best-of/freidora-de-aire-grande`
     - Usa clases CSS existentes o añade el mínimo necesario en `public/assets/css/style.css`.
  3. **Por qué confiar en Deals a tu rollo**
     - 3 puntos cortos (reviews reales, actualizado 2026, marca paraguas dealsatr.com)
  4. **FAQ corta** (3-4 preguntas típicas sobre freidoras de aire)
  5. **CTA final** a la pillar page
- Usa el layout existente (`extend('layout')`).
- Mantén el tono útil y claro.
- No inventes productos ni precios en la home.
- Al final, haz commit y abre un PR a main.

### Notas
- El logo ya está en `/assets/img/logo.svg`. Asegúrate de que el header lo muestre correctamente.
- Prioriza claridad y conversión interna hacia las páginas best-of y la pillar.
