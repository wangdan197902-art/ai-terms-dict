---
title: "Transformer"
term_id: "transformer"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "nlp", "attention"]
difficulty: 4
weight: 1
slug: "transformer"
aliases:
  - /ja/terms/transformer/
date: "2026-07-18T10:55:53.677088Z"
lastmod: "2026-07-18T11:44:45.021870Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "自己注意機構に基づき、逐次処理ではなく並列処理でシーケンシャルデータを処理するディープラーニングアーキテクチャ。"
---

## Definition

「Attention Is All You Need」論文で紹介されたTransformerアーキテクチャは、自然言語処理およびそれ以外の分野に革命をもたらしました。これはマルチヘッド自己注意を用いて、入力データの各要素の重要度を評価・重み付けします。

### Summary

自己注意機構に基づき、逐次処理ではなく並列処理でシーケンシャルデータを処理するディープラーニングアーキテクチャ。

## Key Concepts

- 自己注意
- マルチヘッド注意
- 位置エンコーディング
- エンコーダ-デコーダ構造

## Use Cases

- 機械翻訳
- テキスト生成
- 画像認識（ViT）

## Code Example

```python
import torch.nn as nn
attention_layer = nn.MultiheadAttention(embed_dim=512, num_heads=8)
```

## Related Terms

- [attention_mechanism (アテンションメカニズム: 入力の重要な部分に焦点を当てる仕組み)](/en/terms/attention_mechanism-アテンションメカニズム-入力の重要な部分に焦点を当てる仕組み/)
- [bert (BERT: Transformerベースの双方向言語表現モデル)](/en/terms/bert-bert-transformerベースの双方向言語表現モデル/)
- [gpt (GPT: Transformerベースの生成言語モデル)](/en/terms/gpt-gpt-transformerベースの生成言語モデル/)
- [self_attention (自己注意: シーケンス内の要素間の関係性を捉える機構)](/en/terms/self_attention-自己注意-シーケンス内の要素間の関係性を捉える機構/)
