# Comparativo de Ecosistemas

## Metadata
- **Comando:** /compare
- **Aliases:** /comparar
- **Idioma:** bilingüe (español por defecto)
- **Versión:** 1.0

## Descripción
Compara múltiples ecosistemas diagnosticados, usando los CSVs de indicadores y reportes en `output/`. Genera una tabla comparativa, identifica patrones regionales, cuellos de botella compartidos, fortalezas complementarias, y oportunidades de aprendizaje cruzado entre ecosistemas.

## Trigger
- El usuario escribe `/compare [ciudades]` o `/comparar [ciudades]`
- El usuario pide comparar ecosistemas, hacer benchmark, o análisis regional
- Invocado automáticamente al final de un batch de diagnósticos

## Inputs
- **Ciudades a comparar:** lista específica o "todas" (todas las que tengan CSV en output/)
- **Opcional:** enfoque (ej: "solo financiamiento", "solo LatAm", "ciudades < 500K")
- **Opcional:** preguntas específicas ("¿cuál tiene mejor capital humano?")

---

## Proceso

```
1. IDENTIFICAR ECOSISTEMAS:
   a. Si el usuario lista ciudades → buscar sus CSVs en output/
   b. Si dice "todas" → listar todos los CSVs en output/
   c. Verificar que cada ciudad tenga CSV con scores
   d. Si alguna no tiene diagnóstico → informar y ofrecer opciones

2. CARGAR DATOS:
   a. Leer todos los CSVs de indicadores
   b. Extraer: score por dominio, score global, nivel de madurez
   c. Calcular: cuello de botella, patrón C-R para cada ciudad

3. CONSTRUIR MATRIZ COMPARATIVA:
   Tabla: Ciudad × Dominio × Score

   | Ciudad | Población | Global | P | S | H | I | F | C | M | Madurez | Cuello |
   |--------|-----------|--------|---|---|---|---|---|---|---|---------|--------|

4. IDENTIFICAR PATRONES:
   a. Cuellos de botella compartidos (¿todos sufren en F?)
   b. Fortalezas comunes (¿la región tiene buen H?)
   c. Outliers (¿quién destaca en qué?)
   d. Correlaciones (¿ciudades más grandes = mejor F?)
   e. Patrones C-R por grupo

5. ANÁLISIS NARRATIVO:
   - ¿Qué revela la comparación sobre la región?
   - ¿Dónde hay oportunidades de aprendizaje cruzado?
   - ¿Qué ciudad podría servir de modelo para qué dominio?
   - ¿Hay recursos compartibles (ej: programa nacional que solo opera en una)?
   - Si hay enfoque específico del usuario → profundizar ahí

6. OPCIONALMENTE leer reportes completos:
   - Si la comparación necesita contexto cualitativo
   - Leer output/[ciudad]_[pais] - phase1.md para actores, programas, contexto

7. ENTREGAR:
   a. Tabla comparativa
   b. Análisis narrativo (3-5 párrafos)
   c. Hallazgos clave (top 3-5)
   d. Recomendaciones regionales si aplica
   e. Guardar en output/comparativo_[fecha o descriptor].md
```

---

## Recursos

| Recurso | Path | Cuándo consultar |
|---------|------|-----------------|
| CSVs de indicadores | `output/*indicators.csv` | Siempre, son la fuente principal |
| Reportes de diagnóstico | `output/*phase1.md` | Para contexto cualitativo |
| Metodología | `drive/METODOLOGIA_ES.md` | Si necesita marco teórico para interpretación |
| Knowledge base | `knowledge/INDEX.md` | Si la comparación necesita respaldo teórico |

## Outputs
- `output/comparativo_[descriptor].md` — análisis comparativo completo
- Tabla comparativa incluida en el documento

## Checklist
- [ ] Todos los CSVs cargados correctamente
- [ ] Tabla comparativa con scores por dominio
- [ ] Patrones identificados (cuellos de botella, fortalezas, outliers)
- [ ] Análisis narrativo con hallazgos concretos
- [ ] Si aplica: recomendaciones regionales
- [ ] Archivo guardado en output/
