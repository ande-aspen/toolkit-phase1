# Paso 0 — Workflow de Research Automatizado

Este documento detalla el procedimiento para que Claude ejecute research automatizado de un ecosistema emprendedor usando WebSearch.

---

## Clasificación de Indicadores

| Tipo | Indicadores | Acción en Paso 0 |
|------|------------|------------------|
| **Nacional** (archivo de país) | P1, P2, H5, C5 | Pre-llenar de `references/countries/[pais].md`. NO investigar. |
| **Estimación** | S5 | Usar default del archivo de país. Marcar `(est.)`. |
| **Ciudad** (research web) | Los 25 restantes | Investigar en 8 rondas de búsqueda web. |

Si no existe archivo de país → agregar Ronda 0 para investigar indicadores nacionales y crear el archivo como subproducto.

---

## Fase 0A: Setup (sin búsquedas)

1. Recibir metadata: ciudad, estado/provincia, país, población de referencia
2. Determinar idioma (español por defecto)
3. Capturar contexto del usuario (si lo proporcionó):
   - Organizaciones, programas, fondos, startups que conoce del ecosistema
   - Datos puntuales → incorporar directamente con fuente "Usuario / contexto local"
   - Pistas de búsqueda → agregar como queries específicas en rondas relevantes
4. Buscar documento complementario en `input/`:
   - Patrones de búsqueda: `[ciudad].pdf`, `[ciudad].md`, `[ciudad].txt`, `[ciudad].docx`
     (case-insensitive, con o sin acentos, ej: `hermosillo.pdf` o `Hermosillo.pdf`)
   - Si existe → leerlo completo, extraer todos los datos/indicadores que contenga
   - Marcar qué indicadores ya están cubiertos por el documento
   - Estos datos tienen prioridad sobre web search
   - El web search se enfoca en los gaps (indicadores no cubiertos o parcialmente cubiertos)
5. Cargar `references/countries/[pais].md`:
   - Si existe → extraer P1, P2, H5, C5, S5 default
   - Si no existe → marcar que se necesita Ronda 0
6. **Modo individual:** Confirmar con usuario antes de investigar
7. **Modo batch:** No confirmar — proceder directamente. El archivo de país se carga UNA VEZ para todas las ciudades del mismo país

### Prioridad de fuentes de datos

Cuando hay datos de múltiples fuentes para el mismo indicador:

```
1. Documento complementario del usuario (mayor confianza — datos verificados localmente)
2. Contexto dado por el usuario en chat
3. Web search — fuentes autoritativas (OECD, INEGI, portales gobierno)
4. Web search — prensa y reportes
5. Archivo de país (indicadores nacionales)
6. Estimación por prorrateo (menor confianza)
```

---

## Fase 0B: Research Web (8 rondas)

**Nota:** Si hay documento complementario, revisar antes de cada ronda qué indicadores ya están cubiertos. Enfocar las búsquedas en los gaps y en profundizar los datos del usuario (buscar las organizaciones que mencionó, verificar vigencia, encontrar datos adicionales).

### Ronda 0 (solo si NO existe archivo de país)

**Cubre:** P1, P2, H5, C5

Queries:
```
"[pais] days incorporate business company registration [year]"
"[pais] tax regime startups fiscal incentives entrepreneurship"
"[pais] internet access percentage population"
"[pais] social trust entrepreneurship perception GEM"
```

Al terminar: crear `references/countries/[pais].md` con los datos encontrados.

---

### Ronda 1: Ecosistema + Inversión

**Cubre:** F1, F2, F3, F4, F5, M1, M3 (+ lente de género en M1)

Queries:
```
"[ciudad] startup ecosystem investment venture capital [year]"
"[ciudad] startups funding rounds exits [year]"
"[ciudad] ecosistema emprendedor inversión startups [year]"
"[ciudad] mujeres emprendedoras startups women founders"
```

**Qué extraer:**
- F1: Monto total de inversión documentado (sumar rondas mencionadas)
- F2: Número de rondas por año
- F3: Nombres de VCs con presencia (oficina, GP residente, o inversiones locales)
- F4: Redes de ángeles, individuos con deals documentados
- F5: Exits (adquisiciones, IPOs) con nombre, comprador, año
- M1: Conteo de startups activas mencionadas
- M3: Sectores donde hay concentración (3+ startups)
- Lente de género: startups lideradas por mujeres identificadas por nombre → notes de M1.
  No cambia el score; alimenta la sección de Actores y el párrafo de contexto del reporte.

**Indicadores difíciles:**
- F1-F5 suelen estar detrás de paywalls (Crunchbase, PitchBook, LAVCA). Los resultados web capturan principalmente las rondas más grandes que fueron cubiertas por prensa. Marcar como `(est.)` y notar que probablemente está subestimado.
- F4: Los ángeles rara vez son públicos. Buscar redes formales por nombre.

---

### Ronda 2: Infraestructura de Apoyo

**Cubre:** S1, S2, S3, parcial S4

Queries:
```
"[ciudad] accelerators incubators startups programs"
"[ciudad] aceleradoras incubadoras coworking emprendimiento"
"[ciudad] coworking spaces"
```

**Qué extraer:**
- S1: Aceleradoras con programa estructurado (cohortes, mentoría, demo day). Aplicar criterio de vigencia: ≥1 cohorte en últimos 24 meses.
- S2: Incubadoras (universitarias, gubernamentales, privadas) con operación verificada.
- S3: Espacios de coworking operativos. Coworker.com es buena fuente.
- S4 (parcial): Programas de mentoría mencionados. Completar en Ronda 4.

**Criterio de vigencia para S1/S2:**
- Activa: evidencia de cohorte o programa en últimos 24 meses
- No confirmada: marcar con `(?)`
- Inactiva: solo sitio web estático sin actualización en >12 meses → NO contar

---

### Ronda 3: Gobierno y Programas Públicos

**Cubre:** P3, F6

Queries:
```
"[estado] [ciudad] government programs entrepreneurship startups support [year]"
"[estado] programas gobierno emprendimiento apoyo startups [year]"
"[ciudad] public seed capital grants startups"
```

**Qué extraer:**
- P3: Programas gubernamentales activos (federal con presencia local + estatal + municipal). Verificar convocatorias en últimos 24 meses.
- F6: Programas de capital semilla público (NAFIN, banca de desarrollo, fondos concursables). Incluir ticket promedio si se menciona.
- Lente de género: programas públicos dirigidos a mujeres emprendedoras → notes de P3.

**Nota:** No contar INADEM (cerrado 2019). Verificar que programas federales mencionados tengan operación en la ciudad específica.

---

### Ronda 4: Educación y Talento

**Cubre:** H1, H2, H3, H4, S4

Queries:
```
"[ciudad] universities entrepreneurship programs technology"
"[ciudad] universidades emprendimiento bootcamp tecnología talento"
"[ciudad] tech talent software developers"
```

**Qué extraer:**
- H1: Universidades con: carrera de emprendimiento, incubadora universitaria, OTT, o programa formal de emprendimiento estudiantil. Listar por nombre.
- H2: Bootcamps tech (programación, data science, UX). Listar nombres y especialidad.
- H3: Graduados STEM anuales. Si solo hay dato nacional (ANUIES), prorratear por matrícula estatal vs nacional.
- H4: Talento tech. No se puede consultar LinkedIn directamente. Estimar basándose en: población de ciudad, presencia de tech corporates, reportes que mencionen pool de talento.
- S4: Mentores en plataformas (Endeavor, MicroMentor, programas de aceleradoras). Generalmente es estimación.

**Métodos de prorrateo (H3, H4):**
- H3: Graduados STEM nacionales × (matrícula universitaria estatal / matrícula nacional)
- H4: Si no hay dato directo, estimar como ~2-5% de la población económicamente activa con skills tech, ajustado por presencia de universidades y corporativos tech

---

### Ronda 5: Comunidad y Cultura

**Cubre:** C1, C2, C3, C4

Queries:
```
"[ciudad] startup community meetups events entrepreneurship"
"[ciudad] comunidad emprendedora meetups eventos startups blog podcast"
"[ciudad] startup grind techstars community"
```

**Qué extraer:**
- C1: Meetups activos (frecuencia mínimo mensual). Criterio: ≥1 evento en últimos 3 meses Y ≥3 eventos en últimos 12 meses.
- C2: Eventos anuales (conferencias, demo days, hackathons, startup weekends). Contar los de últimos 12 meses.
- C3: Medios especializados (blogs, podcasts, newsletters, YouTube). Criterio: publicación en últimos 30 días.
- C4: Comunidades online (LinkedIn, Facebook, Slack, Discord, WhatsApp). Criterio: ≥1 post/mes en últimos 3 meses.
- Evidencia local para C5: referentes visibles y casos de éxito locales (fundadores reconocidos,
  cobertura mediática de emprendedores de la ciudad, historias de exit contadas públicamente)
  → notes de C5. El score de C5 sigue siendo el dato nacional del archivo de país, pero esta
  evidencia local es la que alimenta el análisis del dominio Cultura (ver rúbrica, advertencia C5).
- Lente de género: comunidades o eventos de mujeres emprendedoras → notes de C1/C2.

**Vigencia es clave aquí.** Muchos meetups y medios aparecen en búsqueda pero están inactivos. Si no hay evidencia de actividad reciente → marcar con `(?)` o no contar.

---

### Ronda 6: I+D e Innovación

**Cubre:** I1, I2, I3

Queries:
```
"[ciudad] research centers universities patents scientific publications"
"[ciudad] centros investigación universidades patentes publicaciones científicas"
"[ciudad] innovation hub technology park R&D"
```

**Qué extraer:**
- I1: Patentes otorgadas (5 años). Si solo hay dato nacional → prorratear por participación estatal en PIB o gasto I+D. Fuentes: IMPI/WIPO.
- I2: Centros de investigación (públicos, privados, universitarios, corporativos). Listar nombres.
- I3: Publicaciones indexadas (3 años). Buscar en SCImago por institución y agregar por ciudad. Si no hay dato directo → estimar por ranking de universidades presentes.

**Prorrateo para I1:**
```
Patentes locales (est.) = Patentes nacionales × (PIB estatal / PIB nacional)
```

---

### Ronda 7: Corporativos Tech

**Cubre:** M2 (complementa M1)

Queries:
```
"[ciudad] technology companies offices corporate tech presence"
"[ciudad] empresas tecnología oficinas corporativos parque tecnológico"
```

**Qué extraer:**
- M2: Empresas tech (nacionales/multinacionales) con oficinas, centros de desarrollo, o presencia operativa. Importan porque generan talento, demanda para startups, y posibles adquirentes.
- Complementar M1 si aparecen startups adicionales.

---

### Ronda 8: Llenado de Gaps

**Cubre:** Indicadores que quedaron como "Sin dato específico"

1. Revisar los 25 indicadores de ciudad
2. Para cada uno sin dato suficiente:
   - Intentar búsqueda dirigida con query específica
   - Probar dato nacional + prorrateo
   - **Modo individual:** preguntar al usuario si tiene el dato + estimación conservadora
   - **Modo batch:** estimación conservadora automática (score 15-25), marcar y continuar
3. Marcar gaps restantes honestamente como "Sin dato específico"

---

## Fase 0C: Compilar Documento de Research

### Formato del documento

El documento debe seguir el formato exacto de los documentos existentes en `input/`. Estructura:

```markdown
# Research del Ecosistema Emprendedor de [Ciudad], [Estado], [País]

## Metadata
- Ciudad: [ciudad]
- Estado/Provincia: [estado]
- País: [país]
- Población de referencia: [X millones] ([Zona Metropolitana / Ciudad])
- Fecha de research: [fecha]
- Método: Research automatizado (Paso 0) + archivo de país
- Documento complementario: [nombre del archivo si existe, o "ninguno"]
- Contexto del usuario: [resumen breve si lo proporcionó, o "ninguno"]

---

## Dominio: Política y Regulación

| ID | Indicador | Value | Source | Notes |
|----|-----------|-------|--------|-------|
| P1 | Días para constituir empresa | [value] | [source] | [notes] |
| P2 | Régimen fiscal startups | [value] | [source] | [notes — de archivo de país] |
| P3 | Programas públicos activos | [value] | [source] | [notes] |

[1-2 párrafos de contexto narrativo con nombres de actores, programas,
tendencias específicas del ecosistema local]

---

## Dominio: Financiamiento
[misma estructura: tabla + narrativa]

## Dominio: Cultura
[misma estructura]

## Dominio: Servicios de Apoyo
[misma estructura]

## Dominio: Capital Humano
[misma estructura]

## Dominio: Mercados
[misma estructura]

## Dominio: I+D e Innovación
[misma estructura]

---

## Visión Integradora

[1-2 párrafos conectando los hallazgos entre dominios, identificando
patrones preliminares, fortalezas y retos evidentes]

---

## Notas de Calidad del Research

- Indicadores del documento complementario: [listar IDs, o "N/A"]
- Indicadores del contexto del usuario: [listar IDs, o "N/A"]
- Indicadores pre-llenados de archivo de país: P1, P2, H5, C5
- S5 estimado (no investigado): [value] (est.)
- Indicadores de web search: [listar IDs]
- Indicadores con estimación conservadora: [listar]
- Indicadores sin dato específico: [listar]
- Indicadores probablemente subestimados (F1-F5): [notar]
```

### Reglas del documento
1. Cada dominio tiene tabla de datos + 1-2 párrafos narrativos
2. Los párrafos deben incluir nombres específicos de actores, programas, startups
3. Marcar estimaciones con `(est.)` en value
4. Marcar vigencia no confirmada con `(?)` después del nombre del actor
5. Notes del archivo de país: agregar `[dato nacional]` para distinguir
6. El documento debe ser autocontenido — un lector debe poder entender el ecosistema sin consultar otras fuentes

### Guardar como
```
input/[ciudad], [pais].md
```
Ejemplo: `input/hermosillo, mexico.md`

---

## Fase 0D: Verificación y Entrega

### Checklist antes de completar Paso 0

- [ ] Documento complementario buscado en `input/` (y leído si existe)
- [ ] Contexto del usuario capturado e incorporado
- [ ] 30 indicadores tienen fila en el documento (incluyendo "Sin dato específico")
- [ ] P1, P2, H5, C5 pre-llenados del archivo de país (no re-investigados)
- [ ] S5 marcado como `(est.)` con fuente
- [ ] Todos los actores capturados por nombre en notes
- [ ] Vigencia aplicada: `(?)` en actores no confirmados
- [ ] Párrafos narrativos incluyen contexto local, no solo datos
- [ ] Documento guardado en `input/` con formato correcto
- [ ] Notas de calidad: origen de cada dato (doc complementario / usuario / web / país / estimación)
- [ ] F1-F5 flaggeados como probablemente subestimados si aplica

### Entrega

**Modo individual:**
1. Resumen: "Research completo. Documento guardado en input/[ciudad], [pais].md"
2. Tabla resumen: X/30 indicadores con dato, Y estimados, Z sin dato
3. Alertas: indicadores donde la calidad del dato es baja
4. Pregunta: "¿Quieres revisar/complementar el documento o proceder al Paso 1?"

**Modo batch:**
1. Log breve: "[ciudad]: research completo (X/30 con dato, Y estimados)"
2. Continuar automáticamente al Paso 1 sin detenerse
3. Alertas y gaps se acumulan para reporte consolidado al final del batch

---

## Tiers de Calidad de Datos

| Tier | Descripción | Marcado |
|------|------------|---------|
| **1 — Alta confianza** | Fuente autoritativa (OECD, INEGI, Ookla, portal gobierno) | Sin marca especial |
| **2 — Media confianza** | Prensa, reportes de ecosistema, blogs con cifras citadas | Citar fuente y fecha |
| **3 — Baja confianza** | Dato inferido, prorrateo nacional, síntesis de señales indirectas | Marcar `(est.)` + explicar método en notes |
| **4 — Sin dato** | Búsqueda no retornó nada accionable | Value: "Sin dato específico". Notes: listar qué se buscó |

---

## Métodos de Prorrateo (Nacional → Local)

### Por población
```
Valor local = Valor nacional × (Población metro / Población nacional)
```
Usar para: S4 (mentores), C1 (meetups aproximación gruesa)

### Por PIB estatal
```
Valor local = Valor nacional × (PIB estatal / PIB nacional)
```
Usar para: I1 (patentes), F1 (inversión como proxy)

### Por matrícula universitaria
```
Valor local = Valor nacional × (Matrícula estatal / Matrícula nacional)
```
Usar para: H3 (graduados STEM), I3 (publicaciones)

### Nota sobre prorrateo
El prorrateo es el último recurso. Siempre preferir dato directo > dato estatal > prorrateo. Marcar todo prorrateo con `(est.)` y explicar método en notes.
