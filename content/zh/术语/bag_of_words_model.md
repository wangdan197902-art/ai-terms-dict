---
title: "词袋模型"
term_id: "bag_of_words_model"
category: "basic_concepts"
subcategory: ""
tags: ["NLP", "text-processing", "feature-engineering"]
difficulty: 2
weight: 1
slug: "bag_of_words_model"
aliases:
  - /zh/terms/bag_of_words_model/
date: "2026-07-18T11:08:27.712975Z"
lastmod: "2026-07-18T11:44:45.449134Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "词袋模型是一种简化的文本表示方法，描述文档中单词的出现情况，忽略语法和词序。"
---

## Definition

这种自然语言处理技术将文本表示为单词的多重集， disregarding 句法和序列。它根据词频或存在性将文档转换为数值向量。

### Summary

词袋模型是一种简化的文本表示方法，描述文档中单词的出现情况，忽略语法和词序。

## Key Concepts

- 分词
- 频率统计
- 向量空间
- 特征提取

## Use Cases

- 文本分类
- 垃圾邮件过滤
- 信息检索

## Code Example

```python
from sklearn.feature_extraction.text import CountVectorizer
corpus = ["Hello world", "World hello"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
```

## Related Terms

- [TF-IDF (词频-逆文档频率)](/en/terms/tf-idf-词频-逆文档频率/)
- [N-grams (N元语法)](/en/terms/n-grams-n元语法/)
- [Word Embeddings (词嵌入)](/en/terms/word-embeddings-词嵌入/)
