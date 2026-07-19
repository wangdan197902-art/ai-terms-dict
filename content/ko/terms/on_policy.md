---
title: "온-폴리시(on-policy)"
term_id: "on_policy"
category: "basic_concepts"
subcategory: ""
tags: ["RL", "algorithms", "learning"]
difficulty: 4
weight: 1
slug: "on_policy"
date: "2026-07-18T15:32:17.763813Z"
lastmod: "2026-07-18T16:38:06.790542Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "평가 및 개선되는 정책이 데이터를 생성하는 데 사용되는 정책과 동일한 강화학습 접근 방식입니다."
---
## Definition

온-폴리시 알고리즘은 에이전트가 현재 정책이 취한 행동으로부터 직접 학습하도록 요구합니다. 이는 탐색 중에 수집된 데이터가 정책을 업데이트하는 데 즉시 사용되어 일관성을 보장함을 의미합니다.

### Summary

평가 및 개선되는 정책이 데이터를 생성하는 데 사용되는 정책과 동일한 강화학습 접근 방식입니다.

## Key Concepts

- 강화학습(reinforcement learning)
- 정책 경사(policy gradient)
- 데이터 일관성(data consistency)
- 샘플 효율성(sample efficiency)

## Use Cases

- 안전 제약이 있는 로봇 제어
- 정확한 업데이트가 필요한 게임 에이전트
- 실시간 적응 시스템

## Related Terms

- [off-policy (오프-폴리시)](/en/terms/off-policy-오프-폴리시/)
- [REINFORCE (REINFORCE 알고리즘)](/en/terms/reinforce-reinforce-알고리즘/)
- [PPO (프로크시 폴시 최적화)](/en/terms/ppo-프로크시-폴시-최적화/)
- [actor-critic (액터-크리틱)](/en/terms/actor-critic-액터-크리틱/)
