---
title: "Mixture of Experts"
term_id: "moe"
category: "basic_concepts"
subcategory: ""
tags: ["Architecture", "Efficiency", "LLMs"]
difficulty: 4
weight: 1
slug: "moe"
date: "2026-07-18T10:07:54.130361Z"
lastmod: "2026-07-18T11:44:44.701294Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "An architectural pattern where multiple specialized neural networks (experts) are combined via a gating mechanism to process inputs."
---
## Definition

Mixture of Experts (MoE) is a machine learning architecture designed to improve efficiency and scalability. Instead of using a single large model for all tasks, MoE employs multiple smaller 'expert' networks, each specialized in different aspects of the data. A trainable gating network determines which experts should handle specific inputs, allowing the model to activate only a subset of parameters for each token. This sparsity enables significantly larger model capacity with reduced computational cost during inference, making it ideal for large-scale language models.

### Summary

An architectural pattern where multiple specialized neural networks (experts) are combined via a gating mechanism to process inputs.

## Key Concepts

- Sparse Activation
- Gating Network
- Expert Specialization
- Scalability

## Use Cases

- Training large language models efficiently
- Reducing inference latency for massive models
- Handling diverse input types in multimodal systems

## Related Terms

- [Sparse Transformers](/en/terms/sparse-transformers/)
- [Conditional Computation](/en/terms/conditional-computation/)
- [Large Language Models](/en/terms/large-language-models/)
- [Neural Architecture Search](/en/terms/neural-architecture-search/)
