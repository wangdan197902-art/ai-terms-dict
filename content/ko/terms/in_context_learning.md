---
title: "컨텍스트 내 학습 (In-Context Learning)"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
date: "2026-07-18T15:22:46.628524Z"
lastmod: "2026-07-18T16:38:06.767240Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "프롬프트에 제공된 예시를 관찰하여 작업을 수행하도록 모델을 학습시키는 기법."
---
## Definition

컨텍스트 내 학습(ICL)은 대규모 언어 모델이 가중치를 업데이트하지 않고도 새로운 작업에 적응할 수 있게 합니다. 프롬프트 컨텍스트 내에 입력-출력 쌍을 제공함으로써 모델은 패턴을 추론하고 작업을 수행합니다.

### Summary

프롬프트에 제공된 예시를 관찰하여 작업을 수행하도록 모델을 학습시키는 기법.

## Key Concepts

- 퓨 샷 학습 (Few-Shot Learning)
- 제로 샷 (Zero-Shot)
- 프롬프트 설계 (Prompt Design)
- 가중치 없는 적응 (Weight-Free Adaptation)

## Use Cases

- 새로운 데이터셋에 대한 모델 능력 신속 테스트
- 대화형 에이전트에서의 동적 작업 전환
- 재학습 없이 AI 애플리케이션 프로토타이핑

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Prompt Engineering (프롬프트 엔지니어링)](/en/terms/prompt-engineering-프롬프트-엔지니어링/)
- [Few-Shot (퓨 샷)](/en/terms/few-shot-퓨-샷/)
- [Zero-Shot (제로 샷)](/en/terms/zero-shot-제로-샷/)
- [Meta-Learning (메타러닝)](/en/terms/meta-learning-메타러닝/)
