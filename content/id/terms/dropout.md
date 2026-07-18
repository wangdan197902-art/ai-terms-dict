---
title: "Dropout"
term_id: "dropout"
category: "basic_concepts"
subcategory: ""
tags: ["Deep Learning", "Regularization", "Model Training"]
difficulty: 3
weight: 1
slug: "dropout"
aliases:
  - /id/terms/dropout/
date: "2026-07-18T15:34:15.539781Z"
lastmod: "2026-07-18T16:38:07.412776Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Dropout adalah teknik regularisasi yang secara acak mengabaikan neuron selama pelatihan untuk mencegah overfitting."
---

## Definition

Dalam jaringan saraf, dropout mencegah overfitting dengan sementara menghapus subset acak neuron pada setiap langkah pelatihan. Hal ini memaksa jaringan untuk mempelajari fitur yang kuat yang berguna dalam kombinasi dengan neuron lain.

### Summary

Dropout adalah teknik regularisasi yang secara acak mengabaikan neuron selama pelatihan untuk mencegah overfitting.

## Key Concepts

- Regularisasi
- Pencegahan Overfitting
- Jaringan Saraf
- Penekanan Acak

## Use Cases

- Melatih jaringan saraf feedforward yang dalam
- Meningkatkan generalisasi pada model bahasa besar
- Mengurangi ketergantungan komputasi pada jalur neuron tertentu

## Code Example

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(100, 50),
    nn.Dropout(0.5),
    nn.ReLU(),
    nn.Linear(50, 10)
)
```

## Related Terms

- [L2 Regularization (Regularisasi L2)](/en/terms/l2-regularization-regularisasi-l2/)
- [Batch Normalization (Normalisasi Batch)](/en/terms/batch-normalization-normalisasi-batch/)
- [Overfitting (Kelebihan pasokan/pelatihan berlebihan)](/en/terms/overfitting-kelebihan-pasokan-pelatihan-berlebihan/)
- [Generalization (Generalisasi)](/en/terms/generalization-generalisasi/)
