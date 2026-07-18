---
title: "Knowledge Distillation"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
aliases:
  - /cs/terms/knowledge_distillation/
date: "2026-07-18T16:04:20.914947Z"
lastmod: "2026-07-18T17:15:09.144897Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Knowledge Distillation je technika komprese modelu, při které se menší model studenta učí napodobovat chování většího modelu učitele."
---

## Definition

Knowledge Distillation je metoda strojového učení používaná ke kompresi velké, složité neuronové sítě (učitel) do menší, efektivnější sítě (student). Model studenta je trénován tak, aby napodobil výstupy učitele.

### Summary

Knowledge Distillation je technika komprese modelu, při které se menší model studenta učí napodobovat chování většího modelu učitele.

## Key Concepts

- Model Učitel-Student
- Komprese modelu
- Měkké cíle (Soft Targets)
- Efektivita

## Use Cases

- Nasazování modelů na okrajová zařízení (edge devices)
- Snížení latence při inferenci
- Snižování nákladů na cloudové výpočty

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

- [Model Compression (Komprese modelu)](/en/terms/model-compression-komprese-modelu/)
- [Pruning (Prořezávání sítě)](/en/terms/pruning-prořezávání-sítě/)
- [Quantization (Kvantizace)](/en/terms/quantization-kvantizace/)
- [Neural Networks (Neuronové sítě)](/en/terms/neural-networks-neuronové-sítě/)
