---
title: "線形"
term_id: "linear"
category: "basic_concepts"
subcategory: ""
tags: ["Mathematics", "Neural Networks", "Foundations"]
difficulty: 2
weight: 1
slug: "linear"
date: "2026-07-18T10:52:09.964089Z"
lastmod: "2026-07-18T11:44:45.012336Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "出力が入力に直接比例する操作や関係を示し、ニューラルレイヤーのアフィン変換の基礎を形成する。"
---
## Definition

線形操作には、非線形活性化関数を伴わない乗算と加算が含まれます。ニューラルネットワークでは、線形レイヤー（または密結合層）が入力ベクトルに重み行列変換を適用します。線形操作のみでは

### Summary

出力が入力に直接比例する操作や関係を示し、ニューラルレイヤーのアフィン変換の基礎を形成する。

## Key Concepts

- 重み行列
- アフィン変換
- ドット積
- 重ね合わせ

## Use Cases

- 特徴量投影
- ロジスティック回帰
- アテンション機構

## Code Example

```python
import torch.nn as nn
layer = nn.Linear(10, 5)
output = layer(input_tensor)
```

## Related Terms

- [Activation Function (活性化関数)](/en/terms/activation-function-活性化関数/)
- [Dense Layer (密結合層)](/en/terms/dense-layer-密結合層/)
- [Matrix Multiplication (行列乗算)](/en/terms/matrix-multiplication-行列乗算/)
