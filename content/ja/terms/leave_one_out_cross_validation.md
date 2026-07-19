---
title: 留一法交差検証
term_id: leave_one_out_cross_validation
category: basic_concepts
subcategory: ''
tags:
- Machine Learning
- evaluation
- statistics
difficulty: 3
weight: 1
slug: leave_one_out_cross_validation
date: '2026-07-18T11:21:43.563696Z'
lastmod: '2026-07-18T11:44:45.115499Z'
draft: false
source: agnes_llm
status: published
language: ja
description: モデルを1つのサンプルを除くすべてのデータで学習し、その1つを残してテストする厳密なリサンプリング手法であり、このプロセスを各データポイントに対して繰り返す。
---
## Definition

留一法交差検証（LOOCV）は、kの値がデータセット内のサンプル数と等しいk-fold交差検証の特殊なケースです。これはモデル性能のほぼ不偏な推定値を提供します。

### Summary

モデルを1つのサンプルを除くすべてのデータで学習し、その1つを残してテストする厳密なリサンプリング手法であり、このプロセスを各データポイントに対して繰り返す。

## Key Concepts

- リサンプリング
- モデル評価
- バイアス・バリアンストレードオフ
- 計算コスト

## Use Cases

- 小規模な医療データセットでのモデル評価
- データが限られている場合のハイパーパラメータチューニング
- アルゴリズム性能の厳密な比較

## Code Example

```python
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
```

## Related Terms

- [k-fold cross-validation (k分割交差検証)](/en/terms/k-fold-cross-validation-k分割交差検証/)
- [train_test_split (訓練・テスト分割)](/en/terms/train_test_split-訓練-テスト分割/)
- [bootstrap (ブートストラップ)](/en/terms/bootstrap-ブートストラップ/)
- [cross_validation_score (交差検証スコア)](/en/terms/cross_validation_score-交差検証スコア/)
