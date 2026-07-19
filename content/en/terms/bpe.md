---
title: "BPE"
term_id: "bpe"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "Tokenization", "Data Preprocessing"]
difficulty: 3
weight: 1
slug: "bpe"
date: "2026-07-18T09:40:12.570963Z"
lastmod: "2026-07-18T11:44:44.620950Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Byte Pair Encoding is an algorithm used for subword tokenization that iteratively merges the most frequent character pairs to build a vocabulary."
---
## Definition

Byte Pair Encoding (BPE) is a data compression technique adapted for natural language processing to handle out-of-vocabulary words. It starts with a vocabulary of individual characters and iteratively merges the most frequent adjacent pairs of symbols. This process creates a hierarchy of subword units, allowing models to balance between character-level flexibility and word-level efficiency. It is widely used in transformer-based models like GPT-2 and BERT to manage vocabulary size while preserving semantic meaning across diverse languages.

### Summary

Byte Pair Encoding is an algorithm used for subword tokenization that iteratively merges the most frequent character pairs to build a vocabulary.

## Key Concepts

- Subword Tokenization
- Vocabulary Merging
- Frequency Analysis
- Out-of-Vocabulary Handling

## Use Cases

- Preprocessing text for Large Language Models
- Handling morphologically rich languages
- Reducing vocabulary size in neural networks

## Code Example

```python
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("unhappiness")
print(tokens)
```

## Related Terms

- [WordPiece](/en/terms/wordpiece/)
- [SentencePiece](/en/terms/sentencepiece/)
- [Tokenization](/en/terms/tokenization/)
- [Subword Units](/en/terms/subword-units/)
