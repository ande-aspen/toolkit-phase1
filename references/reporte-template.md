# Template del Reporte de Diagnóstico — Fase 1

Este archivo define la estructura, contenido y proceso de redacción para cada sección del reporte. Consultar este archivo durante el Paso 2 (Análisis y Reporte).

---

## Estructura General (8 Secciones)

```
1. Resumen Ejecutivo
2. Situación General y Madurez del Ecosistema
3. Análisis de los Dominios y Radar de Madurez
4. Actores del Ecosistema
5. Fortalezas
6. Retos
7. Recomendaciones y Siguientes Pasos
8. Referencias
```

---

## Header + Metadata

```markdown
# Diagnóstico del Ecosistema Emprendedor
## [Ciudad], [Estado/Provincia], [País]

| | |
|---|---|
| **Fecha** | [Mes Año] |
| **Metodología** | ANDE Ecosystem Diagnostic Toolkit – Fase 1 (Segunda Edición, 2025) |
| **Nivel de madurez** | [Naciente | Emergente | En Desarrollo | Autosostenible] |
| **Score global** | [XX]/100 |
| **Población de referencia** | [X.X millones] ([Zona Metropolitana | Ciudad | Región]) |
```

---

## Sección 1: Resumen Ejecutivo

### Qué es
Síntesis del diagnóstico completo en 3-4 párrafos (~400 palabras). El lector que solo lea esta sección debe entender el estado del ecosistema, su principal restricción y qué hacer al respecto.

### Fuente de información
- Datos del input de indicadores (Paso 1)
- Scores calculados y nivel de madurez

### Estructura (4 párrafos, prosa continua, sin bullets ni tablas)

**Párrafo 1 — Posicionamiento.** Qué es este ecosistema, cuál es su contexto económico, qué activos distintivos tiene. Incluir población de referencia y score global. Footnote a fuente de contexto.

**Párrafo 2 — Restricción principal.** Cuál es el cuello de botella, qué score tiene, qué implicaciones tiene para el ecosistema. No solo nombrar el dominio débil sino explicar POR QUÉ limita al sistema. Footnote a ANDE (metodología).

**Párrafo 3 — Dominios mejor y peor desarrollados.** Rango de scores (del más alto al más bajo). Mencionar los 2 dominios más fuertes y el segundo más débil. No listar los 7.

**Párrafo 4 — Nivel de madurez y dirección.** Clasificación de madurez, qué significa para las intervenciones (referir a la secuencia evolutiva de ANDE), y una oración sobre el horizonte de acción. Footnote a ANDE.

### Qué NO hacer
- No usar bullets ni listas
- No repetir datos que se detallarán en secciones posteriores
- No usar frases como "en un mundo cada vez más" o "es importante destacar que"
- No describir la metodología (eso va en Referencias)

---

## Sección 2: Situación General y Madurez del Ecosistema

### Qué es
Contextualización del ecosistema y justificación del nivel de madurez asignado. Esta sección responde: ¿en qué etapa está este ecosistema y por qué?

### Fuentes de información
- **Primaria:** Datos del input de indicadores (Paso 1) + scores calculados
- **Consultar:** `drive/METODOLOGIA_ES.md` — buscar: niveles de madurez, generaciones (Cukier & Kon), patrón Condición vs Resultado, secuencia evolutiva

### Estructura

**Tabla de evaluación por dominio:**

```markdown
## Evaluación por Dominio

| Dominio | Score | Estado | Observaciones |
|---------|-------|--------|---------------|
| Política y Regulación | XX | 🟢🟡🔴 [Estado] | [Frase corta, máximo 10 palabras, sin punto final] |
| Financiamiento | XX | ... | ... |
| Cultura | XX | ... | ... |
| Servicios de Apoyo | XX | ... | ... |
| Capital Humano | XX | ... | ... |
| Mercados | XX | ... | ... |
| I+D e Innovación | XX | ... | ... |

**Semáforo:** 🟢 ≥60 Bien desarrollado | 🟡 40-59 En desarrollo | 🔴 <40 Atención prioritaria
```

**Estados según score:**
- 🟢 ≥60: "Bien desarrollado"
- 🟡 40-59: "En desarrollo"
- 🔴 <40 + es el más bajo: "Cuello de botella"
- 🔴 <40 + no es el más bajo: "Atención prioritaria"

**Después de la tabla, 3 párrafos con headers en negrita:**

**Nivel de madurez.** Clasificación (Naciente/Emergente/En Desarrollo/Autosostenible), justificación basada en las características observadas, y referencia al concepto de generaciones de Cukier & Kon. ¿Hay evidencia de emprendedores exitosos reinvirtiendo en el ecosistema (Generación 2+)? Si no, ¿en qué generación está? Footnote a ANDE metodología.

**Patrón Condición-Resultado.** Calcular el promedio de dominios Condición (Política, Servicios, Capital Humano, I+D) y el promedio de dominios Resultado (Financiamiento, Cultura, Mercados). Clasificar en uno de los 4 patrones:

| Patrón | Diagnóstico | Implicación |
|--------|-------------|-------------|
| Condiciones altas + Resultados altos | Ecosistema efectivo | Mantener y escalar |
| Condiciones altas + Resultados bajos | Problema de conexión | Los recursos existen pero no se conectan con los emprendedores |
| Condiciones bajas + Resultados altos | Sistema frágil | Resultados dependen de pocos actores, no del sistema |
| Condiciones bajas + Resultados bajos | Ecosistema incipiente | Construir desde las bases |

Explicar qué significa este patrón para el ecosistema específico. Footnote a ANDE.

**Restricción principal.** Identificar el cuello de botella (dominio con score más bajo). Explicar por qué este dominio limita al ecosistema usando la lógica sistémica de ANDE: "las debilidades en un dominio pueden neutralizar las fortalezas en otros." Si la diferencia con el segundo más bajo es <5 puntos, mencionar ambos como críticos. Referir a la secuencia evolutiva para indicar si el cuello de botella corresponde a la etapa actual o es prematuro. Footnote a ANDE.

### Qué NO hacer
- No explicar la metodología ANDE (eso va en Referencias)
- No usar la tabla para rellenar espacio; las observaciones deben ser informativas
- No confundir "cuello de botella" con "dominio que debe atenderse primero" (la secuencia evolutiva determina prioridades, no solo el score)

---

## Sección 3: Análisis de los Dominios y Radar de Madurez

### Qué es
Análisis cualitativo y estratégico de cada dominio. NO es una descripción del score ni un listado de lo que se encontró. Es una interpretación de lo que el estado del dominio significa para el ecosistema.

### Fuentes de información
- **Primaria:** Datos del input de indicadores (Paso 1)
- **Consultar:** `drive/METODOLOGIA_ES.md` — buscar: descripción de cada dominio, marco Condición-Resultado, secuencia evolutiva, intervenciones por madurez (Tabla 4.3)
- **Consultar (selectivamente):** `drive/REF_*.pdf` del proyecto cuando un dominio requiera contexto adicional. Por ejemplo:
  - Financiamiento → buscar en REFs sobre inversión, venture capital en LATAM
  - Servicios de Apoyo → buscar en REFs sobre aceleradoras, BDS, ESOs
  - Cultura → buscar en REFs sobre comunidades emprendedoras
  - Capital Humano → buscar en REFs sobre talento, educación
  - No es obligatorio consultar REFs para cada dominio; solo cuando el análisis se beneficie de contexto adicional.

### Estructura

Referencia al radar: `*Ver archivo HTML adjunto: [ciudad]_[pais] - radar.html*`

Por cada dominio: **H3 con nombre + score + emoji semáforo**

```markdown
### Política y Regulación · Score: XX 🟡
```

**Un solo párrafo por dominio (120-180 palabras).** El párrafo debe:

1. **Abrir con una afirmación estratégica** sobre el estado del dominio (no con el score). Ejemplo bueno: "El marco regulatorio facilita la creación de empresas pero carece de incentivos específicos para startups de base tecnológica." Ejemplo malo: "Política y Regulación obtuvo un score de 55, lo cual indica un nivel en desarrollo."

2. **Incluir 2-3 datos concretos** que sustenten la afirmación (cifras, actores, programas encontrados). Los datos son evidencia, no el protagonista del párrafo.

3. **Cerrar con la implicación estratégica:** qué significa este nivel para el ecosistema, qué limita, qué habilita. Conectar con el marco Condición-Resultado cuando sea relevante.

### Ejemplo de buen análisis vs. mal análisis

**MAL (descriptivo):**
> "Financiamiento obtuvo un score de 28. Se identificaron 2 fondos de VC con presencia regional y no se encontraron redes de ángeles activas. La inversión total en 3 años fue de USD 3.2M en 4 rondas documentadas. No se registraron exits en el período analizado."

**BIEN (estratégico):**
> "El acceso a capital representa la restricción más severa del ecosistema. Con USD 3.2M invertidos en tres años y solo 4 rondas documentadas, la actividad de inversión no alcanza la masa crítica necesaria para generar señales de mercado que atraigan a nuevos inversionistas. La ausencia de una red de ángeles locales agrava el problema: los emprendedores en etapa temprana dependen de capital propio o de programas públicos que no están diseñados para startups de base tecnológica. Sin exits que demuestren retornos, el ciclo de reinversión que caracteriza a los ecosistemas maduros no puede activarse."

### Qué NO hacer
- No abrir con el score ("El dominio X obtuvo un score de...")
- No hacer listas de actores o programas (eso va en Sección 4)
- No repetir la observación de la tabla de evaluación
- No usar dos párrafos (uno descriptivo + uno analítico); fusionar en un solo párrafo estratégico
- No usar frases genéricas como "se requieren esfuerzos adicionales" o "existe un área de oportunidad"

---

## Sección 4: Actores del Ecosistema

### Qué es
Mapa de los actores identificados durante la investigación, clasificados por tipo según la taxonomía ANDE.

### Fuente de información
- Datos del input de indicadores (Paso 1)

### Estructura

```markdown
## Actores del Ecosistema

| Tipo | Actores Identificados |
|------|----------------------|
| **Gobierno** | [Lista separada por punto y coma] |
| **Academia** | [Lista separada por punto y coma] |
| **Organizaciones de Apoyo** | [Lista separada por punto y coma] |
| **Sector Privado** | [Lista separada por punto y coma] |
| **Proveedores de Capital** | [Lista separada por punto y coma] |
```

### Reglas
- Solo incluir actores confirmados como activos (ver criterios de vigencia en CLAUDE.md, sección Criterios de Vigencia)
- Marcar con `(?)` los actores cuya vigencia no se pudo confirmar
- Un actor puede aparecer en más de un tipo si cumple múltiples roles (ej: una universidad que opera incubadora aparece en Academia y en Organizaciones de Apoyo)
- Si un tipo no tiene actores identificados, poner "No identificados" y no inventar

### Párrafo de contexto (después de la tabla)
Un párrafo breve (60-80 palabras) señalando patrones notables: ¿hay concentración excesiva en algún tipo? ¿hay vacíos evidentes? ¿algún actor cumple roles múltiples que lo hacen crítico para el sistema?

---

## Sección 5: Fortalezas

### Qué es
Las 4 fortalezas más relevantes del ecosistema. No son simplemente "los dominios con score alto" sino ventajas competitivas, activos distintivos o condiciones favorables que diferencian a este ecosistema.

### Fuentes de información
- **Primaria:** Datos de investigación + scores
- **Consultar:** `drive/METODOLOGIA_ES.md` — buscar: características de ecosistemas consolidados, factores comunes de éxito, concepto de condiciones framework vs sistémicas
- **Consultar:** `drive/REF_*.pdf` relevantes para contextualizar la fortaleza (ej: si la fortaleza es una red de mentores fuerte, buscar en `ref_Mentors_Final.pdf` para dar contexto de por qué importa)

### Estructura

4 fortalezas. Cada una:

```markdown
### [Título específico y descriptivo]

[Párrafo de 80-120 palabras + footnote]
```

### Cómo identificar fortalezas (no solo mirar scores altos)

Buscar estos patrones:
1. **Activos únicos:** ¿Hay algo que este ecosistema tiene que otros comparables no? (universidad de investigación, industria ancla, programa público innovador)
2. **Dominios Condición fuertes:** Si Política, Servicios, Capital Humano o I+D tienen scores altos, son la base sobre la que se puede construir
3. **Tendencias positivas:** ¿Hay evidencia de crecimiento reciente en algún indicador? (nuevas aceleradoras, primer fondo local, aumento de eventos)
4. **Conectividad:** ¿Hay actores que conectan dominios? (ej: universidad que opera incubadora, conectando Capital Humano con Servicios de Apoyo)

### Reglas para títulos
- Específicos, no genéricos
- BIEN: "Red universitaria con 5 incubadoras activas y programas de transferencia tecnológica"
- MAL: "Buena infraestructura educativa"
- BIEN: "Programa estatal de capital semilla con cobertura a startups tech"
- MAL: "Apoyo gubernamental"

### Qué NO hacer
- No usar títulos genéricos aplicables a cualquier ecosistema
- No inventar fortalezas que no estén respaldadas por datos de la investigación
- No confundir "no está mal" con "es una fortaleza"

---

## Sección 6: Retos

### Qué es
Los 4 retos más importantes del ecosistema. No son simplemente "los dominios con score bajo" sino brechas, limitaciones estructurales o dinámicas problemáticas que impiden el desarrollo del ecosistema.

### Fuentes de información
- **Primaria:** Datos de investigación + scores + cuello de botella identificado
- **Consultar:** `drive/METODOLOGIA_ES.md` — buscar: concepto de cuello de botella, restricción principal, secuencia evolutiva (¿el reto corresponde a la etapa actual?), patrón Condición-Resultado
- **Consultar:** `drive/REF_*.pdf` relevantes para dimensionar el reto (ej: si el reto es falta de financiamiento, buscar en REFs sobre inversión en LATAM para dar escala comparativa)

### Estructura

4 retos. Cada uno:

```markdown
### [Título que describe el PROBLEMA, no la solución]

[Párrafo de 80-120 palabras + footnote]
```

### Cómo identificar retos (no solo mirar scores bajos)

Buscar estos patrones:
1. **El cuello de botella y sus implicaciones:** El dominio más bajo siempre genera un reto, pero el reto no es "score bajo" sino lo que ese score bajo causa en el sistema
2. **Desconexiones Condición-Resultado:** Si las condiciones son buenas pero los resultados son malos, hay un problema de conexión que es un reto en sí mismo
3. **Dependencias frágiles:** ¿El ecosistema depende de un solo actor, un solo programa, o una sola fuente de financiamiento?
4. **Brechas en la secuencia evolutiva:** Si el ecosistema es Emergente pero carece de lo que debería construirse en esa etapa (ej: cultura y comunidad), eso es un reto crítico

### Reglas para títulos
- Nombrar el PROBLEMA, no la solución
- BIEN: "Ausencia de capital de riesgo local para etapas tempranas"
- MAL: "Necesidad de atraer inversionistas"
- BIEN: "Ecosistema dependiente de una sola universidad como articulador"
- MAL: "Diversificar actores del ecosistema"

### Qué NO hacer
- No repetir lo dicho en el análisis de dominios con diferentes palabras
- No presentar retos genéricos ("falta de financiamiento") sin explicar la implicación local
- No confundir "score bajo" con "reto"; el reto es lo que el score bajo causa

---

## Sección 7: Recomendaciones y Siguientes Pasos

### Qué es
6-8 recomendaciones accionables, diferenciadas por prioridad y alineadas con el nivel de madurez del ecosistema.

### Fuentes de información
- **Primaria:** Cuello de botella, nivel de madurez, brechas identificadas
- **Consultar (OBLIGATORIO):** `drive/METODOLOGIA_ES.md` — buscar: Capítulo 5 (intervenciones por actor y madurez), Tabla 4.3 (acciones por dominio y madurez), Tabla 5.1+ (rol de cada actor por madurez), concepto de "claridad en la acción", "prioridad en la restricción principal", "viabilidad de implementación"
- **Consultar (OBLIGATORIO):** `drive/REF_*.pdf` del proyecto para respaldar recomendaciones con evidencia y buenas prácticas. Buscar casos, datos de impacto, lecciones aprendidas que fundamenten la recomendación. Ejemplos:
  - Para recomendaciones sobre servicios de apoyo → `REF_report-fulfilling-the-potential-of-bds.pdf`, `ref_Business_Services_FINAL.pdf`, `REF_GALI_Knowledge_Synthesis_English.pdf`
  - Para recomendaciones sobre financiamiento → REFs sobre inversión, LAVCA, venture capital
  - Para recomendaciones sobre cultura → `ref_eEcosystems_Four_Decades_Final.pdf`, `refEMovements_FINAL.pdf`
  - Para recomendaciones sobre política → `REF_david.pdf`, toolkit de política OECD

### Filtro de la Tabla 4.3

ANTES de redactar recomendaciones, consultar la Tabla 4.3 (Intervenciones por Madurez) y verificar que cada recomendación sea coherente con el nivel del ecosistema:

| Dominio | Naciente | Emergente | En Desarrollo | Autosostenible |
|---------|----------|-----------|---------------|----------------|
| Cultura | Construir | Fortalecer | Mantener | Mantener |
| Capital Humano | Construir | Fortalecer | Escalar | Mantener |
| Servicios Apoyo | Construir | Fortalecer | Escalar | Mantener |
| Política | Esperar | Construir | Fortalecer | Mantener |
| Financiamiento | Esperar | Construir | Fortalecer | Escalar |
| Mercados | Esperar | Esperar | Fortalecer | Escalar |
| I+D | Esperar | Esperar | Construir | Fortalecer |

**Regla de coherencia:** Si la tabla dice "Esperar" para un dominio en el nivel de madurez del ecosistema, NO hacer una recomendación principal para ese dominio. Puede mencionarse como "siguiente paso a futuro" pero no como prioridad Alta.

**Excepción:** Si un dominio marcado como "Esperar" tiene un score crítico (<20) que está causando fuga de talento o bloqueo sistémico evidente, se puede incluir como recomendación con justificación explícita de por qué se desvía de la secuencia estándar.

### Estructura

Distribución: 3 Alta, 3 Media, 1-2 Baja prioridad.

```markdown
### 1. [Nombre de la recomendación — verbo de acción + objeto]
**Prioridad: [Alta|Media|Baja]** · Dominio: [Dominio] · Status: [🆕 Nueva | 🔄 Fortalecer existente]

[Párrafo de fundamentación: qué problema ataca, por qué es prioritaria, qué evidencia la respalda. Incluir al menos un dato o referencia de los REFs del proyecto o de la metodología ANDE. 80-120 palabras. Footnote.]

- **Acción sugerida:** [Específica y medible — no "mejorar el financiamiento" sino "diseñar un programa de preparación para inversión de 12 semanas para 15 startups por cohorte"]
- **Actores posibles:** [Actor] ([rol]), [Actor] ([rol])
- **Alcance esperado:** [Métrica cuantificable + horizonte temporal]
```

### Prioridades:
- **Alta** (0-12 meses): Ataca directamente el cuello de botella o una brecha crítica. Actores y recursos identificables.
- **Media** (12-24 meses): Fortalece dominios en desarrollo o prepara condiciones para el siguiente nivel de madurez.
- **Baja** (24-36 meses): Intervenciones de escala o preparatorias para etapas futuras.

### Test de calidad para cada recomendación

Antes de incluir una recomendación, verificar:
1. **¿Es accionable?** ¿Alguien puede empezar a implementarla mañana? Si no, hacerla más concreta.
2. **¿Quién la lidera?** Si no se puede identificar un actor posible, probablemente es demasiado abstracta.
3. **¿Es coherente con la madurez?** Verificar contra Tabla 4.3.
4. **¿Está respaldada?** ¿Hay evidencia de que esto funciona en contextos similares? Citar REFs.
5. **¿Complementa o duplica?** Verificar que no recomiende crear algo que ya existe.

### Cierre: Siguientes Pasos

Después de las recomendaciones, un párrafo breve (60-80 palabras):
- Mencionar que este diagnóstico es Fase 1 (datos públicos)
- Recomendar Fase 2 (entrevistas a actores clave) para validar hallazgos
- Indicar que las recomendaciones deben priorizarse colectivamente con los actores del ecosistema

### Qué NO hacer
- No recomendar "atraer inversión" a un ecosistema Naciente (la secuencia dice Esperar)
- No hacer recomendaciones genéricas sin actor ni métrica
- No basar recomendaciones solo en el criterio de Claude; fundamentar con ANDE + REFs
- No repetir los retos con otras palabras; las recomendaciones son SOLUCIONES a los retos

---

## Sección 8: Referencias

### Qué es
Tabla detallada de los 30 indicadores + footnotes consolidados + créditos metodológicos.

### Estructura

**Tabla de indicadores por dominio:**

```markdown
## Metodología y Datos

### Política y Regulación

| ID | Indicador | Valor | Score | Fuente |
|----|-----------|-------|-------|--------|
| P1 | Días para constituir empresa | 8.5 días | 75 | OECD B-READY 2024 |
| P2 | ... | ... | ... | ... |

### Financiamiento
[Repetir formato por cada dominio]

### Score total del ecosistema: XX/100 · Nivel: [Naciente/Emergente/En Desarrollo/Autosostenible]
```

**Nota sobre datos:**
```markdown
> **Nota metodológica:** Los valores marcados con (est.) son estimaciones basadas en datos nacionales o regionales proporcionalizados. Los valores marcados con (?) no pudieron verificarse con fuentes recientes. Este diagnóstico se basa en la metodología ANDE Ecosystem Diagnostic Toolkit, Fase 1 (Segunda Edición, 2025).
```

**Siguiente paso:**
```markdown
> **Siguiente paso:** Complementar con Fase 2 del diagnóstico (entrevistas a actores clave) para validar hallazgos cuantitativos y capturar dinámicas no observables con datos públicos.
```

**Footnotes consolidados:**

```markdown
---

## Referencias

¹ ANDE (2025). *Modelo para el Diagnóstico de Ecosistemas de Emprendimiento*, Segunda Edición.
² [Fuente 2]
³ [Fuente 3]
...

---

<div align="center">

**ANDE**
Aspen Network of Development Entrepreneurs

*Diagnóstico elaborado siguiendo la metodología ANDE Ecosystem Diagnostic Toolkit, Fase 1 (Segunda Edición, 2025).*

</div>
```

### Reglas de footnotes
- Cada fuente aparece UNA sola vez con un número único
- Si ANDE se cita 10 veces en el cuerpo, todas llevan ¹
- Formato: `Autor (Año). *Título*. Organización/URL.`
- Los REFs del proyecto consultados durante el análisis y recomendaciones DEBEN aparecer aquí

---

## Estilo de Escritura (aplica a todas las secciones)

### Patrones prohibidos

| Patrón | Ejemplo malo | Corrección |
|--------|-------------|------------|
| Em dashes | "La ciudad — con su infraestructura — destaca" | Usar comas o punto y seguido |
| "No es X, sino Y" | "No es falta de recursos, sino de conexión" | "El problema radica en la conexión, no en los recursos" |
| Oraciones punchy | "Corto. Directo. Impactante." | Ritmo natural con variación |
| Frases hechas AI | "En un mundo cada vez más..." | Ir directo al punto |
| Inflación de significado | "representa una transformación sin precedentes" | Describir lo que realmente es |
| Muletillas | "cabe destacar", "es importante señalar", "vale la pena mencionar" | Eliminar y decir directamente |
| Conclusiones genéricas | "con el esfuerzo conjunto de todos los actores, el ecosistema podrá alcanzar su potencial" | Ser específico sobre qué actores y qué acciones |

### Terminología ANDE

| Usar | Evitar |
|------|--------|
| Pequeñas Empresas en Crecimiento (PEC) | SGBs, scaleups, PyMEs |
| Ecosistema de emprendimiento | "Ecosistema emprendedor" es aceptable |
| Organizaciones de Apoyo | Intermediarios, ESOs |
| Proveedores de Capital | Inversores (solo como especificación) |

### Voz y tono
- Institucional pero accesible
- Orientado a acción y decisiones
- Basado en evidencia
- Honesto sobre limitaciones y datos faltantes
- Sin lenguaje promocional ni optimismo forzado

### Gramática
- Artículos completos: "representa una oportunidad" (no "representa oportunidad")
- Evitar gerundios excesivos
- Preferir voz activa
- Oraciones 15-25 palabras promedio
- Sin bullets en prosa narrativa

---

## Checklist Pre-Entrega

### Contenido
- [ ] 8 secciones completas
- [ ] Resumen ejecutivo: 4 párrafos, sin bullets, con footnotes
- [ ] Tabla de evaluación con semáforos correctos
- [ ] Patrón Condición-Resultado identificado y explicado
- [ ] 7 análisis de dominio: 1 párrafo estratégico cada uno, NO descriptivo
- [ ] Tabla de actores completa con 5 tipos
- [ ] 4 fortalezas con títulos específicos y footnotes
- [ ] 4 retos con títulos que nombren el problema, no la solución
- [ ] 6-8 recomendaciones verificadas contra Tabla 4.3
- [ ] Recomendaciones con fundamentación de ANDE + REFs del proyecto
- [ ] Tabla de 30 indicadores en sección 8 con columna de Score

### Fuentes consultadas
- [ ] `drive/METODOLOGIA_ES.md` consultada para: madurez, Condición-Resultado, secuencia evolutiva, Tabla 4.3
- [ ] Texto del reporte pasado por guía de humanización (guides/editor-humano.md para ES / guides/humanizer.md para EN)
- [ ] `drive/REF_*.pdf` consultados para: al menos 3 recomendaciones tienen respaldo de REFs

### Formato
- [ ] Sin bullets en prosa narrativa
- [ ] Footnotes consolidados (una fuente = un número)
- [ ] Emojis semáforo correctos
- [ ] Títulos de fortalezas y retos son específicos

### Estilo
- [ ] Sin patrones AI prohibidos
- [ ] Terminología ANDE
- [ ] Datos con fuentes
- [ ] Sin conclusiones genéricas tipo "el futuro es prometedor"
