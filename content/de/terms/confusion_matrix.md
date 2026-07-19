---
title: Konfusionsmatrix
term_id: confusion_matrix
category: basic_concepts
subcategory: ''
tags:
- evaluation
- Classification
- metrics
difficulty: 2
weight: 1
slug: confusion_matrix
date: '2026-07-18T11:08:35.675302Z'
lastmod: '2026-07-18T11:44:44.920503Z'
draft: false
source: agnes_llm
status: published
language: de
description: Eine Tabelle zur Beschreibung der Leistung eines Klassifikationsmodells
  auf einem Satz von Testdaten.
---
## Definition

Eine Konfusionsmatrix ist eine spezifische Tabellenanordnung, die die Visualisierung der Leistung eines Algorithmus ermöglicht, typischerweise eines überwachtes Lernverfahrens. Sie zeigt die Häufigkeiten von wahren Positiven, wahren Negativen, falschen Positiven und falschen Negativen.

### Summary

Eine Tabelle zur Beschreibung der Leistung eines Klassifikationsmodells auf einem Satz von Testdaten.

## Key Concepts

- Wahre Positive
- Falsche Negative
- Präzision
- Recall (Trefferquote)

## Use Cases

- Bewertung binärer Klassifikatoren
- Analyse der Leistung bei Multi-Class-Klassifizierung
- Fehlersuche bei Modellverzerrungen in unausgeglichenen Datensätzen

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (Präzision)](/en/terms/precision-präzision/)
- [recall (Trefferquote)](/en/terms/recall-trefferquote/)
- [F1 score (F1-Score)](/en/terms/f1-score-f1-score/)
- [ROC curve (ROC-Kurve)](/en/terms/roc-curve-roc-kurve/)
