---
title: "Distilasi Pengetahuan"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
date: "2026-07-18T15:56:43.108053Z"
lastmod: "2026-07-18T16:38:07.473682Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Distilasi pengetahuan adalah teknik kompresi model di mana model siswa yang lebih kecil belajar meniru perilaku model guru yang lebih besar."
---
## Definition

Distilasi pengetahuan adalah metode pembelajaran mesin yang digunakan untuk mengompresi jaringan saraf besar dan kompleks (guru) menjadi jaringan yang lebih kecil dan efisien (siswa). Model siswa dilatih untuk

### Summary

Distilasi pengetahuan adalah teknik kompresi model di mana model siswa yang lebih kecil belajar meniru perilaku model guru yang lebih besar.

## Key Concepts

- Model Guru-Siswa
- Kompresi Model
- Target Lunak
- Efisiensi

## Use Cases

- Menyebarkan model pada perangkat tepi
- Mengurangi latensi inferensi
- Menurunkan biaya komputasi awan

## Code Example

```python
import torch
import torch.nn as nn

def distillation_loss(student_logits, teacher_logits, temperature=2.0):
    T = temperature
    student_probs = nn.functional.softmax(student_logits / T, dim=1)
    teacher_probs = nn.functional.softmax(teacher_logits / T, dim=1)
    return nn.functional.kl_div(
        nn.functional.log_softmax(student_logits / T, dim=1),
        teacher_probs,
        reduction='batchmean'
    ) * (T * T)
```

## Related Terms

- [Model Compression (Kompresi Model)](/en/terms/model-compression-kompresi-model/)
- [Pruning (Pemangkasan)](/en/terms/pruning-pemangkasan/)
- [Quantization (Kuantisasi)](/en/terms/quantization-kuantisasi/)
- [Neural Networks (Jaringan Saraf)](/en/terms/neural-networks-jaringan-saraf/)
