---
title: "Datendurchsickern"
term_id: "leakage"
category: "basic_concepts"
subcategory: ""
tags: ["data-integrity", "evaluation", "best-practices"]
difficulty: 3
weight: 1
slug: "leakage"
aliases:
  - /de/terms/leakage/
date: "2026-07-18T11:21:20.803347Z"
lastmod: "2026-07-18T11:44:44.957551Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Datendurchsickern tritt auf, wenn Informationen außerhalb des Trainingsdatensatzes das Modell unbemerkt beeinflussen, was zu überoptimistischen Leistungsschätzungen führt."
---

## Definition

Datendurchsickern ist ein kritischer Fehler im maschinellen Lernen, bei dem das Modell während des Trainings auf Informationen zugreifen kann, die zur Vorhersagezeit nicht verfügbar wären. Dies geschieht häufig durch unsachgemäße Datenaufbereitung oder -aufteilung.

### Summary

Datendurchsickern tritt auf, wenn Informationen außerhalb des Trainingsdatensatzes das Modell unbemerkt beeinflussen, was zu überoptimistischen Leistungsschätzungen führt.

## Key Concepts

- Ziel-Durchsickern (Target Leakage)
- Kontamination von Trainings- und Testdaten
- Korrektes Aufteilen der Daten

## Use Cases

- Fehlersuche bei Überanpassung des Modells
- Validierung von Feature-Engineering-Pipelines
- Sicherstellung einer robusten Modellbewertung

## Related Terms

- [Überanpassung (Overfitting)](/en/terms/überanpassung-overfitting/)
- [Kreuzvalidierung (Cross-validation)](/en/terms/kreuzvalidierung-cross-validation/)
- [Merkmalskonstruktion (Feature engineering)](/en/terms/merkmalskonstruktion-feature-engineering/)
