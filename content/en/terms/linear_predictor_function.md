---
title: "Linear predictor function"
term_id: "linear_predictor_function"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "linear_models", "mathematics"]
difficulty: 2
weight: 1
slug: "linear_predictor_function"
aliases:
  - /en/terms/linear_predictor_function/
date: "2026-07-18T10:05:14.961763Z"
lastmod: "2026-07-18T11:44:44.692578Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A mathematical function that computes a linear combination of input variables to predict an outcome."
---

## Definition

In statistical modeling and machine learning, a linear predictor function represents the weighted sum of input features plus a bias term. It serves as the core component in generalized linear models (GLMs) and linear regression, mapping input vectors to a real-valued score before being passed through a link function. This function assumes a linear relationship between predictors and the target variable, forming the basis for many interpretable algorithms used in classification and regression tasks.

### Summary

A mathematical function that computes a linear combination of input variables to predict an outcome.

## Key Concepts

- Weighted sum
- Bias term
- Generalized linear models
- Feature coefficients

## Use Cases

- Linear regression analysis
- Logistic regression classification
- Support vector machines (kernel trick context)

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients](/en/terms/regression_coefficients/)
- [bias_intercept](/en/terms/bias_intercept/)
- [feature_engineering](/en/terms/feature_engineering/)
- [generalized_linear_model](/en/terms/generalized_linear_model/)
