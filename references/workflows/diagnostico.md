# Diagnóstico ANDE Fase 1

## Descripción
Ejecuta un diagnóstico completo de ecosistema emprendedor siguiendo la metodología ANDE Fase 1. Parsea datos de research, extrae y puntúa 30 indicadores en 7 dominios, y genera un reporte profesional de 8 secciones con visualización radar.

## Cuándo se usa
- El usuario pide un diagnóstico de ecosistema, evaluación de ecosistema, o assessment
- El usuario entrega un documento de research y pide procesarlo

## Inputs
- Documento de research (en `input/`, pegado en chat, CSV, tabla, texto libre, o combinación)
- Metadata: ciudad, estado/provincia, país, población de referencia
- Si no hay documento de research, ejecutar primero el workflow de research (`references/workflows/research.md`)

## Formatos de Input Aceptados

| Formato | Descripción |
|---------|-------------|
| **Documento de research** | MD, TXT, PDF o pegado en chat. Se parsea, extrae los 30 indicadores y genera CSV automáticamente. Todo el contexto cualitativo (nombres, programas, actores, cifras secundarias) se preserva en `notes`. |
| CSV completo | `indicator_id,domain,indicator_name,value,source,notes` (opcionalmente `score`) |
| CSV mínimo | `indicator_id,value,source,notes` — se completa domain e indicator_name |
| Tabla en chat | Tabla markdown o texto pegado |
| Texto por dominio | Prosa describiendo hallazgos por dominio |
| Mixto | Documento de research + indicadores adicionales en chat |
| Incremental | Varios mensajes, se acumula hasta completar |

---

## Modos de Ejecución

### Modo individual (con pausa entre pasos)
El usuario ejecuta paso a paso, con oportunidad de revisar y corregir entre cada paso.
Útil cuando el usuario quiere complementar datos manualmente.

### Modo batch / automático (sin pausas)
El usuario da una lista de ciudades y se ejecuta Research → Paso 1 → Paso 2 para cada una sin detenerse.
Indicadores sin dato se estiman conservadoramente (score 15-25). Gaps se reportan al final.

**Trigger batch:** El usuario proporciona una lista de ciudades con metadata.
```
Formato esperado:
- Ciudad, Estado, País, Población
- Ciudad, Estado, País, Población
...
```

**Flujo batch:**
```
1. Cargar archivo de país UNA VEZ (indicadores nacionales compartidos)
2. Leer references/rubrica-scoring.md, references/reporte-template.md,
   references/template-radar.html, y guides/editor-humano.md UNA VEZ
   (aplican igual para todas las ciudades del mismo país)
3. Capturar contexto del usuario: organizaciones, datos, pistas de búsqueda
   que apliquen a ciudades específicas o a todas
4. Para cada ciudad en la lista:
   a. Buscar documento complementario en input/ ([ciudad].pdf, .md, .txt)
      → si existe, leerlo primero y usarlo como base
   b. Research web (workflow research, 8 rondas, enfocado en gaps) → guardar en input/
   c. Paso 1: Parsear, validar, scoring → guardar CSV en output/
      - Indicadores sin dato → estimación conservadora automática (15-25)
      - No detenerse por gaps ni inconsistencias — marcar y continuar
   d. Paso 2: Reporte + Radar → guardar en output/
      - Leer METODOLOGIA_EN y los papers relevantes de knowledge/ para cada ciudad
        (las recomendaciones dependen del perfil específico)
      - Humanizar cada reporte
5. Al terminar TODAS las ciudades:
   a. Presentar tabla comparativa (ciudad × score global × madurez × cuello de botella)
   b. Listar gaps y alertas consolidados por ciudad
   c. Listar entregables generados
```

**Entregables por ciudad (modo batch):**
- `input/[ciudad], [pais].md` (documento de research)
- `output/[ciudad]_[pais] - indicators.csv`
- `output/[ciudad]_[pais] - phase1.md` (reporte)
- `output/[ciudad]_[pais] - radar.html` (visualización)

### Modo re-diagnóstico (v2)

Se activa cuando el usuario pide actualizar, refrescar o re-evaluar una ciudad ya diagnosticada. La metodología recomienda repetirlo a los 24-36 meses; también aplica cuando hay evidencia nueva significativa.

```
1. LEER LA LÍNEA BASE COMPLETA antes de investigar:
   CSV v1 + reporte v1 + documento de research v1
   → Si el documento de research v1 no existe en input/ (ej: Villahermosa),
     reconstruir la línea base desde el reporte v1 y el CSV v1: los actores,
     programas y datos citados ahí son el punto de partida del research enfocado
2. RESEARCH ENFOCADO: verificar cada actor/dato de la v1 (¿sigue activo?)
   y buscar lo que la v1 no encontró
3. TABLA DE DELTAS OBLIGATORIA — para cada indicador que cambió:
   | ID | Valor v1 | Score v1 | Valor v2 | Score v2 | Tipo de cambio |
   Tipo de cambio ∈ {EVIDENCIA (existía, no se había encontrado),
                     REAL (cambió en el terreno),
                     RÚBRICA (re-aplicación de criterios)}
   Ubicación: en la sección 8 del reporte v2, inmediatamente después de la
   tabla de 30 indicadores. En el CSV v2, anotar el tipo de cambio en `notes`
4. El resumen ejecutivo de la v2 ABRE declarando la descomposición:
   "El score pasó de X a Y; Z puntos provienen de mejor evidencia y
   W de cambios reales en el ecosistema"
5. NAMING: sufijo _v2 en los tres entregables. La v1 NUNCA se borra ni
   se sobrescribe (es la línea base para medir cambio real en el tiempo)
6. Congelar criterios: usar la MISMA rúbrica y los mismos criterios de
   vigencia que la v1; si la rúbrica cambió entre versiones, señalarlo
   como tipo de cambio RÚBRICA, no como mejora del ecosistema
```

Precedentes: Nairobi v2 (deltas por realineación con evidencia, +1 punto) y La Paz v2 (+21 puntos, casi todo EVIDENCIA — actores que existían y la v1 no encontró).

---

## Proceso

### PASO 1 — Parsear, Validar y Puntuar

```
1. RECIBIR INPUT:
   - Si viene del workflow de research → el documento ya está en input/, la metadata ya se conoce
   - Si viene del usuario → documento de research en input/ (MD, TXT, PDF),
     pegado en chat, CSV, tabla en chat, texto libre, o combinación
   - Recibir metadata si no se tiene: ciudad, estado, país, población de referencia
2. PARSEAR DOCUMENTO DE RESEARCH:
   a. Leer el documento completo
   b. Extraer los 30 indicadores buscando por dominio y por nombre de indicador
   c. Para cada indicador extraer: valor cuantitativo, fuente(s), y contexto cualitativo
   d. Capturar TODO el contexto local mencionado: nombres de actores, programas,
      instituciones, eventos, fondos, startups, cifras secundarias, anécdotas,
      datos de vigencia — guardar en el campo `notes` del CSV
   e. Si el documento menciona información relevante que no mapea directamente a un
      indicador pero da contexto al ecosistema → preservar en notes del indicador
      más cercano o en un campo de notas generales
   f. Generar tabla CSV estándar con los 30 indicadores
3. VALIDAR:
   a. ¿Están los 30 indicadores? Si faltan:
      - Modo individual → listar cuáles, preguntar si proceder con estimaciones
      - Modo batch → asignar estimación conservadora (15-25), marcar y continuar
   b. ¿Cada indicador tiene value y source? Señalar los que no
   c. ¿Hay valores inconsistentes? (ej: "200 VCs" en ciudad de 300K hab.) Señalar
   d. ¿Los actores cumplen criterios de vigencia? (ver sección Criterios de Vigencia abajo)
4. SCORING:
   a. Leer references/rubrica-scoring.md ANTES de asignar scores
   b. Si el usuario incluyó scores → usarlos, pero señalar discrepancias >15 puntos con la rúbrica
   c. Si NO incluyó scores → aplicar rúbrica indicador por indicador
   d. Ciudades < 1M hab: ajuste por población en indicadores de conteo ANTES de puntuar
5. CALCULAR (usar scripts/score.py si hay Python disponible; si no, aplicar las fórmulas de la sección Cálculos):
   a. Score por dominio = promedio de indicadores del dominio
   b. Score global = promedio de los 7 dominios
   c. Score ajustado por cuello de botella = media geométrica de los 7 dominios
      (ver sección Cálculos). Si la brecha con el global es >8 puntos → señalar
      que los dominios fuertes enmascaran la severidad del cuello de botella
   d. Rango de incertidumbre: recalcular el score global excluyendo los
      indicadores marcados (est.) → reportar "global X (sin estimados: Y),
      Z% del score basado en estimaciones"
   e. Nivel de madurez propuesto por score (0-25: Naciente, 26-45: Emergente,
      46-65: En Desarrollo, 66-100: Autosostenible)
   f. VALIDAR madurez contra marcadores estructurales (ver sección
      Validación Estructural de Madurez). Si score y estructura divergen →
      reportar ambos, no promediar
   g. Cuello de botella = dominio con score más bajo
   h. Patrón Condición-Resultado
6. ENTREGAR:
   a. Tabla resumen con semáforos
   b. Score global (+ ajustado por cuello de botella + rango sin estimados),
      madurez (score y validación estructural), cuello de botella, patrón C-R
   c. Discrepancias o alertas
   d. CSV → guardar en output/[ciudad]_[pais] - indicators.csv
   e. Modo individual → esperar aprobación del usuario antes del Paso 2
   f. Modo batch → continuar automáticamente al Paso 2
```

---

### PASO 2 — Análisis y Reporte

```
1. Idioma: español por defecto. Si pide inglés → redactar todo en inglés
2. Si hubo correcciones (modo individual), actualizar CSV
3. Leer references/reporte-template.md → seguir estructura de 8 secciones al pie de la letra
4. Para secciones que lo requieran: leer drive/METODOLOGIA_EN.md (canónica, V3.7).
   Si el reporte es en español, usar drive/METODOLOGIA_ES.md solo como apoyo de terminología
5. Para recomendaciones: leer knowledge/INDEX.md — usar los temas para localizar los papers relevantes en knowledge/papers/
6. ENRIQUECER CON CONTEXTO LOCAL:
   - Releer el documento de research original (no solo el CSV)
   - Usar nombres concretos de actores, programas, startups, fondos, eventos
     mencionados en el research para dar vida al análisis
   - Incorporar ejemplos específicos del ecosistema en cada sección de dominio
     (ej: no decir "hay pocas aceleradoras", sino "las únicas dos aceleradoras
     identificadas — [Nombre1] y [Nombre2] — operan con cohortes anuales")
   - En fortalezas y retos: usar evidencia concreta del research, no generalidades
   - En recomendaciones: conectar con actores locales que podrían ejecutarlas
7. Redactar reporte completo (8 secciones)
8. Generar radar HTML usando references/template-radar.html como base
9. HUMANIZACIÓN OBLIGATORIA:
   - Español → Leer y aplicar guides/editor-humano.md al texto completo
   - English → Leer y aplicar guides/humanizer.md al texto completo
10. Guardar entregables en output/
```

**Entregables del Paso 2:**
- `output/[ciudad]_[pais] - phase1.md` (reporte, o `phase1_en.md` si es inglés)
- `output/[ciudad]_[pais] - radar.html` (visualización)
- `output/[ciudad]_[pais] - indicators.csv` (actualizado si hubo cambios)

---

## Los 30 Indicadores

### Dominios Condición
- **P: Política y Regulación** (3): P1 Días constituir empresa, P2 Régimen fiscal startups, P3 Programas públicos activos
- **S: Servicios de Apoyo** (5): S1 Aceleradoras, S2 Incubadoras, S3 Coworkings, S4 Mentores, S5 Velocidad internet
- **H: Capital Humano** (5): H1 Universidades con emprendimiento, H2 Bootcamps, H3 Graduados STEM, H4 Talento tech, H5 Acceso internet %
- **I: I+D e Innovación** (3): I1 Patentes, I2 Centros investigación, I3 Publicaciones indexadas

### Dominios Resultado
- **F: Financiamiento** (6): F1 Inversión total 3 años, F2 Rondas anuales, F3 VCs locales, F4 Ángeles activos, F5 Exits, F6 Capital semilla público
- **C: Cultura** (5): C1 Meetups, C2 Eventos, C3 Medios especializados, C4 Comunidades online, C5 Confianza social
- **M: Mercados** (3): M1 Startups activas, M2 Corporativos tech, M3 Sectores especialización

### Clasificación por Tipo de Research

| Tipo | Indicadores | Comportamiento en el research |
|------|------------|--------------------------|
| Nacional (archivo de país) | P1, P2, H5, C5 | Pre-llenados de `references/countries/[pais].md`. No se investigan. |
| Estimación | S5 | Default del archivo de país. Marcado `(est.)`. |
| Ciudad (research web) | Los 25 restantes | 8 rondas de búsqueda web. Ver `references/research-workflow.md`. |

---

## Criterios de Vigencia

Reglas para determinar si un actor, programa o recurso cuenta como "activo":

### Regla general
Un actor está **activo** si hay evidencia de actividad en los últimos 24 meses.

### Por tipo de actor

| Tipo | Criterio de actividad | Ejemplo activo | Ejemplo NO activo |
|------|----------------------|----------------|-------------------|
| Aceleradora | ≥1 cohorte graduada o en curso en últimos 24 meses | "Startup Chile abrió convocatoria en oct 2025" | "Programa sin cohortes desde 2022" |
| Incubadora | Programa de incubación con empresas inscritas en últimos 24 meses | "Incuba UNAM tiene 8 startups en programa" | "Incubadora solo tiene landing page sin actividad" |
| Meetup | ≥1 evento en últimos 3 meses Y ≥3 eventos en últimos 12 meses | "Startup Grind GDL: evento mensual, último hace 2 semanas" | "Grupo en Meetup.com con último evento hace 8 meses" |
| Medio especializado | Publicación en los últimos 30 días | "Podcast semanal, último episodio esta semana" | "Blog sin post desde 2023" |
| Comunidad online | ≥1 post/mes en los últimos 3 meses | "Slack con conversación diaria" | "Grupo de LinkedIn sin posts en 6 meses" |
| Fondo/VC | ≥1 inversión documentada en el ecosistema en últimos 24 meses | "500 Global invirtió en 2 startups locales en 2025" | "Fondo sin deals locales documentados" |
| Red de ángeles | ≥1 deal documentado en últimos 24 meses | "Club de ángeles con 3 inversiones en 2024" | "Red formalmente constituida pero sin deals en 18 meses" |
| Programa público | Convocatoria activa o desembolsos en últimos 24 meses | "CORFO abrió convocatoria en 2025" | "INADEM fue cerrado en 2019" |

### Cómo marcar vigencia

- **Vigencia confirmada:** Incluir directamente → `Startup México SLP`
- **Vigencia no confirmada:** Agregar `(?)` → `TechHub Potosí (?)`
- En el campo `notes`: especificar qué evidencia se encontró o por qué no se pudo confirmar

### Regla de exclusión
NO contar como activo si la única evidencia es un sitio web estático sin actualización en >12 meses, una página de Facebook sin posts en >6 meses, o un registro en directorio sin confirmación independiente.

---

## Cálculos

### Ajuste por población (ciudades < 1M hab)
```
Valor ajustado = (Valor absoluto / Población) × 1,000,000
```
Aplica a: S1, S2, S3, S4, C1, C2, M1, M2, I1, I2
NO aplica a: F1-F6, P3, H1 (institucionales, no per cápita)

### Semáforo
| Color | Rango | Estado |
|-------|-------|--------|
| 🟢 | ≥60 | Bien desarrollado |
| 🟡 | 40-59 | En desarrollo |
| 🔴 | <40 + más bajo | Cuello de botella |
| 🔴 | <40 + no más bajo | Atención prioritaria |

### Score ajustado por cuello de botella
```
Score ajustado = (D1 × D2 × D3 × D4 × D5 × D6 × D7)^(1/7)
```
Media geométrica de los 7 scores de dominio (usar max(dominio, 1) si algún dominio es 0). A diferencia del promedio simple, penaliza los cuellos de botella: los dominios fuertes no compensan al débil, que es la lógica central del modelo ANDE (el dominio más débil limita al sistema). Se reporta como complemento del score global, nunca lo reemplaza. Brecha >8 puntos = los dominios fuertes enmascaran la restricción.

### Rango de incertidumbre por estimaciones
```
% estimado = (# indicadores con (est.) / 30) × 100
Score sin estimados = promedio recalculado excluyendo indicadores (est.)
```
Reportar siempre: "Score global X (sin estimados: Y). Z% de los indicadores son estimaciones." Si Z > 30%, señalar en el reporte que el score es sensible a research adicional (precedente: La Paz subió 21 puntos entre v1 y v2 solo por mejor evidencia).

### Nivel de madurez
| Score Global | Nivel |
|--------------|-------|
| 0-25 | Naciente |
| 26-45 | Emergente |
| 46-65 | En Desarrollo |
| 66-100 | Autosostenible |

### Validación Estructural de Madurez

El score propone el nivel; la estructura lo confirma. Después de clasificar por score, verificar los 4 marcadores estructurales (basados en las generaciones de Cukier & Kon y la Tabla 3.1 de la metodología):

| # | Marcador | Evidencia que buscar en el research |
|---|----------|-------------------------------------|
| 1 | **Reinversión (Gen 2+)** | Emprendedores con exit/liquidez actuando como ángeles, mentores o creando fondos |
| 2 | **Capital local activo** | Fondos locales liderando rondas (no solo coinvirtiendo con externos) |
| 3 | **ESOs sostenibles** | Organizaciones de Apoyo con ingresos diversificados, no dependientes de un solo donante |
| 4 | **Atracción neta** | Talento y capital entrando al ecosistema, no saliendo |

Regla de validación:
- **Autosostenible** requiere los 4 marcadores; **En Desarrollo** requiere al menos 1-2 (típicamente capital local incipiente)
- Si el score dice un nivel y los marcadores dicen otro → **reportar ambos sin promediar**: "Score de Autosostenible (82) con estructura de En Desarrollo: el ciclo de reinversión se debilitó en 2023-2024" (caso Nairobi)
- La divergencia es un hallazgo del diagnóstico, no un error: normalmente indica un ecosistema frágil (score alto sin estructura) o en despegue (estructura mejor que el score)

### Patrón Condición-Resultado
```
Promedio_Condición = (Política + Servicios + Capital_Humano + I+D) / 4
Promedio_Resultado = (Financiamiento + Cultura + Mercados) / 3
```
| Patrón | Diagnóstico |
|--------|-------------|
| C ≥50 + R ≥50 | Ecosistema efectivo |
| C ≥50 + R <50 | Problema de conexión |
| C <50 + R ≥50 | Sistema frágil |
| C <50 + R <50 | Ecosistema incipiente |

### Cuello de botella
Dominio con score más bajo. Excepciones:
- Diferencia <5 puntos con el segundo → ambos son críticos
- Es dominio Condición y hay uno Resultado igual de bajo → señalar ambos

---

## Tabla 4.3: Intervenciones por Madurez

| Dominio | Naciente | Emergente | En Desarrollo | Autosostenible |
|---------|----------|-----------|---------------|----------------|
| Cultura | **Construir** | Fortalecer | Mantener | Mantener |
| Capital Humano | **Construir** | Fortalecer | Escalar | Mantener |
| Servicios Apoyo | **Construir** | Fortalecer | Escalar | Mantener |
| Política | Esperar | **Construir** | Fortalecer | Mantener |
| Financiamiento | Esperar | **Construir** | Fortalecer | Escalar |
| Mercados | Esperar | Esperar | Fortalecer | Escalar |
| I+D | Esperar | Esperar | **Construir** | Fortalecer |

Si la tabla dice "Esperar" para un dominio en el nivel de madurez del ecosistema → NO hacer recomendación principal para ese dominio.

### Secuencia Evolutiva
```
Etapa 1: Cultura → Capital Humano
Etapa 2: Servicios de Apoyo
Etapa 3: Política → Financiamiento
Etapa 4: Mercados → I+D
```

---

## Cómo Usar las Referencias

La fuente de evidencia del diagnóstico es la base de conocimiento: **`knowledge/INDEX.md`** (índice semántico por 13 temas) → **`knowledge/papers/`** (30 papers con insights identificados por INS-#).

### Cómo buscar
- **Leer `knowledge/INDEX.md`** — organizado por tema con micro-resúmenes; indica exactamente qué 2-3 papers abrir según el dominio o la pregunta
- **Abrir solo los papers relevantes** de `knowledge/papers/` — no abrir todos
- **Citar en reporte:** autor + año; agregar el INS-# cuando se use un insight específico (ej: "Argidius (2021), INS-3")

### Regla de mínimos
**Mínimo 3 recomendaciones deben tener respaldo de la base de conocimiento.** Citar con autor + año (+ INS-# si aplica).

`drive/REFERENCES_MASTER.md` es legado (mismo contenido migrado a `knowledge/papers/`): consultarlo solo para verificar un "Extracto ##" citado en reportes históricos.

---

## Prioridades del Paso 2

Invertir la mayor calidad en:

### 1. Análisis estratégico profundo (Secciones 2, 3, 5, 6)
NUNCA ser descriptivo. No decir "Financiamiento obtuvo 28. Se encontraron 2 VCs." En cambio: "El acceso a capital representa la restricción más severa. Con solo 2 fondos regionales, los emprendedores dependen de capital propio o programas públicos no diseñados para startups tech."

Usar el campo `notes` de los indicadores Y el documento de research original — contienen contexto cualitativo que da profundidad. Mencionar actores, programas, startups y eventos por nombre. El lector local debe reconocer su ecosistema en el texto.

### 2. Recomendaciones fundamentadas (Sección 7)
- Coherentes con Tabla 4.3 (dominio × madurez)
- Fundamentadas con METODOLOGIA_EN + papers de knowledge/
- Accionables: actor local específico + acción + métrica + horizonte
- Conectar cada recomendación con actores locales identificados en el research
  (ej: no decir "crear programa de mentoría", sino "la Universidad [X] podría
  liderar un programa de mentoría conectando su red de egresados tech con
  las startups identificadas en [sector]")
- No recomendar lo que ya existe (revisar notes del input y el research)

### 3. Humanización del texto
Todo reporte pasa por el guide de humanización antes de entrega. El documento es para stakeholders — debe leerse como escrito por un experto, no por IA.

---

## Indicadores Faltantes

Si vienen menos de 30:
- **Modo individual:** Listar faltantes por dominio, preguntar si proceder con estimaciones conservadoras (15-25)
- **Modo batch:** Asignar estimación conservadora automática (15-25), marcar como "Sin dato específico", señalar en reporte y en el resumen final del batch

## Discrepancias de Score

Si el usuario da scores que difieren >15 puntos de la rúbrica:
1. Señalar: "Tu score para F1 es 70, pero USD 3M sugiere 30-49 según rúbrica. ¿Info adicional?"
2. Si confirma → usar su score (tiene contexto local)
3. Si no justifica → sugerir el de la rúbrica

---

## CSV Final — Columnas

```csv
indicator_id,domain,indicator_name,value,score,source,notes
```

## HTML Radar — Specs

Ver `references/template-radar.html` para ejemplo completo. Specs clave:
- Container 900px, radar SVG izquierda + lista dominios derecha
- Tipografía: Crimson Pro (títulos) + Barlow (body) via Google Fonts
- Paleta: primary #1a1f2e, accent #2d3a52, danger #8b3a3a
- SVG 420×400, centro (210,200), radio 150px, 7 ejes a 51.43°
- Cuello de botella: círculo doble rojo
- Coordenadas: ángulo = -90° + (i × 51.43°), radio = (score/100) × 150

---

## Recursos

| Recurso | Path | Cuándo leer |
|---------|------|-------------|
| Rúbrica de scoring | `references/rubrica-scoring.md` | Paso 1, antes de asignar scores |
| Template de reporte | `references/reporte-template.md` | Paso 2, antes de redactar |
| Template radar HTML | `references/template-radar.html` | Paso 2, al generar visualización |
| Metodología ANDE (canónica) | `drive/METODOLOGIA_EN.md` | Paso 2, secciones 2,3,5,6,7 |
| Terminología ES | `drive/METODOLOGIA_ES.md` | Paso 2, solo si el reporte es en español |
| Base de conocimiento | `knowledge/INDEX.md` → `knowledge/papers/` | Paso 2, recomendaciones (mín. 3 con respaldo) |
| Humanizador ES | `guides/editor-humano.md` | Paso 2, post-redacción |
| Humanizador EN | `guides/humanizer.md` | Paso 2, si output en inglés |
| Knowledge base | `knowledge/INDEX.md` | Paso 2, para enriquecer análisis |

---

## Checklist Pre-Entrega

### Contenido (Pasos 1-2)
- [ ] 8 secciones completas
- [ ] Resumen ejecutivo: 4 párrafos, sin bullets, con footnotes
- [ ] Tabla de evaluación con semáforos correctos
- [ ] Score ajustado por cuello de botella reportado (y explicado si la brecha >8)
- [ ] Rango de incertidumbre: score sin estimados + % de indicadores estimados
- [ ] Madurez validada contra los 4 marcadores estructurales (divergencia reportada si existe)
- [ ] Patrón Condición-Resultado identificado y explicado
- [ ] 7 análisis de dominio: 1 párrafo estratégico cada uno (120-180 palabras)
- [ ] Contexto local: actores, programas y startups mencionados por nombre en el análisis
- [ ] Tabla de actores con 5 tipos
- [ ] 4 fortalezas con títulos específicos al ecosistema
- [ ] 4 retos con títulos que nombren el problema
- [ ] 6-8 recomendaciones verificadas contra Tabla 4.3, conectadas con actores locales
- [ ] Mínimo 3 recomendaciones con respaldo de knowledge/ (autor + año, INS-# si aplica)
- [ ] Tabla de 30 indicadores en sección 8

### Fuentes consultadas
- [ ] references/rubrica-scoring.md (Paso 1)
- [ ] references/reporte-template.md (Paso 2)
- [ ] references/template-radar.html (Paso 2)
- [ ] drive/METODOLOGIA_EN.md (Secciones 2,3,5,6,7)
- [ ] knowledge/INDEX.md + papers — mínimo 3 recomendaciones respaldadas, citadas con autor + año
- [ ] guides/editor-humano.md o humanizer.md (humanización)

### Estilo
- [ ] Sin bullets en prosa narrativa
- [ ] Sin patrones AI (ver guía de humanización)
- [ ] Terminología ANDE (PEC no SGBs, Organizaciones de Apoyo no ESOs)
- [ ] Datos con fuentes
- [ ] Footnotes consolidados (una fuente = un número)
- [ ] Sin conclusiones genéricas
