---
title: "Stability"
term_id: "stability"
category: "basic_concepts"
subcategory: ""
tags: ["evaluation", "theory", "robustness"]
difficulty: 2
weight: 1
slug: "stability"
aliases:
  - /en/terms/stability/
date: "2026-07-18T10:16:41.447274Z"
lastmod: "2026-07-18T11:44:44.724363Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "The property of a machine learning model to produce consistent predictions when trained on slightly different datasets."
---

## Definition

In machine learning, stability refers to the robustness of a model's performance and parameters when subjected to small perturbations in the training data. A stable algorithm will yield similar models and predictions even if the dataset changes slightly, such as through resampling or adding noise. High stability is crucial for reliable deployment, as unstable models may overfit to specific quirks in the training set, leading to poor generalization on unseen data. It is often analyzed alongside bias and variance trade-offs.

### Summary

The property of a machine learning model to produce consistent predictions when trained on slightly different datasets.

## Key Concepts

- Robustness
- Generalization
- Variance
- Resampling

## Use Cases

- Evaluating model reliability
- Selecting algorithms for critical applications
- Cross-validation strategy design

## Related Terms

- [Overfitting](/en/terms/overfitting/)
- [Bias-Variance Tradeoff](/en/terms/bias-variance-tradeoff/)
- [Bootstrap Aggregating](/en/terms/bootstrap-aggregating/)
- [Regularization](/en/terms/regularization/)
