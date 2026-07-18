---
title: "モデル抽出"
term_id: "model_extraction"
category: "ethics_safety"
subcategory: ""
tags: ["security", "adversarial_ml"]
difficulty: 4
weight: 1
slug: "model_extraction"
aliases:
  - /ja/terms/model_extraction/
date: "2026-07-18T11:37:07.583129Z"
lastmod: "2026-07-18T11:44:45.157548Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "攻撃者がモデルにクエリを送信してパラメータを再構築または複製を作成する攻撃手法。"
---

## Definition

モデル抽出では、攻撃者はターゲット機械学習モデルのAPIをクエリして、その内部構造、重み、または意思決定境界を推測します。これらのクエリを使用して、元のモデルの挙動を模倣するサロゲートモデル（代理モデル）を構築します。

### Summary

攻撃者がモデルにクエリを送信してパラメータを再構築または複製を作成する攻撃手法。

## Key Concepts

- サロゲートモデリング
- APIクエリ
- 知的財産権侵害
- 敵対的攻撃

## Use Cases

- 商用AI APIのセキュリティ監査
- 独自アルゴリズムのクローン作成からの保護
- 抽出攻撃に対する防御メカニズムの研究

## Related Terms

- [メンバーシップ推論 (Membership Inference)](/en/terms/メンバーシップ推論-membership-inference/)
- [敵対的例 (Adversarial Examples)](/en/terms/敵対的例-adversarial-examples/)
- [モデル透かし (Model Watermarking)](/en/terms/モデル透かし-model-watermarking/)
- [APIセキュリティ (API Security)](/en/terms/apiセキュリティ-api-security/)
