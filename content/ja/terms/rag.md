---
title: "Retrieval-Augmented Generation（検索拡張生成）"
term_id: "rag"
category: "application_paradigms"
subcategory: ""
tags: ["architecture", "knowledge_management"]
difficulty: 4
weight: 1
slug: "rag"
aliases:
  - /ja/terms/rag/
date: "2026-07-18T10:54:19.510658Z"
lastmod: "2026-07-18T11:44:45.017721Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "RAGは、応答を生成する前に外部の知識ベースから関連情報を取得することで、生成モデルの能力を強化するAIフレームワークです。"
---

## Definition

検索拡張生成（RAG）は、検索ベースのAIシステムと生成ベースのAIシステムの強みを組み合わせたものです。事前学習された言語モデルのパラメータのみ頼るのではなく、RAGはまずクエリに関連する外部ドキュメントを検索し、それらの情報をコンテキストとしてモデルに入力します。これにより、モデルの知識の鮮度向上、ハルシネーション（幻覚）の削減、および根拠のある回答の生成が可能になります。

### Summary

RAGは、応答を生成する前に外部の知識ベースから関連情報を取得することで、生成モデルの能力を強化するAIフレームワークです。

## Key Concepts

- ベクトルデータベース
- 埋め込み（Embeddings）
- コンテキストウィンドウ
- セマンティック検索

## Use Cases

- エンタープライズナレッジベース
- カスタマーサポートボット
- 研究アシスタント

## Related Terms

- [Vector Search（ベクトル検索）](/en/terms/vector-search-ベクトル検索/)
- [Knowledge Graph（知識グラフ）](/en/terms/knowledge-graph-知識グラフ/)
- [LLM（大規模言語モデル）](/en/terms/llm-大規模言語モデル/)
