---
title: "Co-training (Addestramento congiunto)"
term_id: "co_training"
category: "training_techniques"
subcategory: ""
tags: ["semi_supervised", "algorithm", "data_efficiency"]
difficulty: 4
weight: 1
slug: "co_training"
aliases:
  - /it/terms/co_training/
date: "2026-07-18T15:51:34.339342Z"
lastmod: "2026-07-18T17:15:08.606642Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Il co-training è un algoritmo di apprendimento semi-supervisionato in cui due viste dei dati vengono utilizzate per addestrare classificatori separati che etichettano iterativamente i dati non etichet"
---

## Definition

Questo metodo sfrutta più insiemi distinti di caratteristiche (viste) degli stessi punti dati. Inizialmente, due classificatori vengono addestrati su piccoli dataset etichettati da ciascuna vista. Successivamente, prevedono etichette per i dati non etich

### Summary

Il co-training è un algoritmo di apprendimento semi-supervisionato in cui due viste dei dati vengono utilizzate per addestrare classificatori separati che etichettano iterativamente i dati non etichettati l'uno per l'altro.

## Key Concepts

- Apprendimento Semi-Supervisionato
- Viste Multiple
- Etichettatura Iterativa
- Selezione ad Alta Confidenza

## Use Cases

- Classificazione del testo con più funzionalità
- Categorizzazione di pagine web
- Aumento dei dati con etichette limitate

## Related Terms

- [Semi-Supervised Learning (Apprendimento semi-supervisionato)](/en/terms/semi-supervised-learning-apprendimento-semi-supervisionato/)
- [Self-Training (Auto-addestramento)](/en/terms/self-training-auto-addestramento/)
- [Multi-view Learning (Apprendimento multi-vista)](/en/terms/multi-view-learning-apprendimento-multi-vista/)
- [Active Learning (Apprendimento attivo)](/en/terms/active-learning-apprendimento-attivo/)
