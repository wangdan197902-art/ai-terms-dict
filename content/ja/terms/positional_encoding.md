---
title: 位置エンコーディング
term_id: positional_encoding
category: basic_concepts
subcategory: ''
tags:
- transformers
- NLP
- architecture
difficulty: 3
weight: 1
slug: positional_encoding
date: '2026-07-18T11:00:08.979988Z'
lastmod: '2026-07-18T11:44:45.052802Z'
draft: false
source: agnes_llm
status: published
language: ja
description: シーケンス内のトークンの相対的または絶対的な位置に関する情報をトランスフォーマーモデルに注入する技術。
---
## Definition

トランスフォーマーはRNNのように逐次的ではなく、すべてのトークンを並列で処理するため、トークンの順序に関する内在的な知識を持ちません。位置エンコーディングは、入力埋め込みベクトルに特定のベクトルを追加することで、この順序情報を付与します。

### Summary

シーケンス内のトークンの相対的または絶対的な位置に関する情報をトランスフォーマーモデルに注入する技術。

## Key Concepts

- シーケンスの順序
- 自己注意機構
- 正弦関数
- トークン埋め込み

## Use Cases

- 機械翻訳
- テキスト要約
- 言語モデリング

## Code Example

```python
import torch
import math
def get_positional_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe.unsqueeze(0)
```

## Related Terms

- [Transformer Architecture (トランスフォーマーアーキテクチャ)](/en/terms/transformer-architecture-トランスフォーマーアーキテクチャ/)
- [Embedding (埋め込み表現)](/en/terms/embedding-埋め込み表現/)
- [Attention Mechanism (注意機構)](/en/terms/attention-mechanism-注意機構/)
- [RoPE (回転位置エンコーディング)](/en/terms/rope-回転位置エンコーディング/)
