---
title: "Dönüştürücü (Transformer)"
term_id: "transformer"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "nlp", "attention"]
difficulty: 4
weight: 1
slug: "transformer"
aliases:
  - /tr/terms/transformer/
date: "2026-07-18T15:30:35.879437Z"
lastmod: "2026-07-18T16:38:07.246381Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Sıralı veriyi ardışık olarak değil, paralel olarak işleyen öz-dikkat mekanizmalarına dayalı derin öğrenme mimarisi."
---

## Definition

'Attention Is All You Need' makalesinde tanıtılan Dönüştürücü mimarisi, doğal dil işlemeyi ve ötesini devrim niteliğinde değiştirdi. Çok başlı öz-dikkat kullanarak, girdi dizisindeki farklı kelimeler veya öğeler arasındaki ilişkilerin önemini ölçer.

### Summary

Sıralı veriyi ardışık olarak değil, paralel olarak işleyen öz-dikkat mekanizmalarına dayalı derin öğrenme mimarisi.

## Key Concepts

- Öz-Dikkat (Self-Attention)
- Çok Başlı Dikkat
- Konumsal Kodlama
- Kodlayıcı-Kod Çözücü Yapısı

## Use Cases

- Makine çevirisi
- Metin üretimi
- Görüntü tanıma (ViT)

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (Dikkat mekanizması)](/en/terms/attention_mechanism-dikkat-mekanizması/)
- [bert (BERT modeli)](/en/terms/bert-bert-modeli/)
- [gpt (GPT modeli)](/en/terms/gpt-gpt-modeli/)
- [self_attention (Öz-dikkat)](/en/terms/self_attention-öz-dikkat/)
