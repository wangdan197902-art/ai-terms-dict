---
title: "尖峰-厚尾回归"
term_id: "spike_and_slab_regression"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "bayesian", "regression"]
difficulty: 4
weight: 1
slug: "spike_and_slab_regression"
aliases:
  - /zh/terms/spike_and_slab_regression/
date: "2026-07-18T11:35:05.879806Z"
lastmod: "2026-07-18T11:44:45.558205Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种贝叶斯变量选择方法，使用混合先验分布来区分系数为零和非零的情况。"
---

## Definition

尖峰-厚尾回归（Spike-and-slab regression）是一种用于变量选择和稀疏建模的贝叶斯统计技术。它采用由两个部分组成的混合先验分布：一个‘尖峰’（spike，通常集中在零点附近以表示系数为零）和一个‘厚尾’（slab，较宽的分布以表示非零系数）。这种方法通过概率方式自动进行特征选择，特别适用于高维数据中识别重要变量的场景。

### Summary

一种贝叶斯变量选择方法，使用混合先验分布来区分系数为零和非零的情况。

## Key Concepts

- 贝叶斯推断
- 稀疏建模
- 混合先验
- 变量选择

## Use Cases

- 高维基因组数据分析
- 金融风险因子识别
- 预测模型中的特征选择

## Related Terms

- [Lasso (L1正则化回归)](/en/terms/lasso-l1正则化回归/)
- [Ridge Regression (岭回归/L2正则化)](/en/terms/ridge-regression-岭回归-l2正则化/)
- [Bayesian Linear Regression (贝叶斯线性回归)](/en/terms/bayesian-linear-regression-贝叶斯线性回归/)
- [Sparsity (稀疏性)](/en/terms/sparsity-稀疏性/)
