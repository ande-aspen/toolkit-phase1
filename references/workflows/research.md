# Research Automatizado de Ecosistema

## Descripción
Investiga un ecosistema emprendedor usando búsqueda web para generar el documento de research que alimenta al workflow de diagnóstico. Ejecuta 8 rondas de búsqueda cubriendo los 7 dominios ANDE, integra datos nacionales del archivo de país, y produce un documento narrativo completo en `input/`.

## Cuándo se usa
- El usuario pide investigar un ecosistema sin traer documento de research
- Se ejecuta automáticamente en modo batch antes del Paso 1 del diagnóstico

## Inputs
- **Obligatorio:** ciudad, estado/provincia, país, población de referencia
- **Opcional:** organizaciones, programas, fondos, startups que el usuario conoce
- **Opcional:** datos puntuales del usuario en chat
- **Opcional:** pistas de búsqueda ("busca el programa X del gobierno estatal")
- **Opcional:** documento complementario en `input/` ([ciudad].pdf, .md, .txt)

---

## Proceso

```
1. RECIBIR METADATA: ciudad, estado/provincia, país, población de referencia
2. RECIBIR CONTEXTO DEL USUARIO (opcional):
   - Organizaciones, programas, fondos, startups que el usuario conoce
     → buscarlas con prioridad y mayor profundidad en el research
   - Datos puntuales que el usuario aporta en el chat
     → incorporar directamente, marcar fuente como "Usuario / contexto local"
   - Pistas de búsqueda ("busca el programa X del gobierno estatal")
     → agregar como queries específicas en las rondas relevantes
3. BUSCAR DOCUMENTO COMPLEMENTARIO EN input/:
   a. Buscar archivos que coincidan con el nombre de la ciudad:
      [ciudad].pdf, [ciudad].md, [ciudad].txt, [ciudad].docx
      (case-insensitive, con o sin acentos)
   b. Si existe → leerlo PRIMERO, extraer todos los datos e indicadores que contenga
   c. Estos datos tienen prioridad sobre lo que encuentre web search
   d. El web search complementa lo que el documento no cubra
   e. Si NO existe documento complementario → research 100% web
4. CARGAR DATOS NACIONALES:
   a. Leer references/countries/[pais].md si existe
   b. Pre-llenar P1, P2, H5, C5 del archivo de país
   c. Estimar S5 usando defaults del archivo de país, marcar (est.)
   d. Si NO existe archivo de país → incluir indicadores nacionales en el research
      (agregar Ronda 0 de búsqueda) y crear el archivo de país como subproducto
5. EJECUTAR RESEARCH:
   a. Leer references/research-workflow.md para workflow detallado de las 8 rondas
   b. Ejecutar 8 rondas de búsqueda web (ver workflow)
   c. Para cada ronda: buscar en español e inglés, extraer datos, anotar actores y contexto
   d. Priorizar búsqueda de organizaciones/datos que el usuario mencionó
   e. Si hay documento complementario → enfocar web search en los gaps
      (indicadores que el documento no cubrió o cubrió parcialmente)
   f. Indicadores sin dato suficiente:
      - Modo individual → preguntar al usuario + estimación conservadora
      - Modo batch → estimación conservadora automática (score 15-25), marcar y continuar
6. COMPILAR DOCUMENTO:
   a. Generar documento de research narrativo (7 dominios con tablas + párrafos de contexto)
   b. Integrar datos del documento complementario + web search + contexto del usuario
   c. Formato idéntico a los documentos existentes en input/
   d. Guardar en input/[ciudad], [pais].md
7. ENTREGAR RESUMEN:
   a. Indicadores con dato / estimados / sin dato
   b. Fuentes: cuáles vienen del documento complementario vs web search vs usuario
   c. Alertas de calidad (F1-F5 probablemente subestimados por web search)
   d. Modo individual → preguntar: "¿Revisar/complementar o proceder al diagnóstico?"
   e. Modo batch → continuar automáticamente al Paso 1 del diagnóstico
```

⚠️ **Calidad del research automatizado:** Los resultados de búsqueda web no reemplazan bases de datos especializadas (Crunchbase, LAVCA, PitchBook). Los indicadores de Financiamiento (F1-F5) pueden estar subestimados. En modo individual se recomienda complementar antes del diagnóstico.

---

## Recursos

| Recurso | Path | Cuándo leer |
|---------|------|-------------|
| Workflow detallado (8 rondas) | `references/research-workflow.md` | Antes de ejecutar búsquedas |
| Datos nacionales | `references/countries/[pais].md` | Al inicio, para pre-llenar P1, P2, H5, C5, S5 |
| Documento complementario | `input/[ciudad].*` | Al inicio, si existe |

---

## Outputs
- `input/[ciudad], [pais].md` — documento de research narrativo
- Si no existía archivo de país → `references/countries/[pais].md` como subproducto

---

## Checklist Pre-Entrega

- [ ] Documento complementario buscado en `input/` (y leído si existe)
- [ ] Contexto del usuario capturado (si lo proporcionó)
- [ ] Archivo de país consultado (o indicadores nacionales investigados)
- [ ] S5 estimado con fuente y marcado `(est.)`
- [ ] 8 rondas de búsqueda ejecutadas (enfocadas en gaps si hay doc complementario)
- [ ] 30 indicadores con fila en documento (incluyendo "Sin dato específico")
- [ ] Actores y programas capturados por nombre en notes
- [ ] Vigencia aplicada: `(?)` en actores no confirmados
- [ ] Documento guardado en `input/` con formato correcto
- [ ] Notas de calidad: origen de cada dato (doc complementario / usuario / web / país / estimación)
- [ ] F1-F5 flaggeados si parecen subestimados
