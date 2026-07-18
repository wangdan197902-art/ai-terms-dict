---
title: "Wissensdistillation"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
aliases:
  - /de/terms/knowledge_distillation/
date: "2026-07-18T11:20:22.762723Z"
lastmod: "2026-07-18T11:44:44.954695Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Wissensdistillation ist eine Modellkomprimierungstechnik, bei der ein kleineres Schülermodell lernt, das Verhalten eines größeren Lehrermodells nachzuahmen."
---

## Definition

Wissensdistillation ist eine Methode des maschinellen Lernens, die verwendet wird, um ein großes, komplexes neuronales Netz (den Lehrer) in ein kleineres, effizienteres Netzwerk (den Schüler) zu komprimieren. Das Schülermodell wird so trainiert, dass es

### Summary

Wissensdistillation ist eine Modellkomprimierungstechnik, bei der ein kleineres Schülermodell lernt, das Verhalten eines größeren Lehrermodells nachzuahmen.

## Key Concepts

- Lehrer-Schüler-Modell
- Modellkomprimierung
- Weiche Ziele (Soft Targets)
- Effizienz

## Use Cases

- Bereitstellung von Modellen auf Edge-Geräten
- Reduzierung der Inferenzlatenz
- Senkung der Cloud-Computing-Kosten

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

- [Modellkomprimierung](/en/terms/modellkomprimierung/)
- [Pruning (Beschneiden)](/en/terms/pruning-beschneiden/)
- [Quantisierung](/en/terms/quantisierung/)
- [Neuronale Netze](/en/terms/neuronale-netze/)
