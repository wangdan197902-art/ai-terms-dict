---
title: "Verwarringsmatrix"
term_id: "confusion_matrix"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "classification", "metrics"]
difficulty: 2
weight: 1
slug: "confusion_matrix"
aliases:
  - /nl/terms/confusion_matrix/
date: "2026-07-18T15:47:25.931649Z"
lastmod: "2026-07-18T17:15:08.728273Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een tabel die wordt gebruikt om de prestaties van een classificatiemodel op een set testgegevens te beschrijven."
---

## Definition

Een verwarringsmatrix is een specifieke tabelindeling die visualisatie mogelijk maakt van de prestaties van een algoritme, meestal een onderwezen leermodel. Het toont de aantallen waar positief, waar negatief, vals positief en vals negatief.

### Summary

Een tabel die wordt gebruikt om de prestaties van een classificatiemodel op een set testgegevens te beschrijven.

## Key Concepts

- Waar Positief
- Vals Negatief
- Precisie
- Herinnering

## Use Cases

- Beoordelen van binaire klassificators
- Analyseren van prestaties bij multi-class classificatie
- Foutopsporing van modelbias in onevenwichtige datasets

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (precisie)](/en/terms/precision-precisie/)
- [recall (herinnering)](/en/terms/recall-herinnering/)
- [F1 score (F1-score)](/en/terms/f1-score-f1-score/)
- [ROC curve (ROC-curve)](/en/terms/roc-curve-roc-curve/)
