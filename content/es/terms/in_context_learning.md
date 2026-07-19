---
title: "Aprendizaje en Contexto"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
date: "2026-07-18T07:40:08.332480Z"
lastmod: "2026-07-18T11:44:44.582135Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Una técnica donde los modelos aprenden a realizar tareas observando ejemplos proporcionados en el prompt."
---
## Definition

El aprendizaje en contexto (ICL) permite que los grandes modelos de lenguaje se adapten a nuevas tareas sin actualizar sus pesos. Al proporcionar pares entrada-salida dentro del contexto del prompt, el modelo infiere el patrón y realiza la tarea inmediatamente.

### Summary

Una técnica donde los modelos aprenden a realizar tareas observando ejemplos proporcionados en el prompt.

## Key Concepts

- Aprendizaje Few-Shot
- Cero Ejemplos (Zero-Shot)
- Diseño de Prompt
- Adaptación Sin Pesos

## Use Cases

- Probar rápidamente las capacidades del modelo en nuevos conjuntos de datos
- Cambio dinámico de tareas en agentes conversacionales
- Prototipado de aplicaciones de IA sin necesidad de reentrenamiento

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Ingeniería de Prompts (Creación de entradas efectivas)](/en/terms/ingeniería-de-prompts-creación-de-entradas-efectivas/)
- [Few-Shot (Uso de pocos ejemplos)](/en/terms/few-shot-uso-de-pocos-ejemplos/)
- [Zero-Shot (Sin ejemplos previos)](/en/terms/zero-shot-sin-ejemplos-previos/)
- [Meta-Aprendizaje (Aprender a aprender)](/en/terms/meta-aprendizaje-aprender-a-aprender/)
