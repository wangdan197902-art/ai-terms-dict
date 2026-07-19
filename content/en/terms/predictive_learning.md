---
title: Predictive learning
term_id: predictive_learning
category: training_techniques
subcategory: ''
tags:
- Self Supervised
- pretraining
- representation
difficulty: 3
weight: 1
slug: predictive_learning
date: '2026-07-18T10:11:14.173140Z'
lastmod: '2026-07-18T11:44:44.710215Z'
draft: false
source: agnes_llm
status: published
language: en
description: A self-supervised approach where models learn representations by predicting
  missing parts of input data.
---
## Definition

Predictive learning involves training neural networks to infer unobserved data points from observed inputs without explicit human labels. By solving tasks like next-token prediction in language or masked pixel reconstruction in images, the model learns rich internal representations of structure and semantics. This method leverages vast amounts of unlabeled data, enabling scalable pre-training that captures general patterns useful for downstream tasks through fine-tuning.

### Summary

A self-supervised approach where models learn representations by predicting missing parts of input data.

## Key Concepts

- Self-supervision
- Masked modeling
- Representation learning
- Unlabeled data

## Use Cases

- Pre-training large language models
- Image inpainting tasks
- Anomaly detection in time series

## Related Terms

- [self_supervised_learning](/en/terms/self_supervised_learning/)
- [masked_language_modeling](/en/terms/masked_language_modeling/)
- [contrastive_learning](/en/terms/contrastive_learning/)
- [autoencoder](/en/terms/autoencoder/)
