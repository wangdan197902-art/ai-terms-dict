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
  - /zh/terms/wordpiece/
date: "2026-07-18T11:38:14.659800Z"
lastmod: "2026-07-18T11:44:45.569181Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种子词分词算法，通过递归合并最频繁出现的字符对来处理未登录词（OOV）。"
---

## Definition

WordPiece 是一种广泛应用于 BERT 和 ALBERT 等自然语言处理模型的分词方法。它将单词分解为更小的子词单元，以应对形态学丰富性并减少词汇表大小，从而更好地处理未见过的单词。

### Summary

一种子词分词算法，通过递归合并最频繁出现的字符对来处理未登录词（OOV）。

## Key Concepts

- 子词分词
- 词汇扩展
- 未登录词处理
- 形态分析

## Use Cases

- 为 BERT 模型预处理文本
- 处理低资源语言
- 减小嵌入矩阵大小

## Code Example

```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('unhappiness')
print(tokens)
```

## Related Terms

- [字节对编码 (Byte-Pair Encoding)](/en/terms/字节对编码-byte-pair-encoding/)
- [SentencePiece](/en/terms/sentencepiece/)
- [分词 (Tokenization)](/en/terms/分词-tokenization/)
- [NLP 预处理 (NLP preprocessing)](/en/terms/nlp-预处理-nlp-preprocessing/)
