---
title: "Machine unlearning"
term_id: "machine_unlearning"
category: "training_techniques"
subcategory: ""
tags: ["privacy", "ethics", "maintenance"]
difficulty: 4
weight: 1
slug: "machine_unlearning"
aliases:
  - /en/terms/machine_unlearning/
date: "2026-07-18T10:06:25.398220Z"
lastmod: "2026-07-18T11:44:44.695997Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Machine unlearning is the process of removing specific data points or their influence from a trained model without retraining it from scratch."
---

## Definition

This technique addresses privacy regulations like GDPR's 'right to be forgotten' by allowing models to forget specific user data while retaining general knowledge. It aims to approximate the performance of a model that was never trained on the excluded data. Methods range from exact removal algorithms to approximate gradient-based updates, ensuring compliance and security without the prohibitive computational costs associated with full model retraining.

### Summary

Machine unlearning is the process of removing specific data points or their influence from a trained model without retraining it from scratch.

## Key Concepts

- Right to be Forgotten
- Model Retraining Approximation
- Data Privacy
- Gradient Updates

## Use Cases

- Complying with data deletion requests
- Removing biased or erroneous data from models
- Mitigating data poisoning attacks

## Related Terms

- [Data Privacy](/en/terms/data-privacy/)
- [Federated Learning](/en/terms/federated-learning/)
- [Model Retraining](/en/terms/model-retraining/)
- [GDPR](/en/terms/gdpr/)
