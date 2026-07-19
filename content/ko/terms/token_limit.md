---
title: "토큰 제한"
term_id: "token_limit"
category: "engineering_practice"
subcategory: ""
tags: ["LLM", "constraints", "architecture"]
difficulty: 2
weight: 1
slug: "token_limit"
date: "2026-07-18T15:36:33.156020Z"
lastmod: "2026-07-18T16:38:06.801012Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "AI 모델이 단일 입력 또는 출력 시퀀스에서 처리할 수 있는 토큰의 최대 개수입니다."
---
## Definition

토큰 제한은 대규모 언어 모델의 컨텍스트 윈도우 크기 제약을 정의하며, 한 번에 분석하거나 생성할 수 있는 텍스트의 양을 제한합니다. 이 아키텍처적 경계는 메모리 관리에 영향을 미칩니다.

### Summary

AI 모델이 단일 입력 또는 출력 시퀀스에서 처리할 수 있는 토큰의 최대 개수입니다.

## Key Concepts

- 컨텍스트 윈도우
- 잘라내기(Truncation)
- 프롬프트 엔지니어링
- 메모리 관리

## Use Cases

- RAG 시스템 설계
- 프롬프트 길이 최적화
- 긴 문서 처리

## Related Terms

- [context_window (컨텍스트 윈도우)](/en/terms/context_window-컨텍스트-윈도우/)
- [embedding (임베딩)](/en/terms/embedding-임베딩/)
- [chunking (청킹)](/en/terms/chunking-청킹/)
- [prompt_tuning (프롬프트 튜닝)](/en/terms/prompt_tuning-프롬프트-튜닝/)
