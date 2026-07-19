---
title: Mamba
term_id: mamba
category: basic_concepts
subcategory: ''
tags:
- architecture
- efficiency
- Sequence Modeling
difficulty: 4
weight: 1
slug: mamba
date: '2026-07-18T10:53:03.111169Z'
lastmod: '2026-07-18T11:44:45.376402Z'
draft: false
source: agnes_llm
status: published
language: zh
description: Mamba 是一种状态空间序列模型，它在保持 Transformer 在长上下文任务中性能的同时，提供了线性时间的推理速度。
---
## Definition

Mamba 通过引入硬件感知的选择性状态空间模型（SSM），代表了序列建模领域的重大进步。与随着序列长度呈二次方扩展的传统 Transformer 不同，Mamba 能够高效处理长序列。

### Summary

Mamba 是一种状态空间序列模型，它在保持 Transformer 在长上下文任务中性能的同时，提供了线性时间的推理速度。

## Key Concepts

- 选择性状态空间模型
- 线性复杂度
- 硬件感知架构
- 长上下文处理

## Use Cases

- 长文档摘要
- 基因组序列分析
- 高频时间序列预测

## Related Terms

- [Transformer (变换器)](/en/terms/transformer-变换器/)
- [RNN (循环神经网络)](/en/terms/rnn-循环神经网络/)
- [SSM (状态空间模型)](/en/terms/ssm-状态空间模型/)
- [Attention Mechanism (注意力机制)](/en/terms/attention-mechanism-注意力机制/)
