---
title: 压缩张量
term_id: compressed_tensors
category: basic_concepts
subcategory: ''
tags:
- Optimization
- hardware
- performance
difficulty: 4
weight: 1
slug: compressed_tensors
date: '2026-07-18T11:10:50.277266Z'
lastmod: '2026-07-18T11:44:45.459361Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 通过降低数据精度或大小以优化存储和计算效率的张量。
---
## Definition

压缩张量是深度学习中使用的多维数组，其数值精度（例如从float32降至int8）或稀疏性已降低。这种技术被称为量化或剪枝。

### Summary

通过降低数据精度或大小以优化存储和计算效率的张量。

## Key Concepts

- 量化
- 稀疏性
- 内存优化
- 推理速度

## Use Cases

- 移动AI应用部署
- 边缘设备处理
- 大型语言模型服务优化

## Code Example

```python
import torch
# Example of converting a tensor to half precision
x = torch.randn(10, 10)
x_compressed = x.half()
```

## Related Terms

- [Quantization (量化)](/en/terms/quantization-量化/)
- [Pruning (剪枝)](/en/terms/pruning-剪枝/)
- [Model Distillation (模型蒸馏)](/en/terms/model-distillation-模型蒸馏/)
- [Float16 (半精度浮点数)](/en/terms/float16-半精度浮点数/)
