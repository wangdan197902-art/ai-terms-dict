---
title: "Prompt-tuning"
term_id: "prompt_tuning"
category: "training_techniques"
subcategory: ""
tags: ["LLM", "optimization", "efficiency"]
difficulty: 3
weight: 1
slug: "prompt_tuning"
aliases:
  - /da/terms/prompt_tuning/
date: "2026-07-18T16:13:10.404312Z"
lastmod: "2026-07-18T17:15:09.323643Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "En metode til finjustering med effektiv parameterbrug, der optimerer kontinuerlige input-embeddings frem for at opdatere hele modellens vægte."
---

## Definition

Prompt-tuning indebærer tilføjelsen af trænbare 'bløde prompts' (kontinuerlige vektorer) til inputlaget af en fortrænelt sprogmodel, mens de underliggende modelparametre holdes frosne. Denne tilgang gør det muligt at tilpasse modellen uden at genberegne alle parametre.

### Summary

En metode til finjustering med effektiv parameterbrug, der optimerer kontinuerlige input-embeddings frem for at opdatere hele modellens vægte.

## Key Concepts

- bløde prompts
- effektiv parameterbrug
- frosne vægte
- few-shot learning (læring med få eksempler)

## Use Cases

- Tilpasning af store sprogmodeller (LLM'er) til specifikke domæner
- Finjustering med lav ressourceforbrug
- Optimering af multi-task læring

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning / Finjustering med effektiv parameterbrug)](/en/terms/peft-parameter-efficient-fine-tuning-finjustering-med-effektiv-parameterbrug/)
- [LoRA (Low-Rank Adaptation / Tilpasning med lav rang)](/en/terms/lora-low-rank-adaptation-tilpasning-med-lav-rang/)
- [in-context learning (læring i konteksten)](/en/terms/in-context-learning-læring-i-konteksten/)
- [fine-tuning (finjustering)](/en/terms/fine-tuning-finjustering/)
