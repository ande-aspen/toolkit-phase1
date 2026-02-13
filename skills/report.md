# Reporte Personalizado

## Metadata
- **Comando:** /report
- **Aliases:** /reporte
- **Idioma:** bilingüe (según instrucción del usuario o idioma de la sesión)
- **Versión:** 1.0

## Descripción
Genera reportes personalizados sobre ecosistemas emprendedores según las instrucciones del usuario. No es el diagnóstico ANDE estándar (para eso usar `/diagnostico`), sino reportes de formato libre: temáticos, policy briefs, análisis sectoriales, resúmenes ejecutivos, etc. Se alimenta de la base de conocimiento, diagnósticos existentes, y datos proporcionados por el usuario.

## Trigger
- El usuario escribe `/report` o `/reporte`
- El usuario pide un reporte, brief, análisis, o documento que no es el diagnóstico ANDE estándar
- El usuario da instrucciones específicas sobre qué tipo de documento quiere

## Inputs
- **Obligatorio:** instrucciones del usuario sobre el reporte (qué, para quién, enfoque)
- **Opcional:** datos o fuentes específicas a usar
- **Opcional:** formato, extensión, idioma, audiencia
- **Opcional:** template o estructura que el usuario quiera seguir

---

## Proceso

```
1. RECIBIR INSTRUCCIONES:
   - Qué tipo de reporte
   - Qué datos/fuentes usar
   - Audiencia objetivo
   - Idioma
   - Extensión y formato preferido
   - Si el usuario proporciona un template → seguirlo

2. IDENTIFICAR FUENTES RELEVANTES:
   a. knowledge/INDEX.md → papers sobre el tema
   b. drive/REFERENCES_MASTER.md → si toca temas ANDE
   c. drive/METODOLOGIA_ES.md o _EN.md → si necesita marco teórico
   d. output/ → diagnósticos existentes si el reporte los necesita
   e. input/ → documentos de research si son relevantes
   f. Datos proporcionados por el usuario en chat

3. PROPONER ESTRUCTURA:
   - Presentar outline al usuario antes de escribir
   - Incluir: secciones propuestas, fuentes que se usarán, extensión estimada
   - Esperar aprobación o ajustes

4. REDACTAR:
   - Seguir la estructura aprobada
   - Citar fuentes con autor y año
   - Usar datos concretos, no generalidades
   - Tono: depende de la audiencia (académico, ejecutivo, policy, divulgación)

5. HUMANIZAR:
   - Español → aplicar guides/editor-humano.md
   - English → aplicar guides/humanizer.md

6. ENTREGAR:
   - Guardar en output/[nombre-descriptivo].md
   - Presentar resumen de lo producido
   - Ofrecer iteraciones
```

---

## Recursos

| Recurso | Path | Cuándo consultar |
|---------|------|-----------------|
| Índice de KB | `knowledge/INDEX.md` | Para buscar papers relevantes |
| Papers | `knowledge/papers/*.md` | Los relevantes al tema |
| Referencias ANDE | `drive/REFERENCES_MASTER.md` | Si el reporte toca diagnóstico |
| Metodología | `drive/METODOLOGIA_ES.md` o `_EN.md` | Si necesita marco teórico |
| Diagnósticos | `output/*.csv`, `output/*.md` | Si usa datos de ciudades |
| Humanizador | `guides/editor-humano.md` o `humanizer.md` | Post-redacción |

## Outputs
- `output/[nombre-descriptivo].md` — el reporte
- Cualquier visualización adicional si aplica

## Checklist
- [ ] Estructura aprobada por el usuario antes de redactar
- [ ] Fuentes citadas con autor y año
- [ ] Datos concretos, no generalidades
- [ ] Tono apropiado para la audiencia
- [ ] Humanización aplicada
- [ ] Archivo guardado en output/
