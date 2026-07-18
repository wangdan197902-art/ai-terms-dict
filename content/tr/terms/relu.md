---
title: "ReLU"
term_id: "relu"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "activation-functions", "deep-learning"]
difficulty: 3
weight: 1
slug: "relu"
aliases:
  - /tr/terms/relu/
date: "2026-07-18T15:37:03.168740Z"
lastmod: "2026-07-18T16:38:07.262523Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Düzeltmeli Doğrusal Birim (Rectified Linear Unit), pozitifse girdiyi doğrudan çıktı olarak veren, aksi takdirde sıfır döndüren bir aktivasyon fonksiyonudur."
---

## Definition

ReLU, hesaplama verimliliği ve kaybolan gradyan sorununu hafifletme yeteneği nedeniyle derin öğrenme sinir ağlarında yaygın olarak kullanılır. Matematiksel olarak f(x) = max(0, x) şeklinde tanımlanır ve doğrusal olmayanlık özelliği getirir.

### Summary

Düzeltmeli Doğrusal Birim (Rectified Linear Unit), pozitifse girdiyi doğrudan çıktı olarak veren, aksi takdirde sıfır döndüren bir aktivasyon fonksiyonudur.

## Key Concepts

- Doğrusal Olmayanlık
- Aktivasyon Fonksiyonu
- Kaybolan Gradyan
- Parçalı Doğrusal

## Use Cases

- Evrişimli Sinir Ağları'ndaki (CNN) gizli katmanlar
- Derin Beslemeli Ağlar
- Görüntü Tanıma Modelleri

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (Sigmoid Fonksiyonu)](/en/terms/sigmoid-sigmoid-fonksiyonu/)
- [Tanh (Hiperbolik Tangant)](/en/terms/tanh-hiperbolik-tangant/)
- [Leaky ReLU (Sızdıran ReLU)](/en/terms/leaky-relu-sızdıran-relu/)
- [Sinir Ağı (Neural Network)](/en/terms/sinir-ağı-neural-network/)
