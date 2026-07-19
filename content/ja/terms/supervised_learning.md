---
title: 教師あり学習
term_id: supervised_learning
category: basic_concepts
subcategory: ''
tags:
- ML Basics
- training
- paradigms
difficulty: 1
weight: 1
slug: supervised_learning
date: '2026-07-18T11:01:15.727410Z'
lastmod: '2026-07-18T11:44:45.058360Z'
draft: false
source: agnes_llm
status: published
language: ja
description: モデルがラベル付きの訓練例に基づいて、入力を出力へマッピングする方法を学ぶ機械学習のパラダイム。
---
## Definition

教師あり学習では、アルゴリズムはラベル付きデータセットで訓練されます。つまり、各入力例には正しい出力がペアになっています。目標は、モデルが入力と出力の間の潜在的な関係を学習することです。

### Summary

モデルがラベル付きの訓練例に基づいて、入力を出力へマッピングする方法を学ぶ機械学習のパラダイム。

## Key Concepts

- ラベル付きデータ
- 入出力マッピング
- 分類
- 回帰

## Use Cases

- スパムメール検出
- 家賃予測
- 画像認識

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

## Related Terms

- [Unsupervised Learning (教師なし学習)](/en/terms/unsupervised-learning-教師なし学習/)
- [Training Set (訓練データセット)](/en/terms/training-set-訓練データセット/)
- [Validation Set (検証データセット)](/en/terms/validation-set-検証データセット/)
- [Model Accuracy (モデル精度)](/en/terms/model-accuracy-モデル精度/)
