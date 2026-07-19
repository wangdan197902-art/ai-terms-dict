---
title: 階層的ナビゲート可能スモールワールド
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
date: '2026-07-18T11:17:37.580215Z'
lastmod: '2026-07-18T11:44:45.105672Z'
draft: false
source: agnes_llm
status: published
language: ja
description: 高次元空間における効率的な近似最近傍検索を可能にするグラフベースのデータ構造。
---
## Definition

階層的ナビゲート可能スモールワールド（HNSW）アルゴリズムは、各レイヤーが下のレイヤーのノードの部分集合を含む多層グラフを構築します。検索は最上位レイヤーから始まり、近いノードへと移動しながら探索を進め、最終的に最下層レイヤーで正確な最近傍を検出します。これにより、対数時間計算量で高速かつ高精度な近似最近傍検索を実現します。

### Summary

高次元空間における効率的な近似最近傍検索を可能にするグラフベースのデータ構造。

## Key Concepts

- グラフ検索
- 近似最近傍
- 多層グラフ
- 対数計算量

## Use Cases

- ベクトル検索
- レコメンデーションエンジン
- 画像検索

## Related Terms

- [K-Nearest Neighbors (k近傍法)](/en/terms/k-nearest-neighbors-k近傍法/)
- [Faiss (Facebook AI Similarity Searchライブラリ)](/en/terms/faiss-facebook-ai-similarity-searchライブラリ/)
- [Annoy (Spotifyの開発した近似最近傍検索ライブラリ)](/en/terms/annoy-spotifyの開発した近似最近傍検索ライブラリ/)
