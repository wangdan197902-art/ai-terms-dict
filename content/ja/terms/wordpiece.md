---
title: "WordPiece"
term_id: "wordpiece"
category: "engineering_practice"
subcategory: ""
tags: ["nlp", "tokenization", "bert"]
difficulty: 3
weight: 1
slug: "wordpiece"
aliases:
  - /ja/terms/wordpiece/
date: "2026-07-18T11:36:41.190722Z"
lastmod: "2026-07-18T11:44:45.155887Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "未登録語（OOV）を処理するため、最も頻繁な文字ペアを再帰的に結合するサブワードトークン化アルゴリズム。"
---

## Definition

WordPieceは、BERTやALBERTなどの自然言語処理モデルで広く使用されているトークン化手法です。形態的な豊かさを扱い、語彙サイズを削減するために、単語をより小さなサブワード単位に分解します。

### Summary

未登録語（OOV）を処理するため、最も頻繁な文字ペアを再帰的に結合するサブワードトークン化アルゴリズム。

## Key Concepts

- サブワードトークン化
- 語彙拡張
- 未登録語（OOV）処理
- 形態素解析

## Use Cases

- BERTモデル向けのテキスト前処理
- 低資源言語の処理
- 埋め込み行列サイズの削減

## Code Example

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('unhappiness')
print(tokens)
```

## Related Terms

- [バイトペアエンコーディング](/en/terms/バイトペアエンコーディング/)
- [SentencePiece](/en/terms/sentencepiece/)
- [トークン化](/en/terms/トークン化/)
- [NLP前処理](/en/terms/nlp前処理/)
