---
title: "백도어 공격(Backdoor Attack)"
term_id: "backdoor_attack"
category: "ethics_safety"
subcategory: ""
tags: ["AI Security", "Ethics", "Adversarial ML"]
difficulty: 4
weight: 1
slug: "backdoor_attack"
aliases:
  - /ko/terms/backdoor_attack/
date: "2026-07-18T16:21:03.346707Z"
lastmod: "2026-07-18T16:38:06.921397Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "악의적 행위자가 모델 학습 중 숨겨진 트리거를 삽입하여 특정 조건에서 오분류를 유발하는 보안 위협입니다."
---

## Definition

백도어 공격은 머신러닝 모델의 학습 데이터에 '트리거'라고 불리는 특정 패턴을 포함시켜 데이터를 오염시키는 기법입니다. 정상적인 입력 데이터에 대해서는 모델이 일반적으로 높은 성능을 보이지만, 악의적으로 삽입된 트리거가 포함된 입력이 들어오면 의도한 잘못된 분류나 출력을 수행하도록 모델을 조작합니다.

### Summary

악의적 행위자가 모델 학습 중 숨겨진 트리거를 삽입하여 특정 조건에서 오분류를 유발하는 보안 위협입니다.

## Key Concepts

- 데이터 오염(Data Poisoning)
- 모델 무결성(Model Integrity)
- 적대적 머신러닝(Adversarial Machine Learning)
- 트리거 패턴(Trigger Patterns)

## Use Cases

- ML 파이프라인의 보안 테스트
- 방어 필터 개발
- 타사 모델 감사(Auditing)

## Related Terms

- [Adversarial Examples (적대적 예시)](/en/terms/adversarial-examples-적대적-예시/)
- [Data Poisoning (데이터 오염)](/en/terms/data-poisoning-데이터-오염/)
- [Model Robustness (모델 강건성)](/en/terms/model-robustness-모델-강건성/)
- [Clean Label Attacks (클린 라벨 공격)](/en/terms/clean-label-attacks-클린-라벨-공격/)
