---
title: Multiple-Instance-Lernen
term_id: multiple_instance_learning
category: training_techniques
subcategory: ''
tags:
- Supervised Learning
- Weak Labeling
- ML Paradigm
difficulty: 4
weight: 1
slug: multiple_instance_learning
date: '2026-07-18T10:59:11.210003Z'
lastmod: '2026-07-18T11:44:44.897174Z'
draft: false
source: agnes_llm
status: published
language: de
description: Ein schwach überwachtes Lernparadigma, bei dem Labels ganzen Gruppen
  von Instanzen (sogenannten „Bags“) und nicht einzelnen Instanzen zugewiesen werden.
---
## Definition

Multiple-Instance-Lernen (MIL) adressiert Szenarien, in denen Daten in sogenannte „Bags“ gruppiert sind, die jeweils ein einzelnes Label tragen, während die individuellen Instanzen innerhalb dieser Bags unbeschriftet bleiben. Ein Bag wird typischerweise als positiv klassifiziert, wenn mindestens eine seiner Instanzen das Merkmal aufweist, das mit dem positiven Label verbunden ist, und als negativ, wenn keine der Instanzen dieses Merkmal zeigt.

### Summary

Ein schwach überwachtes Lernparadigma, bei dem Labels ganzen Gruppen von Instanzen (sogenannten „Bags“) und nicht einzelnen Instanzen zugewiesen werden.

## Key Concepts

- Bag-Level-Labeling
- Instanz-Level-Unsicherheit
- Schwache Überwachung
- Logik für positive/negative Bags

## Use Cases

- Vorhersage der Wirkstoffaktivität
- Bildklassifizierung mit Bounding Boxes
- Inhaltsbasierte Bildersuche

## Related Terms

- [weak_supervision (schwache Überwachung)](/en/terms/weak_supervision-schwache-überwachung/)
- [bagging (Ensemble-Methode)](/en/terms/bagging-ensemble-methode/)
- [instance_classification (Instanzklassifizierung)](/en/terms/instance_classification-instanzklassifizierung/)
- [label_noise (Label-Rauschen)](/en/terms/label_noise-label-rauschen/)
