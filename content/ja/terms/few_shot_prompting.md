---
title: フューショットプロンプティング
term_id: few_shot_prompting
category: application_paradigms
subcategory: ''
tags:
- prompting
- LLM
- technique
difficulty: 2
weight: 1
slug: few_shot_prompting
date: '2026-07-18T10:59:07.505610Z'
lastmod: '2026-07-18T11:44:45.047837Z'
draft: false
source: agnes_llm
status: published
language: ja
description: フューショットプロンプティングは、LLM（大規模言語モデル）の動作を誘導するため、プロンプト内に少数の入力-出力例を提供する手法です。
---
## Definition

この手法は、プロンプト内に直接的な例示的なサンプルを提供することで、大規模言語モデルのコンテキスト内学習（インコンテキストラーニング）能力を活用します。モデルの重みを更新するファインチューニングとは異なり、プロンプト工程のみでモデルの出力形式や振る舞いを制御できるため、迅速な適応が可能です。

### Summary

フューショットプロンプティングは、LLM（大規模言語モデル）の動作を誘導するため、プロンプト内に少数の入力-出力例を提供する手法です。

## Key Concepts

- コンテキスト内学習
- プロンプトエンジニアリング
- 例に基づくガイダンス
- ゼロショット比較

## Use Cases

- 感情分析のフォーマット指定
- コードスタイルの適応
- 構造化データ抽出

## Code Example

```python
response = llm.generate(
    prompt="Translate English to French:\n"
           "Hello -> Bonjour\n"
           "World -> Monde\n"
           "Cat -> ?"
)
```

## Related Terms

- [zero_shot (ゼロショット：例なしでの推論)](/en/terms/zero_shot-ゼロショット-例なしでの推論/)
- [prompt_engineering (プロンプトエンジニアリング)](/en/terms/prompt_engineering-プロンプトエンジニアリング/)
- [in_context_learning (コンテキスト内学習)](/en/terms/in_context_learning-コンテキスト内学習/)
- [llm (大規模言語モデル)](/en/terms/llm-大規模言語モデル/)
