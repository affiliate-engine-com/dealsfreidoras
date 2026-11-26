# Content Pipeline — dealsfreidoras.es

Este folder contiene los prompts generados para el Bot y el tracking del estado de cada página.
El plan semanal de long-tail y su checklist de publicación están en `longtail-plan.md`.
**No se despliega** el texto de este folder como página pública (`content/prompts` está excluido en `.dockerignore`).

## Estado de páginas

| URL | Keyword principal | Tipo | Prompt | Estado | Versiones | Notas |
|-----|-------------------|------|--------|--------|-----------|-------|
| `/` | mejor freidora de aire | Home | `prompts/home.md` | Generada | v2 | Hero, cards, confianza, FAQ y CTA |
| `/mejor-freidora-de-aire` | mejores freidoras de aire | Best-of | `prompts/mejor-freidora-de-aire.md` | Generada | — | Pillar page |
| `/best-of/freidora-de-aire-cecotec` | freidora de aire cecotec | Best-of | `prompts/freidora-de-aire-cecotec.md` | Generada | — | 8 modelos, fichas Amazon.es 14 nov 2026 |
| `/best-of/freidora-de-aire-cosori` | freidora de aire cosori | Best-of | `prompts/freidora-de-aire-cosori.md` | Generada | — | 7 modelos, fichas Amazon.es 18 nov 2026 |
| `/best-of/freidora-de-aire-ninja` | freidora de aire ninja | Best-of | `prompts/freidora-de-aire-ninja.md` | Generada | — | 7 modelos, fichas Amazon.es 18 nov 2026 |
| `/best-of/freidora-de-aire-grande` | freidora de aire grande | Best-of | `prompts/freidora-de-aire-grande.md` | Generada | — | 8 modelos, fichas Amazon.es 18 nov 2026 |
| `/mejor-freidora-de-aire-barata` | mejor freidora de aire barata | Long-tail | `longtail-plan.md` | Generada | — | Semana del 2026-11-23. Seguimiento en `longtail-plan.md` |

**Leyenda de estados:**
- Pendiente: sin prompt
- Prompt listo: prompt generado, listo para Bot
- En proceso: Bot trabajando
- Generada: contenido creado en el repo
- Desplegada: live en producción
