# Guía Interna de Scoring — Diagnóstico ANDE Fase 1

Documento interno que explica paso a paso cómo se asignan los scores del diagnóstico de ecosistemas emprendedores bajo la metodología ANDE.

---

## 1. Principios Generales

- **Escala:** Cada indicador se puntúa de 0 a 100.
- **Score de dominio:** Promedio simple de los indicadores dentro del dominio.
- **Score global:** Promedio simple de los 7 dominios (no de los 30 indicadores individuales). Esto evita que dominios con más indicadores pesen más.
- **Sin dato, sin score:** Si no hay dato verificable, registrar `N/D`. Se permite estimar con justificación explícita, marcada como `(est.)`.

---

## 2. Estructura del Diagnóstico

| Dominio | Código | Indicadores | Tipo predominante |
|---------|--------|-------------|-------------------|
| Política y Regulación | P | P1, P2, P3 | Mixto (cuanti + cuali) |
| Servicios de Apoyo | S | S1, S2, S3, S4, S5 | Conteo + absoluto |
| Capital Humano | H | H1, H2, H3, H4, H5 | Absoluto |
| I+D e Innovación | I | I1, I2, I3 | Mixto |
| Financiamiento | F | F1, F2, F3, F4, F5, F6 | Absoluto + cuali |
| Cultura | C | C1, C2, C3, C4, C5 | Mixto + cuali |
| Mercados | M | M1, M2, M3 | Mixto + cuali |

**Total:** 30 indicadores, 7 dominios.

---

## 3. Tipos de Benchmark

Cada indicador usa uno de tres tipos de benchmark, que determina cómo se interpreta el dato crudo antes de asignar el score.

### 3.1 Absoluto

El dato se compara directamente contra rangos fijos, sin ajuste. Se usa cuando el indicador es comparable internacionalmente o cuando el recurso no escala con población.

**Ejemplos:** P1 (días para constituir empresa), F1 (inversión total en USD), H5 (% acceso a internet), S5 (velocidad de internet en Mbps).

```
Dato crudo → Buscar en tabla de rangos → Score
```

### 3.2 Mixto (absoluto o ajustado por población)

Para ciudades con menos de 1 millón de habitantes, se ajusta el dato antes de consultar la rúbrica. Para ciudades de 1M o más, se usa el valor absoluto.

**Aplica a:** S1, S2, S3, S4, C1, C2, M1, M2, I1, I2.

```
Si población < 1,000,000:
    Valor ajustado = (Valor absoluto / Población) × 1,000,000
    Usar valor ajustado en la tabla de rangos

Si población ≥ 1,000,000:
    Usar valor absoluto en la tabla de rangos
```

**Ejemplo práctico:**
- Ciudad con 400,000 habitantes y 6 aceleradoras activas (S1)
- Valor ajustado = (6 / 400,000) × 1,000,000 = 15 por millón
- Según la rúbrica de S1: 15 por millón → Score 80-100

### 3.3 Cualitativo

El dato se evalúa con criterios descriptivos, no numéricos. El evaluador lee la descripción de cada rango y asigna el que mejor encaje con la realidad observada.

**Aplica a:** P2, P3, C3, C4, C5, M3.

```
Dato cualitativo → Leer criterios descriptivos → Elegir el rango que mejor encaje → Score
```

---

## 4. Proceso de Scoring Paso a Paso

### Paso 1: Recopilar datos

Para cada indicador, documentar:

| Campo | Descripción |
|-------|-------------|
| `value` | Dato crudo (número, texto descriptivo, o `N/D`) |
| `source` | De dónde viene el dato (URL, reporte, base de datos) |
| `notes` | Observaciones relevantes (antigüedad del dato, cobertura, limitaciones) |

### Paso 2: Ajustar por población (si aplica)

Solo para indicadores de tipo mixto y solo si la población es menor a 1 millón.

### Paso 3: Consultar la rúbrica

Abrir `references/rubrica-scoring.md` y buscar el indicador. Comparar el valor (ajustado o absoluto) con los rangos de la tabla. Asignar un score dentro del rango que corresponda.

**Dentro de un rango, el evaluador elige el punto exacto:**

| Posición en rango | Cuándo usarla |
|-------------------|---------------|
| Extremo superior | Dato sólido, tendencia positiva, múltiples fuentes confirman |
| Punto medio | Dato estándar, sin señales adicionales |
| Extremo inferior | Dato de fuente única, antigüedad >1 año, señales contradictorias |

### Paso 4: Marcar estimaciones

Si el dato no es directo, agregar `(est.)` al score y documentar el razonamiento en `notes`. Situaciones que requieren esta marca:

- Dato nacional prorrateado a nivel local
- Dato inferido de fuentes indirectas
- Dato con más de 2 años de antigüedad
- Combinación de datos parciales

### Paso 5: Calcular scores de dominio

```
Score dominio = Suma de scores de indicadores del dominio / Número de indicadores del dominio
```

Si un indicador es `N/D`, no se incluye en el promedio (no contar como cero).

### Paso 6: Calcular score global

```
Score global = Suma de 7 scores de dominio / 7
```

---

## 5. Niveles de Madurez

El score global se traduce a un nivel de madurez del ecosistema:

| Score Global | Nivel | Descripción |
|--------------|-------|-------------|
| 0-25 | Naciente | Elementos básicos ausentes o incipientes. Pocas organizaciones de apoyo, sin flujo de capital, talento limitado. |
| 26-45 | Emergente | Algunos elementos presentes pero desconectados. Primeras organizaciones de apoyo, actividad de inversión esporádica, base universitaria en desarrollo. |
| 46-65 | En Desarrollo | Mayoría de elementos presentes con brechas. Flujo de capital visible, organizaciones de apoyo activas, brechas en dominios específicos. |
| 66-100 | Autosostenible | Ecosistema funcional con ciclos de retroalimentación. Reinversión de exits, talento que circula, deal flow constante. |

---

## 6. Reglas para Casos Ambiguos

### Redondear hacia arriba cuando:

- Hay evidencia de tendencia positiva reciente (ej: aceleradora lanzada hace 6 meses)
- Las señales indirectas son consistentes aunque el dato exacto no esté disponible
- El ecosistema es pequeño y los valores absolutos son bajos pero proporcionalmente razonables

### Redondear hacia abajo cuando:

- La fuente no es verificable o tiene más de 2 años
- El dato es de nivel nacional pero la realidad local podría diferir
- Hay señales contradictorias (ej: aceleradora "activa" sin actividad en redes en 12+ meses)
- El valor se basa en una sola fuente sin corroboración

### Marcar como estimación cuando:

- Se prorratea un dato nacional a nivel local
- Se infiere de fuentes indirectas
- El dato tiene más de 2 años sin actualización
- Se combinan datos parciales de varias fuentes

---

## 7. Ejemplo Completo: Scoring de un Dominio

**Dominio: Servicios de Apoyo (S) — Ciudad ficticia, 500,000 habitantes**

| ID | Indicador | Dato crudo | Ajuste | Valor usado | Rango rúbrica | Score |
|----|-----------|------------|--------|-------------|---------------|-------|
| S1 | Aceleradoras activas | 3 | (3/500K)×1M = 6 | 6 por millón | 4-7 → 60-79 | 68 |
| S2 | Incubadoras activas | 2 | (2/500K)×1M = 4 | 4 por millón | 3-5 → 60-79 | 62 |
| S3 | Coworkings | 5 | (5/500K)×1M = 10 | 10 por millón | 8-14 → 60-79 | 65 |
| S4 | Mentores registrados | 8 | (8/500K)×1M = 16 | 16 por millón | 10-19 → 40-59 | 45 |
| S5 | Velocidad internet | 72 Mbps | No aplica (absoluto) | 72 Mbps | 40-79 → 50-69 | 58 |

```
Score S = (68 + 62 + 65 + 45 + 58) / 5 = 59.6 → 60
```

---

## 8. Notas sobre Calibración Regional

Los rangos de la rúbrica están calibrados para ecosistemas en América Latina y economías en desarrollo. Consideraciones importantes:

- **LATAM:** Los rangos funcionan directamente. Referencia: VC regional ~USD 4.5B en 2024 (LAVCA), internet promedio ~77%, días para incorporar empresa ~11 días post-reformas.
- **US/Europa:** Los rangos de Financiamiento (F) y Talento Tech (H4) necesitan ajustarse hacia arriba. Un ecosistema "promedio" en US supera el máximo de la escala LATAM en varios indicadores.
- **Asia/África:** Evaluar caso por caso. Datos de internet y patentes pueden necesitar recalibración.

---

## 9. Referencia Rápida: Los 30 Indicadores

| ID | Indicador | Tipo | Ajuste <1M |
|----|-----------|------|------------|
| P1 | Días para constituir empresa | Absoluto | No |
| P2 | Régimen fiscal startups | Cualitativo | No |
| P3 | Programas públicos activos | Conteo | No |
| S1 | Aceleradoras activas | Mixto | Sí |
| S2 | Incubadoras activas | Mixto | Sí |
| S3 | Coworkings | Mixto | Sí |
| S4 | Mentores registrados | Mixto | Sí |
| S5 | Velocidad internet (Mbps) | Absoluto | No |
| H1 | Universidades con programas emprendimiento | Absoluto | No |
| H2 | Graduados STEM anuales | Absoluto | No |
| H3 | Bootcamps tech activos | Absoluto | No |
| H4 | Talento tech disponible | Absoluto | No |
| H5 | Acceso internet (%) | Absoluto | No |
| I1 | Patentes otorgadas (5 años) | Mixto | Sí |
| I2 | Centros de investigación | Mixto | Sí |
| I3 | Publicaciones científicas (3 años) | Absoluto | No |
| F1 | Inversión total startups (3 años, USD) | Absoluto | No |
| F2 | Rondas de inversión anuales | Absoluto | No |
| F3 | VCs con presencia local | Absoluto | No |
| F4 | Inversionistas ángeles activos | Absoluto | No |
| F5 | Exits documentados (5 años) | Absoluto | No |
| F6 | Capital semilla público | Cualitativo | No |
| C1 | Meetups activos | Mixto | Sí |
| C2 | Eventos anuales de emprendimiento | Mixto | Sí |
| C3 | Medios especializados | Cualitativo | No |
| C4 | Comunidades online | Cualitativo | No |
| C5 | Confianza social / percepción | Cualitativo | No |
| M1 | Startups activas | Mixto | Sí |
| M2 | Corporativos tech | Mixto | Sí |
| M3 | Sectores de especialización | Cualitativo | No |
