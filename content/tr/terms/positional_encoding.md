---
title: "Konumsal Kodlama"
term_id: "positional_encoding"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "nlp", "architecture"]
difficulty: 3
weight: 1
slug: "positional_encoding"
aliases:
  - /tr/terms/positional_encoding/
date: "2026-07-18T15:36:47.227459Z"
lastmod: "2026-07-18T16:38:07.261540Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Dönüştürücü modellerde, bir dizideki belirteçlerin göreli veya mutlak konumuna ilişkin bilgileri enjekte eden bir teknik."
---

## Definition

Dönüştürücüler, RNN'ler gibi ardışık değil, tüm belirteçleri paralel olarak işlediğinden belirteç sırasına dair içsel bir bilgiye sahip değildir. Konumsal kodlama, girdi gömme vektörlerine belirli vektörler ekleyerek belirteçlerin sıralama bilgisini modele sağlar.

### Summary

Dönüştürücü modellerde, bir dizideki belirteçlerin göreli veya mutlak konumuna ilişkin bilgileri enjekte eden bir teknik.

## Key Concepts

- Dizi Sırası
- Öz-Dikkat
- Sinüzoidal Fonksiyonlar
- Belirteç Gömmeleri

## Use Cases

- Makine Çevirisi
- Metin Özetleme
- Dil Modelleme

## Code Example

```python
import torch
import math
def get_positional_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe.unsqueeze(0)
```

## Related Terms

- [Transformer Mimarisi](/en/terms/transformer-mimarisi/)
- [Gömme (Embedding)](/en/terms/gömme-embedding/)
- [Dikkat Mekanizması](/en/terms/dikkat-mekanizması/)
- [RoPE (Rotasyonel Pozisyonel Kodlama)](/en/terms/rope-rotasyonel-pozisyonel-kodlama/)
