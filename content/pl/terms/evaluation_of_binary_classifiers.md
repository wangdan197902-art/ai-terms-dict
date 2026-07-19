---
title: Ocena klasyfikatorów binarnych
term_id: evaluation_of_binary_classifiers
category: basic_concepts
subcategory: ''
tags:
- metrics
- Classification
- evaluation
difficulty: 2
weight: 1
slug: evaluation_of_binary_classifiers
date: '2026-07-18T15:53:59.006516Z'
lastmod: '2026-07-18T17:15:08.871323Z'
draft: false
source: agnes_llm
status: published
language: pl
description: Proces oceny wydajności modeli uczenia maszynowego przewidujących jeden
  z dwóch możliwych wyników.
---
## Definition

Ta dziedzina obejmuje analizę metryk takich jak dokładność, precyzja, czułość, wynik F1 oraz Pole Pod Krzywą ROC (AUC-ROC). Pomaga ona określić, jak dobrze model rozróżnia klasy.

### Summary

Proces oceny wydajności modeli uczenia maszynowego przewidujących jeden z dwóch możliwych wyników.

## Key Concepts

- Macierz pomyłek
- Kompromis między precyzją a czułością
- Krzywa ROC
- Wynik F1

## Use Cases

- Skryning chorób medycznych
- Filtrowanie spamu w e-mailach
- Ocena ryzyka kredytowego

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix (macierz pomyłek)](/en/terms/confusion_matrix-macierz-pomyłek/)
- [roc_auc (pole pod krzywą ROC)](/en/terms/roc_auc-pole-pod-krzywą-roc/)
- [precision_recall (precyzja i czułość)](/en/terms/precision_recall-precyzja-i-czułość/)
- [cross_validation (walidacja krzyżowa)](/en/terms/cross_validation-walidacja-krzyżowa/)
