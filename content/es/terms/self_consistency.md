---
title: "Autoconsistencia"
term_id: "self_consistency"
category: "training_techniques"
subcategory: ""
tags: ["LLM", "inference", "technique"]
difficulty: 4
weight: 1
slug: "self_consistency"
date: "2026-07-18T11:07:20.880656Z"
lastmod: "2026-07-18T11:44:44.852566Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "La autoconsistencia es una estrategia de decodificación donde se muestrean múltiples caminos de razonamiento y se selecciona la respuesta más frecuente como salida final."
---
## Definition

Principalmente utilizada con Modelos de Lenguaje Grande (LLM), esta técnica mejora la precisión generando varias respuestas diversas a un indicador mediante muestreo. En lugar de depender de la decodificación codiciosa (greedy), agrega las predicciones para obtener un resultado más robusto.

### Summary

La autoconsistencia es una estrategia de decodificación donde se muestrean múltiples caminos de razonamiento y se selecciona la respuesta más frecuente como salida final.

## Key Concepts

- Votación mayoritaria
- Estrategia de decodificación
- Razonamiento de LLM
- Reducción de alucinaciones

## Use Cases

- Problemas matemáticos con palabras
- Deducción lógica compleja
- Tareas de síntesis de código

## Related Terms

- [Cadena de pensamiento (técnica de razonamiento paso a paso)](/en/terms/cadena-de-pensamiento-técnica-de-razonamiento-paso-a-paso/)
- [Muestreo de temperatura (control de aleatoriedad en la generación)](/en/terms/muestreo-de-temperatura-control-de-aleatoriedad-en-la-generación/)
- [Métodos de conjunto (combinación de múltiples modelos)](/en/terms/métodos-de-conjunto-combinación-de-múltiples-modelos/)
- [Ingeniería de indicadores (diseño de prompts efectivos)](/en/terms/ingeniería-de-indicadores-diseño-de-prompts-efectivos/)
