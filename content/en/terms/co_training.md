---
title: "Co-training"
term_id: "co_training"
category: "training_techniques"
subcategory: ""
tags: ["semi_supervised", "algorithm", "data_efficiency"]
difficulty: 4
weight: 1
slug: "co_training"
aliases:
  - /en/terms/co_training/
date: "2026-07-18T09:49:31.456594Z"
lastmod: "2026-07-18T11:44:44.651966Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Co-training is a semi-supervised learning algorithm where two views of the data are used to train separate classifiers that iteratively label unlabeled data for each other."
---

## Definition

This method leverages multiple distinct feature sets (views) of the same data points. Initially, two classifiers are trained on small labeled datasets from each view. They then predict labels for unlabeled data, selecting high-confidence predictions to augment the training set of the other classifier. This iterative process expands the effective training data size, improving generalization when labeled data is scarce but abundant unlabeled data exists.

### Summary

Co-training is a semi-supervised learning algorithm where two views of the data are used to train separate classifiers that iteratively label unlabeled data for each other.

## Key Concepts

- Semi-Supervised Learning
- Multiple Views
- Iterative Labeling
- High-Confidence Selection

## Use Cases

- Text classification with multiple features
- Web page categorization
- Data augmentation with limited labels

## Related Terms

- [Semi-Supervised Learning](/en/terms/semi-supervised-learning/)
- [Self-Training](/en/terms/self-training/)
- [Multi-view Learning](/en/terms/multi-view-learning/)
- [Active Learning](/en/terms/active-learning/)
