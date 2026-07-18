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
  - /cs/terms/lora/
date: "2026-07-18T15:26:24.643405Z"
lastmod: "2026-07-18T17:15:09.072002Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Nízkorangová adaptace je metoda jemného doladění efektivního z hlediska parametrů, která vkládá trainovatelné matice rozkladu nízkého řádu do existujících vah modelu."
---

## Definition

LoRA zamrazí předtrénované váhy modelu a vloží trainovatelné matice rozkladu do každé vrstvy architektury transformátoru. Optimalizací pouze těchto matic nízkého řádu LoRA významně snižuje

### Summary

Nízkorangová adaptace je metoda jemného doladění efektivního z hlediska parametrů, která vkládá trainovatelné matice rozkladu nízkého řádu do existujících vah modelu.

## Key Concepts

- Jemné doladění efektivní z hlediska parametrů (PEFT)
- Rozklad řádu
- Zamrazení vah
- Adaptérní moduly

## Use Cases

- Přizpůsobování LLM
- Doménově specifická adaptace
- Trénování s omezenými zdroji

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (Parametr-efficient fine-tuning)](/en/terms/peft-parametr-efficient-fine-tuning/)
- [Jemné doladění (Fine-Tuning)](/en/terms/jemné-doladění-fine-tuning/)
- [Kvantizace](/en/terms/kvantizace/)
