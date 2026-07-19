---
title: 곱승 가중치 업데이트 방법
term_id: multiplicative_weight_update_method
category: basic_concepts
subcategory: ''
tags:
- Optimization
- Online Learning
- algorithm
difficulty: 3
weight: 1
slug: multiplicative_weight_update_method
date: '2026-07-18T16:07:11.441780Z'
lastmod: '2026-07-18T16:38:06.888211Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 후회(regret)를 최소화하기 위해 성능 피드백에 기반하여 가중치를 곱셈 방식으로 업데이트하는 반복형 알고리즘입니다.
---
## Definition

곱승 가중치 업데이트 방법(Multiplicative Weight Update Method)은 불확실한 환경에서 의사결정을 내리기 위해 사용되는 기본 온라인 학습 알고리즘입니다. 이 방법은 다양한 전략이나 전문가 집단에 대해 일련의 가중치를 유지하며, 각 단계에서의 성능에 따라 가중치를 지수적으로 조정합니다. 이를 통해 장기적으로 후회를 최소화하고 최적의 선택에 수렴하도록 유도합니다.

### Summary

후회(regret)를 최소화하기 위해 성능 피드백에 기반하여 가중치를 곱셈 방식으로 업데이트하는 반복형 알고리즘입니다.

## Key Concepts

- 온라인 학습
- 가중치 다수결 알고리즘
- 후회 최소화
- 지수 가중치

## Use Cases

- 포트폴리오 최적화
- 전문가 조언 집계
- 적대적 밴딧 문제

## Related Terms

- [gradient_descent (경사 하강법)](/en/terms/gradient_descent-경사-하강법/)
- [online_learning (온라인 학습)](/en/terms/online_learning-온라인-학습/)
- [regret_bound (후회 한계)](/en/terms/regret_bound-후회-한계/)
- [boosting (부스팅)](/en/terms/boosting-부스팅/)
