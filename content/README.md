# Content Pipeline — dealsfreidoras.es

Este folder contiene los prompts generados para el Bot y el tracking del estado de cada página.
**No se despliega** (excluido en `.dockerignore`).

## Estado de páginas

| URL | Keyword principal | Tipo | Prompt | Estado | Versiones | Notas |
|-----|-------------------|------|--------|--------|-----------|-------|
| `/` | mejor freidora de aire | Home | — | Desplegada | v1 | Home básica |
| `/mejor-freidora-de-aire` | mejores freidoras de aire | Best-of | Pendiente | — | — | Pillar page |
| `/best-of/freidora-de-aire-cecotec` | freidora de aire cecotec | Best-of | Pendiente | — | — | |
| `/best-of/freidora-de-aire-cosori` | freidora de aire cosori | Best-of | Pendiente | — | — | |
| `/best-of/freidora-de-aire-ninja` | freidora de aire ninja | Best-of | Pendiente | — | — | |
| `/best-of/freidora-de-aire-grande` | freidora de aire grande | Best-of | Pendiente | — | — | |

**Leyenda de estados:**
- Pendiente: sin prompt
- Prompt listo: prompt generado, listo para Bot
- En proceso: Bot trabajando
- Generada: contenido creado en el repo
- Desplegada: live en producción
