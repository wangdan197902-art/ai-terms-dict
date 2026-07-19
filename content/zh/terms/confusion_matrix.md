---
title: 混淆矩阵
term_id: confusion_matrix
category: basic_concepts
subcategory: ''
tags:
- evaluation
- Classification
- metrics
difficulty: 2
weight: 1
slug: confusion_matrix
date: '2026-07-18T11:11:15.321096Z'
lastmod: '2026-07-18T11:44:45.461224Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 用于描述分类模型在测试数据集上性能的表格。
---
## Definition

混淆矩阵是一种特定的表格布局，用于可视化算法（通常是监督学习算法）的性能。它显示了真阳性、真阴性、假阳性和假阴性的计数。

### Summary

用于描述分类模型在测试数据集上性能的表格。

## Key Concepts

- 真阳性
- 假阴性
- 精确率
- 召回率

## Use Cases

- 评估二分类器
- 分析多分类性能
- 调试不平衡数据集中的模型偏差

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (精确率)](/en/terms/precision-精确率/)
- [recall (召回率)](/en/terms/recall-召回率/)
- [F1 score (F1分数)](/en/terms/f1-score-f1分数/)
- [ROC curve (ROC曲线)](/en/terms/roc-curve-roc曲线/)
