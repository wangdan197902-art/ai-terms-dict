---
title: "Matricea de confuzie"
term_id: "confusion_matrix"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "classification", "metrics"]
difficulty: 2
weight: 1
slug: "confusion_matrix"
aliases:
  - /ro/terms/confusion_matrix/
date: "2026-07-18T15:50:32.237576Z"
lastmod: "2026-07-18T17:15:09.639044Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "Un tabel utilizat pentru a descrie performanța unui model de clasificare pe un set de date de testare."
---

## Definition

O matrice de confuzie este o structură tabulară specifică care permite vizualizarea performanței unui algoritm, de obicei unul de învățare supravegheată. Aceasta afișează numărul de pozitive adevărate, negative adevărate, false pozitive și false negative.

### Summary

Un tabel utilizat pentru a descrie performanța unui model de clasificare pe un set de date de testare.

## Key Concepts

- Pozitive Adevărate
- Negative False
- Precizie
- Recall (Rata de recuperare)

## Use Cases

- Evaluarea clasificatoarelor binare
- Analiza performanței clasificării multi-clasă
- Depistarea biasului modelului în seturi de date dezechilibrate

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precizie (măsură a exactității predicțiilor pozitive)](/en/terms/precizie-măsură-a-exactității-predicțiilor-pozitive/)
- [recall (măsură a capacității de a găsi toate instanțele relevante)](/en/terms/recall-măsură-a-capacității-de-a-găsi-toate-instanțele-relevante/)
- [scorul F1 (medie armonică între precizie și recall)](/en/terms/scorul-f1-medie-armonică-între-precizie-și-recall/)
- [curba ROC (grafic al performanței clasificatorului)](/en/terms/curba-roc-grafic-al-performanței-clasificatorului/)
