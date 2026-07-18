---
title: "TensorBoard"
term_id: "tensorboard"
category: "basic_concepts"
subcategory: ""
tags: ["tensorflow", "tools", "visualization"]
difficulty: 2
weight: 1
slug: "tensorboard"
aliases:
  - /zh/terms/tensorboard/
date: "2026-07-18T11:35:54.969718Z"
lastmod: "2026-07-18T11:44:45.561866Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一个用于监控机器学习实验和调试模型性能的可视化工具包。"
---

## Definition

TensorBoard 是一套用于检查和理解 TensorFlow 运行过程和计算图的 Web 应用程序套件。它提供了可视化损失和准确率等指标随时间变化的工具，以及查看模型图的功能。

### Summary

一个用于监控机器学习实验和调试模型性能的可视化工具包。

## Key Concepts

- 可视化
- 超参数调优
- 图检查
- 指标跟踪

## Use Cases

- 调试训练收敛情况
- 比较模型架构
- 可视化嵌入空间

## Code Example

```python
from tensorboard.callback import TensorBoardCallback
callback = TensorBoardCallback(log_dir='./logs')
```

## Related Terms

- [MLflow (MLflow平台)](/en/terms/mlflow-mlflow平台/)
- [Weights & Biases (W&B平台)](/en/terms/weights-biases-w-b平台/)
- [TensorFlow (TensorFlow框架)](/en/terms/tensorflow-tensorflow框架/)
- [Experiment Tracking (实验跟踪)](/en/terms/experiment-tracking-实验跟踪/)
