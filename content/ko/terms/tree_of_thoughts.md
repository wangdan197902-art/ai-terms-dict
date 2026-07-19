---
title: "사고의 나무(Tree of Thoughts)"
term_id: "tree_of_thoughts"
category: "training_techniques"
subcategory: ""
tags: ["reasoning", "prompting", "algorithms"]
difficulty: 4
weight: 1
slug: "tree_of_thoughts"
date: "2026-07-18T16:19:06.777548Z"
lastmod: "2026-07-18T16:38:06.917255Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "여러 가능한 추론 경로를 동시에 탐색하고 평가하여 가장 유망한 다음 단계를 선택하는 추론 프레임워크입니다."
---
## Definition

사고의 나무(ToT)는 기존 사슬 사고(chain-of-thought) 프롬프팅을 확장하여, 모델이 각 단계에서 여러 개의 서로 다른 추론 경로를 탐색할 수 있도록 합니다. 이는 트리 구조를 형성하며, 모델은 각 상태의 가치를 평가하여 최선의 다음 단계를 선택하거나 필요시 되돌아가(backtrack) 다른 경로를 시도합니다.

### Summary

여러 가능한 추론 경로를 동시에 탐색하고 평가하여 가장 유망한 다음 단계를 선택하는 추론 프레임워크입니다.

## Key Concepts

- 검색 알고리즘
- 되돌리기(Backtracking)
- 상태 평가
- 추론 경로

## Use Cases

- 복잡한 수학 문제 해결
- 창의적 글쓰기 생성
- 전략적 게임 플레이

## Related Terms

- [Chain of Thought (사슬 사고)](/en/terms/chain-of-thought-사슬-사고/)
- [Beam Search (빔 서치)](/en/terms/beam-search-빔-서치/)
- [Reinforcement Learning (강화 학습)](/en/terms/reinforcement-learning-강화-학습/)
- [Reasoning (추론)](/en/terms/reasoning-추론/)
