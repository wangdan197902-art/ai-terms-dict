---
title: "평생 계획 A* (Lifelong Planning A*)"
term_id: "lifelong_planning_a"
category: "application_paradigms"
subcategory: ""
tags: ["algorithms", "robotics", "graph_theory"]
difficulty: 4
weight: 1
slug: "lifelong_planning_a"
aliases:
  - /ko/terms/lifelong_planning_a/
date: "2026-07-18T16:02:32.715302Z"
lastmod: "2026-07-18T16:38:06.862645Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "간선 가중치 변경 후 처음부터 다시 계산하지 않고도 동적 그래프에서 최단 경로를 효율적으로 업데이트하는 증분 경로 탐색 알고리즘입니다."
---

## Definition

평생 계획 A*(LPA*)는 비용이 시간에 따라 변하는 환경을 위해 설계된 A* 탐색 알고리즘의 확장 버전입니다. LPA*는 탐색을 재시작하는 대신 우선순위 큐를 유지하고 이전 탐색 결과를 활용하여 경로를 점진적으로 업데이트합니다.

### Summary

간선 가중치 변경 후 처음부터 다시 계산하지 않고도 동적 그래프에서 최단 경로를 효율적으로 업데이트하는 증분 경로 탐색 알고리즘입니다.

## Key Concepts

- 증분 탐색
- 경로 탐색
- 동적 그래프
- 로봇 내비게이션

## Use Cases

- 교통 상황에서의 자율주행 차량 경로 최적화
- 변화하는 창고 환경에서의 로봇 내비게이션
- 실시간 전략 게임 AI의 이동 로직

## Related Terms

- [a_star (A* 알고리즘)](/en/terms/a_star-a-알고리즘/)
- [d_star (D* 알고리즘)](/en/terms/d_star-d-알고리즘/)
- [incremental_search (증분 탐색)](/en/terms/incremental_search-증분-탐색/)
- [path_planning (경로 계획)](/en/terms/path_planning-경로-계획/)
