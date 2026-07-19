---
title: "Embedding Model"
term_id: "embedding_model"
category: "application_paradigms"
subcategory: ""
tags: ["NLP", "Representation Learning", "Search"]
difficulty: 4
weight: 1
slug: "embedding_model"
date: "2026-07-18T09:40:59.277024Z"
lastmod: "2026-07-18T11:44:44.624145Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "An embedding model converts raw data like text or images into dense numerical vectors representing semantic meaning."
---
## Definition

These models map high-dimensional data into a lower-dimensional continuous vector space where similar items are located closer together. This transformation captures semantic relationships, allowing algorithms to perform tasks like similarity search, clustering, and recommendation based on vector distance. Embeddings are fundamental to modern NLP and computer vision applications, enabling machines to understand context and nuance beyond simple keyword matching.

### Summary

An embedding model converts raw data like text or images into dense numerical vectors representing semantic meaning.

## Key Concepts

- Vector Representation
- Semantic Similarity
- Dimensionality Reduction
- Feature Extraction

## Use Cases

- Building semantic search engines
- Recommendation systems for products or content
- Clustering similar documents or images

## Code Example

```python
from transformers import AutoTokenizer, AutoModel
import torch

model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
inputs = tokenizer('Hello world', return_tensors='pt')
embeddings = model(**inputs).last_hidden_state.mean(dim=1)
```

## Related Terms

- [Word2Vec](/en/terms/word2vec/)
- [BERT](/en/terms/bert/)
- [Vector Database](/en/terms/vector-database/)
- [Similarity Search](/en/terms/similarity-search/)
