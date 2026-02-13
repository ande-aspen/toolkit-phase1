# México — Indicadores Nacionales y Contexto para ANDE Fase 1

## Metadata
- País: México
- ISO: MX
- Última actualización: 2025-02
- Moneda: MXN (1 USD ~ 17.5 MXN aprox.)

---

## P1 — Días para Constituir Empresa

- **Value:** 1 a 15 días
- **Source:** Secretaría de Economía (2024)
- **Notes:** 1 día hábil mediante la figura federal de Sociedad por Acciones Simplificada (SAS) en línea a través de gob.mx. Hasta 15 días para una S.A. de C.V. tradicional ante notario público y Registro Público del Comercio local. La SAS tiene límite de capital de 5M UDIs (~USD 300K). Para startups que buscan levantar capital, la S.A. de C.V. o S.A.P.I. es más común.

---

## P2 — Régimen Fiscal Especial para Startups

- **Value:** No existe régimen específico para startups
- **Source:** SAT / Ley del ISR (2024)
- **Notes:** El Régimen Simplificado de Confianza (RESICO) beneficia a PyMEs con ingresos menores a $3.5M MXN/año con tasas reducidas de 1-2.5%. Es un régimen general, no diseñado para startups tech. No existen en México: créditos fiscales por I+D, diferimiento de seguridad social para startups, incentivos fiscales para inversión ángel, ni deducciones agresivas en innovación. Algunos estados ofrecen incentivos adicionales (verificar por ciudad). El marco fiscal federal carece de incentivos para la inversión de riesgo.

---

## H5 — Acceso a Internet (%)

- **Value:** 83.5% (promedio nacional)
- **Source:** INEGI ENDUTIH (2023)
- **Notes:** Variación significativa por estado y región. Referencia por zona:

| Zona | Acceso aprox. |
|------|--------------|
| Norte (NL, Chih, Son, BC) | 83-88% |
| Centro (CDMX, Jal, Qro) | 85-92% |
| Sur (Chis, Oax, Gro) | 55-65% |
| Promedio nacional | 83.5% |

Para ciudades específicas: usar dato estatal de INEGI si está disponible. Si no, usar el promedio regional como proxy.

---

## C5 — Confianza Social / Percepción del Emprendimiento

- **Value:** 18% confianza interpersonal
- **Source:** Latinobarómetro (2023)
- **Notes:** Dato nacional. La confianza interpersonal en México es una de las más bajas de América Latina. Sin embargo, el GEM México reporta que ~55% considera el emprendimiento como buena opción de carrera. En la región norte hay históricamente mayor aspiración emprendedora. El "emprendimiento por necesidad" sigue siendo dominante a nivel nacional (~40% del total según GEM). Para el scoring se usa primariamente el dato de confianza interpersonal (18%) complementado con la percepción de carrera del GEM.

---

## S5 — Velocidad de Internet (Defaults para Estimación)

| Tipo de ciudad | Velocidad estimada | Fuente |
|----------------|-------------------|--------|
| Capital (CDMX) | ~100 Mbps | Ookla Speedtest (2024) |
| Ciudades principales (MTY, GDL) | ~80 Mbps | Ookla Speedtest (2024) |
| Ciudades secundarias (Chih, Qro, Mérida, Puebla) | ~65 Mbps | Ookla Speedtest (2024) |
| Ciudades menores (<500K) | ~50 Mbps | Ookla Speedtest (2024) |

Usar como estimación con marca (est.). Adecuado para operaciones digitales estándar en todas las categorías.

---

## Contexto Nacional Común

### Programas Federales con Alcance Local
- **SAS (Sociedad por Acciones Simplificada):** Sistema federal de constitución empresarial en línea
- **RESICO:** Régimen Simplificado de Confianza (fiscal)
- **NAFIN:** Nacional Financiera — créditos y programas de garantías para PyMEs
- **Bancomext:** Banco Nacional de Comercio Exterior — financiamiento para exportadores
- **CONAHCyT (antes CONACYT):** Consejo Nacional de Humanidades, Ciencias y Tecnologías — financiamiento a investigación
- **INADEM:** Instituto Nacional del Emprendedor — **cerrado en 2019**, no contar como activo

### Sistema Educativo (para H2 — Graduados STEM)
- **Fuente principal:** ANUIES (Asociación Nacional de Universidades e Instituciones de Educación Superior)
- **Método de prorrateo:** Dato nacional de graduados STEM / proporción de matrícula estatal vs nacional
- **Disciplinas STEM:** Ingeniería, manufactura, computación, ciencias exactas

### Propiedad Intelectual (para I1 — Patentes)
- **Fuente principal:** IMPI (Instituto Mexicano de la Propiedad Industrial)
- **Método de prorrateo:** Patentes nacionales × participación estatal en PIB o en gasto en I+D
- **Nota:** Gran parte del patentamiento proviene de centros de investigación y universidades, no siempre transferidas comercialmente

### Fuentes de Datos Recurrentes
| Indicador | Fuente nacional | Cómo localizar |
|-----------|----------------|----------------|
| H2 (STEM) | ANUIES | anuies.mx → Anuarios estadísticos |
| H5 (Internet %) | INEGI ENDUTIH | inegi.org.mx → encuestas |
| I1 (Patentes) | IMPI | gob.mx/impi → estadísticas |
| I3 (Publicaciones) | SCImago / Scopus | scimagojr.com → por institución |
| C5 (Confianza) | Latinobarómetro | latinobarometro.org |
| S5 (Velocidad) | Ookla | speedtest.net/global-index |
| P1 (Constitución) | Secretaría de Economía | gob.mx/se |
| P2 (Fiscal) | SAT | sat.gob.mx |
