---
title: "张量"
term_id: "tensor"
category: "basic_concepts"
subcategory: ""
tags: ["math", "data-structures", "pytorch"]
difficulty: 2
weight: 1
slug: "tensor"
aliases:
  - /zh/terms/tensor/
date: "2026-07-18T11:35:54.969710Z"
lastmod: "2026-07-18T11:44:45.561589Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种多维数组，是深度学习框架中的基本数据结构。"
---

## Definition

在计算机科学和深度学习中，张量是一种数学对象，它将标量、向量和矩阵推广到更高维度。它由其秩（维度数量）和形状等特征定义。

### Summary

一种多维数组，是深度学习框架中的基本数据结构。

## Key Concepts

- 秩
- 形状
- 维度
- 广播机制

## Use Cases

- 图像处理（4D张量）
- 神经网络权重存储
- 批量数据输入

## Code Example

```python
import torch
t = torch.tensor([[1, 2], [3, 4]])
```

## Related Terms

- [Matrix (矩阵)](/en/terms/matrix-矩阵/)
- [Vector (向量)](/en/terms/vector-向量/)
- [Deep Learning (深度学习)](/en/terms/deep-learning-深度学习/)
- [NumPy (数值计算库)](/en/terms/numpy-数值计算库/)
