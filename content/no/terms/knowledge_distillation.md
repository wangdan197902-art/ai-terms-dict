---
title: "Knowledge Distillation"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
date: "2026-07-18T16:01:19.026447Z"
lastmod: "2026-07-18T16:38:07.015835Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "Knowledge distillation er en teknikk for modellkomprimering der en mindre «studentmodell» lærer å etterligne oppførselen til en større «lærermodell»."
---
## Definition

Knowledge distillation er en maskinlæringsmetode brukt til å komprimere et stort, komplekst nevralt nettverk (læreren) inn i et mindre, mer effektivt nettverk (studenten). Studentmodellen trenes for å

### Summary

Knowledge distillation er en teknikk for modellkomprimering der en mindre «studentmodell» lærer å etterligne oppførselen til en større «lærermodell».

## Key Concepts

- Lærer-student-modell
- Modellkomprimering
- Mjuk målverdier (soft targets)
- Effektivitet

## Use Cases

- Distribusjon av modeller på kantenheter (edge devices)
- Reduksjon av inferenslatens
- Senking av kostnader for skydatamaskinvare

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
- [Pruning (beskjæring)](/en/terms/pruning-beskjæring/)
- [Quantization (kvantisering)](/en/terms/quantization-kvantisering/)
- [Neural Networks (nevrale nettverk)](/en/terms/neural-networks-nevrale-nettverk/)
