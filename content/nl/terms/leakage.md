---
title: Datalek
term_id: leakage
category: basic_concepts
subcategory: ''
tags:
- Data Integrity
- evaluation
- Best Practices
difficulty: 3
weight: 1
slug: leakage
date: '2026-07-18T16:03:14.504294Z'
lastmod: '2026-07-18T17:15:08.760960Z'
draft: false
source: agnes_llm
status: published
language: nl
description: Datalek treedt op wanneer informatie buiten de trainingsdataset het model
  onbedoeld beïnvloedt, wat leidt tot te optimistische prestatieschattingen.
---
## Definition

Datalek is een kritieke fout in machine learning waarbij het model tijdens het trainen toegang krijgt tot informatie die niet beschikbaar zou zijn geweest op het moment van voorspelling. Dit gebeurt vaak door onjuiste dataverwerking.

### Summary

Datalek treedt op wanneer informatie buiten de trainingsdataset het model onbedoeld beïnvloedt, wat leidt tot te optimistische prestatieschattingen.

## Key Concepts

- Doelvariabele-lek
- Besmetting tussen trainings- en testset
- Juiste gegevensverdeling

## Use Cases

- Foutopsporing bij overfitting van modellen
- Validatie van pipelines voor feature engineering
- Zorgen voor robuuste modelevaluatie

## Related Terms

- [Overfitting (overaanpassing)](/en/terms/overfitting-overaanpassing/)
- [Cross-validatie ( kruisvalidatie )](/en/terms/cross-validatie-kruisvalidatie/)
- [Feature engineering (kenmerkengineering)](/en/terms/feature-engineering-kenmerkengineering/)
