---
title: 率
term_id: rate
category: basic_concepts
subcategory: ''
tags:
- Optimization
- performance
- hyperparameters
difficulty: 3
weight: 1
slug: rate
date: '2026-07-18T10:54:02.537184Z'
lastmod: '2026-07-18T11:44:45.382448Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 频率或速度的度量，通常指优化中的学习率或令牌生成速度。
---
## Definition

在AI中，“率”最常指学习率，这是一个超参数，控制每次更新模型权重时，根据估计误差对模型进行调整的幅度。一个适……

### Summary

频率或速度的度量，通常指优化中的学习率或令牌生成速度。

## Key Concepts

- 学习率
- 优化
- 吞吐量
- 超参数

## Use Cases

- 调整梯度下降优化
- 监控API使用限制
- 测量推理延迟

## Code Example

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
```

## Related Terms

- [Optimizer (优化器)](/en/terms/optimizer-优化器/)
- [Convergence (收敛)](/en/terms/convergence-收敛/)
- [Speed (速度)](/en/terms/speed-速度/)
- [Latency (延迟)](/en/terms/latency-延迟/)
