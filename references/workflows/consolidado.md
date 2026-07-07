# Reporte Consolidado Multi-Ciudad

## Descripción
Genera un documento consolidado que integra múltiples diagnósticos de ecosistema en un reporte único con panorama comparativo, perfiles individuales por ciudad y metodología compartida. Diseñado para producir reportes regionales como "Ecosistemas de emprendimiento en México: Diagnóstico de 10 Ciudades." Reutilizable para cualquier agrupación regional o temática de ecosistemas diagnosticados.

## Cuándo se usa
- El usuario pide consolidar, integrar o unificar diagnósticos existentes
- El usuario pide un reporte multi-ciudad o regional

## Inputs
- **Obligatorio:** descriptor del reporte (ej: "México 10 ciudades", "Sri Lanka", "Norte de México")
- **Opcional:** lista explícita de ciudades a incluir
- **Opcional:** título personalizado del documento
- **Opcional:** orden de ciudades (default: alfabético)
- **Opcional:** idioma (default: español)

## Parámetros
- **titulo:** string — título completo del documento
- **descriptor:** string — identificador corto para nombres de archivo (ej: "mexico_10ciudades")
- **ciudades:** list — lista ordenada de ciudades a incluir
- **pais:** string — país para cargar `references/countries/[pais].md`
- **idioma:** "es" | "en" (default: "es")

---

## Proceso

```
FASE 0 — INVENTARIO Y CONFIGURACIÓN (1 pase):

1. Escanear output/ buscando diagnósticos disponibles:
   a. Patrón estándar: output/[ciudad]_[pais] - phase1.md
   b. Patrón alternativo: output/[ciudad], [pais].md (sin "- phase1")
   c. Para cada ciudad, buscar primero (a), si no existe buscar (b)

2. Escanear CSVs de indicadores:
   a. Patrón: output/[ciudad]_[pais] - indicators.csv
   b. Si una ciudad no tiene CSV → extraer scores de la tabla de evaluación
      dentro del markdown (Sección 2, tabla de "Evaluación por Dominio")

3. Presentar al usuario:
   - Lista de ciudades encontradas
   - Título propuesto
   - Orden propuesto (alfabético por default)
   - Esperar confirmación o ajustes

4. Leer guides/editor-humano.md (o guides/humanizer.md si idioma = "en")

5. Establecer convención de nombres de archivo:
   consolidado_[descriptor] - [componente].md


FASE 1 — CAPÍTULO 1: INTRODUCCIÓN (1 pase):

1. Leer drive/METODOLOGIA_EN.md (canónica, V3.7) para contexto general
2. Leer references/countries/[pais].md para datos nacionales
3. Redactar introducción:
   - Propósito del documento
   - Alcance: qué ciudades, qué periodo, qué metodología
   - Estructura del documento (mapa de lectura)
   - MÁXIMO 300-500 palabras. Breve y directa.
4. Guardar: output/consolidado_[descriptor] - ch1_introduccion.md


FASE 2 — CAPÍTULO 2: PANORAMA COMPARATIVO (1 pase):

1. Leer todos los CSVs de indicadores (~2KB cada uno)
2. Leer líneas 1-49 de cada diagnóstico (tabla inicial + resumen ejecutivo
   + inicio de situación general — ~5KB por ciudad, ~50KB total)
3. Construir matriz comparativa:

   | Ciudad | Población | Global | P | F | C | S | H | M | I | Madurez | Cuello de botella |
   |--------|-----------|--------|---|---|---|---|---|---|---|---------|-------------------|

4. Redactar 3-4 hallazgos transversales (~1,000-1,500 palabras total):
   - Cuellos de botella compartidos
   - Fortalezas regionales
   - Outliers y excepciones
   - Patrón general de madurez
5. Guardar: output/consolidado_[descriptor] - ch2_panorama.md


FASE 3 — CAPÍTULO 3: PERFILES DE CIUDAD (10 pases, 1 por ciudad):

Para cada ciudad en el orden definido:

1. Leer el diagnóstico completo (~37KB)
2. Leer el CSV de indicadores (si existe)
3. Aplicar las REGLAS DE TRANSFORMACIÓN (ver sección abajo)
4. Generar perfil condensado siguiendo la ESTRUCTURA POR CIUDAD (ver abajo)
5. Aplicar humanización según guides/editor-humano.md
6. Guardar: output/consolidado_[descriptor] - ch3_[NN]_[ciudad].md

Orden default para México: Chihuahua, Ciudad Juárez, Guadalajara,
Hermosillo, La Paz, León, Mérida, Oaxaca, San Luis Potosí, Zacatecas


FASE 4 — CAPÍTULO 4: METODOLOGÍA (1 pase):

1. Leer drive/METODOLOGIA_EN.md (canónica, V3.7)
2. Redactar:
   4.1 El modelo ANDE — Explicar el toolkit de diagnóstico.
       Incluir aquí la ÚNICA explicación completa del modelo de generaciones
       de Cukier y Kon (Generación 0, 1, 2, 3) y su relación con los
       niveles de madurez (Naciente, Emergente, En Desarrollo, Autosostenible).
       Incluir aquí la Tabla 4.3 (secuencia evolutiva: Construir/Fortalecer/
       Mantener/Esperar por dominio y nivel de madurez).
   4.2 Proceso de diagnóstico — Pasos del diagnóstico Fase 1, fuentes
       de datos, scoring.
   4.3 Alcance y limitaciones — Qué cubre y qué no, caveats metodológicos.
3. Guardar: output/consolidado_[descriptor] - ch4_metodologia.md


FASE 5 — ENSAMBLAJE FINAL (1 pase):

1. Leer todos los archivos de capítulo generados (en orden)
2. Ensamblar documento único:
   a. Título y portada
   b. Tabla de contenidos
   c. Capítulo 1
   d. Capítulo 2
   e. Capítulo 3 (todos los perfiles en orden)
   f. Capítulo 4
3. Aplicar humanización final al documento completo
4. Verificar checklist (ver sección abajo)
5. Guardar: output/consolidado_[descriptor].md ← ENTREGABLE FINAL
```

---

## Reglas de Transformación de Contenido

Estas reglas se aplican en la Fase 3 (procesamiento por ciudad). Son la diferencia entre copiar los diagnósticos y producir un documento consolidado de calidad.

### Regla 1 — Cukier y Kon

El modelo de generaciones se explica UNA VEZ en Capítulo 4.

En perfiles de ciudad:
- Usar "Generación 0", "Generación 1", "transición Generación 1-2" como clasificación directa
- NO repetir "según el modelo de Cukier y Kon" ni "el marco de Cukier y Kon"
- Máximo 1 mención nominal por ciudad, solo en el párrafo de madurez si aporta valor analítico
- Eliminar completamente de: Resumen Ejecutivo, Fortalezas, Retos, Recomendaciones

### Regla 2 — Limpieza de referencias boilerplate y repetitivas

Las siguientes referencias aparecen en casi todas las ciudades y generan redundancia masiva en un documento consolidado. Deben centralizarse o eliminarse:

| Referencia | Frecuencia original | Acción |
|---|---|---|
| ANDE Methodology | 11/11 ciudades | Explicar en Cap. 4. En perfiles: máximo 1 nota al pie. |
| Cukier y Kon | 11/11 ciudades | Ver Regla 1. |
| Latinobarómetro 18% | 10/11 ciudades | Mencionar en Cap. 2 Panorama una vez. En perfiles: usar el dato sin atribución en texto. |
| Tabla 4.3 ANDE | 10/11 (23 menciones) | Incluir tabla en Cap. 4. Eliminar referencias en perfiles. |
| "Secuencia evolutiva" | 10/11 (23 menciones) | Explicar en Cap. 4. Eliminar de perfiles. |
| "per Extracto XX" | 80 menciones en 10 ciudades | **Eliminar completamente.** |
| Macke et al. | 29 menciones en 8 ciudades | Eliminar del texto. Si es imprescindible, nota al pie. |
| GALI / Roberts et al. | 39 menciones en 9 ciudades | Eliminar del texto narrativo. |
| Guttentag et al. | 11 menciones en 5 ciudades | Eliminar del texto narrativo. |
| Isenberg (Yozma) | 6 menciones en 3 ciudades | Eliminar del texto narrativo. |

**Principio general:** El texto narrativo (resumen ejecutivo, análisis de dominios, fortalezas, retos, recomendaciones) NO incluye citas intercaladas tipo "(Autor, año)", "per Extracto XX, Autor et al.", ni "según [investigación]". Los datos y hallazgos se presentan como propios del diagnóstico. Las fuentes se citan exclusivamente en notas al pie al final de cada perfil de ciudad, de forma limpia y sin las fórmulas repetitivas.

### Regla 3 — Recomendaciones: Top 3, estratégicas

Selección:
- Elegir las 3 recomendaciones más impactantes (priorizar las de prioridad Alta)
- Si hay 2 Alta + varias Media, elegir la Media más transformadora

Reescritura:
- Un párrafo de 80-120 palabras por recomendación
- Tono: "qué necesita pasar y por qué" — NO "cómo implementar paso a paso"
- Eliminar el formato de bullets operativo (Acción sugerida / Actores posibles / Alcance esperado)
- Las recomendaciones son propias del reporte. CERO citas académicas dentro de ellas.
- Nombrar el tipo de actor relevante (organizaciones de apoyo, gobierno, academia), no el plan de implementación

### Regla 4 — Fortalezas y Retos: Top 3

Selección:
- Fortalezas: las 3 más distintivas de este ecosistema (no genéricas compartidas por todos)
- Retos: los 3 más sistémicos y estructurales (no descriptivos basados solo en scores)

Formato:
- ~60-80 palabras cada una
- Sin citas académicas intercaladas
- Títulos concretos y específicos de la ciudad

### Regla 5 — Mapeo de secciones originales al perfil consolidado

| Subsección consolidada | Fuente original | Transformación |
|---|---|---|
| Tabla inicial (header) | Líneas 1-11 del diagnóstico | Mantener tal cual |
| 1. Resumen Ejecutivo | Sección 1 original (4 párrafos) | Condensar a 2 párrafos (~200 palabras). Sin Cukier y Kon. Sin meta-refs ANDE. Datos concretos y hallazgo principal. |
| 2. Situación General y Madurez | Sección 2 original | Tabla de dominios + SOLO párrafo de nivel de madurez. Eliminar párrafos de Patrón Condición-Resultado y Restricción Principal (esa información va al Cap. 2 Panorama). |
| 3. Análisis de Dominios y Radar | Sección 3 original | Mantener los 7 dominios. Reducir cada párrafo a ~100-150 palabras (de ~150-200). Datos concretos, sin citas académicas. |
| 4. Actores del Ecosistema | Sección 4 original | Solo la tabla de actores. Eliminar el párrafo analítico posterior. |
| 5. Fortalezas | Sección 5 original (4 items) | Top 3 a ~60-80 palabras cada una. |
| 6. Retos | Sección 6 original (4 items) | Top 3 a ~60-80 palabras cada una. |
| 7. Recomendaciones | Sección 7 original (6-8 items) | Top 3 estratégicas. Un párrafo cada una. Sin bullets. Sin "Siguientes Pasos". |
| 8. Datos e Indicadores | Sección 8 original | Solo las tablas de indicadores por dominio. Eliminar texto metodológico (va a Cap. 4). Eliminar "Siguiente paso" y nota final. |
| Referencias | Notas al pie originales | Mantener locales por ciudad. Reiniciar numeración. Limpiar formato "per Extracto". |

---

## Estructura del Documento

```
# [Título del reporte]

## Tabla de Contenidos

## 1. Introducción (300-500 palabras)

## 2. Panorama Comparativo
   - Matriz comparativa (tabla ciudad × dominio × score)
   ### 2.1 Hallazgos transversales (3-4 hallazgos, 1,000-1,500 palabras)

## 3. Perfil de madurez y mapeo de indicadores por ecosistema
   ### 3.N [Ciudad]
       [Tabla inicial]
       #### 1. Resumen Ejecutivo
       #### 2. Situación General y Madurez del Ecosistema
       #### 3. Análisis de los Dominios y Radar de Madurez
       #### 4. Actores del Ecosistema
       #### 5. Fortalezas
       #### 6. Retos
       #### 7. Recomendaciones
       #### 8. Datos e Indicadores
       #### Referencias

## 4. Metodología
   ### 4.1 El modelo ANDE
   ### 4.2 Proceso de diagnóstico
   ### 4.3 Alcance y limitaciones
```

---

## Recursos

| Recurso | Path | Fase |
|---------|------|------|
| Diagnósticos | `output/*phase1.md` o `output/*, [pais].md` | 0, 2, 3 |
| CSVs indicadores | `output/*indicators.csv` | 0, 2 |
| Metodología ANDE | `drive/METODOLOGIA_EN.md` (canónica) | 1, 4 |
| Datos por país | `references/countries/[pais].md` | 1, 2 |
| Humanizador | `guides/editor-humano.md` o `humanizer.md` | 3, 5 |
| Rúbrica scoring | `references/rubrica-scoring.md` | 2 (si necesita contexto) |

## Outputs

- `output/consolidado_[descriptor].md` — **Entregable final** (documento único ensamblado)
- `output/consolidado_[descriptor] - ch1_introduccion.md` — Intermedio
- `output/consolidado_[descriptor] - ch2_panorama.md` — Intermedio
- `output/consolidado_[descriptor] - ch3_[NN]_[ciudad].md` — Intermedio (1 por ciudad)
- `output/consolidado_[descriptor] - ch4_metodologia.md` — Intermedio

## Checklist

- [ ] Todas las ciudades incluidas y en el orden correcto
- [ ] Introducción ≤ 500 palabras
- [ ] Matriz comparativa con scores por dominio para todas las ciudades
- [ ] 3-4 hallazgos transversales concretos
- [ ] Cada ciudad tiene exactamente 3 fortalezas, 3 retos, 3 recomendaciones
- [ ] Recomendaciones son estratégicas (sin bullets operativos, sin citas académicas)
- [ ] Cukier y Kon mencionado máximo 1 vez por ciudad (solo en madurez)
- [ ] CERO apariciones de "per Extracto" en todo el documento
- [ ] CERO apariciones de "Tabla 4.3" fuera del Capítulo 4
- [ ] CERO apariciones de "secuencia evolutiva" fuera del Capítulo 4
- [ ] Notas al pie locales por ciudad, numeración reiniciada
- [ ] Humanización aplicada (sin patrones AI)
- [ ] Tablas de datos e indicadores completas en sección 8 de cada ciudad
- [ ] Capítulo 4 contiene explicación completa de modelo ANDE, Cukier y Kon, y Tabla 4.3
- [ ] Documento final ensamblado en archivo único .md
