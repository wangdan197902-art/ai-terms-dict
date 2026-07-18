---
title: "Unsloth"
term_id: "unsloth"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "LLM", "training", "library"]
difficulty: 3
weight: 1
slug: "unsloth"
aliases:
  - /pl/terms/unsloth/
date: "2026-07-18T16:21:51.695349Z"
lastmod: "2026-07-18T17:15:08.927058Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Unsloth to biblioteka open-source, która przyspiesza szkolenie i wnioskowanie dużych modeli językowych (LLM) nawet dwukrotnie dzięki zoptymalizowanemu zarządzaniu pamięcią i implementacjom jąder."
---

## Definition

Unsloth to specjalistyczne narzędzie zaprojektowane w celu optymalizacji dostrajania (fine-tuning) i wdrażania dużych modeli językowych (LLM). Osiąga znaczące przyśpieszenia i redukcję zużycia pamięci poprzez zastąpienie standardowych komponentów PyTorch

### Summary

Unsloth to biblioteka open-source, która przyspiesza szkolenie i wnioskowanie dużych modeli językowych (LLM) nawet dwukrotnie dzięki zoptymalizowanemu zarządzaniu pamięcią i implementacjom jąder.

## Key Concepts

- Optymalizacja pamięci
- Niestandardowe jądra
- Dostrajanie LLM
- Przyspieszenie wydajności

## Use Cases

- Dostrajanie LLM na ograniczonych zasobach GPU
- Przyspieszanie potoków wnioskowania
- Redukcja kosztów obliczeniowych w chmurze podczas szkolenia

## Code Example

```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Llama-2-7b-bnb-4bit",
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True
)
```

## Related Terms

- [LoRA (Low-Rank Adaptation - metoda efektywnego dostrajania modeli)](/en/terms/lora-low-rank-adaptation-metoda-efektywnego-dostrajania-modeli/)
- [PyTorch (biblioteka uczenia maszynowego)](/en/terms/pytorch-biblioteka-uczenia-maszynowego/)
- [Hugging Face (platforma społecznościowa dla ML)](/en/terms/hugging-face-platforma-społecznościowa-dla-ml/)
- [Flash Attention (zoptymalizowany algorytm uwagi)](/en/terms/flash-attention-zoptymalizowany-algorytm-uwagi/)
