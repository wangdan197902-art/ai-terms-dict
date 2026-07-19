---
title: Energy-based model
term_id: energy_based_model
category: basic_concepts
subcategory: ''
tags:
- Generative Models
- probability
- Deep Learning
difficulty: 4
weight: 1
slug: energy_based_model
date: '2026-07-18T09:56:53.750949Z'
lastmod: '2026-07-18T11:44:44.669525Z'
draft: false
source: agnes_llm
status: published
language: en
description: A probabilistic model that assigns low energy values to plausible configurations
  and high energy values to implausible ones.
---
## Definition

Energy-Based Models (EBMs) define a probability distribution over input data using an unnormalized density function derived from an energy function. The energy function maps data points to real numbers, where lower energies correspond to higher probabilities. EBMs are flexible and can model complex multimodal distributions but often require computationally intensive sampling methods, such as Markov Chain Monte Carlo, for inference and training compared to normalized models like softmax classifiers.

### Summary

A probabilistic model that assigns low energy values to plausible configurations and high energy values to implausible ones.

## Key Concepts

- Unnormalized probability
- Partition function
- Energy function
- Markov Chain Monte Carlo

## Use Cases

- Image generation and inpainting
- Density estimation
- Anomaly detection

## Related Terms

- [Boltzmann machine](/en/terms/boltzmann-machine/)
- [Deep Boltzmann machine](/en/terms/deep-boltzmann-machine/)
- [Variational inference](/en/terms/variational-inference/)
- [Probabilistic graphical models](/en/terms/probabilistic-graphical-models/)
