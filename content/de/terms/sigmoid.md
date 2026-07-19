---
title: "Sigmoid-Funktion"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
date: "2026-07-18T11:33:18.365080Z"
lastmod: "2026-07-18T11:44:44.985397Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Eine mathematische Funktion, die jede reelle Zahl auf einen Wert zwischen Null und Eins abbildet und eine S-förmige Kurve bildet."
---
## Definition

Die Sigmoid-Funktion, definiert als σ(z) = 1 / (1 + e^-z), wird im maschinellen Lernen häufig zur Modellierung von Wahrscheinlichkeiten verwendet. Sie komprimiert Eingabewerte in den Bereich (0, 1), was sie für binäre Klassifikationsaufgaben geeignet macht.

### Summary

Eine mathematische Funktion, die jede reelle Zahl auf einen Wert zwischen Null und Eins abbildet und eine S-förmige Kurve bildet.

## Key Concepts

- Logistische Funktion
- Wahrscheinlichkeitsabbildung
- Verschwindender Gradient
- Nichtlinearität

## Use Cases

- Ausgabe bei binärer Klassifikation
- Logistische Regression
- Aktivierung in flachen neuronalen Netzen

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU (Rectified Linear Unit)](/en/terms/relu-rectified-linear-unit/)
- [Softmax (Multiklassen-Aktivierung)](/en/terms/softmax-multiklassen-aktivierung/)
- [Logistische Regression (statistisches Modell)](/en/terms/logistische-regression-statistisches-modell/)
- [Aktivierungsfunktion (Netzwerkkomponente)](/en/terms/aktivierungsfunktion-netzwerkkomponente/)
