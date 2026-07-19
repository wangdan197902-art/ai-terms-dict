---
title: 적합도 근사(Fitness approximation)
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
date: '2026-07-18T15:56:02.182924Z'
lastmod: '2026-07-18T16:38:06.841051Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 진화 알고리즘에서 최적화 중 계산 비용을 줄이기 위해 솔루션의 품질을 추정하는 기법입니다.
---
## Definition

실제 적합도 함수를 평가하는 것이 계산적으로 비용이 많이 들거나 시간이 오래 걸릴 때 진화 계산에서 적합도 근사가 사용됩니다. 정확한 값을 계산하는 대신, 대리 모델(surrogate model) 등을 사용하여 적합도를 근사함으로써 효율성을 높입니다.

### Summary

진화 알고리즘에서 최적화 중 계산 비용을 줄이기 위해 솔루션의 품질을 추정하는 기법입니다.

## Key Concepts

- 대리 모델링(Surrogate Modeling)
- 계산 효율성(Computational Efficiency)
- 진화 알고리즘(Evolutionary Algorithms)
- 선택 압력(Selection Pressure)

## Use Cases

- 공학 설계 최적화(Engineering design optimization)
- 복잡한 시뮬레이션 기반 문제(Complex simulation-based problems)
- 대규모 매개변수 튜닝(Large-scale parameter tuning)

## Related Terms

- [Genetic Algorithm (유전 알고리즘)](/en/terms/genetic-algorithm-유전-알고리즘/)
- [Surrogate Model (대리 모델)](/en/terms/surrogate-model-대리-모델/)
- [Bayesian Optimization (베이지안 최적화)](/en/terms/bayesian-optimization-베이지안-최적화/)
- [Evolutionary Computation (진화 계산)](/en/terms/evolutionary-computation-진화-계산/)
