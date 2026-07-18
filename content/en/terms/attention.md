---
title: "Attention"
term_id: "attention"
category: "training_techniques"
subcategory: ""
tags: ["transformers", "mechanism", "sequence", "core_concept"]
difficulty: 4
weight: 1
slug: "attention"
aliases:
  - /en/terms/attention/
date: "2026-07-18T09:39:58.032360Z"
lastmod: "2026-07-18T11:44:44.620834Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A mechanism that allows neural networks to weigh the importance of different parts of the input sequence dynamically."
---

## Definition

Attention mechanisms enable models to focus on relevant information when processing inputs, particularly in sequential data like text. By calculating attention scores, the model determines which elements of the input have the most influence on the current prediction. This approach overcomes the limitations of fixed-size context windows in recurrent networks. Self-attention, a core component of Transformers, allows every token to attend to every other token, capturing long-range dependencies and contextual relationships efficiently, thereby significantly improving performance in NLP and computer vision tasks.

### Summary

A mechanism that allows neural networks to weigh the importance of different parts of the input sequence dynamically.

## Key Concepts

- Self-Attention
- Contextual Weighting
- Long-Range Dependencies
- Transformer Architecture

## Use Cases

- Machine translation between languages
- Summarizing long documents
- Image captioning and visual question answering

## Related Terms

- [Transformer](/en/terms/transformer/)
- [Self-Attention](/en/terms/self-attention/)
- [Multi-Head Attention](/en/terms/multi-head-attention/)
- [Sequence Modeling](/en/terms/sequence-modeling/)
