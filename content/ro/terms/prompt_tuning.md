---
title: Ajustarea prompturilor (Prompt Tuning)
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
date: '2026-07-18T16:17:22.615043Z'
lastmod: '2026-07-18T17:15:09.694391Z'
draft: false
source: agnes_llm
status: published
language: ro
description: O metodă eficientă din punct de vedere al parametrilor pentru rafinare,
  care optimizează încorporările continue ale intrărilor, în loc să actualizeze întregii
  greutăți ale modelului.
---
## Definition

Ajustarea prompturilor implică adăugarea de prompturi antrenabile (vectori continui) la stratul de intrare al unui model de limbaj pre-antrenat, păstrând parametrii modelului subiacent fixați. Această abordare permite adaptarea rapidă a modelelor mari fără costuri ridicate de calcul.

### Summary

O metodă eficientă din punct de vedere al parametrilor pentru rafinare, care optimizează încorporările continue ale intrărilor, în loc să actualizeze întregii greutăți ale modelului.

## Key Concepts

- prompturi moi (soft prompts)
- eficiență parametrică
- greutăți fixe (frozen weights)
- învățare few-shot

## Use Cases

- Adaptarea modelelor de limbaj mari (LLM) pentru domenii specifice
- Rafinare cu resurse limitate
- Optimizarea învățării multi-sarcină

## Related Terms

- [PEFT (Efficient Fine-Tuning)](/en/terms/peft-efficient-fine-tuning/)
- [LoRA (Low-Rank Adaptation)](/en/terms/lora-low-rank-adaptation/)
- [învățare în context (In-context Learning)](/en/terms/învățare-în-context-in-context-learning/)
- [rafinare (Fine-tuning)](/en/terms/rafinare-fine-tuning/)
