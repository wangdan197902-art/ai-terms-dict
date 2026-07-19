---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
date: "2026-07-18T15:26:45.381560Z"
lastmod: "2026-07-18T17:15:09.597325Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "Adaptarea de Rang Scăzut este o metodă de rafinare eficientă din punct de vedere al parametrilor care injectează matrici antrenabile de descompunere de rang în ponderile existente ale modelului."
---
## Definition

LoRA îngheață ponderile modelului pre-antrenat și inserează matrici antrenabile de descompunere în fiecare strat al arhitecturii Transformer. Prin optimizarea doar a acestor matrici de rang scăzut, LoRA reduce semnificativ

### Summary

Adaptarea de Rang Scăzut este o metodă de rafinare eficientă din punct de vedere al parametrilor care injectează matrici antrenabile de descompunere de rang în ponderile existente ale modelului.

## Key Concepts

- Rafinarea Eficientă a Parametrilor
- Descompunerea de Rang
- Înghețarea Ponderilor
- Module Adaptor

## Use Cases

- Personalizarea LLM-urilor
- Adaptarea Specifică Domeniului
- Antrenamentul cu Resurse Limitate

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT](/en/terms/peft/)
- [Rafinare (Fine-Tuning)](/en/terms/rafinare-fine-tuning/)
- [Cuantizare](/en/terms/cuantizare/)
