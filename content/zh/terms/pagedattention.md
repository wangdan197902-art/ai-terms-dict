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
date: '2026-07-18T11:29:14.184562Z'
lastmod: '2026-07-18T11:44:45.540405Z'
draft: false
source: agnes_llm
status: published
language: zh
description: PagedAttention 是一种内存管理算法，它将虚拟内存分页概念应用于优化 Transformer 模型中键值（KV）缓存的存储和访问。
---
## Definition

PagedAttention 是由 vLLM 项目引入的一项技术，旨在提高大语言模型推理的效率。它解决了管理 KV 缓存时的碎片化和开销问题，通过将 KV 缓存视为非连续的内存块进行分配和管理，从而显著减少了内存浪费，提高了吞吐量并降低了显存占用。

### Summary

PagedAttention 是一种内存管理算法，它将虚拟内存分页概念应用于优化 Transformer 模型中键值（KV）缓存的存储和访问。

## Key Concepts

- KV 缓存管理
- 内存碎片化
- 推理优化
- 虚拟内存分页

## Use Cases

- 高吞吐量大语言模型服务
- 减少 GPU 内存使用
- 生产环境中的批处理优化

## Related Terms

- [vLLM (高性能LLM推理引擎)](/en/terms/vllm-高性能llm推理引擎/)
- [Key-Value Cache (键值缓存)](/en/terms/key-value-cache-键值缓存/)
- [Transformer Architecture (Transformer架构)](/en/terms/transformer-architecture-transformer架构/)
- [GPU Memory Optimization (GPU内存优化)](/en/terms/gpu-memory-optimization-gpu内存优化/)
