---
title: "贝叶斯优化"
term_id: "bayesian_optimization"
category: "training_techniques"
subcategory: ""
tags: ["optimization", "hyperparameters", "surrogate_models"]
difficulty: 3
weight: 1
slug: "bayesian_optimization"
aliases:
  - /zh/terms/bayesian_optimization/
date: "2026-07-18T11:08:51.667549Z"
lastmod: "2026-07-18T11:44:45.450575Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种用于全局优化昂贵评估黑盒函数的顺序设计策略。"
---

## Definition

贝叶斯优化使用概率代理模型（通常为高斯过程）来建模目标函数。它采用采集函数来平衡探索与利用，从而高效地找到最优参数配置。

### Summary

一种用于全局优化昂贵评估黑盒函数的顺序设计策略。

## Key Concepts

- 代理模型
- 采集函数
- 探索与利用权衡
- 黑盒优化

## Use Cases

- 深度学习模型的超参数调优
- 科学实验设计的优化
- 机器人控制参数调整

## Related Terms

- [hyperparameter_tuning (超参数调优)](/en/terms/hyperparameter_tuning-超参数调优/)
- [gaussian_processes (高斯过程)](/en/terms/gaussian_processes-高斯过程/)
- [acquisition_function (采集函数)](/en/terms/acquisition_function-采集函数/)
- [grid_search (网格搜索)](/en/terms/grid_search-网格搜索/)
