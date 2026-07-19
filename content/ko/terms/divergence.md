---
title: 발산(Divergence)
term_id: divergence
category: basic_concepts
subcategory: ''
tags:
- Optimization
- stability
- debugging
difficulty: 2
weight: 1
slug: divergence
date: '2026-07-18T15:23:57.551295Z'
lastmod: '2026-07-18T16:38:06.771797Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 훈련 중 머신러닝 알고리즘의 손실 함수가 감소하지 않아 불안정하거나 악화되는 성능을 보이는 현상.
---
## Definition

최적화 관점에서 발산은 모델의 파라미터 업데이트가 손실을 감소시키지 않고 오히려 증가시킬 때 발생합니다. 이는 종종 NaN 값이나 무한大的인 그래디언트, 그리고 학습 과정의 불안정으로 이어집니다.

### Summary

훈련 중 머신러닝 알고리즘의 손실 함수가 감소하지 않아 불안정하거나 악화되는 성능을 보이는 현상.

## Key Concepts

- 손실 폭발(Loss Explosion)
- 학습률 민감도(Learning Rate Sensitivity)
- 그래디언트 불안정성(Gradient Instability)
- 수치 정밀도(Numerical Precision)

## Use Cases

- 딥러닝 프레임워크의 훈련 루프 디버깅
- 안정적인 수렴을 위한 하이퍼파라미터 튜닝
- 그래디언트 클리핑 전략 구현

## Related Terms

- [Vanishing Gradient (소멸 그래디언트)](/en/terms/vanishing-gradient-소멸-그래디언트/)
- [Exploding Gradient (폭발 그래디언트)](/en/terms/exploding-gradient-폭발-그래디언트/)
- [Convergence (수렴)](/en/terms/convergence-수렴/)
- [Stability (안정성)](/en/terms/stability-안정성/)
