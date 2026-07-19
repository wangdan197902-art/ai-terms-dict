---
title: 文本摘要
term_id: summarization
category: application_paradigms
subcategory: ''
tags:
- NLP
- Text Processing
- applications
difficulty: 3
weight: 1
slug: summarization
date: '2026-07-18T11:02:04.102303Z'
lastmod: '2026-07-18T11:44:45.406354Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一项自然语言处理任务，生成较长文本的简洁连贯摘要，同时保留其关键信息。
---
## Definition

文本摘要将大量文本缩减为较短版本，而不丢失核心含义。它可以是抽取式的，即从源文本中选择重要句子；也可以是抽象式的，即生成新的概括性语句。

### Summary

一项自然语言处理任务，生成较长文本的简洁连贯摘要，同时保留其关键信息。

## Key Concepts

- 抽取式摘要
- 抽象式摘要
- 信息密度
- 连贯性

## Use Cases

- 新闻文章精简
- 会议纪要生成
- 法律文档审查

## Code Example

```python
from transformers import pipeline
summarizer = pipeline("summarization")
result = summarizer("AI is transforming industries...", max_length=50, min_length=10)[0]['summary_text']
```

## Related Terms

- [自然语言处理 (NLP)](/en/terms/自然语言处理-nlp/)
- [Transformer 模型](/en/terms/transformer-模型/)
- [BERT](/en/terms/bert/)
- [T5](/en/terms/t5/)
