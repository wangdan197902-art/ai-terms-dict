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
  - /en/terms/gguf/
date: "2026-07-18T09:58:48.559162Z"
lastmod: "2026-07-18T11:44:44.674861Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A file format developed bygger.ai for storing and loading quantized large language models efficiently on local hardware."
---

## Definition

GGUF (GPT-Generated Unified Format) is a binary file format designed specifically for running large language models on consumer-grade hardware. It supports various quantization techniques, allowing models to be compressed significantly without substantial loss in performance. This format enables efficient inference on CPUs and GPUs by optimizing memory usage and data layout, making it a standard for open-source AI deployment tools like llama.cpp and Ollama, facilitating accessible AI experimentation.

### Summary

A file format developed bygger.ai for storing and loading quantized large language models efficiently on local hardware.

## Key Concepts

- Quantization
- Model Serialization
- Local Inference
- Memory Optimization

## Use Cases

- Running LLMs locally on laptops or desktops
- Deploying models in resource-constrained edge devices
- Sharing optimized model weights in the open-source community

## Related Terms

- [LLAMA.cpp](/en/terms/llama-cpp/)
- [Quantization](/en/terms/quantization/)
- [ONNX](/en/terms/onnx/)
- [Model Weights](/en/terms/model-weights/)
