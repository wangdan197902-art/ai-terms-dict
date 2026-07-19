---
title: Resumen
term_id: summarization
category: application_paradigms
subcategory: ''
tags:
- NLP
- Text Processing
- applications
difficulty: 3
weight: 1
slug: summarization
date: '2026-07-18T10:32:20.236413Z'
lastmod: '2026-07-18T11:44:44.767242Z'
draft: false
source: agnes_llm
status: published
language: es
description: Una tarea de PLN que genera un resumen conciso y coherente de un texto
  más largo, preservando su información clave.
---
## Definition

La generación de resúmenes de texto reduce grandes volúmenes de texto a versiones más cortas sin perder el significado crítico. Puede ser extractiva, seleccionando oraciones importantes del texto original, o abstractiva, generando nuevas frases que capturan la esencia.

### Summary

Una tarea de PLN que genera un resumen conciso y coherente de un texto más largo, preservando su información clave.

## Key Concepts

- Resumen Extractivo
- Resumen Abstractivo
- Densidad de Información
- Coherencia

## Use Cases

- Condensación de artículos de noticias
- Generación de actas de reuniones
- Revisión de documentos legales

## Code Example

```python
from transformers import pipeline
summarizer = pipeline("summarization")
result = summarizer("AI is transforming industries...", max_length=50, min_length=10)[0]['summary_text']
```

## Related Terms

- [PLN (Procesamiento de Lenguaje Natural)](/en/terms/pln-procesamiento-de-lenguaje-natural/)
- [Modelos Transformer (Arquitectura base)](/en/terms/modelos-transformer-arquitectura-base/)
- [BERT (Modelo de lenguaje)](/en/terms/bert-modelo-de-lenguaje/)
- [T5 (Modelo de texto a texto)](/en/terms/t5-modelo-de-texto-a-texto/)
