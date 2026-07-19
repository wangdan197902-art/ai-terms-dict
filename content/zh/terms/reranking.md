---
title: "重排序"
term_id: "reranking"
category: "application_paradigms"
subcategory: ""
tags: ["search", "recommendations", "architecture"]
difficulty: 2
weight: 1
slug: "reranking"
date: "2026-07-18T11:32:14.210922Z"
lastmod: "2026-07-18T11:44:45.550718Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种两阶段检索过程，首先通过粗排获取候选集，再由计算成本更高的精细模型进行排序以提升结果相关性。"
---
## Definition

重排序是信息检索和推荐系统中用于提高准确性的策略。首先，一个快速但精度较低的模型检索出一个较大的候选集；随后，一个更慢但更复杂的模型对这些候选项进行重新排序，以优化最终结果的精确度。

### Summary

一种两阶段检索过程，首先通过粗排获取候选集，再由计算成本更高的精细模型进行排序以提升结果相关性。

## Key Concepts

- 两级检索
- 候选生成
- 交叉注意力机制
- 精度优化

## Use Cases

- 搜索引擎
- 推荐系统
- 检索增强生成 (RAG)

## Related Terms

- [向量搜索](/en/terms/向量搜索/)
- [BM25](/en/terms/bm25/)
- [交叉编码器](/en/terms/交叉编码器/)
- [信息检索](/en/terms/信息检索/)
