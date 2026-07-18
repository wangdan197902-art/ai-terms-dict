---
title: "Sigmoide"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
aliases:
  - /pt/terms/sigmoid/
date: "2026-07-18T15:21:59.173456Z"
lastmod: "2026-07-18T15:51:59.532295Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Uma função matemática que mapeia qualquer número real para um valor entre zero e um, formando uma curva em forma de S."
---

## Definition

A função sigmoide, definida como σ(z) = 1 / (1 + e^-z), é amplamente utilizada em aprendizado de máquina para modelar probabilidades. Ela comprime os valores de entrada no intervalo (0, 1), tornando-a adequada para classificação binária.

### Summary

Uma função matemática que mapeia qualquer número real para um valor entre zero e um, formando uma curva em forma de S.

## Key Concepts

- Função logística
- Mapeamento de probabilidade
- Desvanecimento do gradiente (Vanishing gradient)
- Não linearidade

## Use Cases

- Saída de classificação binária
- Regressão logística
- Ativação em redes neurais rasas

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU (Função de ativação linear por partes)](/en/terms/relu-função-de-ativação-linear-por-partes/)
- [Softmax (Função que converte valores em probabilidades)](/en/terms/softmax-função-que-converte-valores-em-probabilidades/)
- [Regressão Logística (Logistic Regression)](/en/terms/regressão-logística-logistic-regression/)
- [Função de Ativação (Activation Function)](/en/terms/função-de-ativação-activation-function/)
