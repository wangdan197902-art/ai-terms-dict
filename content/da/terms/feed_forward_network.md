---
title: "Feed-Forward Network"
term_id: "feed_forward_network"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "architecture", "fundamentals"]
difficulty: 2
weight: 1
slug: "feed_forward_network"
aliases:
  - /da/terms/feed_forward_network/
date: "2026-07-18T15:55:46.725268Z"
lastmod: "2026-07-18T17:15:09.288621Z"
draft: false
source: "agnes_llm"
status: "published"
language: "da"
description: "En klasse af kunstige neurale netværk, hvor forbindelserne mellem noder ikke danner cyklusser, men spreder information i én retning."
---

## Definition

Feed-Forward Networks (FFN'er), også kendt som Multi-Layer Perceptrons (MLP'er), behandler data sekventielt gennem lag af neuroner fra input til output uden feedback-løkker. Hver neuron modtager input

### Summary

En klasse af kunstige neurale netværk, hvor forbindelserne mellem noder ikke danner cyklusser, men spreder information i én retning.

## Key Concepts

- Ingen cyklusser
- Lag (Input, Skjult, Output)
- Aktiveringsfunktioner
- Vægtede summer

## Use Cases

- Enkle regressionsopgaver
- Klassificeringsproblemer med tabeldata
- Byggeklodser til dybere arkitekturer

## Code Example

```python
import torch.nn as nn

class SimpleFFN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleFFN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
```

## Related Terms

- [Multi-Layer Perceptron](/en/terms/multi-layer-perceptron/)
- [Bagpropagering](/en/terms/bagpropagering/)
- [Aktiveringsfunktion](/en/terms/aktiveringsfunktion/)
- [Neuralt netværk](/en/terms/neuralt-netværk/)
