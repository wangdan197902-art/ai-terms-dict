---
title: Lernrate
term_id: learning_rate
category: training_techniques
subcategory: ''
tags:
- training
- Optimization
- hyperparameters
difficulty: 3
weight: 1
slug: learning_rate
date: '2026-07-18T10:58:44.539823Z'
lastmod: '2026-07-18T11:44:44.896056Z'
draft: false
source: agnes_llm
status: published
language: de
description: Ein Hyperparameter, der die Schrittgröße während der Modelloptimierung
  steuert, um die Verlustfunktion zu minimieren.
---
## Definition

Die Lernrate bestimmt, wie stark die Gewichte des Modells im Verhältnis zum berechneten Gradienten während jeder Trainingsiteration aktualisiert werden. Eine zu hohe Rate kann dazu führen, dass das Modell das Optimum verfehlt (overshooting), während eine zu niedrige Rate den Trainingsprozess verlangsamt.

### Summary

Ein Hyperparameter, der die Schrittgröße während der Modelloptimierung steuert, um die Verlustfunktion zu minimieren.

## Key Concepts

- Gradientenabstieg
- Hyperparameter-Tuning
- Konvergenz
- Optimizer

## Use Cases

- Training neuronaler Netze
- Optimierung von Deep-Learning-Modellen
- Aktualisierung von Richtlinien im Verstärkungslernen

## Code Example

```python
import torch.optim as optim
model = MyModel()
optimizer = optim.SGD(model.parameters(), lr=0.01)
```

## Related Terms

- [gradient_descent (Gradientenabstieg)](/en/terms/gradient_descent-gradientenabstieg/)
- [optimizer (Optimizer)](/en/terms/optimizer-optimizer/)
- [hyperparameter (Hyperparameter)](/en/terms/hyperparameter-hyperparameter/)
- [convergence (Konvergenz)](/en/terms/convergence-konvergenz/)
