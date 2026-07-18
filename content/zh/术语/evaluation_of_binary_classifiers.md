---
title: "二分类器评估"
term_id: "evaluation_of_binary_classifiers"
category: "basic_concepts"
subcategory: ""
tags: ["metrics", "classification", "evaluation"]
difficulty: 2
weight: 1
slug: "evaluation_of_binary_classifiers"
aliases:
  - /zh/terms/evaluation_of_binary_classifiers/
date: "2026-07-18T11:16:37.593404Z"
lastmod: "2026-07-18T11:44:45.495824Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "评估预测两种可能结果之一的机器学习模型性能的过程。"
---

## Definition

该领域涉及分析准确率、精确率、召回率、F1分数以及接收者操作特征曲线下面积（AUC-ROC）等指标。它有助于确定模型在区分正负样本方面的表现，并揭示模型在不同阈值下的权衡情况。

### Summary

评估预测两种可能结果之一的机器学习模型性能的过程。

## Key Concepts

- 混淆矩阵
- 精确率-召回率权衡
- ROC曲线
- F1分数

## Use Cases

- 医学疾病筛查
- 垃圾邮件过滤
- 信用风险评估

## Code Example

```python
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))
```

## Related Terms

- [confusion_matrix (混淆矩阵)](/en/terms/confusion_matrix-混淆矩阵/)
- [roc_auc (ROC曲线下面积)](/en/terms/roc_auc-roc曲线下面积/)
- [precision_recall (精确率与召回率)](/en/terms/precision_recall-精确率与召回率/)
- [cross_validation (交叉验证)](/en/terms/cross_validation-交叉验证/)
