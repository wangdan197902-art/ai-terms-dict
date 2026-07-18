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
  - /it/terms/knowledge_distillation/
date: "2026-07-18T16:06:37.975330Z"
lastmod: "2026-07-18T17:15:08.639976Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "La knowledge distillation è una tecnica di compressione dei modelli in cui un modello studente più piccolo imita il comportamento di un modello insegnante più grande."
---

## Definition

La knowledge distillation è un metodo di apprendimento automatico utilizzato per comprimere una rete neurale grande e complessa (l'insegnante) in una rete più piccola ed efficiente (lo studente). Il modello studente viene addestrato per

### Summary

La knowledge distillation è una tecnica di compressione dei modelli in cui un modello studente più piccolo imita il comportamento di un modello insegnante più grande.

## Key Concepts

- Modello Insegnante-Studente
- Compressione del Modello
- Target Morbidi
- Efficienza

## Use Cases

- Implementazione di modelli su dispositivi edge
- Riduzione della latenza di inferenza
- Abbattimento dei costi di calcolo cloud

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

- [Compressione del Modello (Riduzione delle dimensioni del modello)](/en/terms/compressione-del-modello-riduzione-delle-dimensioni-del-modello/)
- [Pruning (Potatura dei parametri ridondanti)](/en/terms/pruning-potatura-dei-parametri-ridondanti/)
- [Quantizzazione (Riduzione della precisione numerica)](/en/terms/quantizzazione-riduzione-della-precisione-numerica/)
- [Reti Neurali (Strutture computazionali ispirate al cervello)](/en/terms/reti-neurali-strutture-computazionali-ispirate-al-cervello/)
