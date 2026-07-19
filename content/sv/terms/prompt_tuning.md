---
title: Prompt-tuning
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
date: '2026-07-18T16:14:46.969978Z'
lastmod: '2026-07-18T17:15:09.039090Z'
draft: false
source: agnes_llm
status: published
language: sv
description: En metod för finjustering som är effektiv med avseende på parametrar,
  där kontinuerliga inbäddningar optimeras istället för att hela modellens vikter
  uppdateras.
---
## Definition

Prompt-tuning innebär att tränbara mjuka prompts (kontinuerliga vektorer) läggs till i inmatningslagret av en förtränad språkmodell, medan de underliggande modellparametrarna hålls frysta. Denna metod gör det möjligt att anpassa modeller till specifika uppgifter med minimal beräkningskostnad.

### Summary

En metod för finjustering som är effektiv med avseende på parametrar, där kontinuerliga inbäddningar optimeras istället för att hela modellens vikter uppdateras.

## Key Concepts

- mjuka prompts
- effektivitetsoptimering av parametrar
- frysta vikter
- few-shot learning

## Use Cases

- Anpassning av stora språkmodeller (LLM) för specifika domäner
- Finjustering vid resursbegränsningar
- Optimering av multitask-inlärning

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning)](/en/terms/peft-parameter-efficient-fine-tuning/)
- [LoRA (Low-Rank Adaptation)](/en/terms/lora-low-rank-adaptation/)
- [in-context learning](/en/terms/in-context-learning/)
- [finjustering](/en/terms/finjustering/)
