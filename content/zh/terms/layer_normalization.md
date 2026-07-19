---
title: 层归一化
term_id: layer_normalization
category: basic_concepts
subcategory: ''
tags:
- Neural Networks
- Optimization
- architecture
difficulty: 3
weight: 1
slug: layer_normalization
date: '2026-07-18T11:23:41.252122Z'
lastmod: '2026-07-18T11:44:45.523127Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种技术，针对每个单独样本，对神经网络层的激活值在特征维度上进行归一化处理。
---
## Definition

层归一化通过减少内部协变量偏移来稳定训练过程，尤其在循环神经网络和Transformer架构中非常有效。与依赖于批次统计信息的批归一化不同，层归一化不依赖于批次大小。

### Summary

一种技术，针对每个单独样本，对神经网络层的激活值在特征维度上进行归一化处理。

## Key Concepts

- 归一化
- 内部协变量偏移
- Transformer模型
- 循环神经网络

## Use Cases

- 训练BERT等Transformer模型
- 稳定RNN/LSTM的训练
- 小批量大小的深度学习

## Code Example

```python
import torch.nn as nn
norm_layer = nn.LayerNorm(normalized_shape=[768])
```

## Related Terms

- [batch_normalization (批归一化)](/en/terms/batch_normalization-批归一化/)
- [transformer (Transformer)](/en/terms/transformer-transformer/)
- [normalization (归一化)](/en/terms/normalization-归一化/)
- [deep_learning (深度学习)](/en/terms/deep_learning-深度学习/)
