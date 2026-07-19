---
title: 액터-크리틱 알고리즘
term_id: actor_critic_algorithm
category: basic_concepts
subcategory: ''
tags:
- Reinforcement Learning
- Neural Networks
- algorithms
difficulty: 4
weight: 1
slug: actor_critic_algorithm
date: '2026-07-18T15:40:10.467247Z'
lastmod: '2026-07-18T16:38:06.805763Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 액터와 크리틱이라는 두 개의 신경망을 사용하여 가치 기반 및 정책 기반 방법을 결합한 강화학습 프레임워크입니다.
---
## Definition

액터-크리틱 알고리즘은 두 가지 구성 요소를 사용합니다. 액터는 행동을 선택하기 위한 정책을 업데이트하고, 크리틱은 가치 함수를 추정하여 해당 행동의 품질을 평가합니다. 이를 통해 정책 경사 방법과 가치 기반 방법의 장점을 통합합니다.

### Summary

액터와 크리틱이라는 두 개의 신경망을 사용하여 가치 기반 및 정책 기반 방법을 결합한 강화학습 프레임워크입니다.

## Key Concepts

- 정책 경사
- 가치 함수
- 시간차 오차
- 하이브리드 강화학습

## Use Cases

- 로봇 팔 조작
- 게임 에이전트 (예: 알파스타)
- 자율주행차의 연속 제어 시스템

## Related Terms

- [PPO (Proximal Policy Optimization, 근접 정책 최적화)](/en/terms/ppo-proximal-policy-optimization-근접-정책-최적화/)
- [A3C (Asynchronous Advantage Actor-Critic, 비동기 이점 액터-크리틱)](/en/terms/a3c-asynchronous-advantage-actor-critic-비동기-이점-액터-크리틱/)
- [policy_gradient (정책 경사)](/en/terms/policy_gradient-정책-경사/)
- [value_function (가치 함수)](/en/terms/value_function-가치-함수/)
