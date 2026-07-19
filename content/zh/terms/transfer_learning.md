---
title: 迁移学习
term_id: transfer_learning
category: training_techniques
subcategory: ''
tags:
- Optimization
- efficiency
- Deep Learning
difficulty: 3
weight: 1
slug: transfer_learning
date: '2026-07-18T10:55:40.663771Z'
lastmod: '2026-07-18T11:44:45.387273Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种机器学习技术，将在一个任务中开发的模型作为第二个任务的模型的起点进行复用。
---
## Definition

迁移学习利用预训练模型来提高在新且相关任务上的性能并减少训练时间。开发人员无需从头开始训练，而是对现有权重进行微调，从而利用先前学到的知识。

### Summary

一种机器学习技术，将在一个任务中开发的模型作为第二个任务的模型的起点进行复用。

## Key Concepts

- 预训练模型
- 微调
- 领域自适应
- 特征提取

## Use Cases

- 数据有限的图像分类
- 针对小众主题的情感分析
- 医疗诊断辅助

## Code Example

```python
from transformers import AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
```

## Related Terms

- [fine_tuning (微调)](/en/terms/fine_tuning-微调/)
- [pre_training (预训练)](/en/terms/pre_training-预训练/)
- [domain_adaptation (领域自适应)](/en/terms/domain_adaptation-领域自适应/)
- [few_shot_learning (少样本学习)](/en/terms/few_shot_learning-少样本学习/)
