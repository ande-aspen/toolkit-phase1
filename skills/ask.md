# Consulta a la Base de Conocimiento

## Metadata
- **Comando:** /ask
- **Aliases:** /consulta
- **Idioma:** bilingüe (responde en el idioma de la pregunta)
- **Versión:** 1.0

## Descripción
Consulta conversacional a la base de conocimiento del agente. Busca en papers ingresados (`knowledge/`), referencias del diagnóstico (`drive/REFERENCES_MASTER.md`), y metodología ANDE para responder preguntas sobre ecosistemas emprendedores. Soporta preguntas sobre papers específicos, temas, dominios, comparaciones entre autores, y aplicación práctica.

## Trigger
- El usuario escribe `/ask [pregunta]` o `/consulta [pregunta]`
- El usuario hace una pregunta sobre ecosistemas, papers, literatura, o metodología
- El usuario quiere debatir ideas, conectar conceptos, o generar hipótesis

## Inputs
- Pregunta en lenguaje natural (español o inglés)
- Opcionalmente: contexto adicional sobre qué buscar o dónde enfocar

---

## Proceso

```
1. RECIBIR CONSULTA del usuario (lenguaje natural)

2. DETERMINAR ALCANCE:
   - Paper específico → "¿Qué dice Stam sobre cuellos de botella?"
   - Tema → "¿Qué sabemos sobre efectividad de aceleradoras?"
   - Dominio ANDE → "Todo sobre financiamiento en mercados emergentes"
   - Comparación → "¿Cómo difieren Isenberg y Stam en su definición de ecosistema?"
   - Aplicación → "¿Qué funcionaría para un ecosistema Naciente en cultura?"
   - Metodología → "¿Cómo mide ANDE el capital humano?"
   - Ciudad específica → "¿Qué diagnósticos tenemos de México?"

3. BUSCAR EN FUENTES (en orden de prioridad):
   a. Leer knowledge/INDEX.md → identificar papers relevantes por tema/dominio
   b. Leer los papers específicos identificados en knowledge/papers/
   c. Si la consulta toca diagnóstico ANDE o dominios específicos:
      - Leer los índices de drive/REFERENCES_MASTER.md (por dominio o tema)
      - Leer los extractos relevantes identificados
   d. Si la consulta toca metodología:
      - Leer drive/METODOLOGIA_ES.md o _EN.md según idioma
   e. Si la consulta se relaciona con una ciudad diagnosticada:
      - Revisar output/ para CSVs y reportes existentes

4. SINTETIZAR RESPUESTA:
   - Citar fuentes: "Según [Autor] ([Año]), [insight]"
   - Cross-referenciar cuando múltiples fuentes coinciden o difieren
   - Conectar con el framework ANDE cuando sea relevante
   - Ser conversacional pero basado en evidencia
   - Si hay tensiones o debates entre autores, exponerlos
   - Si la pregunta tiene implicaciones prácticas, conectar con recomendaciones

5. SUGERIR SEGUIMIENTO:
   - Preguntas de profundización
   - Papers que podrían complementar lo encontrado
   - Si no hay suficiente información en la KB, decirlo honestamente
     y sugerir: qué tipo de paper abordaría el tema,
     u ofrecer buscar en web como alternativa

6. SI LA KB NO TIENE CONTENIDO RELEVANTE:
   - Decirlo directamente: "La base de conocimiento no tiene papers sobre [tema]"
   - Ofrecer alternativas:
     a. Responder con conocimiento general (marcando que no viene de la KB)
     b. Buscar en web
     c. Sugerir qué tipo de paper ingerir para cubrir el gap
```

---

## Recursos

| Recurso | Path | Cuándo consultar |
|---------|------|-----------------|
| Índice de KB | `knowledge/INDEX.md` | Siempre, para discovery |
| Papers individuales | `knowledge/papers/*.md` | Los que el índice identifique como relevantes |
| Referencias diagnóstico | `drive/REFERENCES_MASTER.md` | Si toca temas ANDE/diagnóstico |
| Metodología ANDE | `drive/METODOLOGIA_ES.md` o `_EN.md` | Si toca metodología |
| Diagnósticos existentes | `output/*.csv`, `output/*.md` | Si pregunta sobre ciudades |

## Outputs
- Respuesta conversacional en chat con citas y cross-referencias
- No genera archivos (es solo consulta)

## Checklist
- [ ] Fuentes consultadas citadas con autor y año
- [ ] Respuesta basada en evidencia de la KB (no inventada)
- [ ] Si la KB no tiene info, declarado transparentemente
- [ ] Preguntas de seguimiento sugeridas
