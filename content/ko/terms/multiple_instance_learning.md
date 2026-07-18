---
title: "다중 인스턴스 학습"
term_id: "multiple_instance_learning"
category: "training_techniques"
subcategory: ""
tags: ["supervised_learning", "weak_labeling", "ml_paradigm"]
difficulty: 4
weight: 1
slug: "multiple_instance_learning"
aliases:
  - /ko/terms/multiple_instance_learning/
date: "2026-07-18T15:35:24.509723Z"
lastmod: "2026-07-18T16:38:06.797780Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "개별 인스턴스가 아닌 인스턴스의 묶음(Bag)에 레이블이 할당되는 약的监督 학습 패러다임입니다."
---

## Definition

다중 인스턴스 학습(Multiple Instance Learning, MIL)은 데이터가 단일 레이블을 가진 '인스턴스 묶음(Bags)'으로 그룹화되고, 그 안의 개별 인스턴스는 레이블이 지정되지 않는 상황을 다룹니다. 일반적으로 묶음에 해당 항목이 하나라도 포함되어 있으면 양수(Positive)로 간주됩니다.(문단이 잘려 있어 완전한 번역은 생략됨)

### Summary

개별 인스턴스가 아닌 인스턴스의 묶음(Bag)에 레이블이 할당되는 약的监督 학습 패러다임입니다.

## Key Concepts

- 묶음 레벨 레이블링(Bag-level labeling)
- 인스턴스 레벨 불확실성(Instance-level uncertainty)
- 약监督 학습(Weak supervision)
- 양수/음수 묶음 논리(Positive/negative bag logic)

## Use Cases

- 약물 활동 예측
- 경계 상자(Bounding Box)가 있는 이미지 분류
- 콘텐츠 기반 이미지 검색

## Related Terms

- [weak_supervision (약监督 학습)](/en/terms/weak_supervision-약监督-학습/)
- [bagging (배깅)](/en/terms/bagging-배깅/)
- [instance_classification (인스턴스 분류)](/en/terms/instance_classification-인스턴스-분류/)
- [label_noise (레이블 노이즈)](/en/terms/label_noise-레이블-노이즈/)
