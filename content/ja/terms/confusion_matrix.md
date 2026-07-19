---
title: 混同行列
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
date: '2026-07-18T11:08:51.058119Z'
lastmod: '2026-07-18T11:44:45.079970Z'
draft: false
source: agnes_llm
status: published
language: ja
description: テストデータセットにおける分類モデルの性能を記述するために使用される表。
---
## Definition

混同行列は、アルゴリズム（通常は教師あり学習）の性能を視覚化するために使用される特定の表形式です。真陽性、真陰性、偽陽性、偽陰性の数を示し、モデルの分類精度やバイアスを評価するのに役立ちます。

### Summary

テストデータセットにおける分類モデルの性能を記述するために使用される表。

## Key Concepts

- 真陽性
- 偽陰性
- 適合率
- 再現率

## Use Cases

- 二値分類器の評価
- 多クラス分類性能の分析
- 不均衡データセットにおけるモデルバイアスのデバッグ

## Code Example

```python
from sklearn.metrics import confusion_matrix
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
print(confusion_matrix(y_true, y_pred))
```

## Related Terms

- [precision (適合率)](/en/terms/precision-適合率/)
- [recall (再現率)](/en/terms/recall-再現率/)
- [F1 score (F1スコア)](/en/terms/f1-score-f1スコア/)
- [ROC curve (ROC曲線)](/en/terms/roc-curve-roc曲線/)
