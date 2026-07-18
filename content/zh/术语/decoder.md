---
title: "解码器"
term_id: "decoder"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "nlp", "architecture"]
difficulty: 4
weight: 1
slug: "decoder"
aliases:
  - /zh/terms/decoder/
date: "2026-07-18T10:59:40.488029Z"
lastmod: "2026-07-18T11:44:45.398366Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "负责从编码后的潜在表示生成输出序列的神经网络组件。"
---

## Definition

在序列到序列（Seq2Seq）模型中，解码器接收由编码器生成的上下文向量，并逐步生成目标输出。它利用注意力机制来关注输入序列的相关部分，从而准确预测下一个输出元素。

### Summary

负责从编码后的潜在表示生成输出序列的神经网络组件。

## Key Concepts

- 序列生成
- 注意力机制
- 潜在空间
- 自回归预测

## Use Cases

- 机器翻译（如英语到法语）
- 文本摘要
- 图像描述生成

## Related Terms

- [Encoder (编码器)](/en/terms/encoder-编码器/)
- [Transformer (变换器架构)](/en/terms/transformer-变换器架构/)
- [RNN (循环神经网络)](/en/terms/rnn-循环神经网络/)
- [Sequence-to-Sequence (序列到序列模型)](/en/terms/sequence-to-sequence-序列到序列模型/)
