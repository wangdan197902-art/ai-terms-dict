---
title: "Reranking"
term_id: "reranking"
category: "application_paradigms"
subcategory: ""
tags: ["search", "recommendations", "architecture"]
difficulty: 2
weight: 1
slug: "reranking"
aliases:
  - /en/terms/reranking/
date: "2026-07-18T10:14:07.773956Z"
lastmod: "2026-07-18T11:44:44.717540Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A two-stage retrieval process where an initial coarse ranking is refined by a more computationally expensive model to improve result relevance."
---

## Definition

Reranking is a strategy used in information retrieval and recommendation systems to enhance accuracy. First, a fast but less accurate model retrieves a large candidate set. Then, a slower, more sophisticated model (often using cross-attention or deep interaction) scores these candidates precisely. This balances efficiency and performance, ensuring high-quality results are presented to users without excessive computational cost during the initial search phase.

### Summary

A two-stage retrieval process where an initial coarse ranking is refined by a more computationally expensive model to improve result relevance.

## Key Concepts

- Two-Tier Retrieval
- Candidate Generation
- Cross-Attention
- Precision Optimization

## Use Cases

- Search Engines
- Recommendation Systems
- Retrieval-Augmented Generation (RAG)

## Related Terms

- [Vector Search](/en/terms/vector-search/)
- [BM25](/en/terms/bm25/)
- [Cross-Encoder](/en/terms/cross-encoder/)
- [Information Retrieval](/en/terms/information-retrieval/)
