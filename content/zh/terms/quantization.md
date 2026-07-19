---
title: 量化
term_id: quantization
category: training_techniques
subcategory: ''
tags:
- Optimization
- deployment
- performance
difficulty: 3
weight: 1
slug: quantization
date: '2026-07-18T11:01:29.499782Z'
lastmod: '2026-07-18T11:44:45.404189Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种模型优化技术，通过降低神经网络计算中数字的精度来减小模型体积并提高速度。
---
## Definition

量化将高精度浮点数（如 FP32）转换为低精度格式（如 INT8 或 FP16）。这种转换减少了模型的内存使用和计算需求，从而加速推理过程并降低硬件要求。

### Summary

一种模型优化技术，通过降低神经网络计算中数字的精度来减小模型体积并提高速度。

## Key Concepts

- 精度降低
- 推理速度
- 内存优化
- INT8/FP16

## Use Cases

- 边缘设备部署
- 移动 AI 应用
- 实时推理

## Code Example

```python
import torch.quantization as quant
# Example of converting a model to quantized format
model.eval()
model.qconfig = quant.get_default_qconfig('fbgemm')
quantized_model = quant.prepare(model, inplace=False)
quantized_model = quant.convert(quantized_model, inplace=False)
```

## Related Terms

- [剪枝 (Pruning)](/en/terms/剪枝-pruning/)
- [知识蒸馏 (Knowledge Distillation)](/en/terms/知识蒸馏-knowledge-distillation/)
- [混合精度训练 (Mixed Precision Training)](/en/terms/混合精度训练-mixed-precision-training/)
- [ONNX](/en/terms/onnx/)
