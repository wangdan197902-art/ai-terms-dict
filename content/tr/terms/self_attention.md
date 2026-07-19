---
title: "Öz-Dikkat"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
date: "2026-07-18T15:29:19.204806Z"
lastmod: "2026-07-18T16:38:07.243949Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Bir sinir ağına, girdi dizisinin farklı parçalarının birbirine göre önem derecesini ağırlıklandırmasına olanak tanıyan mekanizma."
---
## Definition

Öz-dikkat, mesafeden bağımsız olarak bir dizideki tüm konumlar arasındaki bağımlılıkları aynı anda yakalamayı sağlar. Her token çifti arasında dikkat skorları hesaplayarak bağlamsal ağırlıklandırmaya izin verir.

### Summary

Bir sinir ağına, girdi dizisinin farklı parçalarının birbirine göre önem derecesini ağırlıklandırmasına olanak tanıyan mekanizma.

## Key Concepts

- Sorgu-Anahtar-Değer
- Dikkat Skorları
- Bağlamsal Ağırlıklandırma
- Paralel İşlem

## Use Cases

- Makine çevirisi
- Metin özetleme
- Görüş Transformer'ları aracılığıyla görüntü sınıflandırma

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (Dönüştürücü)](/en/terms/transformer-dönüştürücü/)
- [Multi-Head Attention (Çok Başlı Dikkat)](/en/terms/multi-head-attention-çok-başlı-dikkat/)
- [Embeddings (Gömme Temsilleri)](/en/terms/embeddings-gömme-temsilleri/)
- [Sequence Modeling (Dizi Modelleme)](/en/terms/sequence-modeling-dizi-modelleme/)
