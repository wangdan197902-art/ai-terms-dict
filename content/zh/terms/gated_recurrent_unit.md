---
title: "门控循环单元"
term_id: "gated_recurrent_unit"
category: "basic_concepts"
subcategory: ""
tags: ["Neural Networks", "Deep Learning", "Architecture"]
difficulty: 3
weight: 1
slug: "gated_recurrent_unit"
date: "2026-07-18T11:18:04.585960Z"
lastmod: "2026-07-18T11:44:45.504486Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种使用门控机制控制信息流动的循环神经网络架构，作为LSTM的简化替代方案。"
---
## Definition

门控循环单元（GRU）是一种专门的循环神经网络（RNN）单元，旨在捕捉序列数据中的长期依赖关系。它简化了长短期记忆（LSTM）架构。

### Summary

一种使用门控机制控制信息流动的循环神经网络架构，作为LSTM的简化替代方案。

## Key Concepts

- 循环神经网络
- 更新门
- 重置门
- 序列建模

## Use Cases

- 自然语言处理
- 时间序列预测
- 语音识别

## Code Example

```python
import torch.nn as nn

# Define a simple GRU layer
gru = nn.GRU(input_size=10, hidden_size=20, num_layers=1)

# Example input: (seq_len, batch, input_size)
input_data = torch.randn(5, 3, 10)
hidden_state = None

output, hidden = gru(input_data, hidden_state)
```

## Related Terms

- [LSTM (长短期记忆网络)](/en/terms/lstm-长短期记忆网络/)
- [RNN (循环神经网络)](/en/terms/rnn-循环神经网络/)
- [Deep Learning (深度学习)](/en/terms/deep-learning-深度学习/)
- [Sequence-to-Sequence (序列到序列)](/en/terms/sequence-to-sequence-序列到序列/)
