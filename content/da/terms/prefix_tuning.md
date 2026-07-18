---
title: "Prefix-tuning"
term_id: "prefix_tuning"
category: "training_techniques"
subcategory: ""
tags: ["fine_tuning", "efficiency", "transformers"]
difficulty: 4
weight: 1
slug: "prefix_tuning"
aliases:
  - /da/terms/prefix_tuning/
date: "2026-07-18T16:12:25.222708Z"
lastmod: "2026-07-18T17:15:09.322139Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "En parameter-effektiv finjusteringsmetode, der tilføjer trainable kontinuerlige vektorer til inputtet af transformer-lag."
---

## Definition

Prefix-tuning er en parameter-effektiv tilpasningsteknik til for-trænede transformere. I stedet for at opdatere alle modelvægte, tilføjes en sekvens af trainable kontinuerlige vektorer (prefixet) til inputtet af hvert transformer-lag, hvilket tillader effektiv tilpasning med få opdaterbare parametre.

### Summary

En parameter-effektiv finjusteringsmetode, der tilføjer trainable kontinuerlige vektorer til inputtet af transformer-lag.

## Key Concepts

- Parameter-effektiv tuning
- Bløde prompts (soft prompts)
- Transformer-lag
- Frosset rygrad (frozen backbone)

## Use Cases

- Tilpasning til few-shot læring
- Multitask-læring med begrænsede ressourcer
- Tilpasning af store sprogmodeller til nischede domæner

## Related Terms

- [prompt_tuning (prompt-tuning)](/en/terms/prompt_tuning-prompt-tuning/)
- [p_tuning (P-tuning)](/en/terms/p_tuning-p-tuning/)
- [adapter_modules (adapter-moduler)](/en/terms/adapter_modules-adapter-moduler/)
- [peft (parameter-effektiv finjustering)](/en/terms/peft-parameter-effektiv-finjustering/)
