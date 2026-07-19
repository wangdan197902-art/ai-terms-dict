---
title: Actor-critic algorithm
term_id: actor_critic_algorithm
category: basic_concepts
subcategory: ''
tags:
- Reinforcement Learning
- Neural Networks
- algorithms
difficulty: 4
weight: 1
slug: actor_critic_algorithm
date: '2026-07-18T09:44:54.636930Z'
lastmod: '2026-07-18T11:44:44.639017Z'
draft: false
source: agnes_llm
status: published
language: en
description: 'A reinforcement learning framework that combines value-based and policy-based
  methods using two neural networks: an actor and a critic.'
---
## Definition

The actor-critic algorithm employs two components: the actor, which updates the policy to select actions, and the critic, which evaluates the quality of those actions by estimating the value function. The critic provides feedback to the actor, guiding policy improvements based on temporal difference errors. This hybrid approach leverages the low variance of value-based methods and the high bias but potentially lower variance of policy gradient methods, resulting in more stable and efficient learning in complex continuous control tasks.

### Summary

A reinforcement learning framework that combines value-based and policy-based methods using two neural networks: an actor and a critic.

## Key Concepts

- Policy gradient
- Value function
- Temporal difference error
- Hybrid RL

## Use Cases

- Robotic arm manipulation
- Game playing agents (e.g., AlphaStar)
- Continuous control systems in autonomous vehicles

## Related Terms

- [PPO](/en/terms/ppo/)
- [A3C](/en/terms/a3c/)
- [policy_gradient](/en/terms/policy_gradient/)
- [value_function](/en/terms/value_function/)
