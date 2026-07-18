---
title: "Apprendimento nel Contesto"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
aliases:
  - /it/terms/in_context_learning/
date: "2026-07-18T15:22:57.448280Z"
lastmod: "2026-07-18T17:15:08.560518Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Una tecnica in cui i modelli imparano a eseguire compiti osservando esempi forniti nel prompt."
---

## Definition

L'apprendimento nel contesto (ICL) consente ai grandi modelli linguistici di adattarsi a nuovi compiti senza aggiornare i loro pesi. Fornendo coppie input-output all'interno del contesto del prompt, il modello inferisce il modello e

### Summary

Una tecnica in cui i modelli imparano a eseguire compiti osservando esempi forniti nel prompt.

## Key Concepts

- Apprendimento Few-Shot
- Zero-Shot
- Progettazione del Prompt
- Adattamento Senza Pesi

## Use Cases

- Test rapido delle capacità del modello su nuovi dataset
- Cambio dinamico di compito negli agenti conversazionali
- Prototipazione di applicazioni IA senza riaddestramento

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Ingegneria dei Prompt (ottimizzazione degli input per guidare il modello)](/en/terms/ingegneria-dei-prompt-ottimizzazione-degli-input-per-guidare-il-modello/)
- [Few-Shot (apprendimento da pochi esempi)](/en/terms/few-shot-apprendimento-da-pochi-esempi/)
- [Zero-Shot (esecuzione senza esempi precedenti)](/en/terms/zero-shot-esecuzione-senza-esempi-precedenti/)
- [Meta-Apprendimento (apprendimento su come imparare)](/en/terms/meta-apprendimento-apprendimento-su-come-imparare/)
