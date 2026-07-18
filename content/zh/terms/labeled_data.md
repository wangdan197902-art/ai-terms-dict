---
title: "标注数据"
term_id: "labeled_data"
category: "basic_concepts"
subcategory: ""
tags: ["data", "supervised_learning", "fundamentals"]
difficulty: 1
weight: 1
slug: "labeled_data"
aliases:
  - /zh/terms/labeled_data/
date: "2026-07-18T11:23:41.252057Z"
lastmod: "2026-07-18T11:44:45.522655Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "在输入特征旁边提供正确输出或目标值的数据。"
---

## Definition

标注数据由输入样本及其对应的真实标签组成，是监督机器学习的基础。它允许算法学习输入与输出之间的映射关系。

### Summary

在输入特征旁边提供正确输出或目标值的数据。

## Key Concepts

- 监督学习
- 真实标签
- 标注
- 目标变量

## Use Cases

- 训练图像分类器
- 构建语音识别系统
- 金融领域的预测建模

## Code Example

```python
import pandas as pd
# Example of loading labeled data
df = pd.read_csv('train.csv')
X = df.drop('label', axis=1)
y = df['label']
```

## Related Terms

- [unlabeled_data (未标注数据)](/en/terms/unlabeled_data-未标注数据/)
- [supervised_learning (监督学习)](/en/terms/supervised_learning-监督学习/)
- [data_annotation (数据标注)](/en/terms/data_annotation-数据标注/)
- [training_set (训练集)](/en/terms/training_set-训练集/)
