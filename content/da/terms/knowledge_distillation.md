---
title: "Knowledge Distillation"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
date: "2026-07-18T16:02:49.485532Z"
lastmod: "2026-07-18T17:15:09.302157Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "Knowledge distillation er en teknik til modelkomprimering, hvor en mindre 'student'-model lærer at efterligne adfærden hos en større 'teacher'-model."
---
## Definition

Knowledge distillation er en maskinlæringsmetode, der bruges til at komprimere et stort, komplekst neuralt netværk ('teacher') til et mindre, mere effektivt netværk ('student'). Student-modellen trænes til at efterligne teacher-modellens output.

### Summary

Knowledge distillation er en teknik til modelkomprimering, hvor en mindre 'student'-model lærer at efterligne adfærden hos en større 'teacher'-model.

## Key Concepts

- Teacher-Student Model
- Modelkomprimering
- Bløde mål (soft targets)
- Effektivitet

## Use Cases

- Udrulning af modeller på edge-enheder
- Reduktion af inferenslatens
- Sænkning af omkostninger til cloud-computing

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

- [Model Compression (modelkomprimering)](/en/terms/model-compression-modelkomprimering/)
- [Pruning (beskæring)](/en/terms/pruning-beskæring/)
- [Quantization (kvantisering)](/en/terms/quantization-kvantisering/)
- [Neural Networks (neuronetværk)](/en/terms/neural-networks-neuronetværk/)
