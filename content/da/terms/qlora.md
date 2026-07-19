---
title: QLoRA
term_id: qlora
category: training_techniques
subcategory: ''
tags:
- Optimization
- Fine-Tuning
- efficiency
difficulty: 4
weight: 1
slug: qlora
date: '2026-07-18T15:37:15.359737Z'
lastmod: '2026-07-18T17:15:09.248019Z'
draft: false
source: agnes_llm
status: published
language: da
description: Quantized Low-Rank Adaptation, en metode til effektiv finjustering af
  store sprogmodeller ved hjælp af 4-bit-kvantisering og lav-rang adaptere.
---
## Definition

QLoRA kombinerer Low-Rank Adaptation (LoRA) med 4-bit-kvantisering for betydeligt at reducere hukommelsesforbruget ved finjustering af massive modeller. Ved at gemme vægte i 4-bit-format og tilføje træningsbare adaptere gøres finjustering mulig på forbrugerhardware.

### Summary

Quantized Low-Rank Adaptation, en metode til effektiv finjustering af store sprogmodeller ved hjælp af 4-bit-kvantisering og lav-rang adaptere.

## Key Concepts

- Low-Rank Adaptation
- 4-bit-kvantisering
- Hukommelseseffektivitet
- Finjustering

## Use Cases

- Finjustering på forbruger-GPU'er
- Ressourcebegrænsede miljøer
- Hurtig modeliteration

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32, target_modules=["q_proj", "v_proj"])
model = get_peft_model(base_model, config)
```

## Related Terms

- [LoRA (Low-Rank Adaptation)](/en/terms/lora-low-rank-adaptation/)
- [PEFT (Parameter-Efficient Fine-Tuning)](/en/terms/peft-parameter-efficient-fine-tuning/)
- [Kvantisering (Nedsættelse af numerisk præcision)](/en/terms/kvantisering-nedsættelse-af-numerisk-præcision/)
- [Parameter-effektiv finjustering](/en/terms/parameter-effektiv-finjustering/)
