---
title: "线性"
term_id: "linear"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Foundations"]
difficulty: 2
weight: 1
slug: "linear"
date: "2026-07-18T10:52:16.306995Z"
lastmod: "2026-07-18T11:44:45.374557Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "描述输出与输入成正比的操作或关系，构成神经层仿射变换的基础。"
---
## Definition

线性运算涉及乘法和加法，不包含非线性激活。在神经网络中，线性层（或密集层）对输入向量应用权重矩阵变换。虽然线

### Summary

描述输出与输入成正比的操作或关系，构成神经层仿射变换的基础。

## Key Concepts

- 权重矩阵
- 仿射变换
- 点积
- 叠加原理

## Use Cases

- 特征投影
- 逻辑回归
- 注意力机制

## Code Example

```python
import torch.nn as nn
layer = nn.Linear(10, 5)
output = layer(input_tensor)
```

## Related Terms

- [激活函数 (Activation Function)](/en/terms/激活函数-activation-function/)
- [密集层 (Dense Layer)](/en/terms/密集层-dense-layer/)
- [矩阵乘法 (Matrix Multiplication)](/en/terms/矩阵乘法-matrix-multiplication/)
