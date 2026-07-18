---
title: "混合专家模型"
term_id: "moe"
category: "basic_concepts"
subcategory: ""
tags: ["Architecture", "Efficiency", "LLMs"]
difficulty: 4
weight: 1
slug: "moe"
aliases:
  - /zh/terms/moe/
date: "2026-07-18T11:26:37.042799Z"
lastmod: "2026-07-18T11:44:45.533587Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种架构模式，通过门控机制结合多个专用神经网络（专家）来处理输入。"
---

## Definition

混合专家（MoE）是一种旨在提高效率和可扩展性的机器学习架构。MoE 不使用单个大型模型处理所有任务，而是采用多个较小的“专家”网络。

### Summary

一种架构模式，通过门控机制结合多个专用神经网络（专家）来处理输入。

## Key Concepts

- 稀疏激活
- 门控网络
- 专家专业化
- 可扩展性

## Use Cases

- 高效训练大型语言模型
- 降低大型模型的推理延迟
- 在多模态系统中处理多样化的输入类型

## Related Terms

- [稀疏 Transformer (Sparse Transformers)](/en/terms/稀疏-transformer-sparse-transformers/)
- [条件计算 (Conditional Computation)](/en/terms/条件计算-conditional-computation/)
- [大型语言模型 (Large Language Models)](/en/terms/大型语言模型-large-language-models/)
- [神经架构搜索 (Neural Architecture Search)](/en/terms/神经架构搜索-neural-architecture-search/)
