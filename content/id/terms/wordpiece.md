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
  - /id/terms/wordpiece/
date: "2026-07-18T16:13:33.331381Z"
lastmod: "2026-07-18T16:38:07.520148Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Algoritma tokenisasi subkata yang secara rekursif menggabungkan pasangan karakter paling sering muncul untuk menangani kata di luar kosakata."
---

## Definition

WordPiece adalah metode tokenisasi yang banyak digunakan dalam model pemrosesan bahasa alami seperti BERT dan ALBERT. Metode ini memecah kata menjadi unit subkata yang lebih kecil untuk mengelola kekayaan morfologis bahasa dan mengurangi ukuran kosakata. Dengan menggabungkan pasangan karakter yang paling sering muncul secara iteratif, WordPiece memungkinkan model menangani kata-kata yang jarang muncul atau tidak dikenal dengan efektif.

### Summary

Algoritma tokenisasi subkata yang secara rekursif menggabungkan pasangan karakter paling sering muncul untuk menangani kata di luar kosakata.

## Key Concepts

- Tokenisasi subkata
- Ekspansi kosakata
- Penanganan out-of-vocabulary
- Analisis morfologis

## Use Cases

- Pra-pemrosesan teks untuk model BERT
- Menangani bahasa dengan sumber daya terbatas
- Mengurangi ukuran matriks embedding

## Code Example

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('unhappiness')
print(tokens)
```

## Related Terms

- [Byte-Pair Encoding (Algoritma tokenisasi serupa berbasis byte)](/en/terms/byte-pair-encoding-algoritma-tokenisasi-serupa-berbasis-byte/)
- [SentencePiece (Kerangka kerja tokenisasi bahasa independen)](/en/terms/sentencepiece-kerangka-kerja-tokenisasi-bahasa-independen/)
- [Tokenisasi (Proses memecah teks menjadi unit-unit)](/en/terms/tokenisasi-proses-memecah-teks-menjadi-unit-unit/)
- [Pra-pemrosesan NLP (Langkah persiapan data untuk pemrosesan bahasa alami)](/en/terms/pra-pemrosesan-nlp-langkah-persiapan-data-untuk-pemrosesan-bahasa-alami/)
