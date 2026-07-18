---
title: "Dicht"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /de/terms/dense/
date: "2026-07-18T11:11:39.366889Z"
lastmod: "2026-07-18T11:44:44.931210Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Eine Schicht oder einen Tensor, bei dem jedes Element mit jedem Element der vorherigen Schicht oder Dimension verbunden ist."
---

## Definition

In neuronalen Netzen bezeichnet 'dicht' voll verbundene Schichten, bei denen jeder Neuron Eingaben von allen Neuronen der vorangehenden Schicht erhält. Dies steht im Gegensatz zu spärlichen Verbindungen, wie sie in konvolutionalen oder anderen spezialisierten Architekturen vorkommen.

### Summary

Eine Schicht oder einen Tensor, bei dem jedes Element mit jedem Element der vorherigen Schicht oder Dimension verbunden ist.

## Key Concepts

- Vollständig verbunden
- Gewichtsmatrix
- Aktivierungsfunktion
- Merkmalsintegration

## Use Cases

- Letzte Klassifizierungsschichten in Mehrschichtigen Perzeptrons (MLPs)
- Merkmalsfusion in hybriden Modellen
- Einfache Regressionsaufgaben

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (Vorwärtsgerichtetes neuronales Netz)](/en/terms/feedforward-neural-network-vorwärtsgerichtetes-neuronales-netz/)
- [Backpropagation (Fehler-Rückwärtsausbreitung)](/en/terms/backpropagation-fehler-rückwärtsausbreitung/)
- [ReLU (Rectified Linear Unit)](/en/terms/relu-rectified-linear-unit/)
- [Bias Term (Bias-Term / Verschiebungswert)](/en/terms/bias-term-bias-term-verschiebungswert/)
