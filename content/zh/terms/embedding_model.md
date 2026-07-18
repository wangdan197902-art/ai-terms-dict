---
title: "Embedding Model"
term_id: "embedding_model"
category: "application_paradigms"
subcategory: ""
tags: ["NLP", "Representation Learning", "Search"]
difficulty: 4
weight: 1
slug: "embedding_model"
aliases:
  - /zh/terms/embedding_model/
date: "2026-07-18T10:59:51.920760Z"
lastmod: "2026-07-18T11:44:45.399378Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "嵌入模型将文本或图像等原始数据转换为表示语义意义的稠密数值向量。"
---

## Definition

这些模型将高维数据映射到低维连续向量空间中，其中相似的项目彼此靠得更近。这种转换捕捉了语义关系，使得...（原文截断）

### Summary

嵌入模型将文本或图像等原始数据转换为表示语义意义的稠密数值向量。

## Key Concepts

- 向量表示
- 语义相似度
- 降维
- 特征提取

## Use Cases

- 构建语义搜索引擎
- 产品或内容推荐系统
- 聚类相似的文档或图像

## Code Example

```python
from transformers import AutoTokenizer, AutoModel
import torch

model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
inputs = tokenizer('Hello world', return_tensors='pt')
embeddings = model(**inputs).last_hidden_state.mean(dim=1)
```

## Related Terms

- [Word2Vec (词向量模型)](/en/terms/word2vec-词向量模型/)
- [BERT (预训练语言模型)](/en/terms/bert-预训练语言模型/)
- [Vector Database (向量数据库)](/en/terms/vector-database-向量数据库/)
- [Similarity Search (相似度搜索)](/en/terms/similarity-search-相似度搜索/)
