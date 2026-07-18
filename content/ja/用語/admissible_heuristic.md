---
title: "許容可能ヒューリスティック"
term_id: "admissible_heuristic"
category: "basic_concepts"
subcategory: ""
tags: ["search_algorithms", "optimization", "graph_theory"]
difficulty: 3
weight: 1
slug: "admissible_heuristic"
aliases:
  - /ja/terms/admissible_heuristic/
date: "2026-07-18T11:03:01.062670Z"
lastmod: "2026-07-18T11:44:45.063796Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "目標への到達コストを過大評価せず、最適性を保証する探索アルゴリズムにおけるヒューリスティック関数。"
---

## Definition

経路探索や探索問題において、許容可能ヒューリスティックは目標ノードへの実際のコストに対する下限値を提供します。推定コストが常に真のコスト以下であることを保証することで、最適解への収束を保証します。

### Summary

目標への到達コストを過大評価せず、最適性を保証する探索アルゴリズムにおけるヒューリスティック関数。

## Key Concepts

- 下限値
- 最適性の保証
- A*探索
- コスト推定

## Use Cases

- GPSナビゲーションのルート計画
- パズル解決（例：8パズル）
- 障害物の多い環境におけるロボットの動作計画

## Related Terms

- [consistent heuristic (整合的ヒューリスティック)](/en/terms/consistent-heuristic-整合的ヒューリスティック/)
- [A* algorithm (A*アルゴリズム)](/en/terms/a-algorithm-a-アルゴリズム/)
- [search optimization (探索最適化)](/en/terms/search-optimization-探索最適化/)
- [pathfinding (経路探索)](/en/terms/pathfinding-経路探索/)
