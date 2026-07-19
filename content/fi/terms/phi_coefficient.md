---
title: Fikertoiminto
term_id: phi_coefficient
category: basic_concepts
subcategory: ''
tags:
- statistics
- Evaluation Metrics
- Binary Classification
difficulty: 3
weight: 1
slug: phi_coefficient
date: '2026-07-18T16:15:50.742993Z'
lastmod: '2026-07-18T17:15:09.443963Z'
draft: false
source: agnes_llm
status: published
language: fi
description: Tilastollinen mittari kahden binäärimuuttujan välisen yhteyden voimakkuudelle.
---
## Definition

Fikertoiminto (φ) on mittari kahden binäärimuuttujan väliselle yhteydelle, ja se toimii Pearsonin korrelaatiokertoimena dikotomisille muuttujille. Sen arvo vaihtelee välillä -1–+1, jossa 0 tarkoittaa ei-yhteyttä.

### Summary

Tilastollinen mittari kahden binäärimuuttujan välisen yhteyden voimakkuudelle.

## Key Concepts

- Binäärimuuttujat
- Korrelaatio
- Ristiintaulukko
- Yhteyden voimakkuus

## Use Cases

- Binäärisen luokittelijan suorituskyvyn arviointi tarkkuuden lisäksi
- Suhdeanalyysi kyselytutkimuksen datasta, jossa vastaukset ovat kyllä/ei
- Ominaisuusvalinta kategorisissa syötedatajoukoissa

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

- [Cramer's V (Cramerin V-kertoimen)](/en/terms/cramer-s-v-cramerin-v-kertoimen/)
- [Pearson correlation (Pearsonin korrelaatiokerroin)](/en/terms/pearson-correlation-pearsonin-korrelaatiokerroin/)
- [Confusion matrix (sekaannusmatrix)](/en/terms/confusion-matrix-sekaannusmatrix/)
- [Mutual information (keskinäinen informaatio)](/en/terms/mutual-information-keskinäinen-informaatio/)
