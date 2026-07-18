---
title: "GGUF"
term_id: "gguf"
category: "basic_concepts"
subcategory: ""
tags: ["format", "optimization", "local_llm"]
difficulty: 3
weight: 1
slug: "gguf"
aliases:
  - /id/terms/gguf/
date: "2026-07-18T15:51:26.470458Z"
lastmod: "2026-07-18T16:38:07.460016Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Format file yang dikembangkan olehgger.ai untuk menyimpan dan memuat model bahasa besar yang telah dikuantisasi secara efisien pada perangkat keras lokal."
---

## Definition

GGUF (GPT-Generated Unified Format) adalah format file biner yang dirancang khusus untuk menjalankan model bahasa besar pada perangkat keras konsumen. Format ini mendukung berbagai teknik kuantisasi, memungkinkan model yang lebih kecil dan cepat untuk dijalankan pada laptop atau PC tanpa memerlukan GPU kelas server yang mahal.

### Summary

Format file yang dikembangkan olehgger.ai untuk menyimpan dan memuat model bahasa besar yang telah dikuantisasi secara efisien pada perangkat keras lokal.

## Key Concepts

- Kuantisasi
- Serialisasi Model
- Inferensi Lokal
- Optimasi Memori

## Use Cases

- Menjalankan LLM secara lokal di laptop atau desktop
- Menyebarkan model di perangkat tepi dengan sumber daya terbatas
- Berbagi bobot model yang dioptimalkan dalam komunitas sumber terbuka

## Related Terms

- [LLAMA.cpp (Pustaka inferensi C++)](/en/terms/llama-cpp-pustaka-inferensi-c/)
- [Quantization (Kuantisasi)](/en/terms/quantization-kuantisasi/)
- [ONNX (Format pertukaran model)](/en/terms/onnx-format-pertukaran-model/)
- [Model Weights (Bobot model)](/en/terms/model-weights-bobot-model/)
