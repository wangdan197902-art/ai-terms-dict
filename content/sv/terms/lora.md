---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
date: "2026-07-18T15:28:16.200247Z"
lastmod: "2026-07-18T17:15:08.945340Z"
draft: false
source: "agnes_llm"
status: "published"
language: "sv"
description: "Low-Rank Adaptation är en parameter-effektiv metod för finjustering som injicerar tränbara rangdekompositions-matriser i befintliga modellvikter."
---
## Definition

LoRA fryser förtränade modellvikter och infogar tränbara dekompositions-matriser i varje lager av transformerarkitekturen. Genom att endast optimera dessa lågrankade matriser reducerar LoRA avsevärt

### Summary

Low-Rank Adaptation är en parameter-effektiv metod för finjustering som injicerar tränbara rangdekompositions-matriser i befintliga modellvikter.

## Key Concepts

- Parameter-effektiv finjustering
- Rangdekomposition
- Frysning av vikter
- Adapter-moduler

## Use Cases

- Anpassning av stora språkmodeller
- Domänspecifik anpassning
- Träning med begränsade resurser

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning)](/en/terms/peft-parameter-efficient-fine-tuning/)
- [Finjustering](/en/terms/finjustering/)
- [Kvantisering](/en/terms/kvantisering/)
