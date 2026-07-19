---
title: Normalisasi Lapisan
term_id: layer_normalization
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- Optimization
- architecture
difficulty: 3
weight: 1
slug: layer_normalization
date: '2026-07-18T15:57:27.375179Z'
lastmod: '2026-07-18T16:38:07.475959Z'
draft: false
source: agnes_llm
status: published
language: id
description: Sebuah teknik yang menormalisasi aktivasi lapisan jaringan saraf melintasi
  dimensi fitur untuk setiap sampel individu.
---
## Definition

Normalisasi Lapisan menstabilkan pelatihan dengan mengurangi pergeseran kovariat internal, khususnya efektif dalam arsitektur rekuren dan transformer. Berbeda dengan Normalisasi Batch yang bergantung pada statistik batch, normalisasi ini dihitung per sampel.

### Summary

Sebuah teknik yang menormalisasi aktivasi lapisan jaringan saraf melintasi dimensi fitur untuk setiap sampel individu.

## Key Concepts

- Normalisasi
- Pergeseran Kovariat Internal
- Model Transformer
- RNN

## Use Cases

- Melatih model Transformer seperti BERT
- Menstabilkan pelatihan RNN/LSTM
- Pembelajaran mendalam dengan ukuran batch kecil

## Code Example

```python
import torch.nn as nn
norm_layer = nn.LayerNorm(normalized_shape=[768])
```

## Related Terms

- [batch_normalization (normalisasi batch)](/en/terms/batch_normalization-normalisasi-batch/)
- [transformer (transformer)](/en/terms/transformer-transformer/)
- [normalization (normalisasi)](/en/terms/normalization-normalisasi/)
- [deep_learning (pembelajaran mendalam)](/en/terms/deep_learning-pembelajaran-mendalam/)
