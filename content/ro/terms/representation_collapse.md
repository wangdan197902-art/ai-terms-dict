---
title: "Colapsul reprezentării"
term_id: "representation_collapse"
category: "basic_concepts"
subcategory: ""
tags: ["self_supervised", "training_dynamics", "computer_vision"]
difficulty: 3
weight: 1
slug: "representation_collapse"
aliases:
  - /ro/terms/representation_collapse/
date: "2026-07-18T16:19:26.009040Z"
lastmod: "2026-07-18T17:15:09.698825Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "O stare de eșec în învățarea auto-supervizată în care modelul generează reprezentări identice pentru toate intrările, pierzându-și puterea de discriminare."
---

## Definition

Colapsul reprezentării apare când o rețea neuronală, în special în cadrele de învățare contrastivă auto-supervizată, învață să mapeze toate punctele de date de intrare la același vector de ieșire fix. Aceasta constituie o soluție trivială care nu captează structura datelor.

### Summary

O stare de eșec în învățarea auto-supervizată în care modelul generează reprezentări identice pentru toate intrările, pierzându-și puterea de discriminare.

## Key Concepts

- Învățare Auto-supervizată
- Funcția de Pierdere Contrastivă
- Soluții Triviale
- Învățarea Caracteristicilor

## Use Cases

- Depanarea modelelor SimCLR sau MoCo
- Îmbunătățirea Funcțiilor de Pierdere Contrastive
- Analiza Convergenței Modelului

## Related Terms

- [Învățare Contrastivă](/en/terms/învățare-contrastivă/)
- [Normalizare pe Lot (Batch Normalization)](/en/terms/normalizare-pe-lot-batch-normalization/)
- [Encoder de Moment](/en/terms/encoder-de-moment/)
- [Extragerea Caracteristicilor](/en/terms/extragerea-caracteristicilor/)
