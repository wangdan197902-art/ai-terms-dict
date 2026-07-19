---
title: "在线策略"
term_id: "on_policy"
category: "basic_concepts"
subcategory: ""
tags: ["RL", "algorithms", "learning"]
difficulty: 4
weight: 1
slug: "on_policy"
date: "2026-07-18T10:56:59.123969Z"
lastmod: "2026-07-18T11:44:45.393253Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种强化学习方法，其中被评估和改进的策略与用于生成数据的策略相同。"
---
## Definition

在线策略算法要求智能体直接从其当前策略所采取的动作中学习。这意味着在探索过程中收集的数据被立即用于更新策略，从而确保数据分布的一致性。

### Summary

一种强化学习方法，其中被评估和改进的策略与用于生成数据的策略相同。

## Key Concepts

- 强化学习
- 策略梯度
- 数据一致性
- 样本效率

## Use Cases

- 具有安全约束的机器人控制
- 需要精确更新的博弈代理
- 实时自适应系统

## Related Terms

- [off-policy (离线策略)](/en/terms/off-policy-离线策略/)
- [REINFORCE (REINFORCE算法)](/en/terms/reinforce-reinforce算法/)
- [PPO (近端策略优化)](/en/terms/ppo-近端策略优化/)
- [actor-critic (演员-评论家架构)](/en/terms/actor-critic-演员-评论家架构/)
