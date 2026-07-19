---
title: Evaluatie van binaire classificatoren
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
date: '2026-07-18T15:54:32.087261Z'
lastmod: '2026-07-18T17:15:08.742779Z'
draft: false
source: agnes_llm
status: published
language: nl
description: Het proces van het beoordelen van de prestaties van machine learning-modellen
  die een van twee mogelijke uitkomsten voorspellen.
---
## Definition

Dit vakgebied omvat het analyseren van metrieken zoals nauwkeurigheid (accuracy), precisie, recall, F1-score en de Area Under the Receiver Operating Characteristic Curve (AUC-ROC). Het helpt bepalen hoe goed een model presteert bij het onderscheiden van twee klassen.

### Summary

Het proces van het beoordelen van de prestaties van machine learning-modellen die een van twee mogelijke uitkomsten voorspellen.

## Key Concepts

- Verwarringsmatrix
- Precisie-Recall Trade-off
- ROC-curve
- F1-score

## Use Cases

- Medische ziektescreening
- Filteren van spam-e-mails
- Beoordeling van kredietrisico

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix (verwarringsmatrix)](/en/terms/confusion_matrix-verwarringsmatrix/)
- [roc_auc (oppervlakte onder de ROC-curve)](/en/terms/roc_auc-oppervlakte-onder-de-roc-curve/)
- [precision_recall (precisie en recall)](/en/terms/precision_recall-precisie-en-recall/)
- [cross_validation (kruisvalidatie)](/en/terms/cross_validation-kruisvalidatie/)
