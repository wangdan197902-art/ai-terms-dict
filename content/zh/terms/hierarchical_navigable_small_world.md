---
title: 分层可导航小世界
term_id: hierarchical_navigable_small_world
category: basic_concepts
subcategory: ''
tags:
- algorithms
- search
- Data Structures
difficulty: 4
weight: 1
slug: hierarchical_navigable_small_world
date: '2026-07-18T11:20:58.430835Z'
lastmod: '2026-07-18T11:44:45.513694Z'
draft: false
source: agnes_llm
status: published
language: zh
description: 一种基于图的数据结构，用于在高维空间中实现高效的近似最近邻搜索。
---
## Definition

分层可导航小世界（HNSW）算法构建了一个多层图结构，其中每一层包含下一层节点的子集。导航从顶层开始，逐步向下移动到更详细的层级，直到找到最近的邻居。这种方法结合了小世界网络的快速收敛特性和分层结构的效率，实现了高维向量的高效近似最近邻搜索。

### Summary

一种基于图的数据结构，用于在高维空间中实现高效的近似最近邻搜索。

## Key Concepts

- 图搜索
- 近似最近邻
- 多层图
- 对数复杂度

## Use Cases

- 向量搜索
- 推荐引擎
- 图像检索

## Related Terms

- [K-Nearest Neighbors (K近邻)](/en/terms/k-nearest-neighbors-k近邻/)
- [Faiss (Facebook AI Similarity Search库)](/en/terms/faiss-facebook-ai-similarity-search库/)
- [Annoy (Spotify开发的近似最近邻库)](/en/terms/annoy-spotify开发的近似最近邻库/)
