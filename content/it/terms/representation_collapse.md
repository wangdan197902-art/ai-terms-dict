---
title: Collasso della rappresentazione
term_id: representation_collapse
category: basic_concepts
subcategory: ''
tags:
- Self Supervised
- Training Dynamics
- Computer Vision
difficulty: 3
weight: 1
slug: representation_collapse
date: '2026-07-18T16:19:04.742196Z'
lastmod: '2026-07-18T17:15:08.665310Z'
draft: false
source: agnes_llm
status: published
language: it
description: Una modalità di fallimento nell'apprendimento auto-supervisionato in
  cui il modello produce rappresentazioni identiche per tutti gli input, perdendo
  il potere discriminativo.
---
## Definition

Il collasso della rappresentazione si verifica quando una rete neurale, in particolare nei framework di apprendimento contrastivo auto-supervisionato, impara a mappare tutti i punti dati di input sullo stesso vettore di output fisso. Questa soluzione banale riduce la perdita ma elimina l'utilità del modello per compiti successivi.

### Summary

Una modalità di fallimento nell'apprendimento auto-supervisionato in cui il modello produce rappresentazioni identiche per tutti gli input, perdendo il potere discriminativo.

## Key Concepts

- Apprendimento Auto-Supervisionato
- Perdita Contrastiva
- Soluzioni Banali
- Apprendimento delle Caratteristiche

## Use Cases

- Debugging di modelli SimCLR o MoCo
- Miglioramento delle Funzioni di Perdita Contrastiva
- Analisi della Convergenza del Modello

## Related Terms

- [Apprendimento Contrastivo](/en/terms/apprendimento-contrastivo/)
- [Normalizzazione di Batch](/en/terms/normalizzazione-di-batch/)
- [Encoder a Momento](/en/terms/encoder-a-momento/)
- [Estrazione delle Caratteristiche](/en/terms/estrazione-delle-caratteristiche/)
