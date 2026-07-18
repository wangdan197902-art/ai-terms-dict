---
title: "文本生成推理"
term_id: "text_generation_inference"
category: "application_paradigms"
subcategory: ""
tags: ["inference", "optimization", "deployment"]
difficulty: 4
weight: 1
slug: "text_generation_inference"
aliases:
  - /zh/terms/text_generation_inference/
date: "2026-07-18T11:36:07.262483Z"
lastmod: "2026-07-18T11:44:45.562476Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一个高性能的服务引擎，专门针对大规模高效部署大型语言模型以生成文本进行了优化。"
---

## Definition

文本生成推理（TGI）是一个专用的软件框架，旨在以低延迟和高吞吐量服务大型语言模型（LLM）。它针对文本生成的推理过程进行了深度优化，包括连续批处理和张量并行等技术，从而显著提升生产环境下的响应速度和并发处理能力。

### Summary

一个高性能的服务引擎，专门针对大规模高效部署大型语言模型以生成文本进行了优化。

## Key Concepts

- 连续批处理
- 张量并行
- 低延迟服务
- LLM部署

## Use Cases

- 生产级聊天机器人API
- 实时内容生成服务
- 高吞吐量文本分析平台

## Related Terms

- [llm_serving (LLM服务化)](/en/terms/llm_serving-llm服务化/)
- [continuous_batching (连续批处理)](/en/terms/continuous_batching-连续批处理/)
- [huggingface_tgi (Hugging Face TGI工具)](/en/terms/huggingface_tgi-hugging-face-tgi工具/)
- [model_optimization (模型优化)](/en/terms/model_optimization-模型优化/)
