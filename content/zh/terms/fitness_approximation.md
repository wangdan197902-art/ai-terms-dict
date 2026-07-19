---
title: 适应度近似
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
date: '2026-07-18T11:17:25.495538Z'
lastmod: '2026-07-18T11:44:45.500330Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 进化算法中的一种技术，通过估计解的质量来降低优化过程中的计算成本。
---
## Definition

当评估真实适应度函数在计算上昂贵或耗时较长时，适应度近似被用于进化计算中。与其计算精确值，不如使用代理模型来估算适应度，从而加速搜索过程并减少资源消耗。

### Summary

进化算法中的一种技术，通过估计解的质量来降低优化过程中的计算成本。

## Key Concepts

- 代理建模
- 计算效率
- 进化算法
- 选择压力

## Use Cases

- 工程设计优化
- 复杂的基于仿真的问题
- 大规模参数调优

## Related Terms

- [Genetic Algorithm (遗传算法)](/en/terms/genetic-algorithm-遗传算法/)
- [Surrogate Model (代理模型)](/en/terms/surrogate-model-代理模型/)
- [Bayesian Optimization (贝叶斯优化)](/en/terms/bayesian-optimization-贝叶斯优化/)
- [Evolutionary Computation (进化计算)](/en/terms/evolutionary-computation-进化计算/)
