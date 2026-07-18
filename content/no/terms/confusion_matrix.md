---
title: "Forvirringsmatrise"
term_id: "confusion_matrix"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "classification", "metrics"]
difficulty: 2
weight: 1
slug: "confusion_matrix"
aliases:
  - /no/terms/confusion_matrix/
date: "2026-07-18T15:47:24.766085Z"
lastmod: "2026-07-18T16:38:06.983280Z"
draft: false
source: "agnes_llm"
status: "published"
language: "no"
description: "En tabell som brukes til å beskrive ytelsen til en klassifikasjonsmodell på et sett med testdata."
---

## Definition

En forvirringsmatrise er en spesifikk tabellstruktur som gjør det mulig å visualisere ytelsen til en algoritme, typisk en overvåket læringsmodell. Den viser antall sanne positive, sanne negative, falske positive og falske negative resultater.

### Summary

En tabell som brukes til å beskrive ytelsen til en klassifikasjonsmodell på et sett med testdata.

## Key Concepts

- Sanne positive
- Falske negative
- Presisjon
- Omfang (Recall)

## Use Cases

- Vurdering av binære klassifikatorer
- Analyse av flerklasses klassifikasjonsytelse
- Feilsøking av modellbias i ubalanserte datasett

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (presisjon)](/en/terms/precision-presisjon/)
- [recall (omfang/recall)](/en/terms/recall-omfang-recall/)
- [F1 score (F1-score)](/en/terms/f1-score-f1-score/)
- [ROC curve (ROC-kurve)](/en/terms/roc-curve-roc-kurve/)
