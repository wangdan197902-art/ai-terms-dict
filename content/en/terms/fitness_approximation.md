---
title: Fitness approximation
term_id: fitness_approximation
category: basic_concepts
subcategory: ''
tags:
- evolutionary
- Optimization
- surrogate
difficulty: 4
weight: 1
slug: fitness_approximation
date: '2026-07-18T09:58:20.231254Z'
lastmod: '2026-07-18T11:44:44.673687Z'
draft: false
source: agnes_llm
status: published
language: en
description: A technique in evolutionary algorithms that estimates solution quality
  to reduce computational costs during optimization.
---
## Definition

Fitness approximation is used in evolutionary computation when evaluating the true fitness function is computationally expensive or time-consuming. Instead of calculating the exact value, surrogate models or simplified metrics are employed to estimate the fitness of candidate solutions. This approach accelerates the search process by allowing more generations to be evaluated within a fixed time budget, though it may introduce some error in the selection pressure.

### Summary

A technique in evolutionary algorithms that estimates solution quality to reduce computational costs during optimization.

## Key Concepts

- Surrogate Modeling
- Computational Efficiency
- Evolutionary Algorithms
- Selection Pressure

## Use Cases

- Engineering design optimization
- Complex simulation-based problems
- Large-scale parameter tuning

## Related Terms

- [Genetic Algorithm](/en/terms/genetic-algorithm/)
- [Surrogate Model](/en/terms/surrogate-model/)
- [Bayesian Optimization](/en/terms/bayesian-optimization/)
- [Evolutionary Computation](/en/terms/evolutionary-computation/)
