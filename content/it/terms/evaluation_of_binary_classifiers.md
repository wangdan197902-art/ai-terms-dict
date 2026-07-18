---
title: "Valutazione dei classificatori binari"
term_id: "evaluation_of_binary_classifiers"
category: "basic_concepts"
subcategory: ""
tags: ["metrics", "classification", "evaluation"]
difficulty: 2
weight: 1
slug: "evaluation_of_binary_classifiers"
aliases:
  - /it/terms/evaluation_of_binary_classifiers/
date: "2026-07-18T15:58:57.465469Z"
lastmod: "2026-07-18T17:15:08.623842Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Il processo di valutazione delle prestazioni dei modelli di apprendimento automatico che prevedono uno dei due possibili risultati."
---

## Definition

Questo campo coinvolge l'analisi di metriche come accuratezza, precisione, richiamo (recall), punteggio F1 e l'Aire Sotto la Curva ROC (AUC-ROC). Aiuta a determinare quanto bene un modello distingue le classi.

### Summary

Il processo di valutazione delle prestazioni dei modelli di apprendimento automatico che prevedono uno dei due possibili risultati.

## Key Concepts

- Matrice di confusione
- Compromesso Precisione-Richiamo
- Curva ROC
- Punteggio F1

## Use Cases

- Screening per malattie mediche
- Filtraggio della posta indesiderata (spam)
- Valutazione del rischio di credito

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix (matrice di confusione)](/en/terms/confusion_matrix-matrice-di-confusione/)
- [roc_auc (area sotto la curva ROC)](/en/terms/roc_auc-area-sotto-la-curva-roc/)
- [precision_recall (precisione e richiamo)](/en/terms/precision_recall-precisione-e-richiamo/)
- [cross_validation (validazione incrociata)](/en/terms/cross_validation-validazione-incrociata/)
