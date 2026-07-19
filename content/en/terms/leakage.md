---
title: Leakage
term_id: leakage
category: basic_concepts
subcategory: ''
tags:
- Data Integrity
- evaluation
- Best Practices
difficulty: 3
weight: 1
slug: leakage
date: '2026-07-18T10:04:43.446855Z'
lastmod: '2026-07-18T11:44:44.691325Z'
draft: false
source: agnes_llm
status: published
language: en
description: Data leakage occurs when information from outside the training dataset
  inadvertently influences the model, leading to overly optimistic performance estimates.
---
## Definition

Data leakage is a critical error in machine learning where the model gains access to information during training that would not be available at prediction time. This often happens through improper data preprocessing, such as scaling before splitting, or including target-related features in the input set. It results in models that appear highly accurate on validation sets but fail catastrophically in real-world deployment because they rely on impossible-to-obtain data.

### Summary

Data leakage occurs when information from outside the training dataset inadvertently influences the model, leading to overly optimistic performance estimates.

## Key Concepts

- Target leakage
- Training-test contamination
- Proper data splitting

## Use Cases

- Debugging model overfitting
- Validating feature engineering pipelines
- Ensuring robust model evaluation

## Related Terms

- [Overfitting](/en/terms/overfitting/)
- [Cross-validation](/en/terms/cross-validation/)
- [Feature engineering](/en/terms/feature-engineering/)
