---
title: "Structural risk minimization"
term_id: "structural_risk_minimization"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "theory", "regularization"]
difficulty: 3
weight: 1
slug: "structural_risk_minimization"
aliases:
  - /en/terms/structural_risk_minimization/
date: "2026-07-18T10:16:56.152335Z"
lastmod: "2026-07-18T11:44:44.725141Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A principle in statistical learning that seeks to minimize the upper bound of the generalization error by balancing model fit and complexity."
---

## Definition

Structural risk minimization (SRM) is a method for minimizing expected risk by controlling model complexity to prevent overfitting. It extends empirical risk minimization by adding a regularization term that penalizes complex models. SRM relies on the Vapnik-Chervonenkis (VC) dimension to define confidence intervals around empirical error. By selecting a model from a nested sequence of hypothesis spaces, SRM finds the optimal trade-off between fitting training data well and maintaining simplicity. This ensures better generalization performance on unseen data compared to simply minimizing training error.

### Summary

A principle in statistical learning that seeks to minimize the upper bound of the generalization error by balancing model fit and complexity.

## Key Concepts

- VC dimension
- Regularization
- Generalization error
- Model complexity penalty

## Use Cases

- Support Vector Machine (SVM) training
- Selecting polynomial degree in regression
- Pruning decision trees to avoid overfitting

## Related Terms

- [Empirical risk minimization](/en/terms/empirical-risk-minimization/)
- [Occam's razor](/en/terms/occam-s-razor/)
- [Regularization](/en/terms/regularization/)
- [Bias-variance tradeoff](/en/terms/bias-variance-tradeoff/)
