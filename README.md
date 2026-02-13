# Ecosystem Expert Agent

Agente experto en ecosistemas emprendedores. Construido sobre la metodología ANDE y una base de conocimiento creciente.

## Skills

| Comando | Qué hace |
|---------|----------|
| `/diagnostico` | Diagnóstico ANDE Fase 1 completo (30 indicadores, 7 dominios, reporte, radar) |
| `/research` | Research automatizado de ecosistema (8 rondas de búsqueda web) |
| `/ingest` | Ingerir paper o artículo a la base de conocimiento |
| `/ask` | Consultar la base de conocimiento |
| `/report` | Generar reporte personalizado |
| `/compare` | Comparar ecosistemas diagnosticados |

## Quick Start

**Diagnosticar un ecosistema:**
```
/research Hermosillo, Sonora, México, 950000
→ genera documento de research en input/
/diagnostico
→ parsea, puntúa, genera reporte y radar en output/
```

**Alimentar la base de conocimiento:**
```
/ingest [path al PDF o texto del paper]
→ procesa, clasifica, indexa en knowledge/
```

**Consultar:**
```
/ask ¿Qué dice la literatura sobre efectividad de aceleradoras en LatAm?
```

## Estructura

```
ande-toolkit/
├── CLAUDE.md              ← Cerebro del agente
├── skills/                ← Definiciones de skills (1 archivo por skill)
├── knowledge/             ← Base de conocimiento creciente (papers, índice)
├── references/            ← Recursos del diagnóstico ANDE
├── guides/                ← Guías de humanización (ES/EN)
├── drive/                 ← Metodología ANDE y 30 referencias master
├── input/                 ← Documentos de research por ciudad
└── output/                ← Entregables generados
```
