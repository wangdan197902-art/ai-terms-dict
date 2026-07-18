---
title: "Sigmoid"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
aliases:
  - /pl/terms/sigmoid/
date: "2026-07-18T16:16:17.214079Z"
lastmod: "2026-07-18T17:15:08.917191Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Funkcja matematyczna, która przekształca dowolną liczbę rzeczywistą na wartość między zerem a jeden, tworząc krzywą w kształcie litery S."
---

## Definition

Funkcja sigmoidalna, zdefiniowana jako σ(z) = 1 / (1 + e^-z), jest szeroko stosowana w uczeniu maszynowym do modelowania prawdopodobieństw. Spłaszcza wartości wejściowe do zakresu (0, 1), co czyni ją odpowiednią dla klasyfikacji binarnej, choć może prowadzić do problemu zanikającego gradientu w głębokich sieciach.

### Summary

Funkcja matematyczna, która przekształca dowolną liczbę rzeczywistą na wartość między zerem a jeden, tworząc krzywą w kształcie litery S.

## Key Concepts

- Funkcja logistyczna
- Mapowanie prawdopodobieństwa
- Zanikający gradient
- Nielinearność

## Use Cases

- Wyjście klasyfikacji binarnej
- Regresja logistyczna
- Funkcja aktywacji w płytkich sieciach neuronowych

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU](/en/terms/relu/)
- [Softmax](/en/terms/softmax/)
- [Regresja logistyczna](/en/terms/regresja-logistyczna/)
- [Funkcja aktywacji](/en/terms/funkcja-aktywacji/)
