---
title: Bewertung binärer Klassifikatoren
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
date: '2026-07-18T11:13:48.471947Z'
lastmod: '2026-07-18T11:44:44.937846Z'
draft: false
source: agnes_llm
status: published
language: de
description: Der Prozess zur Bewertung der Leistung von Machine-Learning-Modellen,
  die eines von zwei möglichen Ergebnisse vorhersagen.
---
## Definition

Dieses Feld umfasst die Analyse von Metriken wie Genauigkeit (Accuracy), Präzision, Recall, F1-Score und der Fläche unter der ROC-Kurve (AUC-ROC). Es hilft dabei zu bestimmen, wie gut ein Modell die Unterscheidung zwischen den beiden Klassen bewerkstelligt.

### Summary

Der Prozess zur Bewertung der Leistung von Machine-Learning-Modellen, die eines von zwei möglichen Ergebnisse vorhersagen.

## Key Concepts

- Konfusionsmatrix
- Präzision-Recall-Abwägung
- ROC-Kurve
- F1-Score

## Use Cases

- Medizinische Krankheitsscreenings
- Spam-E-Mail-Filterung
- Kreditrisikobewertung

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix (Konfusionsmatrix)](/en/terms/confusion_matrix-konfusionsmatrix/)
- [roc_auc (Fläche unter der ROC-Kurve)](/en/terms/roc_auc-fläche-unter-der-roc-kurve/)
- [precision_recall (Präzision und Recall)](/en/terms/precision_recall-präzision-und-recall/)
- [cross_validation (Kreuzvalidierung)](/en/terms/cross_validation-kreuzvalidierung/)
