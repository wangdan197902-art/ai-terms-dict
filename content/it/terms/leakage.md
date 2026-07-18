---
title: "Data Leakage"
term_id: "leakage"
category: "basic_concepts"
subcategory: ""
tags: ["data-integrity", "evaluation", "best-practices"]
difficulty: 3
weight: 1
slug: "leakage"
aliases:
  - /it/terms/leakage/
date: "2026-07-18T16:07:45.528824Z"
lastmod: "2026-07-18T17:15:08.642347Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Il data leakage si verifica quando informazioni esterne al dataset di addestramento influenzano involontariamente il modello, portando a stime delle prestazioni eccessivamente ottimistiche."
---

## Definition

Il data leakage è un errore critico nell'apprendimento automatico in cui il modello ottiene accesso a informazioni durante l'addestramento che non sarebbero state disponibili al momento della previsione. Questo accade spesso a causa di una suddivisione dei dati impropria o di una manipolazione errata delle feature.

### Summary

Il data leakage si verifica quando informazioni esterne al dataset di addestramento influenzano involontariamente il modello, portando a stime delle prestazioni eccessivamente ottimistiche.

## Key Concepts

- Target leakage
- Contaminazione tra training e test
- Corretta suddivisione dei dati

## Use Cases

- Debugging dell'overfitting del modello
- Validazione dei pipeline di feature engineering
- Garantire una valutazione robusta del modello

## Related Terms

- [Overfitting (sovradattamento)](/en/terms/overfitting-sovradattamento/)
- [Cross-validation (validazione incrociata)](/en/terms/cross-validation-validazione-incrociata/)
- [Feature engineering (ingegneria delle caratteristiche)](/en/terms/feature-engineering-ingegneria-delle-caratteristiche/)
