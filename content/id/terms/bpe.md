---
title: "BPE"
term_id: "bpe"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "Tokenization", "Data Preprocessing"]
difficulty: 3
weight: 1
slug: "bpe"
aliases:
  - /id/terms/bpe/
date: "2026-07-18T15:33:49.614380Z"
lastmod: "2026-07-18T16:38:07.411623Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Byte Pair Encoding adalah algoritma yang digunakan untuk tokenisasi subkata yang secara iteratif menggabungkan pasangan karakter paling sering muncul untuk membangun kosakata."
---

## Definition

Byte Pair Encoding (BPE) adalah teknik kompresi data yang diadaptasi untuk pemrosesan bahasa alami guna menangani kata-kata di luar kosakata (out-of-vocabulary). Algoritma ini dimulai dengan kosakata individu berupa karakter dan secara iteratif

### Summary

Byte Pair Encoding adalah algoritma yang digunakan untuk tokenisasi subkata yang secara iteratif menggabungkan pasangan karakter paling sering muncul untuk membangun kosakata.

## Key Concepts

- Tokenisasi Subkata
- Penggabungan Kosakata
- Analisis Frekuensi
- Penanganan Kata di Luar Kosakata

## Use Cases

- Pra-pemrosesan teks untuk Model Bahasa Besar
- Menangani bahasa yang kaya akan morfologi
- Mengurangi ukuran kosakata dalam jaringan saraf

## Code Example

```python
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("unhappiness")
print(tokens)
```

## Related Terms

- [WordPiece (Metode tokenisasi serupa)](/en/terms/wordpiece-metode-tokenisasi-serupa/)
- [SentencePiece (Kerangka kerja tokenisasi tanpa spasi)](/en/terms/sentencepiece-kerangka-kerja-tokenisasi-tanpa-spasi/)
- [Tokenization (Proses memecah teks menjadi unit-unit)](/en/terms/tokenization-proses-memecah-teks-menjadi-unit-unit/)
- [Subword Units (Unit bahasa yang lebih kecil dari kata)](/en/terms/subword-units-unit-bahasa-yang-lebih-kecil-dari-kata/)
