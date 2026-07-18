---
title: "자연어 처리(Natural Language Processing)"
term_id: "natural_language_processing"
category: "basic_concepts"
subcategory: ""
tags: ["NLP", "AI", "Text Processing"]
difficulty: 3
weight: 1
slug: "natural_language_processing"
aliases:
  - /ko/terms/natural_language_processing/
date: "2026-07-18T15:27:21.460630Z"
lastmod: "2026-07-18T16:38:06.779699Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "컴퓨터가 인간의 언어를 이해하고 해석하며 생성할 수 있도록 하는 인공지능의 한 분야."
---

## Definition

자연어 처리(NLP)는 인공 지능의 하위 분야로, 계산 언어학과 통계적, 기계 학습 및 딥러닝 모델을 결합합니다. 이를 통해 기계는 텍스트나 음성 형태의 인간 언어를 처리하고 이해할 수 있게 됩니다.

### Summary

컴퓨터가 인간의 언어를 이해하고 해석하며 생성할 수 있도록 하는 인공지능의 한 분야.

## Key Concepts

- 토큰화(Tokenization)
- 감성 분석(Sentiment Analysis)
- 개체명 인식(Named Entity Recognition)
- 기계 번역(Machine Translation)

## Use Cases

- 챗봇 및 가상 비서
- 자동 고객 지원
- 언어 번역 서비스

## Code Example

```python
import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp('Apple is looking at buying U.K. startup for $1 billion')
for ent in doc.ents:
    print(ent.text, ent.label_)
```

## Related Terms

- [computational_linguistics (계산 언어학)](/en/terms/computational_linguistics-계산-언어학/)
- [machine_learning (기계 학습)](/en/terms/machine_learning-기계-학습/)
- [deep_learning (딥러닝)](/en/terms/deep_learning-딥러닝/)
- [text_mining (텍스트 마이닝)](/en/terms/text_mining-텍스트-마이닝/)
