---
title: "커리큘럼 학습(Curriculum Learning)"
term_id: "curriculum_learning"
category: "training_techniques"
subcategory: ""
tags: ["optimization", "training_strategy"]
difficulty: 3
weight: 1
slug: "curriculum_learning"
aliases:
  - /ko/terms/curriculum_learning/
date: "2026-07-18T16:21:03.346737Z"
lastmod: "2026-07-18T16:38:06.921512Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "모델이 쉬운 예시부터 학습한 후 점차 어려운 예시로 나아가는 학습 전략입니다."
---

## Definition

커리큘럼 학습은 인간의 교육 방식을 모방하여, 학습 데이터를 단순한 샘플부터 시작해 점진적으로 복잡성을 증가시키는 구조화된 순서로 제시합니다. 이 접근법은 신경망이 전역 최적점(global optimum)으로 수렴하는 속도를 높이고, 일반화 성능을 향상시키는 데 도움을 줍니다.

### Summary

모델이 쉬운 예시부터 학습한 후 점차 어려운 예시로 나아가는 학습 전략입니다.

## Key Concepts

- 점진적 난이도(Progressive Difficulty)
- 샘플 시퀀싱(Sample Sequencing)
- 수렴 속도(Convergence Speed)
- 일반화(Generalization)

## Use Cases

- 복잡한 이미지 데이터셋에 대한 심층 신경망 훈련
- 다양한 문장 난이도를 가진 언어 모델링
- 희소 보상(sparse rewards)이 있는 강화학습 작업

## Related Terms

- [Transfer Learning (전이 학습)](/en/terms/transfer-learning-전이-학습/)
- [Hard Negative Mining (하드 네거티브 마이닝)](/en/terms/hard-negative-mining-하드-네거티브-마이닝/)
- [Data Augmentation (데이터 증강)](/en/terms/data-augmentation-데이터-증강/)
- [Self-Paced Learning (자율 paced 학습)](/en/terms/self-paced-learning-자율-paced-학습/)
