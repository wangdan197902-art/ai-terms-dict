---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
date: "2026-07-18T15:27:26.350415Z"
lastmod: "2026-07-18T16:38:06.940128Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "Low-Rank Adaptation er en parameter-effektiv finjusteringsmetode som injiserer trenbare rang-dekomponeringsmatriser i eksisterende modellvekter."
---
## Definition

LoRA fryser forhåndstrengte modellvekter og setter inn trenbare dekomponeringsmatriser i hvert lag av transformer-arkitekturen. Ved å optimalisere kun disse lav-rang matrisene, reduserer LoRA betydelig

### Summary

Low-Rank Adaptation er en parameter-effektiv finjusteringsmetode som injiserer trenbare rang-dekomponeringsmatriser i eksisterende modellvekter.

## Key Concepts

- Parameter-effektiv finjustering
- Rang-dekomponering
- Frysing av vekter
- Adapter-moduler

## Use Cases

- Tilpasning av store språkmodeller
- Domenespesifikk tilpasning
- Trening med begrensede ressurser

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (Parameter-Effektive Finjusteringsteknikker)](/en/terms/peft-parameter-effektive-finjusteringsteknikker/)
- [Finjustering](/en/terms/finjustering/)
- [Kvantisering](/en/terms/kvantisering/)
