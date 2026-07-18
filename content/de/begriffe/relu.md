---
title: "ReLU"
term_id: "relu"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "activation-functions", "deep-learning"]
difficulty: 3
weight: 1
slug: "relu"
aliases:
  - /de/terms/relu/
date: "2026-07-18T10:59:36.705217Z"
lastmod: "2026-07-18T11:44:44.899129Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Rectified Linear Unit ist eine Aktivierungsfunktion, die die Eingabe direkt ausgibt, wenn sie positiv ist, andernfalls null."
---

## Definition

ReLU wird aufgrund seiner Recheneffizienz und seiner Fähigkeit, das Problem des verschwindenden Gradienten zu mildern, häufig in neuronalen Netzen des Deep Learning eingesetzt. Mathematisch definiert als f(x) = max(0, x), führt es Nichtlinearität in das Netzwerk ein, während es gleichzeitig die Berechnung vereinfacht.

### Summary

Rectified Linear Unit ist eine Aktivierungsfunktion, die die Eingabe direkt ausgibt, wenn sie positiv ist, andernfalls null.

## Key Concepts

- Nichtlinearität
- Aktivierungsfunktion
- Verschwindender Gradient
- Stückweise linear

## Use Cases

- Versteckte Schichten in CNNs
- Tiefe Feedforward-Netzwerke
- Modelle zur Bilderkennung

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid](/en/terms/sigmoid/)
- [Tanh](/en/terms/tanh/)
- [Leaky ReLU](/en/terms/leaky-relu/)
- [Neural Network](/en/terms/neural-network/)
