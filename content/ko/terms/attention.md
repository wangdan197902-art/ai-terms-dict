---
title: "어텐션(주의 메커니즘)"
term_id: "attention"
category: "training_techniques"
subcategory: ""
tags: ["transformers", "mechanism", "sequence", "core_concept"]
difficulty: 4
weight: 1
slug: "attention"
aliases:
  - /ko/terms/attention/
date: "2026-07-18T15:33:36.473855Z"
lastmod: "2026-07-18T16:38:06.792958Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "신경망이 입력 시퀀스의 서로 다른 부분에 대한 중요도를 동적으로 가중치 부여할 수 있도록 하는 메커니즘입니다."
---

## Definition

어텐션 메커니즘은 모델이 입력을 처리할 때 관련 정보에 집중할 수 있게 합니다. 특히 텍스트와 같은 순차적 데이터에서 어텐션 스코어를 계산함으로써 모델은 현재 처리 중인 요소와 입력 시퀀스의 다른 요소들 간의 관계를 파악합니다. 이를 통해 모델은 문맥을 더 잘 이해하고, 긴 시퀀스에서도 중요한 정보를 놓치지 않으며, 장기 의존성 문제를 해결할 수 있습니다.

### Summary

신경망이 입력 시퀀스의 서로 다른 부분에 대한 중요도를 동적으로 가중치 부여할 수 있도록 하는 메커니즘입니다.

## Key Concepts

- 셀프 어텐션
- 맥락적 가중치 부여
- 장기 의존성
- 트랜스포머 아키텍처

## Use Cases

- 언어 간 기계 번역
- 긴 문서 요약
- 이미지 캡셔닝 및 시각적 질문 답변

## Related Terms

- [트랜스포머](/en/terms/트랜스포머/)
- [셀프 어텐션](/en/terms/셀프-어텐션/)
- [멀티 헤드 어텐션](/en/terms/멀티-헤드-어텐션/)
- [순서 모델링](/en/terms/순서-모델링/)
