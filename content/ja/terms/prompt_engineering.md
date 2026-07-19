---
title: "プロンプトエンジニアリング"
term_id: "prompt_engineering"
category: "application_paradigms"
subcategory: ""
tags: ["LLM", "UX", "Optimization"]
difficulty: 2
weight: 1
slug: "prompt_engineering"
date: "2026-07-18T07:41:35.330929Z"
lastmod: "2026-07-18T11:44:44.584983Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "大規模言語モデル（LLM）が望ましい出力を行うよう、入力テキストの設計と最適化を行う実践。"
---
## Definition

プロンプトエンジニアリングとは、生成AIモデルから正確で関連性が高く、高品質な回答を引き出すために、「プロンプト」と呼ばれる特定の入力を構築するプロセスです。これには、モデルが指示をどのように解釈し、処理するかを理解することが不可欠です。

### Summary

大規模言語モデル（LLM）が望ましい出力を行うよう、入力テキストの設計と最適化を行う実践。

## Key Concepts

- 文脈の枠組み設定
- ファインショット学習
- インストラクションチューニング
- トークン最適化

## Use Cases

- 自動化されたカスタマーサポートチャットボット
- コード生成アシスタント
- クリエイティブライティング支援ツール

## Code Example

```python
prompt = "Translate the following English text to French: 'Hello world'"
response = llm.generate(prompt)
```

## Related Terms

- [LLM (大規模言語モデル)](/en/terms/llm-大規模言語モデル/)
- [Chain-of-Thought (思考の連鎖)](/en/terms/chain-of-thought-思考の連鎖/)
- [RAG (検索拡張生成)](/en/terms/rag-検索拡張生成/)
- [Fine-tuning (ファインチューニング)](/en/terms/fine-tuning-ファインチューニング/)
