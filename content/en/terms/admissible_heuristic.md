---
title: Admissible heuristic
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
date: '2026-07-18T09:44:54.636935Z'
lastmod: '2026-07-18T11:44:44.639176Z'
draft: false
source: agnes_llm
status: published
language: en
description: A heuristic function in search algorithms that never overestimates the
  true cost to reach the goal, ensuring optimality.
---
## Definition

In pathfinding and search problems, an admissible heuristic provides a lower bound on the actual cost to reach the target node. By guaranteeing that the estimated cost is always less than or equal to the real cost, algorithms like A* can ensure they find the shortest path if one exists. This property is critical for maintaining solution optimality while still leveraging heuristics to prune the search space efficiently, balancing speed and accuracy in complex graph traversals.

### Summary

A heuristic function in search algorithms that never overestimates the true cost to reach the goal, ensuring optimality.

## Key Concepts

- Lower bound
- Optimality guarantee
- A* search
- Cost estimation

## Use Cases

- GPS navigation route planning
- Puzzle solving (e.g., 8-puzzle)
- Robot motion planning in obstacle-rich environments

## Related Terms

- [consistent heuristic](/en/terms/consistent-heuristic/)
- [A* algorithm](/en/terms/a-algorithm/)
- [search optimization](/en/terms/search-optimization/)
- [pathfinding](/en/terms/pathfinding/)
