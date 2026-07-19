---
title: Distillazione
term_id: distillation
category: training_techniques
subcategory: ''
tags:
- Optimization
- compression
- Model Efficiency
difficulty: 3
weight: 1
slug: distillation
date: '2026-07-18T15:24:21.292392Z'
lastmod: '2026-07-18T17:15:08.563692Z'
draft: false
source: agnes_llm
status: published
language: it
description: La distillazione della conoscenza è una tecnica di compressione del modello
  in cui un modello studente più piccolo imita il comportamento di un modello insegnante
  più grande.
---
## Definition

Questo processo prevede il trasferimento della conoscenza da una rete neurale 'insegnante' complessa e ad alte prestazioni a una rete 'studente' più semplice ed efficiente. Lo studente impara non solo dalle etichette rigide (hard labels), ma anche dalle distribuzioni di probabilità morbide (soft targets) generate dall'insegnante, catturando relazioni più ricche tra le classi.

### Summary

La distillazione della conoscenza è una tecnica di compressione del modello in cui un modello studente più piccolo imita il comportamento di un modello insegnante più grande.

## Key Concepts

- Architettura Insegnante-Studente
- Target Morbidi (Soft Targets)
- Compressione del Modello
- Efficienza di Inferenza

## Use Cases

- Implementazione di grandi modelli linguistici su dispositivi mobili
- Riduzione della latenza nelle applicazioni di visione artificiale in tempo reale
- Ottimizzazione dei modelli di deep learning per ambienti di edge computing

## Related Terms

- [Quantizzazione (riduzione della precisione numerica dei pesi)](/en/terms/quantizzazione-riduzione-della-precisione-numerica-dei-pesi/)
- [Pruning (eliminazione di parametri ridondanti)](/en/terms/pruning-eliminazione-di-parametri-ridondanti/)
- [Apprendimento per Trasferimento (trasferimento di conoscenze tra compiti)](/en/terms/apprendimento-per-trasferimento-trasferimento-di-conoscenze-tra-compiti/)
- [Ricerca dell'Architettura Neurale (automatizzazione del design del modello)](/en/terms/ricerca-dell-architettura-neurale-automatizzazione-del-design-del-modello/)
