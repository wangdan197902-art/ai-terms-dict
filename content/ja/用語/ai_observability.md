---
title: "AI観測可能性"
term_id: "ai_observability"
category: "engineering_practice"
subcategory: ""
tags: ["mlops", "monitoring", "engineering"]
difficulty: 4
weight: 1
slug: "ai_observability"
aliases:
  - /ja/terms/ai_observability/
date: "2026-07-18T11:02:23.128328Z"
lastmod: "2026-07-18T11:44:45.061633Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "ログ、メトリクス、トレースを通じて機械学習システムの内部状態を監視し、理解する実践。"
---

## Definition

AI観測可能性とは、従来のソフトウェア監視を拡張し、機械学習システム特有の課題に対応するものです。これには、モデルパフォーマンス、データドリフト、推論レイテンシなどをリアルタイムで追跡することが含まれます。

### Summary

ログ、メトリクス、トレースを通じて機械学習システムの内部状態を監視し、理解する実践。

## Key Concepts

- データドリフト
- モデル監視
- テレメトリー
- デバッグ

## Use Cases

- 本番環境でのコンセプトドリフトの検出
- 低信頼度予測のトラブルシューティング
- AIサービスに対するSLA（サービスレベル合意）準拠の確保

## Code Example

```python
import mlflow

# Log metrics during training
mlflow.log_metric('accuracy', 0.95)
mlflow.log_metric('loss', 0.05)

# Track model parameters
mlflow.log_param('learning_rate', 0.01)
mlflow.log_param('epochs', 10)
```

## Related Terms

- [MLOps (機械学習運用)](/en/terms/mlops-機械学習運用/)
- [Model Drift (モデルドリフト)](/en/terms/model-drift-モデルドリフト/)
- [System Monitoring (システム監視)](/en/terms/system-monitoring-システム監視/)
- [Telemetry (テレメトリー)](/en/terms/telemetry-テレメトリー/)
