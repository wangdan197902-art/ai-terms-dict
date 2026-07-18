---
title: "Tett"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /no/terms/dense/
date: "2026-07-18T15:51:16.929665Z"
lastmod: "2026-07-18T16:38:06.993060Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "Et lag eller en tensor der hvert element er koblet til hvert element i det forrige laget eller dimensjonen."
---

## Definition

I nevrale nettverk refererer 'tett' til fullt tilkoblede lag der hver neuron mottar input fra alle nerver i det foregående laget. Dette står i kontrast til sparsomme tilkoblinger funnet i konvolusjons-

### Summary

Et lag eller en tensor der hvert element er koblet til hvert element i det forrige laget eller dimensjonen.

## Key Concepts

- Fullt tilkoblet
- Vektmatrise
- Aktiveringsfunksjon
- Funksjonsintegrering

## Use Cases

- Siste klassifiseringslag i MLP-er
- Funksjonsfusjon i hybride modeller
- Enkle regresjonsoppgaver

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward-nevrontverk (Neuralt nettverk med én vei)](/en/terms/feedforward-nevrontverk-neuralt-nettverk-med-én-vei/)
- [Tilbakepropagering (Algoritme for trening)](/en/terms/tilbakepropagering-algoritme-for-trening/)
- [ReLU (Aktiveringsfunksjon)](/en/terms/relu-aktiveringsfunksjon/)
- [Biasledd (Konstant offset)](/en/terms/biasledd-konstant-offset/)
