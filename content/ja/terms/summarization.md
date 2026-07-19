---
title: 要約
term_id: summarization
category: application_paradigms
subcategory: ''
tags:
- NLP
- Text Processing
- applications
difficulty: 3
weight: 1
slug: summarization
date: '2026-07-18T11:01:15.727400Z'
lastmod: '2026-07-18T11:44:45.058119Z'
draft: false
source: agnes_llm
status: published
language: ja
description: 元のテキストの重要な情報を保持しつつ、より短く一貫性のある要約文を生成する自然言語処理（NLP）タスク。
---
## Definition

テキスト要約は、重要な意味を失うことなく、大量のテキストを短いバージョンに圧縮します。抽出型要約ではソースから重要な文を選択し、生成型要約では新しい文章を生成します。

### Summary

元のテキストの重要な情報を保持しつつ、より短く一貫性のある要約文を生成する自然言語処理（NLP）タスク。

## Key Concepts

- 抽出型要約
- 生成型要約
- 情報密度
- 一貫性

## Use Cases

- ニュース記事の要約
- 会議議事録の生成
- 法律文書のレビュー支援

## Code Example

```python
from transformers import pipeline
summarizer = pipeline("summarization")
result = summarizer("AI is transforming industries...", max_length=50, min_length=10)[0]['summary_text']
```

## Related Terms

- [NLP (自然言語処理)](/en/terms/nlp-自然言語処理/)
- [Transformer Models (トランスフォーマーモデル)](/en/terms/transformer-models-トランスフォーマーモデル/)
- [BERT (双方向エンコーダー表現)](/en/terms/bert-双方向エンコーダー表現/)
- [T5 (テキスト-to-text変換フレームワーク)](/en/terms/t5-テキスト-to-text変換フレームワーク/)
