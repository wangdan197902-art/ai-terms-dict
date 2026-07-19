---
title: Multiple instance learning
term_id: multiple_instance_learning
category: training_techniques
subcategory: ''
tags:
- Supervised Learning
- Weak Labeling
- ML Paradigm
difficulty: 4
weight: 1
slug: multiple_instance_learning
date: '2026-07-18T09:41:54.086090Z'
lastmod: '2026-07-18T11:44:44.628375Z'
draft: false
source: agnes_llm
status: published
language: en
description: A weakly supervised learning paradigm where labels are assigned to bags
  of instances rather than individual instances.
---
## Definition

Multiple Instance Learning (MIL) addresses scenarios where data is grouped into 'bags' with a single label, while individual instances within those bags remain unlabeled. A bag is typically positive if at least one instance is positive, and negative only if all instances are negative. This technique is crucial when precise labeling of individual data points is costly or impossible, allowing models to learn from coarse-grained supervision signals effectively.

### Summary

A weakly supervised learning paradigm where labels are assigned to bags of instances rather than individual instances.

## Key Concepts

- Bag-level labeling
- Instance-level uncertainty
- Weak supervision
- Positive/negative bag logic

## Use Cases

- Drug activity prediction
- Image classification with bounding boxes
- Content-based image retrieval

## Related Terms

- [weak_supervision](/en/terms/weak_supervision/)
- [bagging](/en/terms/bagging/)
- [instance_classification](/en/terms/instance_classification/)
- [label_noise](/en/terms/label_noise/)
