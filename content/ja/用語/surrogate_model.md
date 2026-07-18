---
title: "代理モデル"
term_id: "surrogate_model"
category: "basic_concepts"
subcategory: ""
tags: ["optimization", "approximation", "ml_technique"]
difficulty: 3
weight: 1
slug: "surrogate_model"
aliases:
  - /ja/terms/surrogate_model/
date: "2026-07-18T11:33:46.958516Z"
lastmod: "2026-07-18T11:44:45.148568Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "より複雑で計算コストが高く、またはアクセス困難なブラックボックスモデルの挙動を近似するために使用される、簡略化された数学モデル。"
---

## Definition

機械学習および最適化において、代理モデルは直接評価が困難な目的関数のプロキシとして機能します。これは、元のモデルからの入力-出力ペアを用いて訓練され、元のモデルの挙動を効率的に模倣します。

### Summary

より複雑で計算コストが高く、またはアクセス困難なブラックボックスモデルの挙動を近似するために使用される、簡略化された数学モデル。

## Key Concepts

- モデル近似
- ブラックボックス最適化
- 計算効率
- プロキシモデル

## Use Cases

- ハイパーパラメータ最適化
- 工学設計シミュレーションの加速
- 複雑システムの感度分析

## Code Example

```python
from sklearn.gaussian_process import GaussianProcessRegressor
import numpy as np

# Simple surrogate for a noisy function
X = np.array([[1], [2], [3], [4]])
y = np.array([2.1, 3.9, 6.2, 7.8])

surrogate = GaussianProcessRegressor()
surrogate.fit(X, y)
prediction = surrogate.predict(np.array([[2.5]]))
```

## Related Terms

- [Bayesian Optimization (ベイズ最適化)](/en/terms/bayesian-optimization-ベイズ最適化/)
- [Gaussian Process (ガウス過程)](/en/terms/gaussian-process-ガウス過程/)
- [Black-Box Function (ブラックボックス関数)](/en/terms/black-box-function-ブラックボックス関数/)
- [Emulator (エミュレータ)](/en/terms/emulator-エミュレータ/)
