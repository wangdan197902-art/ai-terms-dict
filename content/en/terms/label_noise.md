---
title: "Label noise"
term_id: "label_noise"
category: "basic_concepts"
subcategory: ""
tags: ["data_preprocessing", "machine_learning_basics", "data_quality"]
difficulty: 2
weight: 1
slug: "label_noise"
aliases:
  - /en/terms/label_noise/
date: "2026-07-18T10:04:10.298064Z"
lastmod: "2026-07-18T11:44:44.690528Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Errors or inconsistencies in the target labels of a dataset used for supervised machine learning training."
---

## Definition

Label noise refers to discrepancies between the true class labels of data instances and the labels provided in the training dataset. This can arise from human annotation errors, ambiguous data points, or systematic labeling biases. Noise can be symmetric (random mislabeling) or asymmetric (specific classes mislabeled as others). It degrades model performance and generalization, necessitating robust learning techniques such as noise-tolerant loss functions, data cleaning, or ensemble methods to mitigate its adverse effects during training.

### Summary

Errors or inconsistencies in the target labels of a dataset used for supervised machine learning training.

## Key Concepts

- Data Quality
- Robust Learning
- Annotation Errors
- Symmetric/Asymmetric Noise

## Use Cases

- Training models on crowdsourced data
- Handling real-world imperfect datasets
- Improving model robustness

## Related Terms

- [data_cleaning](/en/terms/data_cleaning/)
- [robust_statistics](/en/terms/robust_statistics/)
- [supervised_learning](/en/terms/supervised_learning/)
- [outlier_detection](/en/terms/outlier_detection/)
