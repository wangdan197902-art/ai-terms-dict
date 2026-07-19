---
title: "バックドア攻撃"
term_id: "backdoor_attack"
category: "ethics_safety"
subcategory: ""
tags: ["AI Security", "Ethics", "Adversarial ML"]
difficulty: 4
weight: 1
slug: "backdoor_attack"
date: "2026-07-18T11:36:54.545449Z"
lastmod: "2026-07-18T11:44:45.157198Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "攻撃者がモデルの訓練中に隠しトリガーを埋め込み、特定の誤分類を引き起こさせるセキュリティ脅威。"
---
## Definition

バックドア攻撃とは、機械学習モデルの訓練データに「トリガー」と呼ばれる特定のパターンを混入させる（ポイズニング）ことです。クリーンなデータでは通常どおり正常に動作しますが、トリガーが含まれる入力に対しては、攻撃者が意図した特定の誤った出力や分類を行います。

### Summary

攻撃者がモデルの訓練中に隠しトリガーを埋め込み、特定の誤分類を引き起こさせるセキュリティ脅威。

## Key Concepts

- データポイズニング
- モデル整合性
- 敵対的機械学習
- トリガーパターン

## Use Cases

- MLパイプラインのセキュリティテスト
- 防御フィルターの開発
- サードパーティ製モデルの監査

## Related Terms

- [敵対的サンプル](/en/terms/敵対的サンプル/)
- [データポイズニング](/en/terms/データポイズニング/)
- [モデルの堅牢性](/en/terms/モデルの堅牢性/)
- [クリーンラベル攻撃](/en/terms/クリーンラベル攻撃/)
