---
title: PagedAttention
term_id: pagedattention
category: training_techniques
subcategory: ''
tags:
- inference
- Optimization
- Memory Management
difficulty: 4
weight: 1
slug: pagedattention
date: '2026-07-18T10:10:06.387829Z'
lastmod: '2026-07-18T11:44:44.707489Z'
draft: false
source: agnes_llm
status: published
language: en
description: PagedAttention is a memory management algorithm that adapts virtual memory
  paging concepts to optimize the storage and access of Key-Value (KV) caches in transformer
  models.
---
## Definition

PagedAttention is a technique introduced by the vLLM project to improve the efficiency of Large Language Model inference. It addresses the fragmentation and overhead issues in managing the KV cache, which stores attention states for generating tokens. By treating the KV cache like virtual memory pages, PagedAttention allows for dynamic allocation and sharing of memory blocks between sequences. This results in significant reductions in memory waste and enables higher batch sizes and throughput without requiring hardware changes.

### Summary

PagedAttention is a memory management algorithm that adapts virtual memory paging concepts to optimize the storage and access of Key-Value (KV) caches in transformer models.

## Key Concepts

- KV Cache Management
- Memory Fragmentation
- Inference Optimization
- Virtual Memory Paging

## Use Cases

- High-throughput LLM serving
- Reducing GPU memory usage
- Optimizing batch processing in production

## Related Terms

- [vLLM](/en/terms/vllm/)
- [Key-Value Cache](/en/terms/key-value-cache/)
- [Transformer Architecture](/en/terms/transformer-architecture/)
- [GPU Memory Optimization](/en/terms/gpu-memory-optimization/)
