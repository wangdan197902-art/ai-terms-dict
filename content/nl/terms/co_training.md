---
title: Co-training
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
date: '2026-07-18T15:46:18.694592Z'
lastmod: '2026-07-18T17:15:08.725546Z'
draft: false
source: agnes_llm
status: published
language: nl
description: Co-training is een semi-gesuperviseerd leeralgoritme waarbij twee weergaven
  van de gegevens worden gebruikt om aparte klassificatoren te trainen die iteratief
  gelabelde gegevens voor elkaar aanduiden.
---
## Definition

Deze methode maakt gebruik van meerdere verschillende kenmerkensets (weergaven) van dezelfde datapunten. Aanvankelijk worden twee klassificatoren getraind op kleine gelabelde datasets van elke weergave. Ze voorspellen vervolgens labels voor onge

### Summary

Co-training is een semi-gesuperviseerd leeralgoritme waarbij twee weergaven van de gegevens worden gebruikt om aparte klassificatoren te trainen die iteratief gelabelde gegevens voor elkaar aanduiden.

## Key Concepts

- Semi-gesuperviseerd leren
- Meerdere weergaven
- Iteratieve labeltoewijzing
- Selectie op hoge betrouwbaarheid

## Use Cases

- Tekstclassificatie met meerdere kenmerken
- Categorisering van webpagina's
- Dataverrijking met beperkte labels

## Related Terms

- [Semi-gesuperviseerd leren](/en/terms/semi-gesuperviseerd-leren/)
- [Zelftrainen](/en/terms/zelftrainen/)
- [Multi-view learning](/en/terms/multi-view-learning/)
- [Actief leren](/en/terms/actief-leren/)
