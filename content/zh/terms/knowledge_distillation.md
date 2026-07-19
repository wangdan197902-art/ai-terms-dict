---
title: "知识蒸馏"
term_id: "knowledge_distillation"
category: "training_techniques"
subcategory: ""
tags: ["Training", "Compression", "Optimization"]
difficulty: 4
weight: 1
slug: "knowledge_distillation"
date: "2026-07-18T11:23:05.463567Z"
lastmod: "2026-07-18T11:44:45.520772Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "知识蒸馏是一种模型压缩技术，其中较小的学生模型通过学习模仿较大的教师模型的行为来工作。"
---
## Definition

知识蒸馏是一种机器学习方法，用于将庞大复杂的神经网络（教师模型）压缩为更小、更高效的网络（学生模型）。学生模型经过训练以模仿教师模型的行为。

### Summary

知识蒸馏是一种模型压缩技术，其中较小的学生模型通过学习模仿较大的教师模型的行为来工作。

## Key Concepts

- 师生模型
- 模型压缩
- 软标签
- 效率

## Use Cases

- 在边缘设备上部署模型
- 降低推理延迟
- 降低云计算成本

## Code Example

```python
import torch
import torch.nn as nn

def distillation_loss(student_logits, teacher_logits, temperature=2.0):
    T = temperature
    student_probs = nn.functional.softmax(student_logits / T, dim=1)
    teacher_probs = nn.functional.softmax(teacher_logits / T, dim=1)
    return nn.functional.kl_div(
        nn.functional.log_softmax(student_logits / T, dim=1),
        teacher_probs,
        reduction='batchmean'
    ) * (T * T)
```

## Related Terms

- [Model Compression (模型压缩)](/en/terms/model-compression-模型压缩/)
- [Pruning (剪枝)](/en/terms/pruning-剪枝/)
- [Quantization (量化)](/en/terms/quantization-量化/)
- [Neural Networks (神经网络)](/en/terms/neural-networks-神经网络/)
