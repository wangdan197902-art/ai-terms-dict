---
title: Augmentação de Dados
term_id: data_augmentation
category: training_techniques
subcategory: ''
tags:
- Machine Learning
- preprocessing
- cv
difficulty: 2
weight: 1
slug: data_augmentation
date: '2026-07-18T14:54:59.597365Z'
lastmod: '2026-07-18T15:51:59.476146Z'
draft: false
source: agnes_llm
status: published
language: pt
description: A augmentação de dados é uma técnica usada para aumentar a diversidade
  e o tamanho dos conjuntos de dados de treinamento aplicando transformações aos pontos
  de dados existentes.
---
## Definition

Este método expande artificialmente o conjunto de dados de treinamento criando versões modificadas das amostras existentes, como rotacionar imagens, adicionar ruído ao áudio ou substituir sinônimos no texto. Ajuda a prevenir

### Summary

A augmentação de dados é uma técnica usada para aumentar a diversidade e o tamanho dos conjuntos de dados de treinamento aplicando transformações aos pontos de dados existentes.

## Key Concepts

- Prevenção de Overfitting
- Expansão de Conjunto de Dados
- Generalização
- Transformações

## Use Cases

- Melhoria da robustez de modelos de visão computacional
- Aumento do desempenho de modelos de PLN com texto limitado
- Equilíbrio de conjuntos de dados desbalanceados

## Code Example

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
gen = ImageDataGenerator(rotation_range=20)

```

## Related Terms

- [Regularization (Regularização)](/en/terms/regularization-regularização/)
- [Synthetic Data (Dados Sintéticos)](/en/terms/synthetic-data-dados-sintéticos/)
- [Transfer Learning (Aprendizado por Transferência)](/en/terms/transfer-learning-aprendizado-por-transferência/)
- [Overfitting (Sobreajuste)](/en/terms/overfitting-sobreajuste/)
