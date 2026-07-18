---
title: "PagedAttention"
term_id: "pagedattention"
category: "training_techniques"
subcategory: ""
tags: ["inference", "optimization", "memory_management"]
difficulty: 4
weight: 1
slug: "pagedattention"
aliases:
  - /vi/terms/pagedattention/
date: "2026-07-18T16:06:41.807858Z"
lastmod: "2026-07-18T16:38:07.790898Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "PagedAttention là một thuật toán quản lý bộ nhớ, áp dụng khái niệm phân trang bộ nhớ ảo để tối ưu hóa việc lưu trữ và truy cập bộ nhớ đệm Key-Value (KV) trong các mô hình Transformer."
---

## Definition

PagedAttention là một kỹ thuật được giới thiệu bởi dự án vLLM nhằm cải thiện hiệu suất suy luận của các Mô hình Ngôn ngữ Lớn (LLM). Nó giải quyết các vấn đề về phân mảnh và chi phí xử lý khi quản lý bộ nhớ đệm KV, vốn...

### Summary

PagedAttention là một thuật toán quản lý bộ nhớ, áp dụng khái niệm phân trang bộ nhớ ảo để tối ưu hóa việc lưu trữ và truy cập bộ nhớ đệm Key-Value (KV) trong các mô hình Transformer.

## Key Concepts

- Quản lý KV Cache (Bộ nhớ đệm Key-Value)
- Phân mảnh bộ nhớ (Memory Fragmentation)
- Tối ưu hóa suy luận (Inference Optimization)
- Phân trang bộ nhớ ảo (Virtual Memory Paging)

## Use Cases

- Phục vụ LLM thông lượng cao
- Giảm thiểu việc sử dụng bộ nhớ GPU
- Tối ưu hóa xử lý theo lô trong môi trường sản xuất

## Related Terms

- [vLLM (Thư viện suy luận LLM)](/en/terms/vllm-thư-viện-suy-luận-llm/)
- [Key-Value Cache (Bộ nhớ đệm Key-Value)](/en/terms/key-value-cache-bộ-nhớ-đệm-key-value/)
- [Transformer Architecture (Kiến trúc Transformer)](/en/terms/transformer-architecture-kiến-trúc-transformer/)
- [GPU Memory Optimization (Tối ưu hóa bộ nhớ GPU)](/en/terms/gpu-memory-optimization-tối-ưu-hóa-bộ-nhớ-gpu/)
