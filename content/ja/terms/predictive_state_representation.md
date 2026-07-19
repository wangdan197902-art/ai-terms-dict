---
title: 予測状態表現
term_id: predictive_state_representation
category: basic_concepts
subcategory: ''
tags:
- RL
- State Representation
- pomdp
difficulty: 4
weight: 1
slug: predictive_state_representation
date: '2026-07-18T11:28:16.095307Z'
lastmod: '2026-07-18T11:44:45.132599Z'
draft: false
source: agnes_llm
status: published
language: ja
description: 行動履歴に基づいて将来の観測値を予測する強化学習における潜在状態の定式化。
---
## Definition

予測状態表現（PSR）は、従来の部分的に観測可能なマルコフ決定過程（POMDP）を拡張したもので、状態を将来の観測可能事象に関する予測ベクトルとして定義します。過去の完全な状態に依存するのではなく、過去の行動と観測の履歴に基づいて将来のイベントを予測することにより、不完全な情報下での意思決定を可能にします。

### Summary

行動履歴に基づいて将来の観測値を予測する強化学習における潜在状態の定式化。

## Key Concepts

- 部分的観測可能性
- 将来予測
- 履歴ベースの状態
- 強化学習

## Use Cases

- 複雑な環境におけるロボティクス
- 隠れた情報があるゲームAI
- 金融市場の予測

## Related Terms

- [partially_observable_mdp (部分的観測可能マルコフ決定過程)](/en/terms/partially_observable_mdp-部分的観測可能マルコフ決定過程/)
- [latent_space (潜在空間)](/en/terms/latent_space-潜在空間/)
- [state_estimation (状態推定)](/en/terms/state_estimation-状態推定/)
- [pomdp (部分的観測可能マルコフ決定過程)](/en/terms/pomdp-部分的観測可能マルコフ決定過程/)
