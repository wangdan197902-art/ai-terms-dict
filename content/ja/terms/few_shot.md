---
title: フューショット
term_id: few_shot
category: basic_concepts
subcategory: ''
tags:
- Learning Paradigms
- Data Efficiency
- NLP
difficulty: 3
weight: 1
slug: few_shot
date: '2026-07-18T10:56:32.271701Z'
lastmod: '2026-07-18T11:44:45.024837Z'
draft: false
source: agnes_llm
status: published
language: ja
description: モデルが限られた数のラベル付き例しか提示されなくても、タスクを正しく実行できる学習パラダイム。
---
## Definition

フューショット学習は、機械学習モデルが非常に限られたデータ（通常、クラスあたり1〜10個の例）から一般化できるようにする手法です。従来の教師あり学習が数千から数百万の例を必要とするのに対し、フューショット学習は事前トレーニングされたモデルの知識を活用し、新しいタスクに適応するためにわずかな追加データのみを使用します。

### Summary

モデルが限られた数のラベル付き例しか提示されなくても、タスクを正しく実行できる学習パラダイム。

## Key Concepts

- メタ学習
- 一般化
- ラベル効率
- 事前トレーニング

## Use Cases

- 希少疾患の診断
- チャットボットのカスタム意図認識
- 限られたデータによるドメイン適応

## Related Terms

- [zero_shot (ゼロショット)](/en/terms/zero_shot-ゼロショット/)
- [one_shot (ワンショット)](/en/terms/one_shot-ワンショット/)
- [transfer_learning (転移学習)](/en/terms/transfer_learning-転移学習/)
- [meta_learning (メタ学習)](/en/terms/meta_learning-メタ学習/)
