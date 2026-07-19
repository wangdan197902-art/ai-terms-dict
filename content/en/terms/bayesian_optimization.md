---
title: Bayesian optimization
term_id: bayesian_optimization
category: training_techniques
subcategory: ''
tags:
- Optimization
- hyperparameters
- Surrogate Models
difficulty: 3
weight: 1
slug: bayesian_optimization
date: '2026-07-18T09:47:51.703280Z'
lastmod: '2026-07-18T11:44:44.647353Z'
draft: false
source: agnes_llm
status: published
language: en
description: A sequential design strategy for global optimization of black-box functions
  that are expensive to evaluate.
---
## Definition

Bayesian optimization uses a probabilistic surrogate model, typically a Gaussian Process, to model the objective function. It employs an acquisition function to balance exploration and exploitation, selecting the next evaluation point that maximizes expected improvement. This method is highly efficient for tuning hyperparameters in machine learning models where each training run is computationally costly, requiring fewer evaluations than grid or random search to find near-optimal configurations.

### Summary

A sequential design strategy for global optimization of black-box functions that are expensive to evaluate.

## Key Concepts

- Surrogate Model
- Acquisition Function
- Exploration vs Exploitation
- Black-Box Optimization

## Use Cases

- Hyperparameter tuning for deep learning models
- Optimizing experimental designs in science
- Robotics control parameter adjustment

## Related Terms

- [hyperparameter_tuning](/en/terms/hyperparameter_tuning/)
- [gaussian_processes](/en/terms/gaussian_processes/)
- [acquisition_function](/en/terms/acquisition_function/)
- [grid_search](/en/terms/grid_search/)
