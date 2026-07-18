---
title: "好み学習"
term_id: "preference_learning"
category: "training_techniques"
subcategory: ""
tags: ["alignment", "human_feedback", "rlhf"]
difficulty: 3
weight: 1
slug: "preference_learning"
aliases:
  - /ja/terms/preference_learning/
date: "2026-07-18T11:28:16.095316Z"
lastmod: "2026-07-18T11:44:45.132708Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "比較フィードバックを用いて、モデルの出力を人間の好みに適合させるための技術。"
---

## Definition

好み学習は、絶対的なラベルではなく人間の判断に基づいて、良い出力と悪い出力を区別できるようにモデルを教育することに焦点を当てています。通常、特定の入力が与えられた際に複数の応答の中からより好ましいものを選ぶようなペアの応答データを収集し、それらの好みから報酬モデルを学習します。これにより、モデルの動作を人間の価値観や意図に合わせることができます。

### Summary

比較フィードバックを用いて、モデルの出力を人間の好みに適合させるための技術。

## Key Concepts

- 人間のフィードバック
- ペアワイズ比較
- 報酬モデリング
- アライメント

## Use Cases

- LLMにおけるRLHF（人間のフィードバックによる強化学習）
- レコメンデーションシステム
- コンテンツモデレーションフィルタリング

## Related Terms

- [rlhf (人間のフィードバックによる強化学習)](/en/terms/rlhf-人間のフィードバックによる強化学習/)
- [reward_modeling (報酬モデリング)](/en/terms/reward_modeling-報酬モデリング/)
- [human_in_the_loop (ヒューマンインザループ)](/en/terms/human_in_the_loop-ヒューマンインザループ/)
- [alignment (アライメント)](/en/terms/alignment-アライメント/)
