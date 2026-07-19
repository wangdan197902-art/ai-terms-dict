---
title: "Sentence Transformers"
term_id: "sentence_transformers"
category: "training_techniques"
subcategory: ""
tags: ["Deep Learning", "NLP", "Architectures"]
difficulty: 3
weight: 1
slug: "sentence_transformers"
date: "2026-07-18T10:15:05.739060Z"
lastmod: "2026-07-18T11:44:44.720389Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Neural network architectures specifically designed to generate fixed-size vector embeddings for arbitrary text sentences."
---
## Definition

Sentence Transformers are extensions of traditional Transformer models (like BERT) fine-tuned to produce meaningful dense vector representations for entire sentences. Unlike standard token-level models, these architectures pool token embeddings to create a single sentence embedding that captures holistic semantic meaning. They are optimized using contrastive learning objectives to ensure that semantically similar sentences have vectors that are close together in the embedding space. This makes them highly effective for downstream tasks requiring semantic comparison.

### Summary

Neural network architectures specifically designed to generate fixed-size vector embeddings for arbitrary text sentences.

## Key Concepts

- Pooling layers
- Contrastive learning
- Dense embeddings
- Transformer architecture

## Use Cases

- Semantic search engines
- Clustering textual data
- Retrieval-Augmented Generation (RAG) pipelines

## Related Terms

- [BERT](/en/terms/bert/)
- [Embeddings](/en/terms/embeddings/)
- [Sentence Similarity](/en/terms/sentence-similarity/)
- [Contrastive Loss](/en/terms/contrastive-loss/)
