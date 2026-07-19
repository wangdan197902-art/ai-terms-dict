---
title: Prefix-tuning
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
date: '2026-07-18T16:13:57.245127Z'
lastmod: '2026-07-18T17:15:09.037563Z'
draft: false
source: agnes_llm
status: published
language: sv
description: En parameter-effektiv finjusteringsmetod som lägger till träningsbara
  kontinuerliga vektorer till ingången av transformatorlager.
---
## Definition

Prefix-tuning är en parameter-effektiv anpassningsteknik för förtränade transformatorer. Istället för att uppdatera alla modellviktningar, förbereds en sekvens av träningsbara kontinuerliga vektorer (prefixet) till de dolda tillstånden i varje transformatorlager. Detta gör det möjligt att anpassa modellen till nya uppgifter med mycket få uppdaterbara parametrar.

### Summary

En parameter-effektiv finjusteringsmetod som lägger till träningsbara kontinuerliga vektorer till ingången av transformatorlager.

## Key Concepts

- Parameter-effektiv justering
- Mjuka prompts
- Transformatorlager
- Frysta ryggradsnät

## Use Cases

- Anpassning för few-shot-inlärning
- Multitask-inlärning med begränsade resurser
- Anpassning av stora språkmodeller för nischade domäner

## Related Terms

- [prompt_tuning (prompt-justering)](/en/terms/prompt_tuning-prompt-justering/)
- [p_tuning (prompt-tuning)](/en/terms/p_tuning-prompt-tuning/)
- [adapter_modules (adaptermoduler)](/en/terms/adapter_modules-adaptermoduler/)
- [peft (parameter-efficient fine-tuning)](/en/terms/peft-parameter-efficient-fine-tuning/)
