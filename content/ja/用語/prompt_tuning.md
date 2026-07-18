---
title: "プロンプトチューニング"
term_id: "prompt_tuning"
category: "training_techniques"
subcategory: ""
tags: ["LLM", "optimization", "efficiency"]
difficulty: 3
weight: 1
slug: "prompt_tuning"
aliases:
  - /ja/terms/prompt_tuning/
date: "2026-07-18T11:28:57.680411Z"
lastmod: "2026-07-18T11:44:45.134434Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "モデル全体の重みを更新するのではなく、連続的な入力埋め込みを最適化することで、パラメータ効率の高いファインチューニング手法。"
---

## Definition

プロンプトチューニングは、事前学習済み言語モデルの入力層にトレーニング可能なソフトプロンプト（連続ベクトル）を追加し、基盤となるモデルのパラメータは凍結したままにするアプローチです。この手法により、大規模なモデルパラメータを更新することなく、特定タスクに適応させることが可能になります。

### Summary

モデル全体の重みを更新するのではなく、連続的な入力埋め込みを最適化することで、パラメータ効率の高いファインチューニング手法。

## Key Concepts

- ソフトプロンプト
- パラメータ効率
- 凍結された重み
- フューショット学習

## Use Cases

- LLMを特定のドメインに適応させる
- 低リソース環境でのファインチューニング
- マルチタスク学習の最適化

## Related Terms

- [PEFT (Parameter-Efficient Fine-Tuning: パラメータ効率的ファインチューニング)](/en/terms/peft-parameter-efficient-fine-tuning-パラメータ効率的ファインチューニング/)
- [LoRA (Low-Rank Adaptation: 低ランク適応)](/en/terms/lora-low-rank-adaptation-低ランク適応/)
- [in-context learning (コンテキスト内学習)](/en/terms/in-context-learning-コンテキスト内学習/)
- [fine-tuning (ファインチューニング)](/en/terms/fine-tuning-ファインチューニング/)
