---
title: 線形予測関数
term_id: linear_predictor_function
category: basic_concepts
subcategory: ''
tags:
- statistics
- Linear Models
- mathematics
difficulty: 2
weight: 1
slug: linear_predictor_function
date: '2026-07-18T11:21:57.579271Z'
lastmod: '2026-07-18T11:44:45.116137Z'
draft: false
source: agnes_llm
status: published
language: ja
description: 入力変数の線形結合を計算して結果を予測する数学関数。
---
## Definition

統計モデリングや機械学習において、線形予測関数は、重み付き入力特徴量の合計にバイアス項を加えたものを指します。これは一般化線形モデル（GLM）の中核的な構成要素として機能します。

### Summary

入力変数の線形結合を計算して結果を予測する数学関数。

## Key Concepts

- 加重和
- バイアス項
- 一般化線形モデル
- 特徴量係数

## Use Cases

- 線形回帰分析
- ロジスティック回帰分類
- サポートベクターマシン（カーネルトリックの文脈）

## Code Example

```python
import numpy as np
X = np.array([[1, 2], [3, 4]])
w = np.array([0.5, 1.0])
b = 0.1
prediction = np.dot(X, w) + b
```

## Related Terms

- [regression_coefficients (回帰係数)](/en/terms/regression_coefficients-回帰係数/)
- [bias_intercept (バイアス切片)](/en/terms/bias_intercept-バイアス切片/)
- [feature_engineering (特徴量エンジニアリング)](/en/terms/feature_engineering-特徴量エンジニアリング/)
- [generalized_linear_model (一般化線形モデル)](/en/terms/generalized_linear_model-一般化線形モデル/)
