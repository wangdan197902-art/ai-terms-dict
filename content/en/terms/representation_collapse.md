---
title: "Representation collapse"
term_id: "representation_collapse"
category: "basic_concepts"
subcategory: ""
tags: ["self_supervised", "training_dynamics", "computer_vision"]
difficulty: 3
weight: 1
slug: "representation_collapse"
aliases:
  - /en/terms/representation_collapse/
date: "2026-07-18T10:14:07.773948Z"
lastmod: "2026-07-18T11:44:44.717408Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A failure mode in self-supervised learning where the model outputs identical representations for all inputs, losing discriminative power."
---

## Definition

Representation collapse occurs when a neural network, particularly in self-supervised contrastive learning frameworks, learns to map all input data points to the same fixed output vector. This trivial solution minimizes the loss function without learning meaningful features. To prevent this, techniques like normalization, momentum encoders, or specific loss formulations are employed to ensure the model preserves distinct information across different inputs.

### Summary

A failure mode in self-supervised learning where the model outputs identical representations for all inputs, losing discriminative power.

## Key Concepts

- Self-Supervised Learning
- Contrastive Loss
- Trivial Solutions
- Feature Learning

## Use Cases

- Debugging SimCLR or MoCo models
- Improving Contrastive Loss Functions
- Analyzing Model Convergence

## Related Terms

- [Contrastive Learning](/en/terms/contrastive-learning/)
- [Batch Normalization](/en/terms/batch-normalization/)
- [Momentum Encoder](/en/terms/momentum-encoder/)
- [Feature Extraction](/en/terms/feature-extraction/)
