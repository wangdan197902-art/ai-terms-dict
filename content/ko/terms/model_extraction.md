---
title: 모델 추출
term_id: model_extraction
category: ethics_safety
subcategory: ''
tags:
- security
- Adversarial ML
difficulty: 4
weight: 1
slug: model_extraction
date: '2026-07-18T16:21:14.229473Z'
lastmod: '2026-07-18T16:38:06.921740Z'
draft: false
source: agnes_llm
status: published
language: ko
description: 적대적 공격자가 모델을 쿼리하여 매개변수를 재구성하거나 대리 모델(surrogate model)을 생성하는 공격 방식입니다.
---
## Definition

모델 추출은 대상 머신러닝 모델의 API를 쿼리하여 내부 구조, 가중치 또는 의사결정 경로를 추론하는 과정을 포함합니다. 공격자는 이러한 쿼리를 사용하여 원본 모델의 동작을 모방하는 대리 모델을 구축합니다.

### Summary

적대적 공격자가 모델을 쿼리하여 매개변수를 재구성하거나 대리 모델(surrogate model)을 생성하는 공격 방식입니다.

## Key Concepts

- 대리 모델링
- API 쿼리
- 지적 재산권 도난
- 적대적 공격

## Use Cases

- 상업용 AI API의 보안 감사
- 독점 알고리즘의 복제 방지
- 추출 공격에 대한 방어 메커니즘 연구

## Related Terms

- [Membership Inference (멤버십 추론)](/en/terms/membership-inference-멤버십-추론/)
- [Adversarial Examples (적대적 예시)](/en/terms/adversarial-examples-적대적-예시/)
- [Model Watermarking (모델 워터마킹)](/en/terms/model-watermarking-모델-워터마킹/)
- [API Security (API 보안)](/en/terms/api-security-api-보안/)
