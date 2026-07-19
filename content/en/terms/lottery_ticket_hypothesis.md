---
title: Lottery ticket hypothesis
term_id: lottery_ticket_hypothesis
category: basic_concepts
subcategory: ''
tags:
- Optimization
- pruning
- theory
difficulty: 4
weight: 1
slug: lottery_ticket_hypothesis
date: '2026-07-18T10:05:43.261516Z'
lastmod: '2026-07-18T11:44:44.694196Z'
draft: false
source: agnes_llm
status: published
language: en
description: The theory that dense neural networks contain smaller subnetworks that,
  when trained in isolation from initialization, can match the accuracy of the original
  network.
---
## Definition

The Lottery Ticket Hypothesis suggests that within a large, randomly initialized neural network, there exists a sparse subnetwork (the 'winning ticket') that is well-initialized for training. By pruning weights iteratively and resetting the remaining ones to their initial values, this subnetwork can converge to high accuracy independently. This concept supports model compression and efficiency, challenging the necessity of training massive models from scratch for every task.

### Summary

The theory that dense neural networks contain smaller subnetworks that, when trained in isolation from initialization, can match the accuracy of the original network.

## Key Concepts

- Weight pruning
- Sparse networks
- Model compression
- Initialization sensitivity

## Use Cases

- Deploying lightweight models on edge devices
- Reducing computational costs during training
- Accelerating inference speeds

## Related Terms

- [Network Pruning](/en/terms/network-pruning/)
- [Model Distillation](/en/terms/model-distillation/)
- [Sparse Training](/en/terms/sparse-training/)
- [Efficient AI](/en/terms/efficient-ai/)
