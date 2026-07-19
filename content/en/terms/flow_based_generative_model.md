---
title: "Flow-based generative model"
term_id: "flow_based_generative_model"
category: "basic_concepts"
subcategory: ""
tags: ["generative", "probability", "invertible"]
difficulty: 4
weight: 1
slug: "flow_based_generative_model"
date: "2026-07-18T09:58:20.231262Z"
lastmod: "2026-07-18T11:44:44.673811Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A class of generative models that use invertible transformations to map simple distributions to complex data distributions."
---
## Definition

Flow-based generative models construct complex probability distributions by applying a series of invertible, differentiable transformations to a simple base distribution, such as a Gaussian. Because the transformations are invertible, these models can compute the exact likelihood of data points efficiently. This property distinguishes them from other generative models like GANs or VAEs, offering precise density estimation and exact sampling without approximation errors.

### Summary

A class of generative models that use invertible transformations to map simple distributions to complex data distributions.

## Key Concepts

- Invertible Transformations
- Exact Likelihood
- Normalizing Flows
- Change of Variables

## Use Cases

- Image generation
- Density estimation
- Anomaly detection

## Related Terms

- [Normalizing Flow](/en/terms/normalizing-flow/)
- [GAN](/en/terms/gan/)
- [VAE](/en/terms/vae/)
- [Coupling Layer](/en/terms/coupling-layer/)
