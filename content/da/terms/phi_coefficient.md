---
title: Phi-koefficient
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
date: '2026-07-18T16:12:11.436127Z'
lastmod: '2026-07-18T17:15:09.321197Z'
draft: false
source: agnes_llm
status: published
language: da
description: Et statistisk mål for sammenhængen mellem to binære variable.
---
## Definition

Phi-koefficienten (φ) er et mål for sammenhæng mellem to binære variable og fungerer som Pearsons korrelationskoefficient for dikotome variable. Den varierer fra -1 til +1, hvor 0 indikerer ingen sammenhæng.

### Summary

Et statistisk mål for sammenhængen mellem to binære variable.

## Key Concepts

- Binære variable
- Korrelation
- Kontingenstabel
- Sammenhængsstyrke

## Use Cases

- Vurdering af ydeevnen hos en binær klassifikator ud over nøjagtighed
- Analyse af sammenhænge i spørgeskema-data med ja/nej-svar
- Funktionsselvvalg i datasæt med kategoriske input

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

- [Cramers V](/en/terms/cramers-v/)
- [Pearsons korrelation](/en/terms/pearsons-korrelation/)
- [Forvekslingsmatrix](/en/terms/forvekslingsmatrix/)
- [Mutuel information](/en/terms/mutuel-information/)
