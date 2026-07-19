---
title: Prefix Tuning
term_id: prefix_tuning
category: training_techniques
subcategory: ''
tags:
- Fine-Tuning
- efficiency
- transformers
difficulty: 4
weight: 1
slug: prefix_tuning
date: '2026-07-18T16:16:30.265877Z'
lastmod: '2026-07-18T17:15:08.659338Z'
draft: false
source: agnes_llm
status: published
language: it
description: Un metodo di affinamento efficiente nei parametri che aggiunge vettori
  continui addestrabili all'input degli strati del transformer.
---
## Definition

Il Prefix Tuning è una tecnica di adattamento efficiente nei parametri per i transformer pre-addestrati. Invece di aggiornare tutti i pesi del modello, prepone una sequenza di vettori continui addestrabili (il prefisso) agli input degli strati del transformer. Questo permette di specializzare il modello per compiti specifici mantenendo congelato il backbone pre-addestrato, riducendo drasticamente il costo computazionale e la memoria rispetto al fine-tuning completo.

### Summary

Un metodo di affinamento efficiente nei parametri che aggiunge vettori continui addestrabili all'input degli strati del transformer.

## Key Concepts

- Affinamento efficiente nei parametri
- Prompt soft
- Strati del transformer
- Backbone congelato

## Use Cases

- Adattamento per few-shot learning
- Apprendimento multi-compito con risorse limitate
- Personalizzazione di LLM per domini di nicchia

## Related Terms

- [prompt_tuning (prompt tuning)](/en/terms/prompt_tuning-prompt-tuning/)
- [p_tuning (p-tuning)](/en/terms/p_tuning-p-tuning/)
- [adapter_modules (moduli adapter)](/en/terms/adapter_modules-moduli-adapter/)
- [peft (parameter-efficient fine-tuning / affinamento efficiente nei parametri)](/en/terms/peft-parameter-efficient-fine-tuning-affinamento-efficiente-nei-parametri/)
