---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
date: "2026-07-18T10:51:21.827437Z"
lastmod: "2026-07-18T11:44:45.165853Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fr"
description: "L'adaptation à faible rang est une méthode d'ajustement fin efficace en paramètres qui injecte des matrices de décomposition de rang entraînable dans les poids existants du modèle."
---
## Definition

LoRA gèle les poids pré-entraînés du modèle et insère des matrices de décomposition entraînables dans chaque couche de l'architecture Transformeur. En optimisant uniquement ces matrices de faible rang, LoRA réduit considérablement

### Summary

L'adaptation à faible rang est une méthode d'ajustement fin efficace en paramètres qui injecte des matrices de décomposition de rang entraînable dans les poids existants du modèle.

## Key Concepts

- Ajustement fin efficace en paramètres
- Décomposition de rang
- Gel des poids
- Modules adaptateurs

## Use Cases

- Personnalisation des LLM
- Adaptation spécifique au domaine
- Entraînement sous contraintes de ressources

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT](/en/terms/peft/)
- [Ajustement fin (Fine-Tuning)](/en/terms/ajustement-fin-fine-tuning/)
- [Quantification](/en/terms/quantification/)
