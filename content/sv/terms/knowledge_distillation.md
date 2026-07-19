---
title: "Knowledge Distillation"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
date: "2026-07-18T16:05:29.614028Z"
lastmod: "2026-07-18T17:15:09.017866Z"
draft: false
source: "agnes_llm"
status: "published"
language: "sv"
description: "Knowledge distillation är en teknik för modellkomprimering där en mindre 'studentmodell' lär sig att imitera beteendet hos en större 'lärarmodell'."
---
## Definition

Knowledge distillation är en metod inom maskininlärning som används för att komprimera ett stort, komplext neuralt nätverk (läraren) till ett mindre, mer effektivt nätverk (studenten). Studentmodellen tränas för att efterlikna lärarens utdata.

### Summary

Knowledge distillation är en teknik för modellkomprimering där en mindre 'studentmodell' lär sig att imitera beteendet hos en större 'lärarmodell'.

## Key Concepts

- Lärar-student-modell
- Modellkomprimering
- Mjukmål (soft targets)
- Effektivitet

## Use Cases

- Distribuera modeller på kantenheter (edge devices)
- Minska latens vid inferens
- Sänka kostnader för molnberäkningar

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

- [Model Compression (modellkomprimering)](/en/terms/model-compression-modellkomprimering/)
- [Pruning (beskärning)](/en/terms/pruning-beskärning/)
- [Quantization (kvantisering)](/en/terms/quantization-kvantisering/)
- [Neural Networks (neuronnätverk)](/en/terms/neural-networks-neuronnätverk/)
