---
title: "Data Augmentation"
term_id: "data_augmentation"
category: "training_techniques"
subcategory: ""
tags: ["machine_learning", "preprocessing", "cv"]
difficulty: 2
weight: 1
slug: "data_augmentation"
aliases:
  - /en/terms/data_augmentation/
date: "2026-07-18T09:52:41.243452Z"
lastmod: "2026-07-18T11:44:44.658798Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Data augmentation is a technique used to increase the diversity and size of training datasets by applying transformations to existing data points."
---

## Definition

This method artificially expands the training dataset by creating modified versions of existing samples, such as rotating images, adding noise to audio, or synonym replacement in text. It helps prevent overfitting by exposing the model to a wider variety of scenarios during training, thereby improving generalization performance. It is particularly crucial in domains where collecting large amounts of real-world labeled data is expensive or difficult.

### Summary

Data augmentation is a technique used to increase the diversity and size of training datasets by applying transformations to existing data points.

## Key Concepts

- Overfitting Prevention
- Dataset Expansion
- Generalization
- Transformations

## Use Cases

- Improving computer vision model robustness
- Enhancing NLP model performance with limited text
- Balancing imbalanced datasets

## Code Example

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator
gen = ImageDataGenerator(rotation_range=20)

```

## Related Terms

- [Regularization](/en/terms/regularization/)
- [Synthetic Data](/en/terms/synthetic-data/)
- [Transfer Learning](/en/terms/transfer-learning/)
- [Overfitting](/en/terms/overfitting/)
