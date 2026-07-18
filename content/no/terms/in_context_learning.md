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
  - /no/terms/in_context_learning/
date: "2026-07-18T15:23:00.635118Z"
lastmod: "2026-07-18T16:38:06.931544Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "En teknikk der modeller lærer å utføre oppgaver ved å observere eksempler gitt i prompten."
---

## Definition

Læring i kontekst (ICL) tillater store språkmodeller å tilpasse seg nye oppgaver uten å oppdatere vektene sine. Ved å gi inn-og-ut-data-par innenfor prompt-konteksten, infererer modellen mønsteret og kan utføre oppgaven umiddelbart.

### Summary

En teknikk der modeller lærer å utføre oppgaver ved å observere eksempler gitt i prompten.

## Key Concepts

- Læring med få eksempler
- Null-eksempel
- Prompt-design
- Vekt-fri tilpasning

## Use Cases

- Rask testing av modellens evner på nye datasett
- Dynamisk oppgavebytte i samtalerobotter
- Prototyping av AI-applikasjoner uten omtrening

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Prompt-ingeniørkunst](/en/terms/prompt-ingeniørkunst/)
- [Få-eksempel](/en/terms/få-eksempel/)
- [Null-eksempel](/en/terms/null-eksempel/)
- [Meta-læring](/en/terms/meta-læring/)
