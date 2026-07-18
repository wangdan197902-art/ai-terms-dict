---
title: "教師あり"
term_id: "supervised"
category: "training_techniques"
subcategory: ""
tags: ["ML", "training"]
difficulty: 2
weight: 1
slug: "supervised"
aliases:
  - /ja/terms/supervised/
date: "2026-07-18T10:55:09.231570Z"
lastmod: "2026-07-18T11:44:45.020439Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "モデルがラベル付きの入出力ペアを用いて訓練される機械学習のパラダイム。"
---

## Definition

教師あり学習では、入力と正解（ラベル）の両方を含むデータアルゴリズムに供給します。モデルは予測誤差を最小化することで、入力を出力へマッピングすることを学びます。この技術は広く使用されています。

### Summary

モデルがラベル付きの入出力ペアを用いて訓練される機械学習のパラダイム。

## Key Concepts

- ラベル付きデータ
- マッピング
- 損失の最小化

## Use Cases

- 画像分類
- スパム検出
- 価格予測

## Code Example

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

## Related Terms

- [Unsupervised (教師なし)](/en/terms/unsupervised-教師なし/)
- [Label (ラベル)](/en/terms/label-ラベル/)
- [Regression (回帰)](/en/terms/regression-回帰/)
