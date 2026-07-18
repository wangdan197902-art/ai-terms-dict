---
title: "생각의 사슬 프롬프팅"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
aliases:
  - /ko/terms/chain_of_thought_prompting/
date: "2026-07-18T15:33:51.302484Z"
lastmod: "2026-07-18T16:38:06.793302Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "생각의 사슬 프롬프팅은 대규모 언어 모델(LLM)이 최종 답변을 생성하기 전에 중간 추론 단계를 생성하도록 유도하는 기법입니다."
---

## Definition

생각의 사슬(Chain-of-Thought, CoT) 프롬프팅은 모델에게 단계별 논리를 명시적으로 서술하도록 요청함으로써 복잡한 추론 작업에서 대규모 언어 모델의 성능을 향상시킵니다. 이는 답으로 바로 뛰어들기보다(Instead of jumping directly to the answer), 문제 해결 과정을 단계별로 설명하도록 함으로써 모델의 추론 능력을 강화합니다.

### Summary

생각의 사슬 프롬프팅은 대규모 언어 모델(LLM)이 최종 답변을 생성하기 전에 중간 추론 단계를 생성하도록 유도하는 기법입니다.

## Key Concepts

- 단계별 추론
- 소수 예시 학습(Few-Shot Learning)
- 논리적 귀결
- 중간 단계

## Use Cases

- 수학적 응용문제 풀이
- 복잡한 논리적 추론 작업
- 코드 생성 오류 디버깅

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Zero-Shot Prompting (제로샷 프롬프팅: 예시 없이 프롬프트하는 방식)](/en/terms/zero-shot-prompting-제로샷-프롬프팅-예시-없이-프롬프트하는-방식/)
- [Few-Shot Prompting (퓨샷 프롬프팅: 소수의 예시를 제공하여 프롬프트하는 방식)](/en/terms/few-shot-prompting-퓨샷-프롬프팅-소수의-예시를-제공하여-프롬프트하는-방식/)
- [Self-Consistency (자기 일관성: 여러 추론 경로를 통해 가장 빈번한 답변을 선택하는 기법)](/en/terms/self-consistency-자기-일관성-여러-추론-경로를-통해-가장-빈번한-답변을-선택하는-기법/)
- [Reasoning (추론: 논리적 과정을 통해 결론에 도달하는 능력)](/en/terms/reasoning-추론-논리적-과정을-통해-결론에-도달하는-능력/)
