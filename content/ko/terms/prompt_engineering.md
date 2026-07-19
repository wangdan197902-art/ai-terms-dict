---
title: "프롬프트 엔지니어링"
term_id: "prompt_engineering"
category: "application_paradigms"
subcategory: ""
tags: ["LLM", "UX", "Optimization"]
difficulty: 2
weight: 1
slug: "prompt_engineering"
date: "2026-07-18T13:43:38.774818Z"
lastmod: "2026-07-18T16:38:06.764620Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "대규모 언어 모델이 원하는 출력을 생성하도록 유도하기 위해 입력 텍스트를 설계하고 최적화하는 관행."
---
## Definition

프롬프트 엔지니어링은 생성형 AI 모델로부터 정확하고 관련성이 높으며 고품질의 응답을 이끌어내기 위해 '프롬프트'라고 불리는 특정 입력을 구성하는 작업을 포함합니다. 이는 모델이 프롬프트를 어떻게 해석하는지에 대한 이해가 필요하며, 문맥적 프레임 설정, 퓨샷 학습(Few-shot learning), 지시어 튜닝(Instruction tuning), 토큰 최적화(Token optimization) 등의 기법을 활용하여 모델의 성능을 극대화합니다.

### Summary

대규모 언어 모델이 원하는 출력을 생성하도록 유도하기 위해 입력 텍스트를 설계하고 최적화하는 관행.

## Key Concepts

- 문맥적 프레임 설정(Contextual framing)
- 퓨샷 학습(Few-shot learning)
- 지시어 튜닝(Instruction tuning)
- 토큰 최적화(Token optimization)

## Use Cases

- 자동화된 고객 지원 챗봇
- 코드 생성 보조 도구
- 창작 글쓰기 지원 도구

## Code Example

```python
prompt = "Translate the following English text to French: 'Hello world'"
response = llm.generate(prompt)
```

## Related Terms

- [LLM (대규모 언어 모델)](/en/terms/llm-대규모-언어-모델/)
- [Chain-of-Thought (사고의 사슬)](/en/terms/chain-of-thought-사고의-사슬/)
- [RAG (검색 증강 생성)](/en/terms/rag-검색-증강-생성/)
- [Fine-tuning (파인튜닝/미세 조정)](/en/terms/fine-tuning-파인튜닝-미세-조정/)
