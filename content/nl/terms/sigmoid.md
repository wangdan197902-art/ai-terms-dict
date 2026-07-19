---
title: "Sigmoid"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
date: "2026-07-18T16:16:52.293122Z"
lastmod: "2026-07-18T17:15:08.786894Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een wiskundige functie die elke reëel getal omzet in een waarde tussen nul en één, met een S-vormige curve als resultaat."
---
## Definition

De sigmoidfunctie, gedefinieerd als σ(z) = 1 / (1 + e^-z), wordt veel gebruikt in machine learning om waarschijnlijkheden te modelleren. Het drukt invoerwaarden samen tot het bereik (0, 1), wat het geschikt maakt voor binaire classificatie.

### Summary

Een wiskundige functie die elke reëel getal omzet in een waarde tussen nul en één, met een S-vormige curve als resultaat.

## Key Concepts

- Logistische functie
- Waarschijnlijkheidsmapping
- Verdwijnend gradientprobleem
- Non-lineariteit

## Use Cases

- Uitvoer bij binaire classificatie
- Logistische regressie
- Activering in ondiepe neurale netwerken

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU](/en/terms/relu/)
- [Softmax](/en/terms/softmax/)
- [Logistic Regression](/en/terms/logistic-regression/)
- [Activation Function](/en/terms/activation-function/)
