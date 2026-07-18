---
title: "期望传播"
term_id: "expectation_propagation"
category: "basic_concepts"
subcategory: ""
tags: ["bayesian_methods", "inference", "probabilistic_models"]
difficulty: 5
weight: 1
slug: "expectation_propagation"
aliases:
  - /zh/terms/expectation_propagation/
date: "2026-07-18T11:16:37.593430Z"
lastmod: "2026-07-18T11:44:45.496849Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种用于估计复杂概率图模型中后验分布的近似推理算法。"
---

## Definition

期望传播（EP）通过迭代 refine 高斯近似值来逼近难以处理的积分，从而估计真实后验分布。它最小化近似分布与真实分布之间的Kullback-Leibler散度，常用于贝叶斯推断和稀疏高斯过程。

### Summary

一种用于估计复杂概率图模型中后验分布的近似推理算法。

## Key Concepts

- 后验近似
- 矩匹配
- Kullback-Leibler散度
- 高斯过程

## Use Cases

- 稀疏高斯过程
- 贝叶斯逻辑回归
- 概率矩阵分解

## Related Terms

- [variational_inference (变分推断)](/en/terms/variational_inference-变分推断/)
- [gaussian_processes (高斯过程)](/en/terms/gaussian_processes-高斯过程/)
- [bayesian_inference (贝叶斯推断)](/en/terms/bayesian_inference-贝叶斯推断/)
- [mean_field_approximation (平均场近似)](/en/terms/mean_field_approximation-平均场近似/)
