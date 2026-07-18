---
title: "エージェント"
term_id: "agent"
category: "application_paradigms"
subcategory: ""
tags: ["Automation", "Architecture", "Advanced"]
difficulty: 3
weight: 1
slug: "agent"
aliases:
  - /ja/terms/agent/
date: "2026-07-18T07:41:35.330998Z"
lastmod: "2026-07-18T11:44:44.585336Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "環境を認識し、推論を行い、自律的に行動して特定の目標を達成できるAIシステム。"
---

## Definition

AIにおいて、エージェントはユーザーやシステムの代わりにタスクを完了するために行動するエンティティです。プロンプトに応答するだけの受動的なモデルとは異なり、エージェントは計画を立て、ツールを使用し、行動を反復的に改善することができます。

### Summary

環境を認識し、推論を行い、自律的に行動して特定の目標を達成できるAIシステム。

## Key Concepts

- 自律性
- ツール使用
- プランニング
- リアクティブループ

## Use Cases

- 自動化されたリサーチアシスタント
- 自己コーディングボット
- スマートホームコントローラー

## Code Example

```python
agent = Agent(model=llm, tools=[search_tool, calculator])
result = agent.run("Find the latest news on AI and summarize it")
```

## Related Terms

- [LLM (大規模言語モデル)](/en/terms/llm-大規模言語モデル/)
- [Orchestration (オーケストレーション)](/en/terms/orchestration-オーケストレーション/)
- [Tool Calling (ツール呼び出し)](/en/terms/tool-calling-ツール呼び出し/)
- [ReAct (Reasoning and Acting)](/en/terms/react-reasoning-and-acting/)
