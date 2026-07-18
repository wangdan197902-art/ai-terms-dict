---
title: "Prompting de Cadena de Pensamiento"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
aliases:
  - /es/terms/chain_of_thought_prompting/
date: "2026-07-18T10:29:46.972300Z"
lastmod: "2026-07-18T11:44:44.760769Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "El Prompting de Cadena de Pensamiento es una técnica que anima a los Modelos de Lenguaje Grandes a generar pasos de razonamiento intermedios antes de producir una respuesta final."
---

## Definition

El prompting de Cadena de Pensamiento (CoT) mejora el rendimiento de los grandes modelos de lenguaje en tareas de razonamiento complejo al solicitar explícitamente al modelo que articule su lógica paso a paso. En lugar de saltar directamente a la conclusión, el modelo desglosa el problema, lo que aumenta la precisión y la transparencia del razonamiento.

### Summary

El Prompting de Cadena de Pensamiento es una técnica que anima a los Modelos de Lenguaje Grandes a generar pasos de razonamiento intermedios antes de producir una respuesta final.

## Key Concepts

- Razonamiento Paso a Paso
- Aprendizaje Few-Shot
- Deducción Lógica
- Pasos Intermedios

## Use Cases

- Resolución de problemas matemáticos verbales
- Tareas complejas de razonamiento lógico
- Depuración de errores en la generación de código

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Prompting Zero-Shot (Sin ejemplos previos)](/en/terms/prompting-zero-shot-sin-ejemplos-previos/)
- [Prompting Few-Shot (Con pocos ejemplos)](/en/terms/prompting-few-shot-con-pocos-ejemplos/)
- [Autoconsistencia (Método de verificación)](/en/terms/autoconsistencia-método-de-verificación/)
- [Razonamiento (Capacidad cognitiva simulada)](/en/terms/razonamiento-capacidad-cognitiva-simulada/)
