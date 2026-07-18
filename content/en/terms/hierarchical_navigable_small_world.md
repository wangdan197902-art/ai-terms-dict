---
title: "Hierarchical navigable small world"
term_id: "hierarchical_navigable_small_world"
category: "basic_concepts"
subcategory: ""
tags: ["algorithms", "search", "data_structures"]
difficulty: 4
weight: 1
slug: "hierarchical_navigable_small_world"
aliases:
  - /en/terms/hierarchical_navigable_small_world/
date: "2026-07-18T10:01:08.569136Z"
lastmod: "2026-07-18T11:44:44.681362Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A graph-based data structure enabling efficient approximate nearest neighbor search in high-dimensional spaces."
---

## Definition

The Hierarchical Navigable Small World (HNSW) algorithm constructs a multi-layered graph where each layer contains a subset of nodes from the layer below. Navigation starts at the top layer, moving closer to the target node before descending to finer layers. This structure allows for logarithmic time complexity in search operations, making it highly effective for large-scale vector databases and similarity searches in machine learning applications like recommendation systems and image retrieval.

### Summary

A graph-based data structure enabling efficient approximate nearest neighbor search in high-dimensional spaces.

## Key Concepts

- Graph Search
- Approximate Nearest Neighbor
- Multi-layer Graph
- Logarithmic Complexity

## Use Cases

- Vector search
- Recommendation engines
- Image retrieval

## Related Terms

- [K-Nearest Neighbors](/en/terms/k-nearest-neighbors/)
- [Faiss](/en/terms/faiss/)
- [Annoy](/en/terms/annoy/)
