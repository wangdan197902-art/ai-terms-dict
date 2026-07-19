---
title: 可容许启发式函数
term_id: admissible_heuristic
category: basic_concepts
subcategory: ''
tags:
- Search Algorithms
- Optimization
- Graph Theory
difficulty: 3
weight: 1
slug: admissible_heuristic
date: '2026-07-18T11:04:13.788389Z'
lastmod: '2026-07-18T11:44:45.438970Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 搜索算法中的一种启发式函数，它从不高估到达目标的真实成本，从而保证最优性。
---
## Definition

在路径查找和搜索问题中，可容许启发式函数提供了到达目标节点实际成本的下界。通过保证估计成本始终小于或等于实际成本，它确保了搜索算法（如A*）能找到最优解。

### Summary

搜索算法中的一种启发式函数，它从不高估到达目标的真实成本，从而保证最优性。

## Key Concepts

- 下界
- 最优性保证
- A*搜索
- 成本估计

## Use Cases

- GPS导航路线规划
- 解谜游戏（如八数码问题）
- 障碍物丰富环境中的机器人运动规划

## Related Terms

- [consistent heuristic (一致启发式函数)](/en/terms/consistent-heuristic-一致启发式函数/)
- [A* algorithm (A*算法)](/en/terms/a-algorithm-a-算法/)
- [search optimization (搜索优化)](/en/terms/search-optimization-搜索优化/)
- [pathfinding (路径查找)](/en/terms/pathfinding-路径查找/)
