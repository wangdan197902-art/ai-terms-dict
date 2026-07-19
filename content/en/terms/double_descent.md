---
title: "Double Descent"
term_id: "double_descent"
category: "basic_concepts"
subcategory: ""
tags: ["Theory", "Deep Learning", "Generalization"]
difficulty: 5
weight: 1
slug: "double_descent"
date: "2026-07-18T09:56:08.548966Z"
lastmod: "2026-07-18T11:44:44.667247Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A phenomenon where test error decreases, increases, and then decreases again as model complexity grows beyond the interpolation threshold."
---
## Definition

Double descent challenges the traditional bias-variance tradeoff by showing that highly overparameterized models can achieve low test error despite interpolating training data. Initially, error rises as models memorize noise, but further increasing capacity allows the model to find smoother solutions that generalize well. This behavior is particularly observed in deep neural networks, explaining why larger models often perform better than smaller ones even when they fit training data perfectly.

### Summary

A phenomenon where test error decreases, increases, and then decreases again as model complexity grows beyond the interpolation threshold.

## Key Concepts

- Interpolation Threshold
- Overparameterization
- Bias-Variance Tradeoff
- Test Error

## Use Cases

- Analyzing neural network scaling laws
- Understanding generalization in deep learning
- Model selection in large-scale AI systems

## Related Terms

- [Overfitting](/en/terms/overfitting/)
- [Underfitting](/en/terms/underfitting/)
- [Neural Tangent Kernel](/en/terms/neural-tangent-kernel/)
- [Regularization](/en/terms/regularization/)
