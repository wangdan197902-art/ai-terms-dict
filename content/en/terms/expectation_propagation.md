---
title: Expectation propagation
term_id: expectation_propagation
category: basic_concepts
subcategory: ''
tags:
- Bayesian Methods
- inference
- Probabilistic Models
difficulty: 5
weight: 1
slug: expectation_propagation
date: '2026-07-18T09:57:25.048633Z'
lastmod: '2026-07-18T11:44:44.670811Z'
draft: false
source: agnes_llm
status: published
language: en
description: An approximate inference algorithm used to estimate posterior distributions
  in complex probabilistic graphical models.
---
## Definition

Expectation Propagation (EP) approximates intractable integrals by iteratively refining Gaussian approximations to the true posterior distribution. It minimizes the Kullback-Leibler divergence between the approximate and true distributions by matching moments. EP is widely used in Bayesian machine learning for tasks like classification and regression where exact inference is computationally prohibitive, offering a balance between accuracy and efficiency.

### Summary

An approximate inference algorithm used to estimate posterior distributions in complex probabilistic graphical models.

## Key Concepts

- Posterior Approximation
- Moment Matching
- Kullback-Leibler Divergence
- Gaussian Processes

## Use Cases

- Sparse Gaussian Processes
- Bayesian logistic regression
- Probabilistic matrix factorization

## Related Terms

- [variational_inference](/en/terms/variational_inference/)
- [gaussian_processes](/en/terms/gaussian_processes/)
- [bayesian_inference](/en/terms/bayesian_inference/)
- [mean_field_approximation](/en/terms/mean_field_approximation/)
