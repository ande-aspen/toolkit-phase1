# Ingesta de Papers y Artículos

## Metadata
- **Comando:** /ingest
- **Aliases:** /paper
- **Idioma:** bilingüe (papers se guardan en idioma original)
- **Versión:** 1.0

## Descripción
Procesa un paper, artículo, reporte o blog post y lo integra a la base de conocimiento (`knowledge/`). Extrae metadata, clasifica por dominios ANDE y temas, identifica insights clave, y actualiza el índice maestro. El contenido queda disponible para consultas (`/ask`) y para enriquecer reportes (`/diagnostico`, `/report`).

## Trigger
- El usuario escribe `/ingest` o `/paper`
- El usuario dice "agrega este paper", "integra este artículo", "guarda esta referencia"
- El usuario proporciona un PDF, URL, o texto de un paper y pide procesarlo

## Inputs
- **Fuente** (al menos uno):
  - PDF en el filesystem (path)
  - Texto pegado en chat
  - URL de artículo
  - Archivo en el filesystem (.md, .txt, .docx)
- **Opcional:** notas del usuario sobre por qué es relevante o qué buscar

---

## Proceso

```
1. RECIBIR INPUT:
   - Identificar la fuente (PDF, URL, texto, path)
   - Leer el material completo
   - Si es URL → usar web fetch para obtener contenido

2. EXTRAER METADATA:
   - Título completo
   - Autor(es)
   - Año de publicación
   - Publisher / journal / organización
   - Tipo: academic | industry-report | blog | policy-doc | case-study | book-chapter
   - Idioma: es | en | otro
   - URL (si aplica)

3. CLASIFICAR:
   a. Dominios ANDE que toca: P, S, H, I, F, C, M (puede ser múltiples)
   b. Temas de la taxonomía (ver knowledge/README.md):
      - Ecosystem Frameworks & Theory
      - Measurement & Diagnostics
      - Accelerators & BDS Effectiveness
      - Financing & Investment
      - Culture & Social Capital
      - Policy Instruments & Regulation
      - Growth-Oriented Entrepreneurs
      - Mentoring & Advisory
      - Ecosystem Maturity & Stages
      - LatAm Context
      - Gender & Inclusion
      - AI & Technology
      - Case Studies
      - [Nuevo tema si ninguno aplica]
   c. Región geográfica: LatAm, Global, Africa, Europe, Asia, North America, etc.
   d. Tags libres: #maturity, #nascent-ecosystems, #policy-design, etc.

4. EXTRAER INSIGHTS CLAVE (3-8 por paper):
   Para cada insight:
   - ID: INS-1, INS-2, etc.
   - Título corto descriptivo
   - Cita textual o paráfrasis cercana (máx 2-3 oraciones)
   - Ubicación en el documento (página, sección, capítulo)
   - Relevancia: por qué importa para trabajo de ecosistemas

   Priorizar:
   - Frameworks accionables
   - Hallazgos cuantitativos
   - Casos de estudio con resultados
   - Visiones contraintuitivas o que desafíen supuestos
   - Innovaciones metodológicas

5. IDENTIFICAR CONEXIONES:
   a. Leer knowledge/INDEX.md para ver qué papers ya existen
   b. Notar papers relacionados (por tema, por hallazgo, por contradicción)
   c. Verificar si algún insight refuerza o contradice extractos
      de drive/REFERENCES_MASTER.md (solo si el tema es cercano al diagnóstico)

6. GENERAR ARCHIVO:
   - Nombre: [primer-autor]-[año]-[2-4-palabras-clave].md
     Ejemplo: stam-2021-entrepreneurial-ecosystems.md
   - Path: knowledge/papers/[nombre].md
   - Formato: ver knowledge/README.md para estructura estándar

7. ACTUALIZAR ÍNDICE:
   - Leer knowledge/INDEX.md
   - Agregar entrada en las secciones relevantes:
     - Por dominio ANDE
     - Por tema
     - Por región
     - Cronológico (por fecha de ingesta)
   - Guardar INDEX.md actualizado

8. CONFIRMAR AL USUARIO:
   - Título y clasificación
   - Número de insights extraídos
   - Conexiones identificadas con otros papers
   - Path del archivo creado
   - Sugerencia: "Usa /ask para consultar sobre este paper o temas relacionados"
```

---

## Recursos

| Recurso | Path | Cuándo leer |
|---------|------|-------------|
| Formato de papers | `knowledge/README.md` | Antes de generar archivo |
| Índice de KB | `knowledge/INDEX.md` | Para conexiones y para actualizar |
| Referencias diagnóstico | `drive/REFERENCES_MASTER.md` | Solo si el paper toca temas del diagnóstico |

## Outputs
- `knowledge/papers/[autor-año-titulo].md` — archivo del paper
- `knowledge/INDEX.md` — actualizado con nueva entrada

## Checklist
- [ ] Metadata completa (título, autor, año, tipo, idioma)
- [ ] Clasificación por dominio ANDE + tema + región
- [ ] 3-8 insights con citas, ubicación y relevancia
- [ ] Conexiones con papers existentes identificadas
- [ ] Archivo guardado en `knowledge/papers/`
- [ ] INDEX.md actualizado en todas las secciones relevantes
- [ ] Confirmación entregada al usuario
