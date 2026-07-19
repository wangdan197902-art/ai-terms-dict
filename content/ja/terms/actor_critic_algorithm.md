---
title: アクター・クリティックアルゴリズム
term_id: actor_critic_algorithm
category: basic_concepts
subcategory: ''
tags:
- Reinforcement Learning
- Neural Networks
- algorithms
difficulty: 4
weight: 1
slug: actor_critic_algorithm
date: '2026-07-18T11:03:01.062662Z'
lastmod: '2026-07-18T11:44:45.063668Z'
draft: false
source: agnes_llm
status: published
language: ja
description: アクターとクリティックという2つのニューラルネットワークを用いて、価値ベースとポリシーベースの手法を組み合わせた強化学習フレームワーク。
---
## Definition

アクター・クリティックアルゴリズムは、アクションを選択するためのポリシーを更新する「アクター」と、価値関数を推定してそれらのアクションの品質を評価する「クリティック」の2つのコンポーネントを採用しています。

### Summary

アクターとクリティックという2つのニューラルネットワークを用いて、価値ベースとポリシーベースの手法を組み合わせた強化学習フレームワーク。

## Key Concepts

- ポリシー勾配
- 価値関数
- 時間差分誤差
- ハイブリッド強化学習

## Use Cases

- ロボットアームの操作
- ゲームプレイエージェント（例：AlphaStar）
- 自動運転車における連続制御システム

## Related Terms

- [PPO (Proximal Policy Optimization)](/en/terms/ppo-proximal-policy-optimization/)
- [A3C (Asynchronous Advantage Actor-Critic)](/en/terms/a3c-asynchronous-advantage-actor-critic/)
- [policy_gradient (ポリシー勾配)](/en/terms/policy_gradient-ポリシー勾配/)
- [value_function (価値関数)](/en/terms/value_function-価値関数/)
