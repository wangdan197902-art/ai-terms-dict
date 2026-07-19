---
title: Macierz pomyłek
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
date: '2026-07-18T15:46:55.085151Z'
lastmod: '2026-07-18T17:15:08.856788Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Tabela służąca do opisywania wydajności modelu klasyfikacyjnego na zbiorze
  danych testowych.
---
## Definition

Macierz pomyłek to specyficzny układ tabelaryczny pozwalający na wizualizację wydajności algorytmu, zazwyczaj uczenia nadzorowanego. Pokazuje liczby prawdziwie dodatnich, prawdziwie ujemnych, fałszywie dodatnich i fałszywie ujemnych wyników predykcji.

### Summary

Tabela służąca do opisywania wydajności modelu klasyfikacyjnego na zbiorze danych testowych.

## Key Concepts

- Prawdziwie dodatnie
- Fałszywie ujemne
- Precyzja
- Czułość

## Use Cases

- Ocena klasyfikatorów binarnych
- Analiza wydajności klasyfikacji wieloklasowej
- Debugowanie obciążenia modelu na zrównoważonych zbiorach danych

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (precyzja)](/en/terms/precision-precyzja/)
- [recall (czułość)](/en/terms/recall-czułość/)
- [F1 score (wskaźnik F1)](/en/terms/f1-score-wskaźnik-f1/)
- [ROC curve (krzywa ROC)](/en/terms/roc-curve-krzywa-roc/)
