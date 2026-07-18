---
title: "Extremal optimization"
term_id: "extremal_optimization"
category: "training_techniques"
subcategory: ""
tags: ["Optimization", "Heuristics", "Algorithms"]
difficulty: 4
weight: 1
slug: "extremal_optimization"
aliases:
  - /en/terms/extremal_optimization/
date: "2026-07-18T09:57:38.908722Z"
lastmod: "2026-07-18T11:44:44.671440Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Extremal optimization is a heuristic search algorithm inspired by self-organized criticality, designed to solve combinatorial optimization problems by iteratively removing the worst-performing compone"
---

## Definition

Unlike genetic algorithms that maintain a population, EO works on a single solution. It identifies the component contributing least to the overall fitness and replaces it with a random alternative. This process continues until a satisfactory solution is found. It is particularly effective for NP-hard problems where traditional gradient-based methods fail. The algorithm mimics natural selection at a microscopic level, focusing on local improvements to achieve global optimization.

### Summary

Extremal optimization is a heuristic search algorithm inspired by self-organized criticality, designed to solve combinatorial optimization problems by iteratively removing the worst-performing components.

## Key Concepts

- Heuristic Search
- Combinatorial Optimization
- Self-Organized Criticality
- Local Improvement

## Use Cases

- Graph partitioning problems
- Scheduling tasks in computing clusters
- Optimizing network routing paths

## Related Terms

- [Genetic Algorithms](/en/terms/genetic-algorithms/)
- [Simulated Annealing](/en/terms/simulated-annealing/)
- [Particle Swarm Optimization](/en/terms/particle-swarm-optimization/)
- [Metaheuristics](/en/terms/metaheuristics/)
