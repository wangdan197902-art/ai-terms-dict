---
title: "差分随机梯度下降"
term_id: "differentially_private_stochastic_gradient_descent"
category: "training_techniques"
subcategory: ""
tags: ["optimization", "privacy", "deep_learning", "algorithms"]
difficulty: 5
weight: 1
slug: "differentially_private_stochastic_gradient_descent"
aliases:
  - /zh/terms/differentially_private_stochastic_gradient_descent/
date: "2026-07-18T11:14:55.241296Z"
lastmod: "2026-07-18T11:44:45.488492Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种优化算法，通过对标准随机梯度下降（SGD）进行梯度裁剪和添加噪声的修改，确保训练后的模型满足差分隐私约束。"
---

## Definition

DP-SGD 是随机梯度下降的一种变体，旨在保护训练数据的隐私。它通过裁剪每个样本梯度的贡献来限制敏感度，然后添加高斯噪声来实现隐私保护。

### Summary

一种优化算法，通过对标准随机梯度下降（SGD）进行梯度裁剪和添加噪声的修改，确保训练后的模型满足差分隐私约束。

## Key Concepts

- 梯度裁剪
- 高斯噪声注入
- 样本子采样
- 隐私会计

## Use Cases

- 在私有用户数据上训练深度神经网络
- 医疗保健预测建模
- 使用受监管数据进行金融欺诈检测

## Related Terms

- [差分隐私 (Differential Privacy)](/en/terms/差分隐私-differential-privacy/)
- [随机梯度下降 (SGD)](/en/terms/随机梯度下降-sgd/)
- [模型反转攻击 (Model Inversion Attacks)](/en/terms/模型反转攻击-model-inversion-attacks/)
- [隐私预算 (Privacy Budget)](/en/terms/隐私预算-privacy-budget/)
