---
title: "토큰화"
term_id: "tokenization"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "preprocessing"]
difficulty: 3
weight: 1
slug: "tokenization"
aliases:
  - /ko/terms/tokenization/
date: "2026-07-18T15:30:34.141606Z"
lastmod: "2026-07-18T16:38:06.786399Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "토큰화는 기계 학습 알고리즘이 처리할 수 있는 더 작은 단위인 토큰으로 원시 텍스트를 분할하는 과정입니다."
---

## Definition

토큰화는 구조화되지 않은 텍스트를 모델이 섭취하기 적합한 구조화된 데이터로 변환하는 자연어 처리(NLP)의 중요한 전처리 단계입니다. 이는 문장을 여러 단위로 분해하는 과정을 포함합니다.

### Summary

토큰화는 기계 학습 알고리즘이 처리할 수 있는 더 작은 단위인 토큰으로 원시 텍스트를 분할하는 과정입니다.

## Key Concepts

- 텍스트 분할
- 전처리(Preprocessing)
- WordPiece
- 바이트 쌍 부호화(Byte-Pair Encoding)

## Use Cases

- BERT 학습을 위한 데이터셋 준비
- GPT 모델을 위한 입력 포맷팅
- 감성 분석을 위한 데이터 클리닝

## Code Example

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('Hello world!')
```

## Related Terms

- [Tokenizer (토크나이저)](/en/terms/tokenizer-토크나이저/)
- [Vocabulary (어휘)](/en/terms/vocabulary-어휘/)
- [Embedding (임베딩)](/en/terms/embedding-임베딩/)
- [Preprocessing (전처리)](/en/terms/preprocessing-전처리/)
