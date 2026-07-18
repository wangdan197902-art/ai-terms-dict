---
title: "Época"
term_id: "epoch"
category: "training_techniques"
subcategory: ""
tags: ["training", "neural_networks", "basics"]
difficulty: 2
weight: 1
slug: "epoch"
aliases:
  - /es/terms/epoch/
date: "2026-07-18T10:48:24.114383Z"
lastmod: "2026-07-18T11:44:44.803231Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Un pase completo del conjunto de datos de entrenamiento a través del algoritmo de aprendizaje automático durante el entrenamiento del modelo."
---

## Definition

En el aprendizaje automático, una época representa una iteración única sobre todo el conjunto de datos de entrenamiento. Durante cada época, el modelo procesa todos los ejemplos de entrenamiento, actualiza sus pesos mediante retropropagación y ajusta sus parámetros internos para minimizar la función de pérdida.

### Summary

Un pase completo del conjunto de datos de entrenamiento a través del algoritmo de aprendizaje automático durante el entrenamiento del modelo.

## Key Concepts

- Iteración de Entrenamiento
- Retropropagación
- Convergencia
- Ajuste de Hiperparámetros

## Use Cases

- Configuración de bucles de entrenamiento de redes neuronales
- Monitoreo de la pérdida de validación por ciclo
- Implementación de estrategias de parada temprana

## Code Example

```python
for epoch in range(num_epochs):
    for inputs, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```

## Related Terms

- [Tamaño del Lote (Batch Size)](/en/terms/tamaño-del-lote-batch-size/)
- [Iteración](/en/terms/iteración/)
- [Tasa de Aprendizaje](/en/terms/tasa-de-aprendizaje/)
- [Sobreajuste (Overfitting)](/en/terms/sobreajuste-overfitting/)
