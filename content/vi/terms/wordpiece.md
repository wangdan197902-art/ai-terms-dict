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
  - /vi/terms/wordpiece/
date: "2026-07-18T16:17:41.977210Z"
lastmod: "2026-07-18T16:38:07.817780Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Thuật toán phân đoạn từ con (subword tokenization) ghép nối đệ quy các cặp ký tự phổ biến nhất để xử lý các từ nằm ngoài từ vựng."
---

## Definition

WordPiece là một phương pháp phân đoạn từ được sử dụng rộng rãi trong các mô hình xử lý ngôn ngữ tự nhiên như BERT và ALBERT. Nó chia nhỏ các từ thành các đơn vị từ con nhỏ hơn để quản lý sự phong phú về hình thái học và giảm kích thước từ vựng.

### Summary

Thuật toán phân đoạn từ con (subword tokenization) ghép nối đệ quy các cặp ký tự phổ biến nhất để xử lý các từ nằm ngoài từ vựng.

## Key Concepts

- Phân đoạn từ con
- Mở rộng từ vựng
- Xử lý từ ngoài từ vựng (OOV)
- Phân tích hình thái học

## Use Cases

- Tiền xử lý văn bản cho mô hình BERT
- Xử lý các ngôn ngữ ít tài nguyên
- Giảm kích thước ma trận nhúng (embedding)

## Code Example

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('unhappiness')
print(tokens)
```

## Related Terms

- [Byte-Pair Encoding (Mã hóa cặp byte)](/en/terms/byte-pair-encoding-mã-hóa-cặp-byte/)
- [SentencePiece (Phân đoạn câu)](/en/terms/sentencepiece-phân-đoạn-câu/)
- [Tokenization (Phân đoạn token)](/en/terms/tokenization-phân-đoạn-token/)
- [NLP preprocessing (Tiền xử lý NLP)](/en/terms/nlp-preprocessing-tiền-xử-lý-nlp/)
