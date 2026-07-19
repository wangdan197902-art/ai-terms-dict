---
title: 에너지 기반 모델
term_id: energy_based_model
category: basic_concepts
subcategory: ''
tags:
- Generative Models
- probability
- Deep Learning
difficulty: 4
weight: 1
slug: energy_based_model
date: '2026-07-18T15:54:35.962850Z'
lastmod: '2026-07-18T16:38:06.837153Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 가능성 있는 구성에는 낮은 에너지 값을, 불가능한 구성에는 높은 에너지 값을 할당하는 확률 모델입니다.
---
## Definition

에너지 기반 모델(EBM)은 에너지 함수에서 유도된 비정규화 밀도 함수를 사용하여 입력 데이터에 대한 확률 분포를 정의합니다. 에너지 함수는 데이터 포인트를 실수 값으로 매핑하며, 가능성이 높은 데이터는 낮은 에너지를, 가능성이 낮은 데이터는 높은 에너지를 갖습니다.

### Summary

가능성 있는 구성에는 낮은 에너지 값을, 불가능한 구성에는 높은 에너지 값을 할당하는 확률 모델입니다.

## Key Concepts

- 비정규화 확률
- 분배 함수
- 에너지 함수
- 마르코프 연쇄 몬테카를로

## Use Cases

- 이미지 생성 및 인페인팅
- 밀도 추정
- 이상 탐지

## Related Terms

- [볼츠만 머신 (Boltzmann machine)](/en/terms/볼츠만-머신-boltzmann-machine/)
- [딥 볼츠만 머신 (Deep Boltzmann machine)](/en/terms/딥-볼츠만-머신-deep-boltzmann-machine/)
- [변분 추론 (Variational inference)](/en/terms/변분-추론-variational-inference/)
- [확률적 그래피컬 모델 (Probabilistic graphical models)](/en/terms/확률적-그래피컬-모델-probabilistic-graphical-models/)
