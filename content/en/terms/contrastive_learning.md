---
title: "Contrastive Learning"
term_id: "contrastive_learning"
category: "training_techniques"
subcategory: ""
tags: ["self_supervised", "representation_learning", "optimization"]
difficulty: 4
weight: 1
slug: "contrastive_learning"
aliases:
  - /en/terms/contrastive_learning/
date: "2026-07-18T09:51:47.617491Z"
lastmod: "2026-07-18T11:44:44.657241Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A self-supervised learning technique that learns representations by pulling positive pairs together and pushing negative pairs apart."
---

## Definition

Contrastive learning is a representation learning method that does not require labeled data. It works by creating augmented views of the same input (positive pairs) and contrasting them with different inputs (negative pairs). The model is trained to minimize the distance between positive pairs in the embedding space while maximizing the distance between negative pairs. This approach has become foundational for achieving state-of-the-art results in computer vision and natural language processing tasks.

### Summary

A self-supervised learning technique that learns representations by pulling positive pairs together and pushing negative pairs apart.

## Key Concepts

- Self-Supervision
- Positive/Negative Pairs
- Embedding Space
- Augmentation Strategies

## Use Cases

- Unlabeled image classification
- Semantic search indexing
- Anomaly detection in time series

## Related Terms

- [SimCLR](/en/terms/simclr/)
- [MoCo](/en/terms/moco/)
- [Self-Supervised Learning](/en/terms/self-supervised-learning/)
- [Representation Learning](/en/terms/representation-learning/)
