---
title: Multiplicative weight update method
term_id: multiplicative_weight_update_method
category: basic_concepts
subcategory: ''
tags:
- Optimization
- Online Learning
- algorithm
difficulty: 3
weight: 1
slug: multiplicative_weight_update_method
date: '2026-07-18T10:08:53.980475Z'
lastmod: '2026-07-18T11:44:44.702654Z'
draft: false
source: agnes_llm
status: published
language: en
description: An iterative algorithm that updates weights multiplicatively based on
  performance feedback to minimize regret.
---
## Definition

The multiplicative weight update method is a fundamental online learning algorithm used to make decisions in uncertain environments. It maintains a set of weights for different strategies or experts, updating them multiplicatively based on their past performance. Strategies that perform well have their weights increased, while poor performers see their weights decreased. This method is widely used in game theory, optimization, and machine learning for constructing efficient prediction algorithms with provable convergence guarantees.

### Summary

An iterative algorithm that updates weights multiplicatively based on performance feedback to minimize regret.

## Key Concepts

- Online learning
- Weighted majority algorithm
- Regret minimization
- Exponential weighting

## Use Cases

- Portfolio optimization
- Expert advice aggregation
- Adversarial bandit problems

## Related Terms

- [gradient_descent](/en/terms/gradient_descent/)
- [online_learning](/en/terms/online_learning/)
- [regret_bound](/en/terms/regret_bound/)
- [boosting](/en/terms/boosting/)
