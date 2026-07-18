---
title: "ELMo"
term_id: "elmo"
category: "basic_concepts"
subcategory: ""
tags: ["NLP", "Embeddings", "History"]
difficulty: 3
weight: 1
slug: "elmo"
aliases:
  - /ja/terms/elmo/
date: "2026-07-18T11:12:52.607872Z"
lastmod: "2026-07-18T11:44:45.093191Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "双方向LSTMを用いた深層文脈依存語表現手法である、Language Modelsからの埋め込み。"
---

## Definition

ELMoは、大規模コーパスで訓練された双方向LSTMに入力テキストを処理することで、文脈依存の単語埋め込みを生成します。Word2Vecなどの静的な埋め込みとは異なり、ELMoは多義性を捉えるために、単語の出現文脈に基づいて異なる埋め込みベクトルを出力します。

### Summary

双方向LSTMを用いた深層文脈依存語表現手法である、Language Modelsからの埋め込み。

## Key Concepts

- 文脈依存埋め込み
- 双方向LSTM
- 事前学習
- 多義性

## Use Cases

- 感情分析
- 固有表現認識
- 共参照解決

## Related Terms

- [Word2Vec (ワード2vec)](/en/terms/word2vec-ワード2vec/)
- [BERT (ビート)](/en/terms/bert-ビート/)
- [Transformer (トランスフォーマー)](/en/terms/transformer-トランスフォーマー/)
- [Language Modeling (言語モデリング)](/en/terms/language-modeling-言語モデリング/)
