---
title: 共トレーニング
term_id: co_training
category: training_techniques
subcategory: ''
tags:
- Semi Supervised
- algorithm
- Data Efficiency
difficulty: 4
weight: 1
slug: co_training
date: '2026-07-18T11:07:35.495208Z'
lastmod: '2026-07-18T11:44:45.077291Z'
draft: false
source: agnes_llm
status: published
language: ja
description: 共トレーニングは、データの2つのビューを使用して別々の分類器をトレーニングし、それらが互いの未ラベルデータに反復的にラベルを付ける半教師あり学習アルゴリズムです。
---
## Definition

この手法は、同じデータポイントの複数の異なる特徴セット（ビュー）を活用します。最初は、各ビューからの小さなラベル付きデータセットで2つの分類器をトレーニングします。その後、未ラベル

### Summary

共トレーニングは、データの2つのビューを使用して別々の分類器をトレーニングし、それらが互いの未ラベルデータに反復的にラベルを付ける半教師あり学習アルゴリズムです。

## Key Concepts

- 半教師あり学習
- マルチビュー
- 反復的ラベリング
- 高信頼性選択

## Use Cases

- 複数特徴を持つテキスト分類
- ウェブページのカテゴリ分け
- 限られたラベルでのデータ拡張

## Related Terms

- [Semi-Supervised Learning (半教師あり学習)](/en/terms/semi-supervised-learning-半教師あり学習/)
- [Self-Training (自己トレーニング)](/en/terms/self-training-自己トレーニング/)
- [Multi-view Learning (マルチビュー学習)](/en/terms/multi-view-learning-マルチビュー学習/)
- [Active Learning (能動学習)](/en/terms/active-learning-能動学習/)
