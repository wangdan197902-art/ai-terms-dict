---
title: "自己整合性（セルフコンシステンシー）"
term_id: "self_consistency"
category: "training_techniques"
subcategory: ""
tags: ["LLM", "inference", "technique"]
difficulty: 4
weight: 1
slug: "self_consistency"
date: "2026-07-18T11:31:32.706625Z"
lastmod: "2026-07-18T11:44:45.141222Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "自己整合性は、複数の推論パスをサンプリングし、最も頻繁に出現する回答を最終出力として選択するデコーディング戦略です。"
---
## Definition

主に大規模言語モデル（LLM）で使用されるこの手法は、プロンプトに対してサンプリングによって複数の多様な応答を生成し、それらの集約によって精度を向上させます。貪欲デコーディング（greedy decoding）に頼るのではなく、多数決のようなアプローチを採用することで、より信頼性の高い結果を得ることができます。

### Summary

自己整合性は、複数の推論パスをサンプリングし、最も頻繁に出現する回答を最終出力として選択するデコーディング戦略です。

## Key Concepts

- 多数決投票
- デコーディング戦略
- LLMの推論
- 幻覚（ハルシネーション）の低減

## Use Cases

- 数学的な文章題の解決
- 複雑な論理的推論
- コード合成タスク

## Related Terms

- [思考の連鎖（Chain-of-thought）](/en/terms/思考の連鎖-chain-of-thought/)
- [温度サンプリング（Temperature sampling）](/en/terms/温度サンプリング-temperature-sampling/)
- [アンサンブル手法 (Ensemble methods)](/en/terms/アンサンブル手法-ensemble-methods/)
- [プロンプトエンジニアリング (Prompt engineering)](/en/terms/プロンプトエンジニアリング-prompt-engineering/)
