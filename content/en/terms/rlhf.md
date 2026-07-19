---
title: Reinforcement Learning from Human Feedback
term_id: rlhf
category: training_techniques
subcategory: ''
tags:
- alignment
- Fine-Tuning
difficulty: 5
weight: 1
slug: rlhf
date: '2026-07-18T09:36:45.466788Z'
lastmod: '2026-07-18T11:44:44.606747Z'
draft: false
source: agnes_llm
status: published
language: en
description: RLHF is a technique that aligns AI models with human preferences by using
  human feedback to train a reward model for reinforcement learning.
---
## Definition

Reinforcement Learning from Human Feedback (RLHF) is a method used to fine-tune large language models so their outputs align better with human values and expectations. It typically involves three steps: collecting human preference data, training a separate reward model based on this data, and then using reinforcement learning (often Proximal Policy Optimization) to adjust the main model to maximize the reward predicted by the model. This results in more helpful, honest, and harmless responses.

### Summary

RLHF is a technique that aligns AI models with human preferences by using human feedback to train a reward model for reinforcement learning.

## Key Concepts

- Preference Data
- Reward Model
- Alignment
- PPO (Proximal Policy Optimization)

## Use Cases

- Chatbot refinement
- Content moderation
- Improving instruction following

## Related Terms

- [Supervised Fine-Tuning](/en/terms/supervised-fine-tuning/)
- [Preference Optimization](/en/terms/preference-optimization/)
- [DPO](/en/terms/dpo/)
