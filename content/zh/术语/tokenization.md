---
title: "分词"
term_id: "tokenization"
category: "engineering_practice"
subcategory: ""
tags: ["NLP", "preprocessing"]
difficulty: 3
weight: 1
slug: "tokenization"
aliases:
  - /zh/terms/tokenization/
date: "2026-07-18T10:55:25.447575Z"
lastmod: "2026-07-18T11:44:45.386977Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "分词是将原始文本拆分为称为词元的较小单元的过程，这些单元可以被机器学习算法处理。"
---

## Definition

分词是自然语言处理（NLP）中的关键预处理步骤，它将非结构化文本转换为适合模型输入的结构化数据。该过程涉及将句子分解为更小的单元，如单词、子词或字符，以便模型能够有效理解语义。

### Summary

分词是将原始文本拆分为称为词元的较小单元的过程，这些单元可以被机器学习算法处理。

## Key Concepts

- 文本拆分
- 预处理
- WordPiece
- 字节对编码

## Use Cases

- 为BERT训练准备数据集
- GPT模型的输入格式化
- 情感分析的数据清洗

## Code Example

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize('Hello world!')
```

## Related Terms

- [Tokenizer (分词器)](/en/terms/tokenizer-分词器/)
- [Vocabulary (词汇表)](/en/terms/vocabulary-词汇表/)
- [Embedding (嵌入)](/en/terms/embedding-嵌入/)
- [Preprocessing (预处理)](/en/terms/preprocessing-预处理/)
