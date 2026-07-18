---
title: "Phi koeficient"
term_id: "phi_coefficient"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "evaluation_metrics", "binary_classification"]
difficulty: 3
weight: 1
slug: "phi_coefficient"
aliases:
  - /cs/terms/phi_coefficient/
date: "2026-07-18T16:12:54.345755Z"
lastmod: "2026-07-18T17:15:09.189508Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Statistická míra asociace mezi dvěma binárními proměnnými."
---

## Definition

Phi koeficient (φ) je míra asociace pro dvě binární proměnné, která slouží jako Pearsonův korelační koeficient pro dichotomické proměnné. Pohybuje se v rozmezí od -1 do +1, kde 0 označuje žádnou asoc

### Summary

Statistická míra asociace mezi dvěma binárními proměnnými.

## Key Concepts

- Binární proměnné
- Korelace
- Kontingenční tabulka
- Síla asociace

## Use Cases

- Hodnocení výkonu binárního klasifikátoru přesahujícího přesnost
- Analýza vztahů v datech z dotazníků s odpověďmi ano/ne
- Výběr znaků v datech s kategoriálními vstupy

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

- [Cramer's V (Cramerova V)](/en/terms/cramer-s-v-cramerova-v/)
- [Pearson correlation (Pearsonova korelace)](/en/terms/pearson-correlation-pearsonova-korelace/)
- [Confusion matrix (Kontingenční tabulka / Matice záměny)](/en/terms/confusion-matrix-kontingenční-tabulka-matice-záměny/)
- [Mutual information (Vzájemná informace)](/en/terms/mutual-information-vzájemná-informace/)
