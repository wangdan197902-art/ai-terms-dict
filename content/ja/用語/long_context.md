---
title: "ロングコンテキスト"
term_id: "long_context"
category: "basic_concepts"
subcategory: ""
tags: ["nlp", "transformers", "architecture"]
difficulty: 2
weight: 1
slug: "long_context"
aliases:
  - /ja/terms/long_context/
date: "2026-07-18T11:22:25.279085Z"
lastmod: "2026-07-18T11:44:45.117727Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "言語モデルが、数千〜数百万トークンを含む入力シーケンスからの情報を処理・保持する能力。"
---

## Definition

ロングコンテキストとは、トランスフォーマーベースのモデルが標準的な制限（2kや4kトークンなど）を超えて広範な入力長を扱える能力を指します。この機能により、モデルは完全な文書全体を分析することが可能になります。

### Summary

言語モデルが、数千〜数百万トークンを含む入力シーケンスからの情報を処理・保持する能力。

## Key Concepts

- コンテキストウィンドウ
- トークン制限
- アテンション機構
- 位置エンコーディング

## Use Cases

- 法的契約書全文の要約
- 完全なソースコードリポジトリの分析
- 長時間の音声トランスクリプトの処理

## Related Terms

- [Context Window (コンテキストウィンドウ)](/en/terms/context-window-コンテキストウィンドウ/)
- [Transformer Architecture (トランスフォーマーアーキテクチャ)](/en/terms/transformer-architecture-トランスフォーマーアーキテクチャ/)
- [RoPE (Rotary Positional Embeddings)](/en/terms/rope-rotary-positional-embeddings/)
- [KV Cache (KVキャッシュ)](/en/terms/kv-cache-kvキャッシュ/)
