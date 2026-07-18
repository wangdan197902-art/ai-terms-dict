---
title: "Tokenization"
term_id: "tokenization"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "preprocessing"]
difficulty: 3
weight: 1
slug: "tokenization"
aliases:
  - /en/terms/tokenization/
date: "2026-07-18T09:37:37.819988Z"
lastmod: "2026-07-18T11:44:44.611651Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Tokenization is the process of splitting raw text into smaller units called tokens, which can be processed by machine learning algorithms."
---

## Definition

Tokenization is a critical preprocessing step in Natural Language Processing (NLP) that converts unstructured text into structured data suitable for model ingestion. It involves breaking down sentences into words, subwords, or characters based on specific rules or learned patterns. Different tokenizers (e.g., WordPiece, Byte-Pair Encoding) handle edge cases like punctuation and rare words differently. Effective tokenization ensures that the model can accurately capture linguistic features while managing computational constraints related to sequence length.

### Summary

Tokenization is the process of splitting raw text into smaller units called tokens, which can be processed by machine learning algorithms.

## Key Concepts

- Text Splitting
- Preprocessing
- WordPiece
- Byte-Pair Encoding

## Use Cases

- Preparing datasets for BERT training
- Input formatting for GPT models
- Data cleaning for sentiment analysis

## Code Example

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('Hello world!')
```

## Related Terms

- [Tokenizer](/en/terms/tokenizer/)
- [Vocabulary](/en/terms/vocabulary/)
- [Embedding](/en/terms/embedding/)
- [Preprocessing](/en/terms/preprocessing/)
