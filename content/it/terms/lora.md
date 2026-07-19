---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
date: "2026-07-18T15:26:09.314132Z"
lastmod: "2026-07-18T17:15:08.568933Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Low-Rank Adaptation è un metodo di affinamento efficiente nei parametri che inietta matrici di decomposizione di rango addestrabili nei pesi esistenti del modello."
---
## Definition

LoRA congela i pesi del modello pre-addestrato e inserisce matrici di decomposizione addestrabili in ciascuno strato dell'architettura Transformer. Ottimizzando solo queste matrici a basso rango, LoRA riduce significativamente

### Summary

Low-Rank Adaptation è un metodo di affinamento efficiente nei parametri che inietta matrici di decomposizione di rango addestrabili nei pesi esistenti del modello.

## Key Concepts

- Affinamento Efficiente nei Parametri
- Decomposizione di Rango
- Congelamento dei Pesi
- Moduli Adattatori

## Use Cases

- Personalizzazione degli LLM
- Adattamento Specifico per Dominio
- Addestramento con Risorse Limitate

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT](/en/terms/peft/)
- [Fine-Tuning](/en/terms/fine-tuning/)
- [Quantizzazione](/en/terms/quantizzazione/)
