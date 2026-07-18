---
title: "Transformers"
term_id: "transformers"
category: "training_techniques"
subcategory: ""
tags: ["library", "tools", "ecosystem"]
difficulty: 2
weight: 1
slug: "transformers"
aliases:
  - /ko/terms/transformers/
date: "2026-07-18T15:30:47.132125Z"
lastmod: "2026-07-18T16:38:06.786860Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "이 맥락에서는 최신 자연어 처리(NLP) 및 멀티모달 모델을 위한 인기 있는 오픈소스 도구キット인 Hugging Face Transformers 라이브러리를 지칭합니다."
---

## Definition

'Transformers'라는 용어는 종종 Hugging Face가 유지 관리하는 널리 사용되는 Python 라이브러리를 가리킵니다. 이 라이브러리는 사전 훈련된 모델의 다운로드, 학습 및 배포를 위한 사용하기 쉬운 인터페이스를 제공하며, 주로 트랜스포머 아키텍처를 기반으로 합니다.

### Summary

이 맥락에서는 최신 자연어 처리(NLP) 및 멀티모달 모델을 위한 인기 있는 오픈소스 도구キット인 Hugging Face Transformers 라이브러리를 지칭합니다.

## Key Concepts

- Hugging Face Hub
- Pipeline API
- Model Cards
- Tokenizer Integration

## Use Cases

- NLP 애플리케이션의 빠른 프로토타이핑
- 커뮤니티에서 사전 훈련한 모델 접근
- 모델 배포 워크플로우 표준화

## Code Example

```python
from transformers import pipeline
classifier = pipeline('sentiment-analysis')
```

## Related Terms

- [hugging_face (허깅 페이스)](/en/terms/hugging_face-허깅-페이스/)
- [pipeline (파이프라인 API)](/en/terms/pipeline-파이프라인-api/)
- [tokenizer (토크나이저)](/en/terms/tokenizer-토크나이저/)
- [pytorch (파이토치)](/en/terms/pytorch-파이토치/)
