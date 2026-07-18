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
  - /en/terms/whisper/
date: "2026-07-18T10:20:04.565030Z"
lastmod: "2026-07-18T11:44:44.733352Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "An automatic speech recognition (ASR) system developed by OpenAI that is trained on a large dataset of diverse audio."
---

## Definition

Whisper is a general-purpose speech recognition model designed to handle various languages, dialects, and accents. It is trained on hundreds of thousands of hours of multilingual and multitask supervised data collected from the web. The model excels at robustness against noise and background sounds, making it suitable for real-world applications. It supports transcription, translation, and voice activity detection, providing high accuracy across different audio contexts without requiring extensive fine-tuning for specific domains.

### Summary

An automatic speech recognition (ASR) system developed by OpenAI that is trained on a large dataset of diverse audio.

## Key Concepts

- Automatic Speech Recognition
- Multilingual support
- Robustness to noise
- Transformer architecture

## Use Cases

- Video captioning and subtitles
- Transcribing meetings or lectures
- Voice command processing

## Code Example

```python
import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

## Related Terms

- [Speech-to-text](/en/terms/speech-to-text/)
- [Natural Language Processing](/en/terms/natural-language-processing/)
- [OpenAI](/en/terms/openai/)
- [Audio classification](/en/terms/audio-classification/)
