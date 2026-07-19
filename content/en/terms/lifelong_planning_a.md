---
title: Lifelong Planning A*
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
date: '2026-07-18T10:04:58.089014Z'
lastmod: '2026-07-18T11:44:44.692278Z'
draft: false
source: agnes_llm
status: published
language: en
description: An incremental pathfinding algorithm that efficiently updates shortest
  paths in dynamic graphs without recomputing from scratch after edge weight changes.
---
## Definition

Lifelong Planning A* (LPA*) is an extension of the A* search algorithm designed for environments where costs change over time. Instead of restarting the search, LPA* maintains a priority queue and updates only the affected nodes when edge weights are modified. This makes it highly efficient for robotics and navigation systems operating in partially known or changing terrains, significantly reducing computational overhead compared to standard replanning methods.

### Summary

An incremental pathfinding algorithm that efficiently updates shortest paths in dynamic graphs without recomputing from scratch after edge weight changes.

## Key Concepts

- Incremental Search
- Pathfinding
- Dynamic Graphs
- Robotics Navigation

## Use Cases

- Autonomous vehicle routing in traffic
- Robot navigation in changing warehouses
- Real-time strategy game AI movement

## Related Terms

- [a_star](/en/terms/a_star/)
- [d_star](/en/terms/d_star/)
- [incremental_search](/en/terms/incremental_search/)
- [path_planning](/en/terms/path_planning/)
