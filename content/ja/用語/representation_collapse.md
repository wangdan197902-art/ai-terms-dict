---
title: "表現崩壊"
term_id: "representation_collapse"
category: "basic_concepts"
subcategory: ""
tags: ["self_supervised", "training_dynamics", "computer_vision"]
difficulty: 3
weight: 1
slug: "representation_collapse"
aliases:
  - /ja/terms/representation_collapse/
date: "2026-07-18T11:30:33.410980Z"
lastmod: "2026-07-18T11:44:45.138866Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "自己教師あり学習において、モデルが入力に対して同一の表現を出力し、識別力を失う失敗モード。"
---

## Definition

表現崩壊とは、特に自己教師ありのコントラスト学習フレームワークにおいて、ニューラルネットワークがすべての入力データポイントを同じ固定された出力ベクトルにマッピングするように学習してしまう現象です。これは自明な解（trivial solution）であり、モデルがデータの構造や特徴を学習できていないことを示します。これを回避するために、バッチ正規化やモーメンタムエンコーダーなどの技術が用いられます。

### Summary

自己教師あり学習において、モデルが入力に対して同一の表現を出力し、識別力を失う失敗モード。

## Key Concepts

- 自己教師あり学習
- コントラスト損失
- 自明な解
- 特徴学習

## Use Cases

- SimCLRやMoCoモデルのデバッグ
- コントラスト損失関数の改善
- モデルの収束分析

## Related Terms

- [Contrastive Learning (コントラスト学習)](/en/terms/contrastive-learning-コントラスト学習/)
- [Batch Normalization (バッチ正規化)](/en/terms/batch-normalization-バッチ正規化/)
- [Momentum Encoder (モーメンタムエンコーダ)](/en/terms/momentum-encoder-モーメンタムエンコーダ/)
- [Feature Extraction (特徴抽出)](/en/terms/feature-extraction-特徴抽出/)
