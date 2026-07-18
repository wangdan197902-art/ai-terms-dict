---
title: "Coeficientul Phi"
term_id: "phi_coefficient"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "evaluation_metrics", "binary_classification"]
difficulty: 3
weight: 1
slug: "phi_coefficient"
aliases:
  - /ro/terms/phi_coefficient/
date: "2026-07-18T16:16:14.630817Z"
lastmod: "2026-07-18T17:15:09.691433Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ro"
description: "O măsură statistică a asocierii dintre două variabile binare."
---

## Definition

Coeficientul Phi (φ) este o măsură a asocierii pentru două variabile binare, servind ca coeficient de corelație Pearson pentru variabile dicotomice. Acesta variază între -1 și +1, unde 0 indică lipsa unei asocieri.

### Summary

O măsură statistică a asocierii dintre două variabile binare.

## Key Concepts

- Variabile binare
- Corelație
- Tabel de contingență
- Puterea asocierii

## Use Cases

- Evaluarea performanței clasificatoarelor binare dincolo de acuratețe
- Analiza relațiilor în datele sondajelor cu răspunsuri da/nu
- Selecția caracteristicilor în seturi de date cu intrări categorice

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

- [V lui Cramer (o măsură a asocierii între variabile nominale)](/en/terms/v-lui-cramer-o-măsură-a-asocierii-între-variabile-nominale/)
- [Corelația Pearson (măsură a legăturii liniare dintre două variabile)](/en/terms/corelația-pearson-măsură-a-legăturii-liniare-dintre-două-variabile/)
- [Matricea de confuzie (tabel utilizat pentru evaluarea performanței unui model de clasificare)](/en/terms/matricea-de-confuzie-tabel-utilizat-pentru-evaluarea-performanței-unui-model-de-clasificare/)
- [Informația mutuală (măsură a dependenței statistice dintre două variabile)](/en/terms/informația-mutuală-măsură-a-dependenței-statistice-dintre-două-variabile/)
