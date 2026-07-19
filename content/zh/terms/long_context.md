---
title: 长上下文
term_id: long_context
category: basic_concepts
subcategory: ''
tags:
- NLP
- transformers
- architecture
difficulty: 2
weight: 1
slug: long_context
date: '2026-07-18T11:24:46.268045Z'
lastmod: '2026-07-18T11:44:45.527041Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 语言模型处理并保留包含数千或数百万个标记（token）的输入序列信息的能力。
---
## Definition

长上下文指的是基于 Transformer 的模型处理极长输入长度的能力，通常超过标准的 2k 或 4k 标记限制。这种能力使模型能够分析完整的文档、代码库或长文本，保持全局一致性和细节记忆。

### Summary

语言模型处理并保留包含数千或数百万个标记（token）的输入序列信息的能力。

## Key Concepts

- 上下文窗口
- 标记限制
- 注意力机制
- 位置编码

## Use Cases

- 总结完整的法律合同
- 分析完整的源代码仓库
- 处理长篇音频转录文本

## Related Terms

- [Context Window (上下文窗口)](/en/terms/context-window-上下文窗口/)
- [Transformer Architecture (Transformer 架构)](/en/terms/transformer-architecture-transformer-架构/)
- [RoPE (Rotary Positional Embeddings, 旋转位置编码)](/en/terms/rope-rotary-positional-embeddings-旋转位置编码/)
- [KV Cache (键值缓存)](/en/terms/kv-cache-键值缓存/)
