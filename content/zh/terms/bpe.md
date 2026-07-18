---
title: "字节对编码 (BPE)"
term_id: "bpe"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "Tokenization", "Data Preprocessing"]
difficulty: 3
weight: 1
slug: "bpe"
aliases:
  - /zh/terms/bpe/
date: "2026-07-18T10:59:27.500261Z"
lastmod: "2026-07-18T11:44:45.397295Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "字节对编码是一种用于子词分词的算法，它通过迭代合并出现频率最高的字符对来构建词汇表。"
---

## Definition

字节对编码（BPE）是一种数据压缩技术，经过调整后应用于自然语言处理中，以处理未登录词（Out-of-Vocabulary）。它从单个字符的词汇表开始，并迭代地合并最频繁出现的字符对，直到达到预定的词汇表大小或收敛。这种方法允许模型将罕见词分解为更常见的子词单元，从而提高对未知词汇的处理能力。

### Summary

字节对编码是一种用于子词分词的算法，它通过迭代合并出现频率最高的字符对来构建词汇表。

## Key Concepts

- 子词分词
- 词汇表合并
- 频率分析
- 未登录词处理

## Use Cases

- 为大语言模型预处理文本
- 处理形态丰富的语言
- 减少神经网络中的词汇表规模

## Code Example

```python
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("unhappiness")
print(tokens)
```

## Related Terms

- [WordPiece (WordPiece分词算法)](/en/terms/wordpiece-wordpiece分词算法/)
- [SentencePiece (SentencePiece分词工具库)](/en/terms/sentencepiece-sentencepiece分词工具库/)
- [Tokenization (分词)](/en/terms/tokenization-分词/)
- [Subword Units (子词单元)](/en/terms/subword-units-子词单元/)
