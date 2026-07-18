---
title: "Tokenizasyon"
term_id: "tokenization"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "preprocessing"]
difficulty: 3
weight: 1
slug: "tokenization"
aliases:
  - /tr/terms/tokenization/
date: "2026-07-18T15:30:21.481363Z"
lastmod: "2026-07-18T16:38:07.246053Z"
draft: false
source: "agnes_llm"
status: "published"
language: "tr"
description: "Tokenizasyon, ham metin makine öğrenmesi algoritmaları tarafından işlenebilen 'token' adı verilen daha küçük birimlere bölünmesi işlemidir."
---

## Definition

Tokenizasyon, Yapay Doğal Dil İşleme'de (NLP) kritik bir ön işleme adımıdır ve yapılandırılmamış metni model tarafından tüketilebilir yapılandırılmış verilere dönüştürür. Cümleleri kelimelere, alt-kelimelere veya karakterlere ayırma sürecini içerir.

### Summary

Tokenizasyon, ham metin makine öğrenmesi algoritmaları tarafından işlenebilen 'token' adı verilen daha küçük birimlere bölünmesi işlemidir.

## Key Concepts

- Metin Bölme
- Ön İşleme
- WordPiece
- Byte-Pair Encoding (Bayt-Çifti Kodlama)

## Use Cases

- BERT eğitimi için veri setlerini hazırlama
- GPT modelleri için girdi formatlama
- Duygu analizi için veri temizleme

## Code Example

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('Hello world!')
```

## Related Terms

- [Tokenizer (Tokenizör)](/en/terms/tokenizer-tokenizör/)
- [Vocabulary (Sözlük)](/en/terms/vocabulary-sözlük/)
- [Embedding (Gömme)](/en/terms/embedding-gömme/)
- [Preprocessing (Ön İşleme)](/en/terms/preprocessing-ön-i-şleme/)
