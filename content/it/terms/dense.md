---
title: "Dense"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /it/terms/dense/
date: "2026-07-18T15:56:22.399525Z"
lastmod: "2026-07-18T17:15:08.618060Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Uno strato o tensore in cui ogni elemento è connesso a ogni elemento dello strato o della dimensione precedente."
---

## Definition

Nelle reti neurali, 'dense' si riferisce agli strati completamente connessi in cui ogni neurone riceve l'input da tutti i neuroni dello strato precedente. Questo contrasta con le connessioni sparse tipiche delle reti convoluzionali o...

### Summary

Uno strato o tensore in cui ogni elemento è connesso a ogni elemento dello strato o della dimensione precedente.

## Key Concepts

- Completamente Connesso
- Matrice dei Pesi
- Funzione di Attivazione
- Integrazione delle Caratteristiche

## Use Cases

- Strati di classificazione finale nei MLP
- Fusione delle caratteristiche nei modelli ibridi
- Compiti semplici di regressione

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward Neural Network (Rete neurale feedforward)](/en/terms/feedforward-neural-network-rete-neurale-feedforward/)
- [Backpropagation (Retropropagazione dell'errore)](/en/terms/backpropagation-retropropagazione-dell-errore/)
- [ReLU (Funzione di attivazione lineare rettificata)](/en/terms/relu-funzione-di-attivazione-lineare-rettificata/)
- [Bias Term (Termine di bias)](/en/terms/bias-term-termine-di-bias/)
