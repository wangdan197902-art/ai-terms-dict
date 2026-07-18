---
title: "Phi-coëfficiënt"
term_id: "phi_coefficient"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "evaluation_metrics", "binary_classification"]
difficulty: 3
weight: 1
slug: "phi_coefficient"
aliases:
  - /nl/terms/phi_coefficient/
date: "2026-07-18T16:12:34.826997Z"
lastmod: "2026-07-18T17:15:08.776769Z"
draft: false
source: "agnes_llm"
status: "published"
language: "nl"
description: "Een statistische maat voor de associatie tussen twee binaire variabelen."
---

## Definition

De Phi-coëfficiënt (φ) is een maat voor associatie tussen twee binaire variabelen en fungeert als de Pearson-correlatiecoëfficiënt voor dichotome variabelen. De waarde varieert van -1 tot +1, waarbij 0 geen associatie aangeeft.

### Summary

Een statistische maat voor de associatie tussen twee binaire variabelen.

## Key Concepts

- Binaire variabelen
- Correlatie
- Contingentietabel
- Associatiesterkte

## Use Cases

- Evalueren van de prestaties van binaire classificatoren, naast nauwkeurigheid
- Analyseren van relaties in enquêtegegevens met ja/nee-antwoorden
- Kenmerkselectie in datasets met categorische invoer

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

- [Cramér's V](/en/terms/cramér-s-v/)
- [Pearson-correlatie](/en/terms/pearson-correlatie/)
- [Confusietafel](/en/terms/confusietafel/)
- [Wederzijdse informatie](/en/terms/wederzijdse-informatie/)
