---
title: "함수 호출"
term_id: "function_calling"
category: "application_paradigms"
subcategory: ""
tags: ["LLM", "Integration", "Agents"]
difficulty: 3
weight: 1
slug: "function_calling"
date: "2026-07-18T15:34:33.739730Z"
lastmod: "2026-07-18T16:38:06.795657Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "함수 호출은 대규모 언어 모델(LLM)이 구조화된 데이터를 출력하여 특정 소프트웨어 함수를 트리거(실행)할 수 있게 하는 메커니즘입니다."
---
## Definition

함수 호출은 대규모 언어 모델이 외부 도구 및 API와 상호작용할 수 있도록 합니다. 모델은 실행할 함수 이름과 필요한 인자(arguments)를 명시하는 JSON 객체와 같은 구조화된 출력을 생성합니다. 이를 통해 LLM은 단순히 텍스트를 생성하는 것을 넘어, 실제 외부 시스템과 연동하여 복잡한 작업을 수행하거나 정확한 실시간 정보를 가져올 수 있습니다.

### Summary

함수 호출은 대규모 언어 모델(LLM)이 구조화된 데이터를 출력하여 특정 소프트웨어 함수를 트리거(실행)할 수 있게 하는 메커니즘입니다.

## Key Concepts

- 구조화된 출력
- API 통합
- 도구 사용
- JSON 스키마

## Use Cases

- 여행 API를 통한 항공권 예약
- 복잡한 수학 계산 수행
- 데이터베이스 레코드 쿼리

## Related Terms

- [ReAct (추론과 행동의 결합 패턴)](/en/terms/react-추론과-행동의-결합-패턴/)
- [Agent (에이전트: 자율적으로 작업을 수행하는 AI 시스템)](/en/terms/agent-에이전트-자율적으로-작업을-수행하는-ai-시스템/)
- [API (응용 프로그램 인터페이스)](/en/terms/api-응용-프로그램-인터페이스/)
- [Tool Use (도구 사용: AI가 외부 도구를 활용하는 것)](/en/terms/tool-use-도구-사용-ai가-외부-도구를-활용하는-것/)
