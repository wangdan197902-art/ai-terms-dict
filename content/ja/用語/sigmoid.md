---
title: "シグモイド関数"
term_id: "sigmoid"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Activation Functions"]
difficulty: 2
weight: 1
slug: "sigmoid"
aliases:
  - /ja/terms/sigmoid/
date: "2026-07-18T11:31:59.766559Z"
lastmod: "2026-07-18T11:44:45.143936Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "任意の実数値を0から1の間の値にマッピングし、S字型の曲線を描く数学関数。"
---

## Definition

シグモイド関数（σ(z) = 1 / (1 + e^-z)）は、機械学習で確率をモデル化するために広く使用されています。入力値を(0, 1)の範囲に圧縮するため、二値分類の出力層などに適しています。ただし、勾配消失問題を引き起こす可能性があります。

### Summary

任意の実数値を0から1の間の値にマッピングし、S字型の曲線を描く数学関数。

## Key Concepts

- ロジスティック関数
- 確率マッピング
- 勾配消失
- 非線形性

## Use Cases

- 二値分類の出力層
- ロジスティック回帰
- 浅いニューラルネットワークの活性化関数

## Code Example

```python
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
```

## Related Terms

- [ReLU (整流線形ユニット)](/en/terms/relu-整流線形ユニット/)
- [Softmax (ソフトマックス関数)](/en/terms/softmax-ソフトマックス関数/)
- [Logistic Regression (ロジスティック回帰)](/en/terms/logistic-regression-ロジスティック回帰/)
- [Activation Function (活性化関数)](/en/terms/activation-function-活性化関数/)
