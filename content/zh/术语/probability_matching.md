---
title: "概率匹配"
term_id: "probability_matching"
category: "basic_concepts"
subcategory: ""
tags: ["RL", "behavioral_modeling", "decision_making"]
difficulty: 3
weight: 1
slug: "probability_matching"
aliases:
  - /zh/terms/probability_matching/
date: "2026-07-18T11:30:38.310457Z"
lastmod: "2026-07-18T11:44:45.545394Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种决策策略，智能体选择动作的频率与其估计的概率成正比。"
---

## Definition

概率匹配是一种在强化学习和心理学中经常观察到的行为模式，与最优的“最大化”策略形成对比。它并不总是选择概率最高的动作，而是根据各动作的概率分布来随机选择动作。这种策略虽然不如贪婪策略在静态环境中高效，但在非平稳环境或需要探索的场景中可能更具鲁棒性。

### Summary

一种决策策略，智能体选择动作的频率与其估计的概率成正比。

## Key Concepts

- 探索与利用
- 强化学习
- 随机环境
- 决策理论

## Use Cases

- 在心理学实验中模拟人类行为
- 在非平稳多臂老虎机问题中进行稳健探索
- 分析次优学习算法

## Related Terms

- [epsilon-greedy (ε-贪婪策略)](/en/terms/epsilon-greedy-ε-贪婪策略/)
- [softmax_action_selection (Softmax动作选择)](/en/terms/softmax_action_selection-softmax动作选择/)
- [maximizing_strategy (最大化策略)](/en/terms/maximizing_strategy-最大化策略/)
- [exploration_bonus (探索奖励)](/en/terms/exploration_bonus-探索奖励/)
