---
title: İleri Yönlü Ağ
term_id: feed_forward_network
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
- fundamentals
difficulty: 2
weight: 1
slug: feed_forward_network
date: '2026-07-18T15:53:29.767861Z'
lastmod: '2026-07-18T16:38:07.309384Z'
draft: false
source: agnes_llm
status: published
language: tr
description: Düğimler arasındaki bağlantıların döngü oluşturmadığı ve bilgileri tek
  yönde ilettiği bir yapay sinir ağı sınıfı.
---
## Definition

İleri Yönlü Ağlar (FFN'ler), çok katmanlı algılayıcılar (MLP'ler) olarak da bilinir ve geri besleme döngüleri olmadan girdiden çıktıya doğru nöron katmanları üzerinden verileri sıralı olarak işler. Her nöron girdileri alır

### Summary

Düğimler arasındaki bağlantıların döngü oluşturmadığı ve bilgileri tek yönde ilettiği bir yapay sinir ağı sınıfı.

## Key Concepts

- Döngü yok
- Katmanlar (Girdi, Gizli, Çıktı)
- Aktivasyon fonksiyonları
- Ağırlıklı toplamlar

## Use Cases

- Basit regresyon görevleri
- Tablo verisiyle sınıflandırma problemleri
- Daha derin mimariler için yapı taşları

## Code Example

```python
import torch.nn as nn

class SimpleFFN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleFFN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
```

## Related Terms

- [Multi-Layer Perceptron (Çok Katmanlı Algılayıcı)](/en/terms/multi-layer-perceptron-çok-katmanlı-algılayıcı/)
- [Backpropagation (Geri Yayılım)](/en/terms/backpropagation-geri-yayılım/)
- [Activation Function (Aktivasyon Fonksiyonu)](/en/terms/activation-function-aktivasyon-fonksiyonu/)
- [Neural Network (Sinir Ağı)](/en/terms/neural-network-sinir-ağı/)
