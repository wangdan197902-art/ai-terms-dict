---
title: "Tokenisasi"
term_id: "tokenization"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "preprocessing"]
difficulty: 3
weight: 1
slug: "tokenization"
aliases:
  - /id/terms/tokenization/
date: "2026-07-18T15:30:15.952174Z"
lastmod: "2026-07-18T16:38:07.404936Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Tokenisasi adalah proses memecah teks mentah menjadi unit-unit lebih kecil yang disebut token, yang dapat diproses oleh algoritma pembelajaran mesin."
---

## Definition

Tokenisasi adalah langkah pra-pemrosesan kritis dalam Pemrosesan Bahasa Alami (NLP) yang mengubah teks tidak terstruktur menjadi data terstruktur yang cocok untuk dimakan oleh model. Proses ini melibatkan pemecahan kalimat atau dokumen menjadi bagian-bagian kecil seperti kata atau subkata, seringkali menggunakan teknik seperti WordPiece atau Byte-Pair Encoding.

### Summary

Tokenisasi adalah proses memecah teks mentah menjadi unit-unit lebih kecil yang disebut token, yang dapat diproses oleh algoritma pembelajaran mesin.

## Key Concepts

- Pemisahan Teks
- Pra-pemrosesan
- WordPiece
- Byte-Pair Encoding

## Use Cases

- Menyiapkan dataset untuk pelatihan BERT
- Format input untuk model GPT
- Pembersihan data untuk analisis sentimen

## Code Example

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('Hello world!')
```

## Related Terms

- [Tokenizer (Tokeniser)](/en/terms/tokenizer-tokeniser/)
- [Vocabulary (Kosakata)](/en/terms/vocabulary-kosakata/)
- [Embedding (Embedding)](/en/terms/embedding-embedding/)
- [Preprocessing (Pra-pemrosesan)](/en/terms/preprocessing-pra-pemrosesan/)
