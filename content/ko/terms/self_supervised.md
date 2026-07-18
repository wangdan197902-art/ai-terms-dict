---
title: "자기지도학습"
term_id: "self_supervised"
category: "training_techniques"
subcategory: ""
tags: ["learning_paradigms", "nlp", "scalability"]
difficulty: 4
weight: 1
slug: "self_supervised"
aliases:
  - /ko/terms/self_supervised/
date: "2026-07-18T15:32:52.125860Z"
lastmod: "2026-07-18T16:38:06.791583Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "자기지도학습은 모델이 인간의 주석 없이 입력 데이터로부터 자체적으로 라벨을 생성하여 표현을 학습하는 기법입니다."
---

## Definition

자기지도학습은 기계학습의 하위 분야로, 감독 신호가 수동 레이블링 없이 데이터 자체에서 자동으로 유도됩니다. 모델은 일반적으로 데이터의 구조를 활용하여 숨겨진 패턴이나 관계를 예측하는 과제를 해결함으로써 특징을 학습합니다.

### Summary

자기지도학습은 모델이 인간의 주석 없이 입력 데이터로부터 자체적으로 라벨을 생성하여 표현을 학습하는 기법입니다.

## Key Concepts

- 프텍스트 태스크(Pretext Tasks)
- 마스킹 모델링(Masked Modeling)
- 라벨 없는 데이터(Unlabeled Data)
- 표현 학습(Representation Learning)

## Use Cases

- 마스킹 언어 모델링을 통한 BERT 학습
- 이미지 임베딩을 위한 대비 학습(Contrastive Learning)
- 대규모 언어모델(LLM)에서의 다음 토큰 예측

## Related Terms

- [unsupervised (비지도학습)](/en/terms/unsupervised-비지도학습/)
- [contrastive_learning (대조 학습)](/en/terms/contrastive_learning-대조-학습/)
- [masked_language_modeling (마스킹 언어 모델링)](/en/terms/masked_language_modeling-마스킹-언어-모델링/)
- [representation_learning (표현 학습)](/en/terms/representation_learning-표현-학습/)
