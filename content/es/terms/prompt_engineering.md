---
title: "Ingeniería de Prompts"
term_id: "prompt_engineering"
category: "application_paradigms"
subcategory: ""
tags: ["LLM", "UX", "Optimization"]
difficulty: 2
weight: 1
slug: "prompt_engineering"
aliases:
  - /es/terms/prompt_engineering/
date: "2026-07-18T07:39:26.713988Z"
lastmod: "2026-07-18T11:44:44.579385Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "La práctica de diseñar y optimizar textos de entrada para guiar a los modelos de lenguaje grandes hacia salidas deseadas."
---

## Definition

La ingeniería de prompts implica crear entradas específicas, conocidas como prompts, para elicitar respuestas precisas, relevantes y de alta calidad de los modelos de IA generativa. Requiere comprender cómo los modelos interpretan las instrucciones y el contexto para generar el resultado óptimo.

### Summary

La práctica de diseñar y optimizar textos de entrada para guiar a los modelos de lenguaje grandes hacia salidas deseadas.

## Key Concepts

- Enmarcado contextual
- Aprendizaje few-shot
- Ajuste por instrucciones
- Optimización de tokens

## Use Cases

- Chatbots de atención al cliente automatizados
- Asistentes de generación de código
- Ayudas para la escritura creativa

## Code Example

```python
prompt = "Translate the following English text to French: 'Hello world'"
response = llm.generate(prompt)
```

## Related Terms

- [LLM (Modelo de Lenguaje Grande)](/en/terms/llm-modelo-de-lenguaje-grande/)
- [Chain-of-Thought (Cadena de Pensamiento)](/en/terms/chain-of-thought-cadena-de-pensamiento/)
- [RAG (Recuperación Aumentada por Generación)](/en/terms/rag-recuperación-aumentada-por-generación/)
- [Fine-tuning (Ajuste Fino)](/en/terms/fine-tuning-ajuste-fino/)
