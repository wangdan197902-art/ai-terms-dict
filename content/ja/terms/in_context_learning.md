---
title: "コンテキスト内学習"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
date: "2026-07-18T07:42:13.833802Z"
lastmod: "2026-07-18T11:44:44.587157Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "モデルがプロンプト内で提供された例を観察することでタスクを実行する方法を学習する技術。"
---
## Definition

コンテキスト内学習（ICL）により、大規模言語モデルは重みを更新せずに新しいタスクに適応できます。プロンプトの文脈に入力と出力のペアを提供することで、モデルはそのパターンを推論し、タスクを遂行します。

### Summary

モデルがプロンプト内で提供された例を観察することでタスクを実行する方法を学習する技術。

## Key Concepts

- フューショット学習
- ゼロショット
- プロンプト設計
- 重みなし適応

## Use Cases

- 新しいデータセットに対するモデル能力の迅速なテスト
- 会話エージェントでの動的なタスク切り替え
- 再トレーニングなしでのAIアプリケーションのプロトタイピング

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [プロンプトエンジニアリング (Prompt Engineering) (指示設計)](/en/terms/プロンプトエンジニアリング-prompt-engineering-指示設計/)
- [フューショット (Few-Shot) (少量の例による学習)](/en/terms/フューショット-few-shot-少量の例による学習/)
- [ゼロショット (Zero-Shot) (例なしでの推論)](/en/terms/ゼロショット-zero-shot-例なしでの推論/)
- [メタラーニング (Meta-Learning)](/en/terms/メタラーニング-meta-learning/)
