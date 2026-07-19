---
title: Spike-and-slab regression
term_id: spike_and_slab_regression
category: basic_concepts
subcategory: ''
tags:
- statistics
- bayesian
- Regression
difficulty: 4
weight: 1
slug: spike_and_slab_regression
date: '2026-07-18T10:16:41.447254Z'
lastmod: '2026-07-18T11:44:44.724142Z'
draft: false
source: agnes_llm
status: published
language: en
description: A Bayesian variable selection method that uses a mixture prior to distinguish
  between zero and non-zero coefficients.
---
## Definition

Spike-and-slab regression is a Bayesian statistical technique used for variable selection and sparse modeling. It employs a mixture prior distribution consisting of two components: a 'spike' (typically a narrow distribution centered at zero) representing null effects, and a 'slab' (a broader distribution) representing significant effects. This approach allows the model to automatically determine which predictors are relevant by shrinking irrelevant coefficients toward zero while retaining large estimates for important ones, effectively performing feature selection within a probabilistic framework.

### Summary

A Bayesian variable selection method that uses a mixture prior to distinguish between zero and non-zero coefficients.

## Key Concepts

- Bayesian inference
- Sparse modeling
- Mixture priors
- Variable selection

## Use Cases

- High-dimensional genomic data analysis
- Financial risk factor identification
- Feature selection in predictive modeling

## Related Terms

- [Lasso](/en/terms/lasso/)
- [Ridge Regression](/en/terms/ridge-regression/)
- [Bayesian Linear Regression](/en/terms/bayesian-linear-regression/)
- [Sparsity](/en/terms/sparsity/)
