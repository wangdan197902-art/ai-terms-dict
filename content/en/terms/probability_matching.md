---
title: Probability matching
term_id: probability_matching
category: basic_concepts
subcategory: ''
tags:
- RL
- Behavioral Modeling
- Decision Making
difficulty: 3
weight: 1
slug: probability_matching
date: '2026-07-18T10:11:46.005677Z'
lastmod: '2026-07-18T11:44:44.711639Z'
draft: false
source: agnes_llm
status: published
language: en
description: A decision-making strategy where an agent selects actions with frequencies
  proportional to their estimated probabilities.
---
## Definition

Probability matching is a behavioral pattern often observed in reinforcement learning and psychology, contrasting with optimal 'maximizing' strategies. Instead of always choosing the action with the highest expected reward, a probability-matching agent distributes its choices according to the underlying probability distribution of rewards. While suboptimal in stationary environments compared to pure exploitation, it can be advantageous in non-stationary settings where exploring different options helps track changing environmental dynamics. It serves as a baseline for understanding exploration-exploitation trade-offs.

### Summary

A decision-making strategy where an agent selects actions with frequencies proportional to their estimated probabilities.

## Key Concepts

- Exploration vs Exploitation
- Reinforcement Learning
- Stochastic Environments
- Decision Theory

## Use Cases

- Modeling human behavior in psychological experiments
- Robust exploration in non-stationary multi-armed bandit problems
- Analyzing suboptimal learning algorithms

## Related Terms

- [epsilon-greedy](/en/terms/epsilon-greedy/)
- [softmax_action_selection](/en/terms/softmax_action_selection/)
- [maximizing_strategy](/en/terms/maximizing_strategy/)
- [exploration_bonus](/en/terms/exploration_bonus/)
