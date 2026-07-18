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
  - /no/terms/prompt_tuning/
date: "2026-07-18T16:13:05.722359Z"
lastmod: "2026-07-18T16:38:07.036549Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "En parameter-effektiv finjusteringsmetode som optimaliserer kontinuerlige input-embeddings i stedet for å oppdatere hele modellvektene."
---

## Definition

Prompt-tuning innebærer å legge til trenbare 'soft prompts' (kontinuerlige vektorer) til inngangslaget av en forhåndstrenet språkmodell, mens de underliggende modellparameterene holdes låst. Denne tilnærmingen lar modellen tilpasses spesifikke oppgaver uten å endre den grunnleggende arkitekturen.

### Summary

En parameter-effektiv finjusteringsmetode som optimaliserer kontinuerlige input-embeddings i stedet for å oppdatere hele modellvektene.

## Key Concepts

- soft prompts (bløde instruksjoner)
- parameter-effektivitet
- låste vekter
- few-shot learning (læring med få eksempler)

## Use Cases

- Tilpasning av store språkmodeller (LLMs) til spesifikke domener
- Finjustering med lave ressurser
- Optimalisering av fleroppgavelæring

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning / parameter-effektiv finjustering)](/en/terms/peft-parameter-efficient-fine-tuning-parameter-effektiv-finjustering/)
- [LoRA (Low-Rank Adaptation / lav-rang tilpasning)](/en/terms/lora-low-rank-adaptation-lav-rang-tilpasning/)
- [in-context learning (læring i konteksten)](/en/terms/in-context-learning-læring-i-konteksten/)
- [fine-tuning (finjustering)](/en/terms/fine-tuning-finjustering/)
