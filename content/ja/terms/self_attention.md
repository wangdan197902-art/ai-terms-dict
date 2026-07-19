---
title: "セルフアテンション"
term_id: "self_attention"
category: "basic_concepts"
subcategory: ""
tags: ["transformers", "architecture"]
difficulty: 4
weight: 1
slug: "self_attention"
date: "2026-07-18T10:54:57.923562Z"
lastmod: "2026-07-18T11:44:45.019323Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "ニューラルネットワークが入力シーケンスの異なる部分間の相対的な重要性を重み付けできるメカニズム。"
---
## Definition

セルフアテンションにより、モデルは距離に関係なく、シーケンス内のすべての位置間の依存関係を同時に捉えることができます。すべてのトークンのペア間でアテンションスコアを計算することにより、これを実現します。

### Summary

ニューラルネットワークが入力シーケンスの異なる部分間の相対的な重要性を重み付けできるメカニズム。

## Key Concepts

- クエリ・キー・バリュー
- アテンションスコア
- 文脈的重み付け
- 並列処理

## Use Cases

- 機械翻訳
- テキスト要約
- ビジョントランスフォーマーによる画像分類

## Code Example

```python
import torch.nn as nn
attn = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [Transformer (トランスフォーマー)](/en/terms/transformer-トランスフォーマー/)
- [Multi-Head Attention (マルチヘッドアテンション)](/en/terms/multi-head-attention-マルチヘッドアテンション/)
- [Embeddings (埋め込み表現)](/en/terms/embeddings-埋め込み表現/)
- [Sequence Modeling (シーケンスモデリング)](/en/terms/sequence-modeling-シーケンスモデリング/)
