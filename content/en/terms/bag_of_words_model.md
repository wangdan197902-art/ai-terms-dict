---
title: Bag-of-words model
term_id: bag_of_words_model
category: basic_concepts
subcategory: ''
tags:
- NLP
- Text Processing
- Feature Engineering
difficulty: 2
weight: 1
slug: bag_of_words_model
date: '2026-07-18T09:47:37.691850Z'
lastmod: '2026-07-18T11:44:44.646029Z'
draft: false
source: agnes_llm
status: published
language: en
description: The bag-of-words model is a simplifying representation of text that describes
  document occurrence of words, ignoring grammar and word order.
---
## Definition

This natural language processing technique represents text as a multiset of words, disregarding syntax and sequence. It converts documents into numerical vectors based on word frequency or presence. While it loses contextual information like word order, it remains computationally efficient and effective for tasks such as text classification, spam detection, and topic modeling. It serves as a foundational feature extraction method before more advanced embeddings like Word2Vec became prevalent.

### Summary

The bag-of-words model is a simplifying representation of text that describes document occurrence of words, ignoring grammar and word order.

## Key Concepts

- Tokenization
- Frequency counting
- Vector space
- Feature extraction

## Use Cases

- Text classification
- Spam filtering
- Information retrieval

## Code Example

```python
from sklearn.feature_extraction.text import CountVectorizer
corpus = ["Hello world", "World hello"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
```

## Related Terms

- [TF-IDF](/en/terms/tf-idf/)
- [N-grams](/en/terms/n-grams/)
- [Word Embeddings](/en/terms/word-embeddings/)
