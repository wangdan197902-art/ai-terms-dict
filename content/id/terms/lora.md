---
title: "LoRA"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
date: "2026-07-18T15:26:54.087914Z"
lastmod: "2026-07-18T16:38:07.396412Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Adaptasi Rank Rendah adalah metode penyetelan halus yang efisien terhadap parameter yang menyuntikkan matriks dekomposisi rank yang dapat dilatih ke dalam bobot model yang ada."
---
## Definition

LoRA membekukan bobot model pra-dilatih dan menyisipkan matriks dekomposisi yang dapat dilatih ke setiap lapisan arsitektur Transformer. Dengan mengoptimalkan hanya matriks rank rendah ini, LoRA secara signifikan mengurangi

### Summary

Adaptasi Rank Rendah adalah metode penyetelan halus yang efisien terhadap parameter yang menyuntikkan matriks dekomposisi rank yang dapat dilatih ke dalam bobot model yang ada.

## Key Concepts

- Penyetelan Halus Efisien Parameter
- Dekomposisi Rank
- Pembekuan Bobot
- Modul Adapter

## Use Cases

- Kustomisasi LLM
- Adaptasi Spesifik Domain
- Pelatihan dengan Keterbatasan Sumber Daya

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning)](/en/terms/peft-parameter-efficient-fine-tuning/)
- [Penyetelan Halus](/en/terms/penyetelan-halus/)
- [Kuantisasi](/en/terms/kuantisasi/)
