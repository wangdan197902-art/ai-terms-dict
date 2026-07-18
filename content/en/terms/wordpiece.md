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
  - /en/terms/wordpiece/
date: "2026-07-18T10:20:04.565036Z"
lastmod: "2026-07-18T11:44:44.733604Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A subword tokenization algorithm that recursively merges the most frequent character pairs to handle out-of-vocabulary words."
---

## Definition

WordPiece is a tokenization method widely used in natural language processing models like BERT and ALBERT. It breaks down words into smaller subword units to manage morphological richness and reduce vocabulary size. The algorithm starts with a base vocabulary and iteratively adds the most frequent character pairs until a target size is reached. This allows the model to represent rare or unseen words by combining known subwords, improving generalization and handling of linguistic variations effectively.

### Summary

A subword tokenization algorithm that recursively merges the most frequent character pairs to handle out-of-vocabulary words.

## Key Concepts

- Subword tokenization
- Vocabulary expansion
- Out-of-vocabulary handling
- Morphological analysis

## Use Cases

- Preprocessing text for BERT models
- Handling low-resource languages
- Reducing embedding matrix size

## Code Example

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('unhappiness')
print(tokens)
```

## Related Terms

- [Byte-Pair Encoding](/en/terms/byte-pair-encoding/)
- [SentencePiece](/en/terms/sentencepiece/)
- [Tokenization](/en/terms/tokenization/)
- [NLP preprocessing](/en/terms/nlp-preprocessing/)
