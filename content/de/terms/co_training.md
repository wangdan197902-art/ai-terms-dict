---
title: Ko-Training
term_id: co_training
category: training_techniques
subcategory: ''
tags:
- Semi Supervised
- algorithm
- Data Efficiency
difficulty: 4
weight: 1
slug: co_training
date: '2026-07-18T11:07:28.137971Z'
lastmod: '2026-07-18T11:44:44.917897Z'
draft: false
source: agnes_llm
status: published
language: de
description: Ko-Training ist ein semi-supervisierter Lernalgorithmus, bei dem zwei
  Ansichten der Daten verwendet werden, um separate Klassifikatoren zu trainieren,
  die unbeschriftete Daten iterativ gegenseitig bes
---
## Definition

Diese Methode nutzt mehrere unterschiedliche Merkmalsätze (Ansichten) derselben Datenpunkte. Zunächst werden zwei Klassifikatoren auf kleinen beschrifteten Datensätzen aus jeder Ansicht trainiert. Sie sagen dann Labels für unbes

### Summary

Ko-Training ist ein semi-supervisierter Lernalgorithmus, bei dem zwei Ansichten der Daten verwendet werden, um separate Klassifikatoren zu trainieren, die unbeschriftete Daten iterativ gegenseitig beschriften.

## Key Concepts

- Semi-supervised Learning
- Mehrere Ansichten
- Iteratives Beschriften
- Auswahl mit hoher Konfidenz

## Use Cases

- Textklassifizierung mit mehreren Merkmalen
- Kategorisierung von Webseiten
- Datenaugmentierung mit begrenzten Labels

## Related Terms

- [Semi-supervised Learning](/en/terms/semi-supervised-learning/)
- [Self-Training (Selbsttraining)](/en/terms/self-training-selbsttraining/)
- [Multi-view Learning](/en/terms/multi-view-learning/)
- [Aktives Lernen](/en/terms/aktives-lernen/)
