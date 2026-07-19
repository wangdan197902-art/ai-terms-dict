---
title: 重参数化技巧
term_id: reparameterization_trick
category: basic_concepts
subcategory: ''
tags:
- Deep Learning
- Probabilistic Models
- Optimization
difficulty: 4
weight: 1
slug: reparameterization_trick
date: '2026-07-18T11:32:14.210884Z'
lastmod: '2026-07-18T11:44:45.550516Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种将随机变量与可学习参数分离的技术，旨在变分推断中实现基于梯度的优化。
---
## Definition

重参数化技巧是变分自编码器及其他概率模型中使用的一种基本方法。它通过将随机变量表示为确定性函数和独立噪声变量的组合，使得梯度能够流经随机节点，从而允许使用反向传播算法进行优化。

### Summary

一种将随机变量与可学习参数分离的技术，旨在变分推断中实现基于梯度的优化。

## Key Concepts

- 变分推断
- 梯度估计
- 随机节点
- 可微模拟

## Use Cases

- 训练变分自编码器 (VAE)
- 贝叶斯神经网络
- 概率图模型

## Code Example

```python
import torch
epsilon = torch.randn(100, 10)
mu = torch.zeros(100, 10)
sigma = torch.ones(100, 10)
z = mu + sigma * epsilon  # Reparameterized sampling
```

## Related Terms

- [ELBO (证据下界)](/en/terms/elbo-证据下界/)
- [潜在变量](/en/terms/潜在变量/)
- [反向传播](/en/terms/反向传播/)
- [蒙特卡洛估计](/en/terms/蒙特卡洛估计/)
