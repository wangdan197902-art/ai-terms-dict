---
title: "LoRA (Low-Rank Adaptation)"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
aliases:
  - /da/terms/lora/
date: "2026-07-18T15:26:53.490710Z"
lastmod: "2026-07-18T17:15:09.227453Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "Low-Rank Adaptation er en parameter-effektiv finjusteringsmetode, der indsætter trainable rang-dekompositions-matricer i eksisterende modelvægte."
---

## Definition

LoRA fryser fortrænede modelvægte og indsætter trainable dekompositions-matricer i hvert lag af transformer-arkitekturen. Ved kun at optimere disse lav-rang matricer reducerer LoRA betydeligt

### Summary

Low-Rank Adaptation er en parameter-effektiv finjusteringsmetode, der indsætter trainable rang-dekompositions-matricer i eksisterende modelvægte.

## Key Concepts

- Parameter-effektiv finjustering
- Rang-dekomposition
- Frysning af vægte
- Adapter-moduler

## Use Cases

- Tilpasning af store sprogmodeller
- Domænespecifik tilpasning
- Træning under ressourcebegrænsninger

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning)](/en/terms/peft-parameter-efficient-fine-tuning/)
- [Finjustering (Fine-tuning)](/en/terms/finjustering-fine-tuning/)
- [Kvantisering](/en/terms/kvantisering/)
