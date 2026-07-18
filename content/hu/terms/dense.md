---
title: "Sűrű"
term_id: "dense"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "architecture"]
difficulty: 2
weight: 1
slug: "dense"
aliases:
  - /hu/terms/dense/
date: "2026-07-18T15:56:19.897284Z"
lastmod: "2026-07-18T17:15:09.774999Z"
draft: false
source: "agnes_llm"
status: "published"
language: "hu"
description: "Egy réteg vagy tenzor, ahol minden elem kapcsolódik az előző réteg vagy dimenzió minden eleméhez."
---

## Definition

Az ideghálózatokban a „sűrű” kifejezés a teljesen összekapcsolt rétegekre utal, ahol minden neuront az előző réteg összes neurona bemenete táplál. Ez ellentétben áll a konvolúciós vagy más ritkán összekapcsolt architektúrákban található sparsus kapcsolatokkal.

### Summary

Egy réteg vagy tenzor, ahol minden elem kapcsolódik az előző réteg vagy dimenzió minden eleméhez.

## Key Concepts

- Teljesen összekapcsolt
- Súlymátrix
- Aktivációs függvény
- Jellemzőintegráció

## Use Cases

- Végső osztályozási rétegek MLP-kben
- Jellemzőfúzió hibrid modellekben
- Egyszerű regressziós feladatok

## Code Example

```python
import tensorflow as tf
layer = tf.keras.layers.Dense(64, activation='relu')
```

## Related Terms

- [Feedforward neurális hálózat (Előrefelé irányuló neurális hálózat)](/en/terms/feedforward-neurális-hálózat-előrefelé-irányuló-neurális-hálózat/)
- [Hátr_PROPAGÁCIÓ (Backpropagation)](/en/terms/hátr_propagáció-backpropagation/)
- [ReLU (Rectified Linear Unit aktivációs függvény)](/en/terms/relu-rectified-linear-unit-aktivációs-függvény/)
- [Biais tag (Eltolási paraméter)](/en/terms/biais-tag-eltolási-paraméter/)
