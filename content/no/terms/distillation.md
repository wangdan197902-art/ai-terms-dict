---
title: Distillering
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
date: '2026-07-18T15:25:34.270247Z'
lastmod: '2026-07-18T16:38:06.934797Z'
draft: false
source: agnes_llm
status: published
language: 'no'
description: Kunnskapsdistillering er en teknikk for modellkomprimering der en mindre
  «studentmodell» lærer å etterligne oppførselen til en større «lærermodell».
---
## Definition

Denne prosessen involverer overføring av kunnskap fra et komplekst, høytytende «lærer»-nøyronettverk til et enklere, mer effektivt «student»-nøyronettverk. Studenten lærer ikke bare fra harde etiketter (hard labels), men også fra de sannsynlighetsfordelte utgangene fra læreren.

### Summary

Kunnskapsdistillering er en teknikk for modellkomprimering der en mindre «studentmodell» lærer å etterligne oppførselen til en større «lærermodell».

## Key Concepts

- Lærer-Student-arkitektur
- Målløse mål (Soft targets)
- Modellkomprimering
- Effektivitet ved inferens

## Use Cases

- Distribusjon av store språkmodeller på mobile enheter
- Reduksjon av latens i sanntids datamaskinse-applikasjoner
- Optimalisering av dype læringsmodeller for edge computing-miljøer

## Related Terms

- [Kvantisering (Quantization)](/en/terms/kvantisering-quantization/)
- [Forkorting (Pruning)](/en/terms/forkorting-pruning/)
- [Overføringslæring (Transfer Learning)](/en/terms/overføringslæring-transfer-learning/)
- [Søk etter nøyronarkitektur (Neural Architecture Search)](/en/terms/søk-etter-nøyronarkitektur-neural-architecture-search/)
