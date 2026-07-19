---
title: Darstellungskollaps
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
date: '2026-07-18T11:32:10.084751Z'
lastmod: '2026-07-18T11:44:44.981785Z'
draft: false
source: agnes_llm
status: published
language: de
description: Ein Fehlermodus im selbstüberwachten Lernen, bei dem das Modell für alle
  Eingaben identische Darstellungen ausgibt und dabei seine Unterscheidungskraft verliert.
---
## Definition

Darstellungskollaps tritt auf, wenn ein neuronales Netz, insbesondere in selbstüberwachten kontrastiven Lernrahmenwerken, lernt, alle Eingabedatenpunkte auf denselben festen Ausgabvektor abzubilden. Dies ist eine triviale Lösung, die verhindert, dass das Modell sinnvolle Merkmale lernt.

### Summary

Ein Fehlermodus im selbstüberwachten Lernen, bei dem das Modell für alle Eingaben identische Darstellungen ausgibt und dabei seine Unterscheidungskraft verliert.

## Key Concepts

- Selbstüberwachtes Lernen
- Kontrastiver Verlust
- Triviale Lösungen
- Merkmalslernen

## Use Cases

- Fehlersuche in SimCLR- oder MoCo-Modellen
- Verbesserung kontrastiver Verlustfunktionen
- Analyse der Modellkonvergenz

## Related Terms

- [Kontrastives Lernen](/en/terms/kontrastives-lernen/)
- [Batch-Normalisierung](/en/terms/batch-normalisierung/)
- [Momentum-Encoder](/en/terms/momentum-encoder/)
- [Merkmalsextraktion](/en/terms/merkmalsextraktion/)
