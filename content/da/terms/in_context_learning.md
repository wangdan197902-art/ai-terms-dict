---
title: "Læring i kontekst"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
aliases:
  - /da/terms/in_context_learning/
date: "2026-07-18T15:22:59.182865Z"
lastmod: "2026-07-18T17:15:09.218484Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "En teknik, hvor modeller lærer at udføre opgaver ved at observere eksempler leveret i promptet."
---

## Definition

Læring i kontekst (ICL) tillader store sprogmodeller at tilpasse sig nye opgaver uden at opdatere deres vægte. Ved at give input-output-par inden for prompt-konteksten, infererer modellen mønsteret og kan løse opgaven umiddelbart.

### Summary

En teknik, hvor modeller lærer at udføre opgaver ved at observere eksempler leveret i promptet.

## Key Concepts

- Few-shot learning
- Zero-shot
- Prompt-design
- Vægtfri tilpasning

## Use Cases

- Hurtig test af modellens evner på nye datasæt
- Dynamisk opgaveskift i samtaleagenter
- Prototyping af AI-applikationer uden retræning

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Prompt-engineering (instruktionsdesign)](/en/terms/prompt-engineering-instruktionsdesign/)
- [Few-shot (få eksempler)](/en/terms/few-shot-få-eksempler/)
- [Zero-shot (ingen eksempler)](/en/terms/zero-shot-ingen-eksempler/)
- [Meta-learning (læring om læring)](/en/terms/meta-learning-læring-om-læring/)
