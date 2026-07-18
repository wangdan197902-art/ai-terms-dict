---
title: "思考の連鎖プロンプティング"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
aliases:
  - /ja/terms/chain_of_thought_prompting/
date: "2026-07-18T10:58:22.790641Z"
lastmod: "2026-07-18T11:44:45.031234Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "思考の連鎖プロンプティングは、最終的な回答を生成する前に、中間的な推論ステップを生成することを大規模言語モデルに促す手法です。"
---

## Definition

思考の連鎖（CoT）プロンプティングは、モデルに段階的なロジックを明示的に記述させることで、複雑な推論タスクにおける大規模言語モデルのパフォーマンスを向上させます。飛躍的に

### Summary

思考の連鎖プロンプティングは、最終的な回答を生成する前に、中間的な推論ステップを生成することを大規模言語モデルに促す手法です。

## Key Concepts

- 段階的な推論
- ファインショット学習
- 論理的帰納
- 中間ステップ

## Use Cases

- 数学の文章題の解決
- 複雑な論理推論タスク
- コード生成エラーのデバッグ

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Zero-Shot Prompting（ゼロショットプロンプティング）](/en/terms/zero-shot-prompting-ゼロショットプロンプティング/)
- [Few-Shot Prompting（ファインショットプロンプティング）](/en/terms/few-shot-prompting-ファインショットプロンプティング/)
- [Self-Consistency（自己一貫性）](/en/terms/self-consistency-自己一貫性/)
- [Reasoning（推論）](/en/terms/reasoning-推論/)
