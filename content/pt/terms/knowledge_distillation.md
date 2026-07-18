---
title: "Distilação de Conhecimento"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
aliases:
  - /pt/terms/knowledge_distillation/
date: "2026-07-18T15:07:05.715565Z"
lastmod: "2026-07-18T15:51:59.504771Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "A distilação de conhecimento é uma técnica de compressão de modelos na qual um modelo menor (aluno) aprende a imitar o comportamento de um modelo maior (professor)."
---

## Definition

A distilação de conhecimento é um método de aprendizado de máquina utilizado para comprimir uma rede neural grande e complexa (o professor) em uma rede menor e mais eficiente (o aluno). O modelo aluno é treinado para replicar as saídas e o comportamento do modelo professor, permitindo que o modelo compacto mantenha alta precisão com menos recursos computacionais.

### Summary

A distilação de conhecimento é uma técnica de compressão de modelos na qual um modelo menor (aluno) aprende a imitar o comportamento de um modelo maior (professor).

## Key Concepts

- Modelo Professor-Aluno
- Compressão de Modelo
- Alvos Suaves (Soft Targets)
- Eficiência

## Use Cases

- Implantação de modelos em dispositivos de borda
- Redução da latência de inferência
- Diminuição dos custos de computação em nuvem

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

- [Compressão de Modelo (técnica geral de redução de tamanho do modelo)](/en/terms/compressão-de-modelo-técnica-geral-de-redução-de-tamanho-do-modelo/)
- [Poda (remover partes desnecessárias da rede)](/en/terms/poda-remover-partes-desnecessárias-da-rede/)
- [Quantização (reduzir a precisão numérica dos pesos)](/en/terms/quantização-reduzir-a-precisão-numérica-dos-pesos/)
- [Redes Neurais (estrutura base dos modelos)](/en/terms/redes-neurais-estrutura-base-dos-modelos/)
