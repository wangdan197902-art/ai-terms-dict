---
title: 演员-评论家算法
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
date: '2026-07-18T11:04:13.788385Z'
lastmod: '2026-07-18T11:44:45.438668Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种结合基于价值和基于策略方法的强化学习框架，使用两个神经网络：演员（Actor）和评论家（Critic）。
---
## Definition

演员-评论家算法包含两个组件：演员负责更新策略以选择动作，评论家则通过估计价值函数来评估这些动作的质量。两者协同工作，以提高强化学习的稳定性和效率。

### Summary

一种结合基于价值和基于策略方法的强化学习框架，使用两个神经网络：演员（Actor）和评论家（Critic）。

## Key Concepts

- 策略梯度
- 价值函数
- 时序差分误差
- 混合强化学习

## Use Cases

- 机械臂操作
- 游戏代理（如AlphaStar）
- 自动驾驶中的连续控制系统

## Related Terms

- [PPO (近端策略优化)](/en/terms/ppo-近端策略优化/)
- [A3C (异步优势演员-评论家)](/en/terms/a3c-异步优势演员-评论家/)
- [policy_gradient (策略梯度)](/en/terms/policy_gradient-策略梯度/)
- [value_function (价值函数)](/en/terms/value_function-价值函数/)
