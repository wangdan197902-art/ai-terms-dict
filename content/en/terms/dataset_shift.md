---
title: Dataset shift
term_id: dataset_shift
category: basic_concepts
subcategory: ''
tags:
- Machine Learning
- statistics
- Model Deployment
difficulty: 3
weight: 1
slug: dataset_shift
date: '2026-07-18T09:53:01.226752Z'
lastmod: '2026-07-18T11:44:44.659846Z'
draft: false
source: agnes_llm
status: published
language: en
description: Dataset shift refers to the phenomenon where the statistical properties
  of the input data change between training and deployment.
---
## Definition

Dataset shift occurs when the distribution of data used to train a machine learning model differs from the distribution of data encountered during inference. This discrepancy can lead to significant performance degradation. Common types include covariate shift, prior probability shift, and concept drift. Addressing dataset shift is critical for ensuring model robustness and generalization in real-world applications, often requiring techniques like domain adaptation or continuous monitoring.

### Summary

Dataset shift refers to the phenomenon where the statistical properties of the input data change between training and deployment.

## Key Concepts

- Covariate shift
- Concept drift
- Domain adaptation
- Generalization

## Use Cases

- Monitoring production ML models
- Retraining strategies
- Robustness testing

## Related Terms

- [Overfitting](/en/terms/overfitting/)
- [Underfitting](/en/terms/underfitting/)
- [Domain Adaptation](/en/terms/domain-adaptation/)
- [Data Drift](/en/terms/data-drift/)
