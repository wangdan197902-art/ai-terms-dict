---
title: "Predictive state representation"
term_id: "predictive_state_representation"
category: "basic_concepts"
subcategory: ""
tags: ["rl", "state_representation", "pomdp"]
difficulty: 4
weight: 1
slug: "predictive_state_representation"
aliases:
  - /en/terms/predictive_state_representation/
date: "2026-07-18T10:11:14.173177Z"
lastmod: "2026-07-18T11:44:44.710319Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A latent state formulation in reinforcement learning that predicts future observations based on action history."
---

## Definition

Predictive State Representations (PSRs) extend traditional partially observable Markov decision processes by defining states as vectors of predictions about future observable events. Instead of relying on hidden true states, PSRs use the history of actions and observations to predict what will happen next. This allows agents to operate effectively in environments with partial observability, providing a more flexible and often more compact representation of the environment dynamics for planning and control.

### Summary

A latent state formulation in reinforcement learning that predicts future observations based on action history.

## Key Concepts

- Partial observability
- Future predictions
- History-based states
- Reinforcement learning

## Use Cases

- Robotics in cluttered environments
- Game AI with hidden information
- Financial market forecasting

## Related Terms

- [partially_observable_mdp](/en/terms/partially_observable_mdp/)
- [latent_space](/en/terms/latent_space/)
- [state_estimation](/en/terms/state_estimation/)
- [pomdp](/en/terms/pomdp/)
