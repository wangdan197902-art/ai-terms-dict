---
title: "监督学习"
term_id: "supervised_learning"
category: "basic_concepts"
subcategory: ""
tags: ["ml-basics", "training", "paradigms"]
difficulty: 1
weight: 1
slug: "supervised_learning"
aliases:
  - /zh/terms/supervised_learning/
date: "2026-07-18T11:02:04.102315Z"
lastmod: "2026-07-18T11:44:45.406541Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种机器学习范式，模型基于带标签的训练示例学习将输入映射到输出。"
---

## Definition

在监督学习中，算法在带标签的数据集上进行训练，意味着每个输入示例都与正确的输出配对。目标是让模型学习输入与输出之间的潜在关系。

### Summary

一种机器学习范式，模型基于带标签的训练示例学习将输入映射到输出。

## Key Concepts

- 带标签数据
- 输入-输出映射
- 分类
- 回归

## Use Cases

- 垃圾邮件检测
- 房价预测
- 图像识别

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [无监督学习](/en/terms/无监督学习/)
- [训练集](/en/terms/训练集/)
- [验证集](/en/terms/验证集/)
- [模型准确率](/en/terms/模型准确率/)
