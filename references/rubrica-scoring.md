# Rúbrica de Scoring — 30 Indicadores ANDE Fase 1

Este archivo define los rangos de score para cada indicador. Consultar ANTES de asignar cualquier score.

---

## Reglas generales

1. **Escala:** 0-100 para cada indicador
2. **Ajuste por población:** Para ciudades < 1M habitantes, ajustar indicadores de conteo ANTES de aplicar la rúbrica:
   ```
   Valor ajustado = (Valor absoluto / Población) × 1,000,000
   ```
   Aplica a: S1, S2, S3, S4, C1, C2, M1, M2, I1, I2
3. **Indicadores cualitativos:** Algunos indicadores (P2, P3, C3, C4, C5, M3) se evalúan con criterios descriptivos, no numéricos puros
4. **Score del dominio:** Promedio simple de los indicadores del dominio
5. **Fuente siempre requerida:** No asignar score sin dato. Si no hay dato, registrar "N/D" y estimar con justificación explícita marcada como (est.)

---

## P: Política y Regulación

### P1 · Días para constituir empresa

| Score | Rango | Referencia |
|-------|-------|------------|
| 90-100 | 1-3 días | NZ, Singapur, Chile (SPA en línea), Georgia, Estonia |
| 70-89 | 4-7 días | Dinamarca, Canadá, Colombia (post-reforma), México (CDMX) |
| 50-69 | 8-15 días | Promedio LATAM reformado (~11 días), Perú, Costa Rica |
| 30-49 | 16-30 días | Promedio histórico LATAM (~34 días), Ecuador, Argentina |
| 10-29 | 31-60 días | Brasil (ciudades medianas), Bolivia, Honduras |
| 0-9 | >60 días | Venezuela, países sin reforma de registro |

**Tipo de benchmark:** Absoluto (dato comparable internacionalmente)
**Fuente benchmark:** World Bank Doing Business / B-READY, OECD

---

### P2 · Régimen fiscal especial para startups

Evaluar presencia y calidad de incentivos fiscales dirigidos específicamente a startups, emprendedores o empresas de base tecnológica. NO contar regímenes generales de PyMEs a menos que incluyan beneficios significativos para startups.

| Score | Criterio |
|-------|----------|
| 80-100 | Régimen dedicado a startups con al menos 3 beneficios: exención ISR temporal, deducción acelerada I+D, diferimiento seguridad social, simplificación administrativa. Vigente y accesible. |
| 60-79 | Régimen general de PyMEs con beneficios aplicables a startups (ej: RIF en México, Régimen Simple en Colombia). Al menos 2 beneficios claros. |
| 40-59 | Existen incentivos parciales (ej: solo zona franca, solo sector específico, solo crédito fiscal I+D). Cobertura limitada. |
| 20-39 | Incentivos anunciados pero no implementados, o existen solo a nivel nacional sin aplicación local efectiva. Burocracia excesiva para acceder. |
| 0-19 | Sin régimen diferenciado. Startups tributan igual que cualquier empresa desde el día 1. |

**Tipo de benchmark:** Cualitativo (criterios descriptivos)
**Nota:** Si el ecosistema es subnacional, evaluar tanto incentivos nacionales como locales/estatales.

---

### P3 · Programas públicos activos de apoyo al emprendimiento

Contar programas gubernamentales (federal, estatal, municipal) **activos y verificados** en los últimos 24 meses. Incluir: fondos concursables, programas de capacitación, incubación pública, compras públicas dirigidas a startups, programas de internacionalización.

| Score | Rango | Referencia |
|-------|-------|------------|
| 80-100 | 8+ programas activos | Ecosistemas con política articulada: Bogotá, Santiago, São Paulo, CDMX |
| 60-79 | 5-7 programas | Política fragmentada pero con cobertura razonable |
| 40-59 | 3-4 programas | Algunos esfuerzos, generalmente de un solo nivel de gobierno |
| 20-39 | 1-2 programas | Dependencia de un programa nacional genérico |
| 0-19 | 0 programas verificados | Sin política pública de emprendimiento activa |

**Tipo de benchmark:** Conteo absoluto (no ajustar por población — la política es institucional, no per cápita)

---

## F: Financiamiento

### F1 · Inversión total en startups (últimos 3 años, USD)

Sumar todas las rondas de inversión documentadas (seed, pre-seed, Series A+, grants de inversión) en startups con sede o operaciones principales en el ecosistema.

| Score | Rango | Referencia |
|-------|-------|------------|
| 90-100 | >USD 500M | São Paulo, CDMX, Bogotá, Buenos Aires |
| 70-89 | USD 100M-500M | Medellín, Monterrey, Santiago, Lima |
| 50-69 | USD 30M-100M | Guadalajara, Barranquilla, San José CR |
| 30-49 | USD 5M-30M | Ciudades secundarias con actividad emergente |
| 10-29 | USD 500K-5M | Ecosistemas incipientes con rondas esporádicas |
| 0-9 | <USD 500K o sin registros | Sin actividad de inversión formal documentada |

**Tipo de benchmark:** Absoluto (no ajustar por población — el capital fluye a oportunidades, no proporcionalmente a habitantes)
**Nota:** Para LATAM, el total regional fue ~USD 4.5B en 2024 (LAVCA). Brazil + Mexico capturan ~70%.

---

### F2 · Rondas de inversión anuales

Número promedio de rondas cerradas por año en los últimos 3 años.

| Score | Rango | Referencia |
|-------|-------|------------|
| 90-100 | 50+ rondas/año | Hubs principales: São Paulo, CDMX |
| 70-89 | 20-49 rondas/año | Hubs consolidados: Bogotá, Santiago, Monterrey |
| 50-69 | 8-19 rondas/año | Ecosistemas en desarrollo activo |
| 30-49 | 3-7 rondas/año | Actividad emergente pero visible |
| 10-29 | 1-2 rondas/año | Rondas esporádicas, no hay patrón |
| 0-9 | 0 rondas documentadas | Sin actividad |

**Tipo de benchmark:** Absoluto

---

### F3 · VCs con presencia local

Fondos de venture capital con oficina, GP residente, o mandato explícito para invertir en el ecosistema. Incluir fondos regionales si invierten activamente en la ciudad.

| Score | Rango | Referencia |
|-------|-------|------------|
| 80-100 | 10+ VCs | Hubs principales de LATAM |
| 60-79 | 5-9 VCs | Ecosistemas con masa crítica de inversión |
| 40-59 | 2-4 VCs | Presencia emergente, generalmente fondos regionales |
| 20-39 | 1 VC | Dependencia de un solo fondo |
| 0-19 | 0 VCs | Sin presencia de capital de riesgo formal |

**Tipo de benchmark:** Absoluto (los VCs van donde hay deal flow, no proporcionalmente a población)

---

### F4 · Inversionistas ángeles activos

Individuos o redes de ángeles con al menos 1 inversión documentada en los últimos 24 meses en el ecosistema.

| Score | Rango | Referencia |
|-------|-------|------------|
| 80-100 | 30+ ángeles activos o red formal consolidada | Club de Inversionistas Ángeles con track record |
| 60-79 | 15-29 ángeles o red en crecimiento | Red organizada con deal flow regular |
| 40-59 | 5-14 ángeles o red incipiente | Algunos ángeles individuales, posible red en formación |
| 20-39 | 1-4 ángeles identificados | Inversión ángel esporádica, no organizada |
| 0-19 | Sin ángeles documentados | No hay cultura de inversión ángel |

**Tipo de benchmark:** Absoluto

---

### F5 · Exits documentados (últimos 5 años)

Eventos de liquidez: adquisiciones, IPOs, fusiones con retorno positivo para inversionistas. Incluir acqui-hires si el monto es significativo (>USD 1M).

| Score | Rango | Referencia |
|-------|-------|------------|
| 80-100 | 5+ exits | Ecosistema con ciclo de reinversión activo |
| 60-79 | 3-4 exits | Señales de mercado positivas, ciclo empezando |
| 40-59 | 1-2 exits | Primeros casos demuestran que es posible |
| 20-39 | Exits nacionales pero no locales | El ecosistema no ha producido exits propios pero hay referentes en el país |
| 0-9 | 0 exits | Sin eventos de liquidez documentados |

**Tipo de benchmark:** Absoluto

---

### F6 · Programas de capital semilla público

Programas gubernamentales o de banca de desarrollo que provean capital semilla, grants, o créditos blandos específicamente para startups o emprendimientos innovadores.

| Score | Rango | Referencia |
|-------|-------|------------|
| 80-100 | 3+ programas activos con ticket promedio >USD 20K | CORFO Chile, FONTAR Argentina, Startup India |
| 60-79 | 2 programas o 1 programa robusto (>USD 50K ticket) | INADEM histórico, Fondo Emprender Colombia |
| 40-59 | 1 programa activo con cobertura limitada | Programas estatales pequeños, ticket <USD 10K |
| 20-39 | Programa anunciado pero sin desembolsos recientes, o solo microcrédito | Confusión entre microcrédito y capital semilla |
| 0-19 | Sin programas de capital semilla público | No hay financiamiento público para etapa temprana |

**Tipo de benchmark:** Cualitativo + conteo

---

## C: Cultura

### C1 · Meetups de emprendimiento activos

Grupos que se reúnen con frecuencia regular (mínimo mensual) en temas de emprendimiento, startups, tecnología, innovación.

| Score | Rango (absoluto) | Ajustado <1M hab |
|-------|-------------------|------------------|
| 80-100 | 15+ meetups activos | ≥15 por millón |
| 60-79 | 8-14 meetups | 8-14 por millón |
| 40-59 | 4-7 meetups | 4-7 por millón |
| 20-39 | 1-3 meetups | 1-3 por millón |
| 0-19 | 0 meetups regulares | 0 por millón |

**Tipo de benchmark:** Mixto (absoluto para ciudades ≥1M, ajustado para <1M)
**Criterio "activo":** Al menos 1 evento en los últimos 3 meses Y al menos 3 eventos en los últimos 12 meses.

---

### C2 · Eventos anuales de emprendimiento

Eventos tipo conferencia, hackathon, startup weekend, demo day, pitch competition celebrados en los últimos 12 meses.

| Score | Rango (absoluto) | Ajustado <1M hab |
|-------|-------------------|------------------|
| 80-100 | 20+ eventos/año | ≥20 por millón |
| 60-79 | 10-19 eventos | 10-19 por millón |
| 40-59 | 5-9 eventos | 5-9 por millón |
| 20-39 | 2-4 eventos | 2-4 por millón |
| 0-9 | 0-1 eventos | 0-1 por millón |

**Tipo de benchmark:** Mixto

---

### C3 · Medios especializados en emprendimiento local

Blogs, podcasts, newsletters, secciones de medios locales dedicados al ecosistema emprendedor de la ciudad/región.

| Score | Criterio |
|-------|----------|
| 80-100 | 5+ medios especializados activos (publicación al menos quincenal). Combinación de formatos (podcast + blog + newsletter). Cobertura regular del ecosistema local. |
| 60-79 | 3-4 medios activos. Al menos 2 formatos diferentes. Publicación regular. |
| 40-59 | 1-2 medios locales activos, o cobertura regular en medios nacionales con sección local. |
| 20-39 | Cobertura esporádica en medios nacionales. Sin medio local dedicado. |
| 0-19 | Sin cobertura mediática del ecosistema emprendedor local. |

**Tipo de benchmark:** Cualitativo
**Criterio "activo":** Publicación en los últimos 30 días.

---

### C4 · Comunidades online de emprendedores locales

Grupos activos en LinkedIn, Facebook, Slack, Discord, WhatsApp u otras plataformas donde emprendedores locales se conectan.

| Score | Criterio |
|-------|----------|
| 80-100 | 5+ comunidades activas con >500 miembros combinados. Interacción regular (posts semanales). Variedad de plataformas. |
| 60-79 | 3-4 comunidades activas. >200 miembros combinados. Interacción al menos quincenal. |
| 40-59 | 1-2 comunidades identificables. Actividad intermitente. |
| 20-39 | Comunidades existen pero con baja actividad (<1 post/mes). |
| 0-19 | Sin comunidades online de emprendedores locales identificables. |

**Tipo de benchmark:** Cualitativo

---

### C5 · Confianza social / percepción del emprendimiento

Proxy de la disposición cultural hacia el emprendimiento. Fuentes: GEM (actitudes), World Values Survey (confianza interpersonal), Latinobarómetro, encuestas locales.

| Score | Criterio |
|-------|----------|
| 80-100 | GEM: >70% de la población considera que emprender es buena opción de carrera. Confianza interpersonal >30% (WVS). Referentes locales visibles. |
| 60-79 | GEM: 50-70% consideran emprender buena opción. Confianza interpersonal 20-30%. Algunos referentes visibles. |
| 40-59 | GEM: 30-50%. Confianza interpersonal 10-20%. Cultura de emprendimiento emergente, todavía dominada por empleo formal como aspiración principal. |
| 20-39 | GEM: <30% o sin datos. Confianza interpersonal <10%. Emprendimiento visto como último recurso ("emprendimiento por necesidad" dominante). |
| 0-19 | Estigma activo contra el emprendimiento. Fracaso empresarial severamente penalizado social o legalmente. |

**Tipo de benchmark:** Cualitativo con datos cuantitativos de referencia
**Nota:** Si no hay datos GEM o WVS para la ciudad, usar datos nacionales con nota (est.)

---

## S: Servicios de Apoyo

### S1 · Aceleradoras activas

Programas de aceleración con al menos 1 cohorte en los últimos 24 meses. Incluir programas corporativos si son abiertos.

| Score | Rango (absoluto) | Ajustado <1M hab |
|-------|-------------------|------------------|
| 80-100 | 8+ aceleradoras | ≥8 por millón |
| 60-79 | 4-7 aceleradoras | 4-7 por millón |
| 40-59 | 2-3 aceleradoras | 2-3 por millón |
| 20-39 | 1 aceleradora | 1 por millón |
| 0-19 | 0 aceleradoras | 0 |

**Tipo de benchmark:** Mixto
**Criterio "activa":** Al menos 1 cohorte graduada o en curso en últimos 24 meses. Verificar en sitio web, redes sociales, o prensa.

---

### S2 · Incubadoras activas

Programas de incubación (universitarios, públicos, privados) con operación verificada. Diferenciar de aceleradoras: incubadoras operan en etapa más temprana, con horizonte más largo.

| Score | Rango (absoluto) | Ajustado <1M hab |
|-------|-------------------|------------------|
| 80-100 | 6+ incubadoras | ≥6 por millón |
| 60-79 | 3-5 incubadoras | 3-5 por millón |
| 40-59 | 2 incubadoras | 2 por millón |
| 20-39 | 1 incubadora | 1 por millón |
| 0-19 | 0 incubadoras verificadas | 0 |

**Tipo de benchmark:** Mixto

---

### S3 · Espacios de coworking

Espacios de trabajo compartido activos y operando. Incluir espacios dentro de incubadoras/aceleradoras si son accesibles al público.

| Score | Rango (absoluto) | Ajustado <1M hab |
|-------|-------------------|------------------|
| 80-100 | 15+ coworkings | ≥15 por millón |
| 60-79 | 8-14 coworkings | 8-14 por millón |
| 40-59 | 4-7 coworkings | 4-7 por millón |
| 20-39 | 1-3 coworkings | 1-3 por millón |
| 0-19 | 0 coworkings | 0 |

**Tipo de benchmark:** Mixto

---

### S4 · Mentores registrados en plataformas

Mentores activos en plataformas de mentoría (Endeavor, MentorMe, plataformas locales), programas de mentoría formales, o con track record documentado.

| Score | Rango (absoluto) | Ajustado <1M hab |
|-------|-------------------|------------------|
| 80-100 | 50+ mentores | ≥50 por millón |
| 60-79 | 20-49 mentores | 20-49 por millón |
| 40-59 | 10-19 mentores | 10-19 por millón |
| 20-39 | 3-9 mentores | 3-9 por millón |
| 0-19 | 0-2 mentores identificados | 0-2 por millón |

**Tipo de benchmark:** Mixto

---

### S5 · Velocidad de internet (Mbps descarga promedio)

Velocidad promedio de descarga de banda ancha fija según Speedtest/OOKLA u fuentes equivalentes.

| Score | Rango | Referencia |
|-------|-------|------------|
| 90-100 | >150 Mbps | Chile urbano, Uruguay, top LATAM |
| 70-89 | 80-150 Mbps | Brasil urbano, Colombia urbano, México principales |
| 50-69 | 40-79 Mbps | Promedio LATAM (~55 Mbps en 2024) |
| 30-49 | 20-39 Mbps | Ciudades secundarias, infraestructura limitada |
| 10-29 | 5-19 Mbps | Zonas rurales conectadas, infraestructura deficiente |
| 0-9 | <5 Mbps | Conectividad insuficiente para trabajo remoto |

**Tipo de benchmark:** Absoluto
**Fuente benchmark:** Ookla Speedtest Global Index

---

## H: Capital Humano

### H1 · Universidades con programas de emprendimiento

Instituciones de educación superior con al menos uno de: programa académico en emprendimiento, incubadora universitaria, centro de transferencia tecnológica (OTT), competencias de emprendimiento estudiantil.

| Score | Rango | Referencia |
|-------|-------|------------|
| 80-100 | 5+ universidades con programas activos | Ciudades universitarias grandes: Bogotá, Santiago, Guadalajara |
| 60-79 | 3-4 universidades | Cobertura buena para ecosistema mediano |
| 40-59 | 2 universidades | Masa crítica mínima |
| 20-39 | 1 universidad | Dependencia de una sola institución |
| 0-19 | 0 universidades con programas de emprendimiento | Sin vínculo universidad-emprendimiento |

**Tipo de benchmark:** Absoluto (las universidades son instituciones, no se ajustan per cápita)

---

### H2 · Graduados STEM anuales

Egresados anuales de carreras STEM (Ciencia, Tecnología, Ingeniería, Matemáticas) de universidades en el ecosistema.

| Score | Rango | Referencia |
|-------|-------|------------|
| 80-100 | >5,000 graduados STEM/año | Grandes centros universitarios |
| 60-79 | 2,000-5,000 | Ecosistemas con buena base educativa |
| 40-59 | 500-1,999 | Ciudades universitarias medianas |
| 20-39 | 100-499 | Oferta limitada de talento STEM |
| 0-9 | <100 o sin datos | Brecha crítica de talento STEM |

**Tipo de benchmark:** Absoluto
**Nota:** Usar datos de la autoridad educativa nacional (ANUIES en México, SNIES en Colombia, etc.)

---

### H3 · Bootcamps tech activos

Programas de formación intensiva en programación, diseño UX, data science, etc. Incluir presenciales y remotos con presencia local (oficina o comunidad).

| Score | Rango | Referencia |
|-------|-------|------------|
| 80-100 | 5+ bootcamps activos | Hub tech consolidado |
| 60-79 | 3-4 bootcamps | Buena oferta de formación alternativa |
| 40-59 | 1-2 bootcamps | Oferta básica, generalmente 1 presencial + 1 remoto |
| 20-39 | Solo bootcamps remotos sin presencia local | Acceso solo digital, sin comunidad local |
| 0-19 | 0 bootcamps | Sin formación tech intensiva |

**Tipo de benchmark:** Absoluto

---

### H4 · Talento tech (estimación LinkedIn)

Profesionales en el ecosistema con skills en desarrollo de software, data science, producto digital, UX, según búsqueda en LinkedIn.

| Score | Rango | Referencia |
|-------|-------|------------|
| 80-100 | >10,000 perfiles tech | Hubs tech principales |
| 60-79 | 3,000-10,000 | Ecosistemas con base de talento sólida |
| 40-59 | 1,000-2,999 | Talento emergente, suficiente para startups iniciales |
| 20-39 | 300-999 | Talento limitado, riesgo de fuga |
| 0-9 | <300 | Brecha crítica de talento tech |

**Tipo de benchmark:** Absoluto
**Nota:** La búsqueda de LinkedIn es un proxy imperfecto. Documentar criterios de búsqueda usados.

---

### H5 · Acceso a internet (% de población)

Porcentaje de la población con acceso a internet.

| Score | Rango | Referencia |
|-------|-------|------------|
| 90-100 | >90% | Chile (94.5%), Costa Rica (93%), Bahamas, top LATAM |
| 70-89 | 80-90% | Uruguay, Rep. Dominicana, Argentina, Brasil, promedio LATAM alto |
| 50-69 | 70-79% | Promedio LATAM (~77%). México, Colombia, Perú |
| 30-49 | 55-69% | Centroamérica promedio, Ecuador |
| 10-29 | 40-54% | Guatemala (56%), El Salvador, Honduras |
| 0-9 | <40% | Haití, países con brecha digital severa |

**Tipo de benchmark:** Absoluto (dato comparable internacionalmente)
**Fuente benchmark:** ITU, DataReportal, World Bank

---

## M: Mercados

### M1 · Startups activas identificadas

Empresas de base tecnológica o innovadora activas en el ecosistema. Criterio: fundadas en los últimos 10 años, con producto/servicio tecnológico, al menos 1 empleado además de fundadores. NO contar negocios tradicionales ni freelancers.

| Score | Rango (absoluto) | Ajustado <1M hab |
|-------|-------------------|------------------|
| 80-100 | 100+ startups | ≥100 por millón |
| 60-79 | 40-99 startups | 40-99 por millón |
| 40-59 | 15-39 startups | 15-39 por millón |
| 20-39 | 5-14 startups | 5-14 por millón |
| 0-9 | <5 startups | <5 por millón |

**Tipo de benchmark:** Mixto
**Criterio "activa":** Sitio web funcional, presencia en redes sociales en últimos 6 meses, o registro en Crunchbase/AngelList/directorio local.

---

### M2 · Corporativos tech con presencia local

Empresas tecnológicas (nacionales o multinacionales) con oficinas, centros de desarrollo, o presencia operativa significativa en el ecosistema. Importa porque generan talento, demanda para startups, y posibles acquirers.

| Score | Rango (absoluto) | Ajustado <1M hab |
|-------|-------------------|------------------|
| 80-100 | 15+ corporativos tech | ≥15 por millón |
| 60-79 | 8-14 corporativos | 8-14 por millón |
| 40-59 | 3-7 corporativos | 3-7 por millón |
| 20-39 | 1-2 corporativos | 1-2 por millón |
| 0-19 | 0 corporativos tech | 0 |

**Tipo de benchmark:** Mixto

---

### M3 · Sectores de especialización

Sectores verticales donde el ecosistema muestra concentración de startups (3+ startups en el mismo vertical). Importa porque indica formación de clusters.

| Score | Criterio |
|-------|----------|
| 80-100 | 4+ sectores con 3+ startups cada uno. Al menos 1 sector con ventaja competitiva clara (vinculado a industria local, recurso natural, o talento especializado). |
| 60-79 | 2-3 sectores identificables con concentración. Alineamiento parcial con vocación económica local. |
| 40-59 | 1 sector con concentración visible. El resto es disperso. |
| 20-39 | Sin sectores claros, pero las startups existentes comparten algunas características. |
| 0-19 | Sin concentración sectorial. Startups aisladas sin patrón. |

**Tipo de benchmark:** Cualitativo

---

## I: I+D e Innovación

### I1 · Patentes otorgadas (últimos 5 años)

Patentes otorgadas por la oficina nacional de propiedad intelectual (IMPI, SIC, INPI, etc.) originadas en el ecosistema.

| Score | Rango (absoluto) | Ajustado <1M hab |
|-------|-------------------|------------------|
| 80-100 | 200+ patentes (5 años) | ≥200 por millón |
| 60-79 | 80-199 patentes | 80-199 por millón |
| 40-59 | 30-79 patentes | 30-79 por millón |
| 20-39 | 10-29 patentes | 10-29 por millón |
| 0-9 | <10 patentes | <10 por millón |

**Tipo de benchmark:** Mixto
**Nota:** Concentración alta en capitales y ciudades con universidades de investigación. Ciudades secundarias en LATAM rara vez superan 30 patentes/5 años.

---

### I2 · Centros de investigación

Centros de investigación públicos o privados, laboratorios universitarios de investigación con producción activa, centros de I+D corporativos.

| Score | Rango (absoluto) | Ajustado <1M hab |
|-------|-------------------|------------------|
| 80-100 | 10+ centros | ≥10 por millón |
| 60-79 | 5-9 centros | 5-9 por millón |
| 40-59 | 2-4 centros | 2-4 por millón |
| 20-39 | 1 centro | 1 por millón |
| 0-19 | 0 centros de investigación | 0 |

**Tipo de benchmark:** Mixto

---

### I3 · Publicaciones científicas indexadas (últimos 3 años)

Publicaciones en revistas indexadas (Scopus, Web of Science) de instituciones con sede en el ecosistema.

| Score | Rango | Referencia |
|-------|-------|------------|
| 80-100 | >2,000 publicaciones (3 años) | Ciudades con universidades de investigación de primer nivel |
| 60-79 | 500-2,000 | Buenos centros universitarios con producción activa |
| 40-59 | 100-499 | Producción académica moderada |
| 20-39 | 20-99 | Producción limitada, pocas instituciones investigadoras |
| 0-9 | <20 | Casi sin producción científica indexada |

**Tipo de benchmark:** Absoluto
**Nota:** La producción científica se concentra fuertemente en universidades de investigación. Ciudades sin universidades top tendrán scores bajos aquí, lo cual es esperado.

---

## Guía de Decisión para Casos Ambiguos

### Cuándo dar el beneficio de la duda (redondear hacia arriba)
- Hay evidencia de tendencia positiva (ej: aceleradora lanzada hace 6 meses, aún sin cohorte graduada)
- El dato no está disponible exacto pero las señales indirectas son consistentes
- El ecosistema es muy pequeño y los valores absolutos son bajos pero proporcionalmente razonables

### Cuándo ser conservador (redondear hacia abajo)
- La fuente no es verificable o tiene >2 años de antigüedad
- El dato es de nivel nacional pero el ecosistema local podría ser muy diferente
- Hay señales contradictorias (ej: aceleradora "activa" pero sin actividad en redes en 12+ meses)
- El valor se basa en una sola fuente sin corroboración

### Cuándo marcar como estimación (est.)
- Dato nacional prorrateado a nivel local
- Dato inferido de fuentes indirectas
- Dato de hace >2 años sin actualización
- Combinación de datos parciales de múltiples fuentes

---

## Notas sobre Benchmarks

### Contexto LATAM
- VC en LATAM: USD 4.5B total 2024, ~751 deals (LAVCA). Brazil + Mexico = ~70%
- Internet LATAM: Promedio ~77% (2023), rango Chile 94.5% a Guatemala 56.1%
- Días para incorporar empresa: Promedio LATAM ~11 días (post-reformas), rango NZ <1 a Venezuela >100
- Patentes: LATAM produce ~3% de patentes mundiales; concentración >80% en Brazil, Mexico, Argentina, Chile

### Limitaciones de los benchmarks
- Los rangos están calibrados para ecosistemas en LATAM y economías en desarrollo
- Para ecosistemas en US/Europa, los rangos de Financiamiento y Talento Tech necesitan ajustarse hacia arriba
- Los datos de LinkedIn son un proxy imperfecto y varían por penetración de la plataforma
- Los datos de meetups y eventos subestiman la actividad real (no todo está en Meetup.com/Eventbrite)
