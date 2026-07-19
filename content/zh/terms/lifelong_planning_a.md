---
title: 终身规划A*算法
term_id: lifelong_planning_a
category: application_paradigms
subcategory: ''
tags:
- algorithms
- robotics
- Graph Theory
difficulty: 4
weight: 1
slug: lifelong_planning_a
date: '2026-07-18T11:24:07.939926Z'
lastmod: '2026-07-18T11:44:45.524763Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种增量式路径查找算法，能够在边权重发生变化后，无需从头重新计算即可高效地更新最短路径。
---
## Definition

终身规划A*（LPA*）是为成本随时间变化的环境设计的A*搜索算法的扩展。与重新启动搜索不同，LPA*维护一个优先级队列并仅更新受更改影响的节点，从而显著提高了在动态图环境中重新规划路径的效率。

### Summary

一种增量式路径查找算法，能够在边权重发生变化后，无需从头重新计算即可高效地更新最短路径。

## Key Concepts

- 增量搜索
- 路径查找
- 动态图
- 机器人导航

## Use Cases

- 交通中的自动驾驶车辆路线规划
- 变化仓库中的机器人导航
- 实时战略游戏中的AI移动

## Related Terms

- [a_star (A*算法)](/en/terms/a_star-a-算法/)
- [d_star (D*算法)](/en/terms/d_star-d-算法/)
- [incremental_search (增量搜索)](/en/terms/incremental_search-增量搜索/)
- [path_planning (路径规划)](/en/terms/path_planning-路径规划/)
