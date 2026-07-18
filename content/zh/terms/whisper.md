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
  - /zh/terms/whisper/
date: "2026-07-18T11:38:14.659782Z"
lastmod: "2026-07-18T11:44:45.568809Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "由 OpenAI 开发的自动语音识别 (ASR) 系统，基于大量多样化音频数据集训练而成。"
---

## Definition

Whisper 是一个通用语音识别模型，旨在处理多种语言、方言和口音。它是在数十万小时的多语言和 multitask 监督数据上训练而成的，具有强大的鲁棒性。

### Summary

由 OpenAI 开发的自动语音识别 (ASR) 系统，基于大量多样化音频数据集训练而成。

## Key Concepts

- 自动语音识别
- 多语言支持
- 抗噪鲁棒性
- Transformer 架构

## Use Cases

- 视频字幕生成
- 会议或讲座转录
- 语音命令处理

## Code Example

```python
import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

## Related Terms

- [语音转文本 (Speech-to-text)](/en/terms/语音转文本-speech-to-text/)
- [自然语言处理 (Natural Language Processing)](/en/terms/自然语言处理-natural-language-processing/)
- [OpenAI](/en/terms/openai/)
- [音频分类 (Audio classification)](/en/terms/音频分类-audio-classification/)
