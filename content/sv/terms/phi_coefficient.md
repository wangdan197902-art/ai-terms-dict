---
title: Fikoefficient
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
date: '2026-07-18T16:13:43.189679Z'
lastmod: '2026-07-18T17:15:09.036593Z'
draft: false
source: agnes_llm
status: published
language: sv
description: Ett statistiskt mått på sambandet mellan två binära variabler.
---
## Definition

Fikoefficienten (φ) är ett mått på sambandet mellan två binära variabler och fungerar som Pearsons korrelationskoefficient för dikotoma variabler. Den varierar från -1 till +1, där 0 indikerar inget samband.

### Summary

Ett statistiskt mått på sambandet mellan två binära variabler.

## Key Concepts

- Binära variabler
- Korrelation
- Kontingenstabell
- Sambandets styrka

## Use Cases

- Utvärdering av binära klassificerarens prestanda utöver noggrannhet
- Analys av samband i enkätdata med ja/nej-svar
- Funktionssval i dataset med kategoriska indata

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

- [Cramers V (Cramers V)](/en/terms/cramers-v-cramers-v/)
- [Pearsons korrelation (Pearsons korrelation)](/en/terms/pearsons-korrelation-pearsons-korrelation/)
- [Konfusionsmatris (Konfusionsmatris)](/en/terms/konfusionsmatris-konfusionsmatris/)
- [Ömsesidig information (Ömsesidig information)](/en/terms/ömsesidig-information-ömsesidig-information/)
