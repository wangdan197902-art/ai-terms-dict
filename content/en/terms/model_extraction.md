---
title: Model Extraction
term_id: model_extraction
category: ethics_safety
subcategory: ''
tags:
- security
- Adversarial ML
difficulty: 4
weight: 1
slug: model_extraction
date: '2026-07-18T10:20:32.579087Z'
lastmod: '2026-07-18T11:44:44.734960Z'
draft: false
source: agnes_llm
status: published
language: en
description: An attack where an adversary queries a model to reconstruct its parameters
  or create a surrogate copy.
---
## Definition

Model extraction involves querying a target machine learning model's API to infer its internal structure, weights, or decision boundaries. Attackers use these queries to build a surrogate model that mimics the original, potentially stealing intellectual property or bypassing security measures. This threat highlights the vulnerability of proprietary models exposed via public interfaces without sufficient rate limiting or monitoring.

### Summary

An attack where an adversary queries a model to reconstruct its parameters or create a surrogate copy.

## Key Concepts

- Surrogate Modeling
- API Querying
- Intellectual Property Theft
- Adversarial Attack

## Use Cases

- Security auditing of commercial AI APIs
- Protecting proprietary algorithms from cloning
- Researching defense mechanisms against extraction

## Related Terms

- [Membership Inference](/en/terms/membership-inference/)
- [Adversarial Examples](/en/terms/adversarial-examples/)
- [Model Watermarking](/en/terms/model-watermarking/)
- [API Security](/en/terms/api-security/)
