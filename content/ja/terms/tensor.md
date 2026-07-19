---
title: テンソル
term_id: tensor
category: basic_concepts
subcategory: ''
tags:
- math
- Data Structures
- pytorch
difficulty: 2
weight: 1
slug: tensor
date: '2026-07-18T11:34:13.391055Z'
lastmod: '2026-07-18T11:44:45.149587Z'
draft: false
source: agnes_llm
status: published
language: ja
description: ディープラーニングフレームワークの基本データ構造である多次元配列。
---
## Definition

コンピュータサイエンスおよびディープラーニングにおいて、テンソルはスカラー、ベクトル、行列を高次元に一般化した数学的对象です。そのランク（次元の数）と形状によって特徴付けられます。

### Summary

ディープラーニングフレームワークの基本データ構造である多次元配列。

## Key Concepts

- ランク
- 形状
- 次元性
- ブロードキャスティング

## Use Cases

- 画像処理（4Dテンソル）
- ニューラルネットワークの重み保存
- バッチ処理されたデータ入力

## Code Example

```python
import torch
t = torch.tensor([[1, 2], [3, 4]])
```

## Related Terms

- [Matrix (行列)](/en/terms/matrix-行列/)
- [Vector (ベクトル)](/en/terms/vector-ベクトル/)
- [Deep Learning (ディープラーニング)](/en/terms/deep-learning-ディープラーニング/)
- [NumPy (数値計算ライブラリ)](/en/terms/numpy-数値計算ライブラリ/)
