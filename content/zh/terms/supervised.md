---
title: "监督式"
term_id: "supervised"
category: "training_techniques"
subcategory: ""
tags: ["ML", "training"]
difficulty: 2
weight: 1
slug: "supervised"
date: "2026-07-18T10:55:02.592487Z"
lastmod: "2026-07-18T11:44:45.385709Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种机器学习范式，模型在有标签的输入-输出对上进行训练。"
---
## Definition

监督学习涉及向算法提供包含输入和正确答案（标签）的数据。模型通过最小化预测误差来学习将输入映射到输出。这项技术...

### Summary

一种机器学习范式，模型在有标签的输入-输出对上进行训练。

## Key Concepts

- 有标签数据
- 映射
- 损失最小化

## Use Cases

- 图像分类
- 垃圾邮件检测
- 价格预测

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

## Related Terms

- [无监督 (Unsupervised)](/en/terms/无监督-unsupervised/)
- [标签 (Label)](/en/terms/标签-label/)
- [回归 (Regression)](/en/terms/回归-regression/)
