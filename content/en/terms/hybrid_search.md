---
title: Hybrid Search
term_id: hybrid_search
category: application_paradigms
subcategory: ''
tags:
- retrieval
- Search Engine
- rag
difficulty: 3
weight: 1
slug: hybrid_search
date: '2026-07-18T10:01:39.627636Z'
lastmod: '2026-07-18T11:44:44.682528Z'
draft: false
source: agnes_llm
status: published
language: en
description: A retrieval strategy that combines semantic vector search with traditional
  keyword-based indexing to improve accuracy and relevance.
---
## Definition

Hybrid Search integrates two distinct retrieval methods: dense vector search, which captures semantic meaning and context, and sparse vector (keyword) search, which matches exact terms. By leveraging the strengths of both approaches, it mitigates the limitations of relying on a single method, such as missing synonyms in keyword search or lacking precision in pure semantic search. This approach is widely used in modern enterprise search engines and RAG applications to deliver highly relevant results across diverse query types.

### Summary

A retrieval strategy that combines semantic vector search with traditional keyword-based indexing to improve accuracy and relevance.

## Key Concepts

- Vector Search
- Keyword Matching
- Reranking
- Reciprocal Rank Fusion

## Use Cases

- Enterprise document retrieval
- E-commerce product search
- Advanced RAG pipelines

## Related Terms

- [semantic_search](/en/terms/semantic_search/)
- [sparse_vectors](/en/terms/sparse_vectors/)
- [dense_vectors](/en/terms/dense_vectors/)
- [vector_database](/en/terms/vector_database/)
