---
title: Tæt
term_id: dense
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- architecture
difficulty: 2
weight: 1
slug: dense
date: '2026-07-18T15:52:22.737616Z'
lastmod: '2026-07-18T17:15:09.279980Z'
draft: false
source: agnes_llm
status: published
language: da
description: Et lag eller en tensor, hvor hvert element er forbundet med hvert element
  i det foregående lag eller dimension.
---
## Definition

I neurale netværk henviser 'tæt' til fuldt tilsluttede lag, hvor hver neuron modtager input fra alle neuroner i det foregående lag. Dette står i kontrast til sparsomme forbindelser, der findes i konvolutionære eller

### Summary

Et lag eller en tensor, hvor hvert element er forbundet med hvert element i det foregående lag eller dimension.

## Key Concepts

- Fuldt tilsluttet
- Vægtmatrix
- Aktiveringsfunktion
- Funktionintegration

## Use Cases

- Endelige klassificeringslag i MLP'er
- Fusionslag af funktioner i hybride modeller
- Enkle regressionsopgaver

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward-neuralt netværk (En type neuralt netværk, hvor informationen kun bevæger sig fremad)](/en/terms/feedforward-neuralt-netværk-en-type-neuralt-netværk-hvor-informationen-kun-bevæger-sig-fremad/)
- [Bagudpropagering (Algoritme til træning af neurale netværk)](/en/terms/bagudpropagering-algoritme-til-træning-af-neurale-netværk/)
- [ReLU (En almindelig aktiveringsfunktion)](/en/terms/relu-en-almindelig-aktiveringsfunktion/)
- [Biasled (En konstant offset i en neuron)](/en/terms/biasled-en-konstant-offset-i-en-neuron/)
