---
title: Forvirringsmatrix
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
date: '2026-07-18T15:47:35.551916Z'
lastmod: '2026-07-18T17:15:09.270940Z'
draft: false
source: agnes_llm
status: published
language: da
description: En tabel, der bruges til at beskrive ydeevnen for en klassifikationsmodel
  på et sæt testdata.
---
## Definition

En forvirringsmatrix er en specifik tabelstruktur, der gør det muligt at visualisere algoritmens ydeevne, typisk en overvåget læringsalgoritme. Den viser antallet af sande positive, sande negative, falske positive og falske negative resultater.

### Summary

En tabel, der bruges til at beskrive ydeevnen for en klassifikationsmodel på et sæt testdata.

## Key Concepts

- Sande positive
- Falske negative
- Præcision
- Genkendelse (Recall)

## Use Cases

- Vurdering af binære klassifikatorer
- Analyse af flerklasses klassificeringsydeevne
- Fejlfinding af modelbias i ubalancerede datasæt

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (præcision)](/en/terms/precision-præcision/)
- [recall (genkendelse/recall)](/en/terms/recall-genkendelse-recall/)
- [F1 score (F1-score)](/en/terms/f1-score-f1-score/)
- [ROC curve (ROC-kurve)](/en/terms/roc-curve-roc-kurve/)
