---
title: "Tiedon distillointi"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
date: "2026-07-18T16:05:03.325031Z"
lastmod: "2026-07-18T17:15:09.425045Z"
draft: false
source: "agnes_llm"
status: "published"
language: "fi"
description: "Tiedon distillointi on mallin purkamistekniikka, jossa pienempi opiskelijamalli oppii jäljittelemään suuremman opettajamallin käyttäytymistä."
---
## Definition

Tiedon distillointi on koneoppimismenetelmä, jota käytetään suuren, monimutkaisen neuroverkon (opettaja) purkamiseen pienemmäksi, tehokkaammaksi verkoksi (opiskelija). Opiskelijamallia koulutetaan

### Summary

Tiedon distillointi on mallin purkamistekniikka, jossa pienempi opiskelijamalli oppii jäljittelemään suuremman opettajamallin käyttäytymistä.

## Key Concepts

- Opettaja-opiskelija-malli
- Mallin purkaminen
- Pehmeät kohdistukset (soft targets)
- Tehokkuus

## Use Cases

- Mallien käyttöönotto reunalaitteissa (edge devices)
- Johtopäätöksenteon viiveen vähentäminen
- Pilvipalveluiden kustannusten alentaminen

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

- [Model Compression (mallin purkaminen)](/en/terms/model-compression-mallin-purkaminen/)
- [Pruning (vartaloisanomi / oksien leikkaus)](/en/terms/pruning-vartaloisanomi-oksien-leikkaus/)
- [Quantization (kvantisointi)](/en/terms/quantization-kvantisointi/)
- [Neural Networks (neuroverkot)](/en/terms/neural-networks-neuroverkot/)
