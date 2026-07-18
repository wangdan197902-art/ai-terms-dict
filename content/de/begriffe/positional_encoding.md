---
title: "Positions-Encoding"
term_id: "positional_encoding"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "nlp", "architecture"]
difficulty: 3
weight: 1
slug: "positional_encoding"
aliases:
  - /de/terms/positional_encoding/
date: "2026-07-18T10:59:24.106163Z"
lastmod: "2026-07-18T11:44:44.897838Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Eine Technik, die Informationen über die relative oder absolute Position von Tokens in einer Sequenz in Transformer-Modelle einfügt."
---

## Definition

Da Transformer alle Tokens parallel und nicht sequenziell wie RNNs verarbeiten, fehlt ihnen das inhärente Wissen über die Token-Reihenfolge. Das Positions-Encoding fügt den Eingabe-Embeddings spezifische Vektoren hinzu, um diese Reihenfolgeinformation bereitzustellen.

### Summary

Eine Technik, die Informationen über die relative oder absolute Position von Tokens in einer Sequenz in Transformer-Modelle einfügt.

## Key Concepts

- Sequenzreihenfolge
- Selbst-Aufmerksamkeit
- Sinusfunktionale Funktionen
- Token-Embeddings

## Use Cases

- Maschinelle Übersetzung
- Zusammenfassung von Texten
- Sprachmodellierung

## Code Example

```python
import torch
import math
def get_positional_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe.unsqueeze(0)
```

## Related Terms

- [Transformer-Architektur](/en/terms/transformer-architektur/)
- [Embedding](/en/terms/embedding/)
- [Aufmerksamkeitsmechanismus](/en/terms/aufmerksamkeitsmechanismus/)
- [RoPE (Rotary Positional Embeddings)](/en/terms/rope-rotary-positional-embeddings/)
