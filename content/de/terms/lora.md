---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
date: "2026-07-18T10:51:11.932679Z"
lastmod: "2026-07-18T11:44:44.877352Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Low-Rank Adaptation ist eine parameter-effiziente Feinabstimmungsmethode, die trainierbare Rang-Zerlegungsmatrizen in bestehende Modellgewichte einfügt."
---
## Definition

LoRA friert die vorab trainierten Modellgewichte ein und fügt jeder Schicht der Transformer-Architektur trainierbare Zerlegungsmatrizen hinzu. Durch die Optimierung nur dieser niedrigdimensionalen Matrizen reduziert LoRA erheblich...

### Summary

Low-Rank Adaptation ist eine parameter-effiziente Feinabstimmungsmethode, die trainierbare Rang-Zerlegungsmatrizen in bestehende Modellgewichte einfügt.

## Key Concepts

- Parameter-effiziente Feinabstimmung
- Rangzerlegung
- Einfrieren der Gewichte
- Adapter-Module

## Use Cases

- Anpassung von LLMs
- Domänenspezifische Anpassung
- Training unter Ressourcenbeschränkungen

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning)](/en/terms/peft-parameter-efficient-fine-tuning/)
- [Fine-Tuning (Feinabstimmung)](/en/terms/fine-tuning-feinabstimmung/)
- [Quantisierung](/en/terms/quantisierung/)
