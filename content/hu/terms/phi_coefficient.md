---
title: Phi-együttható
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
date: '2026-07-18T16:18:20.876314Z'
lastmod: '2026-07-18T17:15:09.822641Z'
draft: false
source: agnes_llm
status: published
language: hu
description: Két bináris változó közötti asszociáció statisztikai mértéke.
---
## Definition

A phi-együttható (φ) két bináris változó közötti asszociációt mérő mutató, amely a dichotóm változók esetén a Pearson-korrelációs együttható szerepét tölti be. Értéke -1 és +1 között mozog, ahol a 0 az összefüggés hiányát jelzi.

### Summary

Két bináris változó közötti asszociáció statisztikai mértéke.

## Key Concepts

- Bináris változók
- Korreláció
- Táblázatos összefüggés
- Asszociáció erőssége

## Use Cases

- Bináris osztályozó teljesítményének értékelése a pontosságon túl
- Összefüggések elemzése igen/nem válaszokat tartalmazó felmérésekben
- Jelölőválasztás kategorikus bemenetekkel rendelkező adathalmazokban

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

- [Cramér-V (Cramér-féle V együttható)](/en/terms/cramér-v-cramér-féle-v-együttható/)
- [Pearson-korreláció (Pearson-féle korrelációs együttható)](/en/terms/pearson-korreláció-pearson-féle-korrelációs-együttható/)
- [Zavartábla (Konfúziós mátrix)](/en/terms/zavartábla-konfúziós-mátrix/)
- [Kölcsönös információ (Mutual information)](/en/terms/kölcsönös-információ-mutual-information/)
