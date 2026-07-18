---
title: "AI可观测性"
term_id: "ai_observability"
category: "engineering_practice"
subcategory: ""
tags: ["mlops", "monitoring", "engineering"]
difficulty: 4
weight: 1
slug: "ai_observability"
aliases:
  - /zh/terms/ai_observability/
date: "2026-07-18T11:03:04.566035Z"
lastmod: "2026-07-18T11:44:45.435808Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "通过日志、指标和追踪来监控和理解机器学习系统内部状态的做法。"
---

## Definition

AI可观测性将传统的软件监控扩展到解决机器学习系统的独特挑战。它涉及实时跟踪模型性能、数据漂移和推理延迟，从而帮助开发者深入理解黑盒模型的决策过程及其在生产环境中的行为。

### Summary

通过日志、指标和追踪来监控和理解机器学习系统内部状态的做法。

## Key Concepts

- 数据漂移
- 模型监控
- 遥测
- 调试

## Use Cases

- 检测生产模型中的概念漂移
- 排查低置信度预测问题
- 确保AI服务符合服务等级协议(SLA)

## Code Example

```python
import mlflow

# Log metrics during training
mlflow.log_metric('accuracy', 0.95)
mlflow.log_metric('loss', 0.05)

# Track model parameters
mlflow.log_param('learning_rate', 0.01)
mlflow.log_param('epochs', 10)
```

## Related Terms

- [MLOps (机器学习运维)](/en/terms/mlops-机器学习运维/)
- [模型漂移 (Model Drift)](/en/terms/模型漂移-model-drift/)
- [系统监控 (System Monitoring)](/en/terms/系统监控-system-monitoring/)
- [遥测 (Telemetry)](/en/terms/遥测-telemetry/)
