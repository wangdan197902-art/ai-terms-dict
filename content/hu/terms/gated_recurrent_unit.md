---
title: "Záras visszatérő egység"
term_id: "gated_recurrent_unit"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Networks", "Deep Learning", "Architecture"]
difficulty: 3
weight: 1
slug: "gated_recurrent_unit"
aliases:
  - /hu/terms/gated_recurrent_unit/
date: "2026-07-18T16:00:53.828294Z"
lastmod: "2026-07-18T17:15:09.787140Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "Egy típusú visszatérő neurális hálózati architektúra, amely záramechanizmusokat használ az információáramlás szabályozására, és az LSTM egyszerűsített alternatívájaként szolgál."
---

## Definition

A Záras Visszatérő Egység (GRU) egy specializált visszatérő neurális hálózati (RNN) sejt, amelyet szekvenciális adatokban lévő hosszú távú függőségek rögzítésére terveztek. Egyszerűsíti a Hosszú Rövidtávmemóriás (LSTM) architektúrát, miközben hasonló teljesítményt nyújt kevesebb paraméterrel.

### Summary

Egy típusú visszatérő neurális hálózati architektúra, amely záramechanizmusokat használ az információáramlás szabályozására, és az LSTM egyszerűsített alternatívájaként szolgál.

## Key Concepts

- Visszatérő neurális hálózat
- Frissítési zár
- Visszaállítási zár
- Szekvenciamodellés

## Use Cases

- Természetes nyelvfeldolgozás
- Idősoros előrejelzés
- Beszédfelismerés

## Code Example

```python
import torch.nn as nn

# Define a simple GRU layer
gru = nn.GRU(input_size=10, hidden_size=20, num_layers=1)

# Example input: (seq_len, batch, input_size)
input_data = torch.randn(5, 3, 10)
hidden_state = None

output, hidden = gru(input_data, hidden_state)
```

## Related Terms

- [LSTM (hosszú rövidtávmemória)](/en/terms/lstm-hosszú-rövidtávmemória/)
- [RNN (visszatérő neurális hálózat)](/en/terms/rnn-visszatérő-neurális-hálózat/)
- [Mélytanulás](/en/terms/mélytanulás/)
- [Szekvencia-szekvencia (modellezés)](/en/terms/szekvencia-szekvencia-modellezés/)
