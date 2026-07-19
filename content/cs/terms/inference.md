---
title: "Inference (Odvozování)"
term_id: "inference"
category: "engineering_practice"
subcategory: ""
tags: ["Deployment", "Production", "Performance"]
difficulty: 2
weight: 1
slug: "inference"
date: "2026-07-18T15:23:01.660707Z"
lastmod: "2026-07-18T17:15:09.063209Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Fáze, ve které trénovaný model zpracovává nová data za účelem generování predikcí nebo výstupů."
---
## Definition

Inference označuje fázi nasazení, kdy je finální model používán k přijímání rozhodnutí nebo generování predikcí na neviděných datech. Na rozdíl od tréninku, který aktualizuje váhy, inference spotřebovává výpočetní zdroje pouze pro rychlé zpracování vstupů a produkci výsledků.

### Summary

Fáze, ve které trénovaný model zpracovává nová data za účelem generování predikcí nebo výstupů.

## Key Concepts

- Predikce
- Latence (zpoždění)
- Průchodnost (Throughput)
- Nasazení (Deployment)

## Use Cases

- Detekce podvodů v bankovních transakcích v reálném čase
- Generování odpovědí v živých interakcích s chatbotem
- Klasifikace obrázků v systémech autonomních vozidel

## Code Example

```python
import torch
model.eval()
with torch.no_grad():
    output = model(input_tensor)
    prediction = torch.argmax(output, dim=1)
```

## Related Terms

- [Trénink (Training)](/en/terms/trénink-training/)
- [Optimalizace latence (Latency Optimization)](/en/terms/optimalizace-latence-latency-optimization/)
- [Dávkování (Batching)](/en/terms/dávkování-batching/)
- [Služby modelu (Model Serving)](/en/terms/služby-modelu-model-serving/)
