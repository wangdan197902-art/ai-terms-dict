---
title: "Product of experts"
term_id: "product_of_experts"
category: "basic_concepts"
subcategory: ""
tags: ["generative_models", "probabilistic_graphical_models", "deep_learning"]
difficulty: 4
weight: 1
slug: "product_of_experts"
aliases:
  - /en/terms/product_of_experts/
date: "2026-07-18T10:11:46.005693Z"
lastmod: "2026-07-18T11:44:44.711896Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A probabilistic modeling framework where the joint distribution is formed by multiplying the outputs of multiple independent expert models."
---

## Definition

The Product of Experts (PoE) is a method for constructing complex probability distributions by combining simpler ones. Unlike the 'Mixture of Experts,' which averages probabilities, PoE multiplies them, resulting in a distribution that is zero wherever any single expert assigns zero probability. This creates a more peaked and constrained distribution, effectively requiring all experts to agree on a valid configuration. It is particularly useful in energy-based models and deep learning architectures for capturing intricate dependencies in data, such as image textures or natural language structures.

### Summary

A probabilistic modeling framework where the joint distribution is formed by multiplying the outputs of multiple independent expert models.

## Key Concepts

- Energy-Based Models
- Joint Distribution
- Multiplicative Combination
- Constraint Satisfaction

## Use Cases

- Image texture synthesis and modeling
- Deep Boltzmann Machines
- Complex dependency modeling in generative models

## Related Terms

- [mixture_of_experts](/en/terms/mixture_of_experts/)
- [energy_based_model](/en/terms/energy_based_model/)
- [deep_boltzmann_machine](/en/terms/deep_boltzmann_machine/)
- [joint_probability](/en/terms/joint_probability/)
