---
title: ソフトマックス
term_id: softmax
category: basic_concepts
subcategory: ''
tags:
- math
- Neural Networks
- Classification
difficulty: 2
weight: 1
slug: softmax
date: '2026-07-18T11:01:15.727389Z'
lastmod: '2026-07-18T11:44:45.057980Z'
draft: false
source: agnes_llm
status: published
language: ja
description: 任意の実数値のスコアベクトルを確率分布に変換する数学関数。
---
## Definition

ソフトマックスは、多クラス分類タスクにおけるニューラルネットワークの出力層で広く使用されています。これは生のロジット（logits）ベクトルを入力として受け取り、正規化を行うことで、各要素が確率を表すようにします。

### Summary

任意の実数値のスコアベクトルを確率分布に変換する数学関数。

## Key Concepts

- 確率分布
- ロジット
- 正規化
- 多クラス分類

## Use Cases

- 画像分類の出力層
- 言語モデルのトークン予測
- マルチラベル分類

## Code Example

```python
import torch
import torch.nn.functional as F
logits = torch.tensor([1.0, 2.0, 3.0])
probs = F.softmax(logits, dim=0)
print(probs)
```

## Related Terms

- [Argmax (最大値のインデックスを取得)](/en/terms/argmax-最大値のインデックスを取得/)
- [Cross-Entropy Loss (交差エントロピー誤差)](/en/terms/cross-entropy-loss-交差エントロピー誤差/)
- [Logits (未正規化の出力スコア)](/en/terms/logits-未正規化の出力スコア/)
- [Neural Network (ニューラルネットワーク)](/en/terms/neural-network-ニューラルネットワーク/)
