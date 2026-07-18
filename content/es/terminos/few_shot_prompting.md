---
title: "Inducción por Ejemplos (Few-Shot Prompting)"
term_id: "few_shot_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["prompting", "llm", "technique"]
difficulty: 2
weight: 1
slug: "few_shot_prompting"
aliases:
  - /es/terms/few_shot_prompting/
date: "2026-07-18T10:30:29.634927Z"
lastmod: "2026-07-18T11:44:44.762536Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "La inducción por ejemplos es una técnica en la que se proporcionan a los LLM un pequeño número de ejemplos de entrada-salida dentro del prompt para guiar su comportamiento."
---

## Definition

Este método aprovecha las capacidades de aprendizaje en contexto de los grandes modelos de lenguaje proporcionando algunos ejemplos ilustrativos directamente en el prompt. A diferencia del ajuste fino (fine-tuning), que requiere actualizar los pesos del modelo, esta técnica guía al modelo mediante el contexto textual inmediato, demostrándole el formato o el razonamiento deseado sin necesidad de reentrenamiento.

### Summary

La inducción por ejemplos es una técnica en la que se proporcionan a los LLM un pequeño número de ejemplos de entrada-salida dentro del prompt para guiar su comportamiento.

## Key Concepts

- Aprendizaje en contexto
- Ingeniería de prompts
- Orientación basada en ejemplos
- Comparación con cero ejemplos

## Use Cases

- Formato para análisis de sentimiento
- Adaptación de estilo de código
- Extracción de datos estructurados

## Code Example

```python
response = llm.generate(
    prompt="Translate English to French:\n"
           "Hello -> Bonjour\n"
           "World -> Monde\n"
           "Cat -> ?"
)
```

## Related Terms

- [zero_shot (cero ejemplos)](/en/terms/zero_shot-cero-ejemplos/)
- [prompt_engineering (ingeniería de prompts)](/en/terms/prompt_engineering-ingeniería-de-prompts/)
- [in_context_learning (aprendizaje en contexto)](/en/terms/in_context_learning-aprendizaje-en-contexto/)
- [llm (gran modelo de lenguaje)](/en/terms/llm-gran-modelo-de-lenguaje/)
