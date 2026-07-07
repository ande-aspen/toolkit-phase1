# Base de Conocimiento — Knowledge Base

Base de conocimiento creciente sobre ecosistemas emprendedores. Cada paper, artículo o reporte ingresado se almacena como archivo individual con metadata estructurada e insights extraídos.

## Cómo funciona

1. **Ingerir:** pedir que se agregue un paper (workflow `references/workflows/ingest.md`)
2. **Consultar:** hacer preguntas sobre el contenido (workflow `references/workflows/ask.md`)
3. **Usar en reportes:** los workflows de diagnóstico y reporte buscan aquí para enriquecer análisis

## Estructura

```
knowledge/
├── README.md          ← Este archivo
├── INDEX.md           ← Índice maestro (discovery layer)
├── papers/            ← Un archivo por paper/artículo
│   └── [autor-año-titulo].md
└── topics/            ← Síntesis temáticas (opcionales)
    └── [tema].md
```

## Relación con REFERENCES_MASTER.md

- `drive/REFERENCES_MASTER.md` contiene 30 referencias específicas del diagnóstico ANDE, con IDs de extracto (1A, 9B, etc.) referenciados en reportes existentes. Es estable, no crece.
- `knowledge/` es el sistema nuevo y creciente para todo tipo de papers.
- Las consultas a la KB buscan en ambas fuentes.
- La ingesta puede cross-referenciar con extractos de REFERENCES_MASTER.md.

---

## Formato de Paper

Cada paper se guarda en `knowledge/papers/[primer-autor]-[año]-[palabras-clave].md`.

Ejemplo de nombre: `stam-2021-entrepreneurial-ecosystems.md`

### Estructura del archivo

```markdown
# [Título completo del paper]

## Metadata
- **Autor(es):** [Nombres]
- **Año:** [YYYY]
- **Publisher:** [Journal / Organización / Editorial]
- **Tipo:** [academic | industry-report | blog | policy-doc | case-study | book-chapter]
- **Idioma:** [es | en | otro]
- **URL:** [si disponible]
- **Fecha de ingesta:** [YYYY-MM-DD]

## Clasificación
- **Dominios ANDE:** [P, S, H, I, F, C, M] — cuáles toca
- **Temas:** [de la taxonomía abajo]
- **Regiones:** [LatAm, Global, Africa, Europe, Asia, North America, etc.]
- **Tags:** [tags libres: #maturity, #nascent-ecosystems, #policy-design, etc.]

## Resumen
[2-4 oraciones: de qué trata y cuál es su contribución principal]

## Insights Clave

### INS-1: [Título corto del insight]
> [Cita textual o paráfrasis cercana, máx 2-3 oraciones]

**Ubicación:** [página / sección / capítulo]
**Relevancia:** [Por qué importa para trabajo de ecosistemas]

### INS-2: [Título corto]
> [Cita / paráfrasis]

**Ubicación:** [página / sección]
**Relevancia:** [Por qué importa]

[...3-8 insights total]

## Conexiones
- **Relacionado con:** [links a otros papers en la KB por nombre de archivo]
- **Refuerza:** [qué insights de REFERENCES_MASTER.md apoya, ej: "Alinea con Extracto 9A (Stam & Van de Ven)"]
- **Contradice o matiza:** [tensiones con conocimiento existente]
```

---

## Taxonomía de Temas

Categorías para clasificar papers. Heredadas de REFERENCES_MASTER.md, extensibles.

1. **Ecosystem Frameworks & Theory** — Marcos teóricos, definiciones, modelos
2. **Measurement & Diagnostics** — Métricas, indicadores, metodologías de evaluación
3. **Accelerators & BDS Effectiveness** — Aceleradoras, incubadoras, servicios de desarrollo empresarial
4. **Financing & Investment** — VC, ángeles, fondos públicos, instrumentos financieros
5. **Culture & Social Capital** — Confianza, comunidad, actitudes hacia emprendimiento
6. **Policy Instruments & Regulation** — Políticas públicas, regulación, incentivos
7. **Growth-Oriented Entrepreneurs** — PEC, scaleups, empresas de alto crecimiento
8. **Mentoring & Advisory** — Mentoría, advisory boards, redes de soporte
9. **Ecosystem Maturity & Stages** — Etapas de desarrollo, evolución, transiciones
10. **LatAm Context** — Especificidades de América Latina
11. **Gender & Inclusion** — Género, diversidad, inclusión en ecosistemas
12. **AI & Technology** — Impacto de tecnología en ecosistemas
13. **Case Studies** — Estudios de caso de ecosistemas específicos

Para agregar un nuevo tema: simplemente usarlo en la clasificación del paper y agregarlo a esta lista.

---

## Convenciones

- **Idioma:** los papers se guardan en su idioma original. El tag `Idioma` permite filtrar.
- **Insights:** priorizar hallazgos accionables, cuantitativos, o contraintuitivos.
- **Conexiones:** siempre buscar cómo el paper se conecta con lo que ya existe en la KB.
- **Nombres de archivo:** minúsculas, guiones, sin acentos ni caracteres especiales.
