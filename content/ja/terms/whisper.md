---
title: "Whisper"
term_id: "whisper"
category: "basic_concepts"
subcategory: ""
tags: ["speech_recognition", "openai", "practical_ai"]
difficulty: 2
weight: 1
slug: "whisper"
aliases:
  - /ja/terms/whisper/
date: "2026-07-18T11:36:41.190698Z"
lastmod: "2026-07-18T11:44:45.155624Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "多様なオーディオデータセットで学習した、OpenAIが開発した自動音声認識（ASR）システム。"
---

## Definition

Whisperは、さまざまな言語、方言、アクセントに対応するために設計された汎用音声認識モデルです。多言語かつマルチタスクの教師ありデータから、数十万時間分のオーディオを用いて学習しています。

### Summary

多様なオーディオデータセットで学習した、OpenAIが開発した自動音声認識（ASR）システム。

## Key Concepts

- 自動音声認識
- 多言語サポート
- ノイズへの頑健性
- トランスフォーマーアーキテクチャ

## Use Cases

- 動画の字幕生成
- 会議や講義の文字起こし
- 音声コマンドの処理

## Code Example

```python
import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

## Related Terms

- [スピーチ・トゥ・テキスト (音声テキスト変換)](/en/terms/スピーチ-トゥ-テキスト-音声テキスト変換/)
- [自然言語処理](/en/terms/自然言語処理/)
- [OpenAI](/en/terms/openai/)
- [オーディオ分類](/en/terms/オーディオ分類/)
