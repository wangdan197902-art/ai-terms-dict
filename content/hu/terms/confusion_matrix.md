---
title: Zavari mátrix
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
date: '2026-07-18T15:51:20.361187Z'
lastmod: '2026-07-18T17:15:09.764799Z'
draft: false
source: agnes_llm
status: published
language: hu
description: Egy táblázat, amely egy osztályozási modell teljesítményét írja le egy
  tesztadatkészleten.
---
## Definition

A zavari mátrix egy specifikus táblázatos elrendezés, amely lehetővé teszi egy algoritmus (általában felügyelt tanulású) teljesítményének vizualizálását. Megmutatja a valódi pozitív, valódi negatív, hamis pozitív és hamis negatív eredmények számát.

### Summary

Egy táblázat, amely egy osztályozási modell teljesítményét írja le egy tesztadatkészleten.

## Key Concepts

- Valódi pozitívok
- Hamis negatívok
- Pontosság
- Recall (visszakeresési arány)

## Use Cases

- Bináris osztályozók értékelése
- Többosztályos osztályozási teljesítmény elemzése
- Modell torzításának hibakeresése torzított adathalmazokon

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (pontosság)](/en/terms/precision-pontosság/)
- [recall (visszakeresési arány)](/en/terms/recall-visszakeresési-arány/)
- [F1 score (F1-érték)](/en/terms/f1-score-f1-érték/)
- [ROC curve (ROC-görbe)](/en/terms/roc-curve-roc-görbe/)
