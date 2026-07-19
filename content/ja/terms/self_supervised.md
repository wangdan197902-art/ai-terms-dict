---
title: 自己教師あり
term_id: self_supervised
category: training_techniques
subcategory: ''
tags:
- Learning Paradigms
- NLP
- scalability
difficulty: 4
weight: 1
slug: self_supervised
date: '2026-07-18T10:57:44.225592Z'
lastmod: '2026-07-18T11:44:45.028977Z'
draft: false
source: agnes_llm
status: published
language: ja
description: 自己教師あり学習とは、モデルが入力データから独自のラベルを生成し、人間の注釈なしに表現を学習する手法です。
---
## Definition

自己教師あり学習は、教師信号が手動ラベリングの必要性を排除するためにデータ自体から自動的に導き出される機械学習の一分野です。モデルは通常、データ内の構造を利用して予備課題を解くことで、データの潜在表現を学習します。

### Summary

自己教師あり学習とは、モデルが入力データから独自のラベルを生成し、人間の注釈なしに表現を学習する手法です。

## Key Concepts

-  pretextタスク（予備課題）
- マスクドモデリング
- ラベルなしデータ
- 表現学習

## Use Cases

- マスクド言語モデリングによるBERTのトレーニング
- 画像埋め込みのためのコントラスト学習
- LLMにおける次のトークンの予測

## Related Terms

- [unsupervised (教師なし)](/en/terms/unsupervised-教師なし/)
- [contrastive_learning (コントラスト学習)](/en/terms/contrastive_learning-コントラスト学習/)
- [masked_language_modeling (マスクド言語モデリング)](/en/terms/masked_language_modeling-マスクド言語モデリング/)
- [representation_learning (表現学習)](/en/terms/representation_learning-表現学習/)
