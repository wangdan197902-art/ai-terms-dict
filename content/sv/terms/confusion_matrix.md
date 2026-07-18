---
title: "Förvirringsmatris"
term_id: "confusion_matrix"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "classification", "metrics"]
difficulty: 2
weight: 1
slug: "confusion_matrix"
aliases:
  - /sv/terms/confusion_matrix/
date: "2026-07-18T15:50:19.210889Z"
lastmod: "2026-07-18T17:15:08.986913Z"
draft: false
source: "agnes_llm"
status: "published"
language: "sv"
description: "En tabell som används för att beskriva prestandan hos en klassificeringsmodell på ett uppsättning testdata."
---

## Definition

En förvirringsmatris är en specifik tabelllayout som möjliggör visualisering av en algoritms prestanda, vanligtvis en övervakad inlärningsalgoritm. Den visar antalet sanna positiva, sanna negativa, falska positiva och falska negativa resultat.

### Summary

En tabell som används för att beskriva prestandan hos en klassificeringsmodell på ett uppsättning testdata.

## Key Concepts

- Sanna positiva
- Falska negativa
- Precision
- Recall

## Use Cases

- Utvärdering av binära klassificerare
- Analys av prestanda vid flerklassklassificering
- Felsökning av modellbias i obalanserade dataset

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (noggrannhet)](/en/terms/precision-noggrannhet/)
- [recall (träffsäkerhet)](/en/terms/recall-träffsäkerhet/)
- [F1 score (F1-poäng)](/en/terms/f1-score-f1-poäng/)
- [ROC curve (ROC-kurva)](/en/terms/roc-curve-roc-kurva/)
