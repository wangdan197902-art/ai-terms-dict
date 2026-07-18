---
title: "WordPiece"
term_id: "wordpiece"
category: "engineering_practice"
subcategory: ""
tags: ["nlp", "tokenization", "bert"]
difficulty: 3
weight: 1
slug: "wordpiece"
aliases:
  - /ko/terms/wordpiece/
date: "2026-07-18T16:20:48.436305Z"
lastmod: "2026-07-18T16:38:06.920645Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ko"
description: "미출현 단어(OOV)를 처리하기 위해 가장 빈번한 문자 쌍을 재귀적으로 병합하는 서브워드 토큰화 알고리즘입니다."
---

## Definition

WordPiece는 BERT와 ALBERT와 같은 자연어 처리 모델에서 널리 사용되는 토큰화 방법입니다. 이는 단어의 형태론적 풍부함을 관리하고 어휘 범위를 확장하기 위해 단어를 더 작은 서브워드 단위로 분해합니다.

### Summary

미출현 단어(OOV)를 처리하기 위해 가장 빈번한 문자 쌍을 재귀적으로 병합하는 서브워드 토큰화 알고리즘입니다.

## Key Concepts

- 서브워드 토큰화
- 어휘 확장
- 미출현 단어 처리
- 형태론 분석

## Use Cases

- BERT 모델용 텍스트 전처리
- 저자원 언어 처리
- 임베딩 행렬 크기 축소

## Code Example

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('unhappiness')
print(tokens)
```

## Related Terms

- [Byte-Pair Encoding (바이트 페어 인코딩)](/en/terms/byte-pair-encoding-바이트-페어-인코딩/)
- [SentencePiece (센텐스피스)](/en/terms/sentencepiece-센텐스피스/)
- [토큰화 (토큰화)](/en/terms/토큰화-토큰화/)
- [NLP 전처리 (자연어 처리 전처리)](/en/terms/nlp-전처리-자연어-처리-전처리/)
