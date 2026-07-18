---
title: "マルチインスタンス学習"
term_id: "multiple_instance_learning"
category: "training_techniques"
subcategory: ""
tags: ["supervised_learning", "weak_labeling", "ml_paradigm"]
difficulty: 4
weight: 1
slug: "multiple_instance_learning"
aliases:
  - /ja/terms/multiple_instance_learning/
date: "2026-07-18T10:59:55.934755Z"
lastmod: "2026-07-18T11:44:45.051869Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "個々のインスタンスではなく、インスタンスの集合（バッグ）に対してラベルが割り当てられる弱教師あり学習のパラダイム。"
---

## Definition

マルチインスタンス学習（MIL）は、データが単一のラベルを持つ「バッグ」にグループ化され、そのバッグ内の個々のインスタンスにはラベルが付けられていないシナリオに対処する手法です。通常、少なくとも1つのインスタンスが正例であるバッグは正例として、すべてのインスタンスが負例であるバッグは負例として分類されます。

### Summary

個々のインスタンスではなく、インスタンスの集合（バッグ）に対してラベルが割り当てられる弱教師あり学習のパラダイム。

## Key Concepts

- バッグレベルのラベリング
- インスタンスレベルの不確実性
- 弱教師あり学習
- 正/負のバッグの論理

## Use Cases

- 薬物活性の予測
- バウンディングボックス付き画像分類
- コンテンツベース画像検索

## Related Terms

- [weak_supervision (弱教師あり学習)](/en/terms/weak_supervision-弱教師あり学習/)
- [bagging (ブートストラップ集約)](/en/terms/bagging-ブートストラップ集約/)
- [instance_classification (インスタンス分類)](/en/terms/instance_classification-インスタンス分類/)
- [label_noise (ラベルノイズ)](/en/terms/label_noise-ラベルノイズ/)
