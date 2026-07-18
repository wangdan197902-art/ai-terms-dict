---
title: "Differentially private stochastic gradient descent"
term_id: "differentially_private_stochastic_gradient_descent"
category: "training_techniques"
subcategory: ""
tags: ["optimization", "privacy", "deep_learning", "algorithms"]
difficulty: 5
weight: 1
slug: "differentially_private_stochastic_gradient_descent"
aliases:
  - /en/terms/differentially_private_stochastic_gradient_descent/
date: "2026-07-18T09:55:28.230156Z"
lastmod: "2026-07-18T11:44:44.665281Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "An optimization algorithm that modifies standard SGD by clipping gradients and adding noise to ensure the trained model satisfies differential privacy constraints."
---

## Definition

DP-SGD is a variant of Stochastic Gradient Descent designed to protect the privacy of training data. It works by clipping the contribution of each sample's gradient to limit sensitivity, then adding Gaussian noise scaled to the privacy budget before updating model weights. This process ensures that the final model does not memorize specific training examples, making it resistant to membership inference attacks while maintaining reasonable utility.

### Summary

An optimization algorithm that modifies standard SGD by clipping gradients and adding noise to ensure the trained model satisfies differential privacy constraints.

## Key Concepts

- Gradient Clipping
- Gaussian Noise Injection
- Sample Subsampling
- Privacy Accounting

## Use Cases

- Training deep neural networks on private user data
- Healthcare predictive modeling
- Financial fraud detection with regulated data

## Related Terms

- [Differential Privacy](/en/terms/differential-privacy/)
- [SGD](/en/terms/sgd/)
- [Model Inversion Attacks](/en/terms/model-inversion-attacks/)
- [Privacy Budget](/en/terms/privacy-budget/)
