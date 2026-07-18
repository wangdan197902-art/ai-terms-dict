---
title: "Współczynnik phi"
term_id: "phi_coefficient"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "evaluation_metrics", "binary_classification"]
difficulty: 3
weight: 1
slug: "phi_coefficient"
aliases:
  - /pl/terms/phi_coefficient/
date: "2026-07-18T16:11:25.745997Z"
lastmod: "2026-07-18T17:15:08.906891Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pl"
description: "Statystyczna miara zależności między dwiema zmiennymi binarnymi."
---

## Definition

Współczynnik phi (φ) to miara zależności dla dwóch zmiennych binarnych, pełniąca funkcję współczynnika korelacji Pearsonsa dla zmiennych dychotomicznych. Przyjmuje wartości od -1 do +1, gdzie 0 oznacza brak zależności.

### Summary

Statystyczna miara zależności między dwiema zmiennymi binarnymi.

## Key Concepts

- Zmienne binarne
- Korelacja
- Tabela kontingencji
- Siła zależności

## Use Cases

- Ocena wydajności klasyfikatora binarnego poza dokładnością (accuracy)
- Analiza zależności w danych ankietowych z odpowiedziami tak/nie
- Wybór cech w zbiorach danych z danymi kategorialnymi

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

- [V Cramera (Miara zależności dla tabel kontingencji)](/en/terms/v-cramera-miara-zależności-dla-tabel-kontingencji/)
- [Korelacja Pearsonsa (Miara liniowej zależności)](/en/terms/korelacja-pearsonsa-miara-liniowej-zależności/)
- [Macierz pomyłek (Narzędzie oceny klasyfikatorów)](/en/terms/macierz-pomyłek-narzędzie-oceny-klasyfikatorów/)
- [Informacja wzajemna (Miara zależności statystycznej)](/en/terms/informacja-wzajemna-miara-zależności-statystycznej/)
