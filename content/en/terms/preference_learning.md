---
title: Preference learning
term_id: preference_learning
category: training_techniques
subcategory: ''
tags:
- alignment
- Human Feedback
- rlhf
difficulty: 3
weight: 1
slug: preference_learning
date: '2026-07-18T10:11:14.173190Z'
lastmod: '2026-07-18T11:44:44.710435Z'
draft: false
source: agnes_llm
status: published
language: en
description: A technique that trains models to align outputs with human preferences
  using comparative feedback.
---
## Definition

Preference learning focuses on teaching models to distinguish between good and bad outputs based on human judgments rather than absolute labels. It typically involves collecting pairs of responses where humans indicate their preferred option. Algorithms then optimize the model to maximize the likelihood of generating preferred responses. This is crucial for aligning large language models with human values, improving safety, and enhancing relevance in conversational AI systems.

### Summary

A technique that trains models to align outputs with human preferences using comparative feedback.

## Key Concepts

- Human feedback
- Pairwise comparison
- Reward modeling
- Alignment

## Use Cases

- RLHF for LLMs
- Recommendation systems
- Content moderation filtering

## Related Terms

- [rlhf](/en/terms/rlhf/)
- [reward_modeling](/en/terms/reward_modeling/)
- [human_in_the_loop](/en/terms/human_in_the_loop/)
- [alignment](/en/terms/alignment/)
