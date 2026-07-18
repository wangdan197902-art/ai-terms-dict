---
title: "特征工程"
term_id: "feature_engineering"
category: "basic_concepts"
subcategory: ""
tags: ["preprocessing", "technique", "optimization"]
difficulty: 3
weight: 1
slug: "feature_engineering"
aliases:
  - /zh/terms/feature_engineering/
date: "2026-07-18T11:17:01.610015Z"
lastmod: "2026-07-18T11:44:45.498415Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "利用领域知识创建新特征或修改现有特征，以增强机器学习模型性能的做法。"
---

## Definition

特征工程是利用领域专业知识，将原始数据转换为更能代表底层模式的特征的艺术。该过程包括创建新变量、转换现有数据以及选择最具预测力的特征，从而提升算法效果。

### Summary

利用领域知识创建新特征或修改现有特征，以增强机器学习模型性能的做法。

## Key Concepts

- 领域知识
- 数据转换
- 模型性能
- 变量创建

## Use Cases

- 提高回归模型准确性
- 增强分类边界
- 优化时间序列预测

## Code Example

```python
df['new_feature'] = df['feature_a'] * df['feature_b']
```

## Related Terms

- [特征提取](/en/terms/特征提取/)
- [数据预处理](/en/terms/数据预处理/)
- [模型调优](/en/terms/模型调优/)
- [领域专长](/en/terms/领域专长/)
