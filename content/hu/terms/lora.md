---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
aliases:
  - /hu/terms/lora/
date: "2026-07-18T15:27:31.373026Z"
lastmod: "2026-07-18T17:15:09.723722Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "A Low-Rank Adaptation (Alacsony rangú adaptáció) egy paraméter-hatékony finomhangolási módszer, amely betanítható rang-dekompozíciós mátrixokat injektál a meglévő modell súlyokba."
---

## Definition

A LoRA felfüggeszti (fagyasztja) az előre betanított modell súlyait, és betanítható dekompozíciós mátrixokat helyez el a transzformátor architektúra minden rétegében. Csak ezeknek az alacsony rangú mátrixoknak az optimalizálásával a LoRA jelentősen csökkenti...

### Summary

A Low-Rank Adaptation (Alacsony rangú adaptáció) egy paraméter-hatékony finomhangolási módszer, amely betanítható rang-dekompozíciós mátrixokat injektál a meglévő modell súlyokba.

## Key Concepts

- Paraméter-hatékony finomhangolás (PEFT)
- Rang-dekompozíció
- Súlyok fagyasztása
- Adapter modulok

## Use Cases

- LLM testreszabása
- Domain-specifikus adaptáció
- Erőforrás-korlátozott tanítás

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning)](/en/terms/peft-parameter-efficient-fine-tuning/)
- [Finomhangolás (Fine-tuning)](/en/terms/finomhangolás-fine-tuning/)
- [Kvantálás (Quantization)](/en/terms/kvantálás-quantization/)
