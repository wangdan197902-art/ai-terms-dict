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
  - /id/terms/pagedattention/
date: "2026-07-18T16:03:09.620760Z"
lastmod: "2026-07-18T16:38:07.491969Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "PagedAttention adalah algoritma manajemen memori yang mengadaptasi konsep paging memori virtual untuk mengoptimalkan penyimpanan dan akses cache Key-Value (KV) dalam model transformer."
---

## Definition

PagedAttention adalah teknik yang diperkenalkan oleh proyek vLLM untuk meningkatkan efisiensi inferensi Model Bahasa Besar. Teknik ini mengatasi masalah fragmentasi dan overhead dalam mengelola cache KV, w

### Summary

PagedAttention adalah algoritma manajemen memori yang mengadaptasi konsep paging memori virtual untuk mengoptimalkan penyimpanan dan akses cache Key-Value (KV) dalam model transformer.

## Key Concepts

- Manajemen Cache KV
- Fragmentasi Memori
- Optimasi Inferensi
- Paging Memori Virtual

## Use Cases

- Penyajian LLM ber throughput tinggi
- Mengurangi penggunaan memori GPU
- Mengoptimalkan pemrosesan batch dalam produksi

## Related Terms

- [vLLM](/en/terms/vllm/)
- [Cache Key-Value](/en/terms/cache-key-value/)
- [Arsitektur Transformer](/en/terms/arsitektur-transformer/)
- [Optimasi Memori GPU](/en/terms/optimasi-memori-gpu/)
