---
title: "Distilarea cunoștințelor"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
aliases:
  - /ro/terms/knowledge_distillation/
date: "2026-07-18T16:06:53.291258Z"
lastmod: "2026-07-18T17:15:09.671531Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "Distilarea cunoștințelor este o tehnică de comprimare a modelelor în care un model student mai mic învață să imite comportamentul unui model profesor mai mare."
---

## Definition

Distilarea cunoștințelor este o metodă de învățare automată utilizată pentru a comprima o rețea neuronală mare și complexă (profesorul) într-o rețea mai mică și mai eficientă (studentul). Modelul student este antrenat să

### Summary

Distilarea cunoștințelor este o tehnică de comprimare a modelelor în care un model student mai mic învață să imite comportamentul unui model profesor mai mare.

## Key Concepts

- Model profesor-student
- Comprimarea modelelor
- Ținte moi (Soft Targets)
- Eficiență

## Use Cases

- Implementarea modelelor pe dispozitive edge
- Reducerea latenței de inferență
- Scăderea costurilor de calcul în cloud

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

- [Model Compression (Comprimarea modelelor)](/en/terms/model-compression-comprimarea-modelelor/)
- [Pruning (Tunsul rețelelor)](/en/terms/pruning-tunsul-rețelelor/)
- [Quantization (Cuantizarea)](/en/terms/quantization-cuantizarea/)
- [Neural Networks (Rețele neuronale)](/en/terms/neural-networks-rețele-neuronale/)
