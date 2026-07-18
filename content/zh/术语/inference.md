---
title: "推理"
term_id: "inference"
category: "engineering_practice"
subcategory: ""
tags: ["Deployment", "Production", "Performance"]
difficulty: 2
weight: 1
slug: "inference"
aliases:
  - /zh/terms/inference/
date: "2026-07-18T07:44:46.533469Z"
lastmod: "2026-07-18T11:44:44.592342Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "训练好的模型处理新数据以生成预测或输出的阶段。"
---

## Definition

推理指的是部署阶段，在此阶段使用最终确定的模型对未见过的数据进行决策或预测。与更新权重的训练不同，推理消耗计算资源以产生结果。

### Summary

训练好的模型处理新数据以生成预测或输出的阶段。

## Key Concepts

- 预测
- 延迟
- 吞吐量
- 部署

## Use Cases

- 银行交易中的实时欺诈检测
- 实时聊天交互中生成响应
- 自动驾驶系统中的图像分类

## Code Example

```python
import torch
model.eval()
with torch.no_grad():
    output = model(input_tensor)
    prediction = torch.argmax(output, dim=1)
```

## Related Terms

- [训练](/en/terms/训练/)
- [延迟优化](/en/terms/延迟优化/)
- [批处理](/en/terms/批处理/)
- [模型服务](/en/terms/模型服务/)
