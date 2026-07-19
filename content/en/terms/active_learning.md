---
title: Active learning
term_id: active_learning
category: training_techniques
subcategory: ''
tags:
- Supervised Learning
- efficiency
- annotation
difficulty: 3
weight: 1
slug: active_learning
date: '2026-07-18T09:44:54.636924Z'
lastmod: '2026-07-18T11:44:44.638780Z'
draft: false
source: agnes_llm
status: published
language: en
description: A machine learning strategy where the algorithm selectively queries a
  user or oracle to label new data points, optimizing the training process.
---
## Definition

Active learning reduces the amount of labeled data required by allowing the model to choose the most informative instances for human labeling. Instead of passively receiving random samples, the algorithm identifies regions of high uncertainty or potential impact and requests labels specifically for those cases. This iterative process significantly lowers annotation costs and accelerates convergence, making it ideal for scenarios where data labeling is expensive, time-consuming, or requires specialized expertise.

### Summary

A machine learning strategy where the algorithm selectively queries a user or oracle to label new data points, optimizing the training process.

## Key Concepts

- Query strategy
- Label efficiency
- Uncertainty sampling
- Human-in-the-loop

## Use Cases

- Medical image annotation with expert radiologists
- Sentiment analysis labeling for rare dialects
- Autonomous driving scenario selection

## Related Terms

- [semi-supervised learning](/en/terms/semi-supervised-learning/)
- [query strategies](/en/terms/query-strategies/)
- [data annotation](/en/terms/data-annotation/)
- [label efficiency](/en/terms/label-efficiency/)
