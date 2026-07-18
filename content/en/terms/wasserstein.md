---
title: "Wasserstein"
term_id: "wasserstein"
category: "basic_concepts"
subcategory: ""
tags: ["metrics", "gan", "probability"]
difficulty: 4
weight: 1
slug: "wasserstein"
aliases:
  - /en/terms/wasserstein/
date: "2026-07-18T09:38:06.621849Z"
lastmod: "2026-07-18T11:44:44.614815Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A metric measuring the distance between probability distributions based on the minimum cost of transforming one into another."
---

## Definition

The Wasserstein distance, also known as Earth Mover's Distance, quantifies the dissimilarity between two probability distributions by calculating the minimum 'work' required to move mass from one distribution to match the other. Unlike KL divergence, it provides a smooth gradient even when distributions have disjoint support, making it highly effective for training Generative Adversarial Networks (GANs) and stabilizing convergence in generative modeling tasks.

### Summary

A metric measuring the distance between probability distributions based on the minimum cost of transforming one into another.

## Key Concepts

- Earth Mover's Distance
- Probability Distributions
- Optimal Transport
- Gradient Stability

## Use Cases

- Training Stable GANs
- Domain Adaptation
- Measuring Distribution Similarity

## Related Terms

- [KL Divergence](/en/terms/kl-divergence/)
- [Generative Adversarial Networks](/en/terms/generative-adversarial-networks/)
- [Optimal Transport](/en/terms/optimal-transport/)
- [Distribution Matching](/en/terms/distribution-matching/)
