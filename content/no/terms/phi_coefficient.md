---
title: Phikoeffisient
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
date: '2026-07-18T16:11:44.476064Z'
lastmod: '2026-07-18T16:38:07.033848Z'
draft: false
source: agnes_llm
status: published
language: 'no'
description: Et statistisk mål på sammenheng mellom to binære variabler.
---
## Definition

Phikoeffisienten (φ) er et mål på sammenheng mellom to binære variabler og fungerer som Pearsons korrelasjonskoeffisient for dikotome variabler. Den varierer fra -1 til +1, der 0 indikerer ingen sammenheng.

### Summary

Et statistisk mål på sammenheng mellom to binære variabler.

## Key Concepts

- Binære variabler
- Korrelasjon
- Kontingenstabell
- Sammenhengsstyrke

## Use Cases

- Vurdering av binær klassifiserers ytelse utover nøyaktighet
- Analyse av sammenhenger i spørundersøkelser med ja/nei-svar
- Funksjonsutvalg i datasett med kategoriske inndata

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
- [Pearsons korrelasjon](/en/terms/pearsons-korrelasjon/)
- [Forvekslingsmatrise](/en/terms/forvekslingsmatrise/)
- [Gjensidig informasjon](/en/terms/gjensidig-informasjon/)
