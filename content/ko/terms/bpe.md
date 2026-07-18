---
title: "BPE(바이트 페어 인코딩)"
term_id: "bpe"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "Tokenization", "Data Preprocessing"]
difficulty: 3
weight: 1
slug: "bpe"
aliases:
  - /ko/terms/bpe/
date: "2026-07-18T15:33:36.473862Z"
lastmod: "2026-07-18T16:38:06.793076Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "가장 빈번하게 나타나는 문자 쌍을 반복적으로 병합하여 어휘를 구축하는 서브워드 토큰화 알고리즘입니다."
---

## Definition

바이트 페어 인코딩(BPE)은 낯선 단어(out-of-vocabulary)를 처리하기 위해 자연어 처리에 적용된 데이터 압축 기술입니다. 개별 문자로 구성된 어휘로 시작하여, 통계적으로 가장 자주 함께 나타나는 문자 쌍을 찾아 하나의 토큰으로 병합하는 과정을 반복합니다. 이 방법은 단어의 의미를 해치지 않으면서도 어휘 크기를 제한하고, 희귀어나 신조어를 효과적으로 처리할 수 있게 합니다.

### Summary

가장 빈번하게 나타나는 문자 쌍을 반복적으로 병합하여 어휘를 구축하는 서브워드 토큰화 알고리즘입니다.

## Key Concepts

- 서브워드 토큰화
- 어휘 병합
- 빈도 분석
- 미등재 단어 처리

## Use Cases

- 대규모 언어 모델을 위한 텍스트 전처리
- 형태소가 풍부한 언어 처리
- 신경망의 어휘 크기 축소

## Code Example

```python
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("unhappiness")
print(tokens)
```

## Related Terms

- [WordPiece](/en/terms/wordpiece/)
- [SentencePiece](/en/terms/sentencepiece/)
- [토큰화](/en/terms/토큰화/)
- [서브워드 유닛](/en/terms/서브워드-유닛/)
