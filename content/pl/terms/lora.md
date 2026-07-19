---
title: "LoRA (Low-Rank Adaptation)"
term_id: "lora"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Efficiency", "Fine-Tuning"]
difficulty: 4
weight: 1
slug: "lora"
date: "2026-07-18T15:26:49.337534Z"
lastmod: "2026-07-18T17:15:08.814344Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Niskorzutowa Adaptacja to metoda dopracowywania (fine-tuningu) efektywnego pod kątem parametrów, która wprowadza trenowalne macierze dekompozycji rzędu niskiego do istniejących wag modelu."
---
## Definition

LoRA zamraża wstępnie wytrenowane wagi modelu i wstawia trenowalne macierze dekompozycji do każdej warstwy architektury Transformera. Optymalizując tylko te niskorzutowe macierze, LoRA znacznie redukuje

### Summary

Niskorzutowa Adaptacja to metoda dopracowywania (fine-tuningu) efektywnego pod kątem parametrów, która wprowadza trenowalne macierze dekompozycji rzędu niskiego do istniejących wag modelu.

## Key Concepts

- Dopracowywanie Efektywne Pod Kątem Parametrów
- Dekompozycja Rzędu
- Zamrażanie Wag
- Moduły Adapterów

## Use Cases

- Dostosowywanie Dużych Modeli Językowych
- Adaptacja Specyficzna dla Domeny
- Trenowanie w Warunkach Ograniczonych Zasobowo

## Code Example

```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(r=8, lora_alpha=32)
model = get_peft_model(base_model, config)
```

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning - Dopracowywanie Efektywne Pod Kątem Parametrów)](/en/terms/peft-parameter-efficient-fine-tuning-dopracowywanie-efektywne-pod-kątem-parametrów/)
- [Fine-Tuning (Dopracowywanie / Dostrajanie)](/en/terms/fine-tuning-dopracowywanie-dostrajanie/)
- [Quantization (Kwantyzacja)](/en/terms/quantization-kwantyzacja/)
