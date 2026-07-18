---
title: "Phi coefficient"
term_id: "phi_coefficient"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "evaluation_metrics", "binary_classification"]
difficulty: 3
weight: 1
slug: "phi_coefficient"
aliases:
  - /en/terms/phi_coefficient/
date: "2026-07-18T10:10:59.166640Z"
lastmod: "2026-07-18T11:44:44.709594Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A statistical measure of association between two binary variables."
---

## Definition

The Phi coefficient (φ) is a measure of association for two binary variables, serving as the Pearson correlation coefficient for dichotomous variables. It ranges from -1 to +1, where 0 indicates no association, +1 indicates perfect positive association, and -1 indicates perfect negative association. It is widely used in contingency table analysis to determine the strength of the relationship between two categorical features, particularly in classification tasks involving binary outcomes.

### Summary

A statistical measure of association between two binary variables.

## Key Concepts

- Binary variables
- Correlation
- Contingency table
- Association strength

## Use Cases

- Evaluating binary classifier performance beyond accuracy
- Analyzing relationships in survey data with yes/no responses
- Feature selection in datasets with categorical inputs

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

- [Cramer's V](/en/terms/cramer-s-v/)
- [Pearson correlation](/en/terms/pearson-correlation/)
- [Confusion matrix](/en/terms/confusion-matrix/)
- [Mutual information](/en/terms/mutual-information/)
