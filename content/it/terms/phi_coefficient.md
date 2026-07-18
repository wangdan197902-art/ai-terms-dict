---
title: "Coefficiente Phi"
term_id: "phi_coefficient"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "evaluation_metrics", "binary_classification"]
difficulty: 3
weight: 1
slug: "phi_coefficient"
aliases:
  - /it/terms/phi_coefficient/
date: "2026-07-18T16:16:15.417338Z"
lastmod: "2026-07-18T17:15:08.658446Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Una misura statistica dell'associazione tra due variabili binarie."
---

## Definition

Il coefficiente Phi (φ) è una misura di associazione per due variabili binarie, che funge da coefficiente di correlazione di Pearson per variabili dicotomiche. Varia da -1 a +1, dove 0 indica assenza di as

### Summary

Una misura statistica dell'associazione tra due variabili binarie.

## Key Concepts

- Variabili binarie
- Correlazione
- Tabella di contingenza
- Forza dell'associazione

## Use Cases

- Valutazione delle prestazioni del classificatore binario oltre l'accuratezza
- Analisi delle relazioni nei dati di sondaggio con risposte sì/no
- Selezione delle funzionalità in dataset con input categorici

## Code Example

```python
import numpy as np
from scipy.stats import chi2_contingency
# Example: Calculate phi coefficient from a 2x2 confusion matrix
tn, fp, fn, tp = 90, 10, 5, 95
matrix = [[tn, fp], [fn, tp]]
chi2, p, dof, expected = chi2_contingency(matrix)
phi = np.sqrt(chi2 / (tn + fp + fn + tp))
print(f'Phi coefficient: {phi:.3f}')
```

## Related Terms

- [V di Cramer (misura di associazione per variabili categoriali)](/en/terms/v-di-cramer-misura-di-associazione-per-variabili-categoriali/)
- [Correlazione di Pearson (misura di linearità)](/en/terms/correlazione-di-pearson-misura-di-linearità/)
- [Matrice di confusione (tabella per valutare le prestazioni di classificazione)](/en/terms/matrice-di-confusione-tabella-per-valutare-le-prestazioni-di-classificazione/)
- [Informazione mutua (misura della dipendenza statistica)](/en/terms/informazione-mutua-misura-della-dipendenza-statistica/)
