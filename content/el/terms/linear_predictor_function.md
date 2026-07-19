---
title: Γραμμική συνάρτηση προβλέψης
term_id: linear_predictor_function
category: basic_concepts
subcategory: ''
tags:
- statistics
- Linear Models
- mathematics
difficulty: 2
weight: 1
slug: linear_predictor_function
date: '2026-07-18T16:18:35.726829Z'
lastmod: '2026-07-18T17:15:09.926541Z'
draft: false
source: agnes_llm
status: published
language: el
description: Μια μαθηματική συνάρτηση που υπολογίζει ένα γραμμικό συνδυασμό μεταβλητών
  εισόδου για να προβλέψει μια έκβαση.
---
## Definition

Στη στατιστική μοντελοποίηση και την μηχανική μάθηση, η γραμμική συνάρτηση προβλέψης αντιπροσωπεύει το σταθμισμένο άθροισμα των χαρακτηριστικών εισόδου συν έναν όρο προκατάληψης (bias). Αποτελεί τον βασικό πυρήνα των γενικευμένων γραμμικών μοντέλων (GLM).

### Summary

Μια μαθηματική συνάρτηση που υπολογίζει ένα γραμμικό συνδυασμό μεταβλητών εισόδου για να προβλέψει μια έκβαση.

## Key Concepts

- Σταθμισμένο άθροισμα
- Όρος προκατάληψης
- Γενικευμένα γραμμικά μοντέλα
- Συντελεστές χαρακτηριστικών

## Use Cases

- Ανάλυση γραμμικής παλινδρόμησης
- Ταξινόμηση με λογιστική παλινδρόμηση
- Μηχανές διανυσμάτων υποστήριξης (στο πλαίσιο της τρικυλίας πυρήνα)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (συντελεστές παλινδρόμησης)](/en/terms/regression_coefficients-συντελεστές-παλινδρόμησης/)
- [bias_intercept (παρεμβολή προκατάληψης)](/en/terms/bias_intercept-παρεμβολή-προκατάληψης/)
- [feature_engineering (μηχανική χαρακτηριστικών)](/en/terms/feature_engineering-μηχανική-χαρακτηριστικών/)
- [generalized_linear_model (γενικευμένο γραμμικό μοντέλο)](/en/terms/generalized_linear_model-γενικευμένο-γραμμικό-μοντέλο/)
