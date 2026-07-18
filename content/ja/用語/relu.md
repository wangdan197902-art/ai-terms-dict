---
title: "ReLU"
term_id: "relu"
category: "basic_concepts"
subcategory: ""
tags: ["neural-networks", "activation-functions", "deep-learning"]
difficulty: 3
weight: 1
slug: "relu"
aliases:
  - /ja/terms/relu/
date: "2026-07-18T11:00:21.252638Z"
lastmod: "2026-07-18T11:44:45.056840Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "ReLU（Rectified Linear Unit）は、入力が正の場合は入力をそのまま出力し、負の場合はゼロを出力する活性化関数です。"
---

## Definition

ReLUは、計算効率が高く、勾配消失問題を緩和できるため、ディープラーニングニューラルネットワークで広く使用されています。数学的には f(x) = max(0, x) と定義され、非線形性を導入しながらも計算コストを抑えることができます。

### Summary

ReLU（Rectified Linear Unit）は、入力が正の場合は入力をそのまま出力し、負の場合はゼロを出力する活性化関数です。

## Key Concepts

- 非線形性
- 活性化関数
- 勾配消失問題
- 区間線形関数

## Use Cases

- CNNの隠れ層
- ディープ順伝播ネットワーク
- 画像認識モデル

## Code Example

```python
import torch.nn as nn
activation = nn.ReLU()
```

## Related Terms

- [Sigmoid (シグモイド関数)](/en/terms/sigmoid-シグモイド関数/)
- [Tanh (双曲線正接関数)](/en/terms/tanh-双曲線正接関数/)
- [Leaky ReLU (リーキーReLU)](/en/terms/leaky-relu-リーキーrelu/)
- [Neural Network (ニューラルネットワーク)](/en/terms/neural-network-ニューラルネットワーク/)
