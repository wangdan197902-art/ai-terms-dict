---
title: Prompt Tuning
term_id: prompt_tuning
category: training_techniques
subcategory: ''
tags:
- LLM
- Optimization
- efficiency
difficulty: 3
weight: 1
slug: prompt_tuning
date: '2026-07-18T16:17:13.628701Z'
lastmod: '2026-07-18T17:15:08.660850Z'
draft: false
source: agnes_llm
status: published
language: it
description: Un metodo di affinamento efficiente nei parametri che ottimizza gli embedding
  continui di input anziché aggiornare i pesi dell'intero modello.
---
## Definition

Il prompt tuning consiste nell'aggiungere prompt morbidi addestrabili (vettori continui) allo strato di input di un modello linguistico pre-addestrato, mantenendo congelati i parametri sottostanti del modello. Questo approccio consente

### Summary

Un metodo di affinamento efficiente nei parametri che ottimizza gli embedding continui di input anziché aggiornare i pesi dell'intero modello.

## Key Concepts

- prompt morbidi
- efficienza dei parametri
- pesi congelati
- apprendimento few-shot

## Use Cases

- Adattamento di LLM a domini specifici
- Affinamento con risorse limitate
- Ottimizzazione dell'apprendimento multi-task

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning)](/en/terms/peft-parameter-efficient-fine-tuning/)
- [LoRA (Low-Rank Adaptation)](/en/terms/lora-low-rank-adaptation/)
- [apprendimento nel contesto (in-context learning)](/en/terms/apprendimento-nel-contesto-in-context-learning/)
- [fine-tuning](/en/terms/fine-tuning/)
