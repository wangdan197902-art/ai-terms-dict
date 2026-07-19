---
title: Softmax
term_id: softmax
category: basic_concepts
subcategory: ''
tags:
- math
- Neural Networks
- Classification
difficulty: 2
weight: 1
slug: softmax
date: '2026-07-18T11:02:04.102285Z'
lastmod: '2026-07-18T11:44:45.406257Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种数学函数，将任意实数值分数向量转换为概率分布。
---
## Definition

Softmax 广泛用于多分类任务中神经网络的输出层。它接收原始对数几率（logits）向量并对其进行归一化，使每个元素代表一个概率值。

### Summary

一种数学函数，将任意实数值分数向量转换为概率分布。

## Key Concepts

- 概率分布
- 对数几率 (Logits)
- 归一化
- 多分类

## Use Cases

- 图像分类的输出层
- 语言模型的词元预测
- 多标签分类

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (取最大值索引)](/en/terms/argmax-取最大值索引/)
- [交叉熵损失 (Cross-Entropy Loss)](/en/terms/交叉熵损失-cross-entropy-loss/)
- [对数几率 (Logits)](/en/terms/对数几率-logits/)
- [神经网络 (Neural Network)](/en/terms/神经网络-neural-network/)
