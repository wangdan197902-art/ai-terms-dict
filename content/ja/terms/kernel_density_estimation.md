---
title: "カーネル密度推定"
term_id: "kernel_density_estimation"
category: "basic_concepts"
subcategory: ""
tags: ["statistics", "probability", "data-analysis"]
difficulty: 3
weight: 1
slug: "kernel_density_estimation"
aliases:
  - /ja/terms/kernel_density_estimation/
date: "2026-07-18T11:20:29.257234Z"
lastmod: "2026-07-18T11:44:45.111903Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "有限のデータサンプルに基づいて、確率変数の確率密度関数を推定するために使用される非パラメトリック手法。"
---

## Definition

カーネル密度推定（KDE）は、離散データポイントを平滑化して連続的な確率分布曲線を作成する基本的な統計的手法です。通常、ガウス関数などのカーネル関数が各データポイントに配置され、全体の密度が推定されます。

### Summary

有限のデータサンプルに基づいて、確率変数の確率密度関数を推定するために使用される非パラメトリック手法。

## Key Concepts

- 確率密度関数
- 非パラメトリック統計
- 平滑化
- ガウスカーネル

## Use Cases

- 探索的データ分析（EDA）
- 単変量データにおける異常検出
- データセット内の特徴量の分布の可視化

## Code Example

```python
from scipy.stats import gaussian_kde
import numpy as np

data = np.random.normal(0, 1, 100)
kde = gaussian_kde(data)
x_vals = np.linspace(-3, 3, 100)
y_vals = kde(x_vals)
```

## Related Terms

- [Histogram (ヒストグラム)](/en/terms/histogram-ヒストグラム/)
- [Parzen Window (パーゼンウィンドウ)](/en/terms/parzen-window-パーゼンウィンドウ/)
- [Bandwidth Selection (バンド幅選択)](/en/terms/bandwidth-selection-バンド幅選択/)
- [Scipy Stats (Scipy統計ライブラリ)](/en/terms/scipy-stats-scipy統計ライブラリ/)
