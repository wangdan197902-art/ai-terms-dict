---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
date: "2026-07-18T15:27:34.409272Z"
lastmod: "2026-07-18T17:15:08.687796Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Low-Rank Adaptation is een parameter-efficiënte methode voor fine-tuning die trainbare rangontbindingsmatrices injecteert in bestaande modelgewichten."
---
## Definition

LoRA bevriest voorgekochte modelgewichten en voegt trainbare decompositiematrices in elke laag van de Transformer-architectuur. Door alleen deze laag-rang matrices te optimaliseren, reduceert LoRA aanzienlijk...

### Summary

Low-Rank Adaptation is een parameter-efficiënte methode voor fine-tuning die trainbare rangontbindingsmatrices injecteert in bestaande modelgewichten.

## Key Concepts

- Parameter-efficiënte fine-tuning
- Rangontbinding
- Bevriezen van gewichten
- Adaptermodules

## Use Cases

- Aanpassen van LLM's
- Domeinspecifieke adaptatie
- Training met beperkte middelen

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning)](/en/terms/peft-parameter-efficient-fine-tuning/)
- [Fine-tuning](/en/terms/fine-tuning/)
- [Kwantisering](/en/terms/kwantisering/)
