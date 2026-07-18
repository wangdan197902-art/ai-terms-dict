---
title: "ExBERT"
term_id: "exbert"
category: "basic_concepts"
subcategory: ""
tags: ["nlp", "interpretability", "transformers"]
difficulty: 4
weight: 1
slug: "exbert"
aliases:
  - /zh/terms/exbert/
date: "2026-07-18T11:16:37.593427Z"
lastmod: "2026-07-18T11:44:45.496700Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种通过识别对特定输出贡献最大的注意力头和层来解释BERT预测的方法。"
---

## Definition

ExBERT通过分析不同层中单个注意力头的重要性，为BERT Transformer模型提供可解释性。它使用基于梯度的归因或其他技术来量化每个组件对最终预测的贡献，从而帮助理解模型的决策过程。

### Summary

一种通过识别对特定输出贡献最大的注意力头和层来解释BERT预测的方法。

## Key Concepts

- 注意力头
- 模型可解释性
- 梯度归因
- Transformer架构

## Use Cases

- 调试NLP模型
- 理解句法与语义处理
- 医疗文本分析中的可解释AI

## Related Terms

- [bert (BERT模型)](/en/terms/bert-bert模型/)
- [attention_mechanism (注意力机制)](/en/terms/attention_mechanism-注意力机制/)
- [explainable_ai (可解释人工智能)](/en/terms/explainable_ai-可解释人工智能/)
- [transformer_models (Transformer模型)](/en/terms/transformer_models-transformer模型/)
