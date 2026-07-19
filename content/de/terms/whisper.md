---
title: Whisper
term_id: whisper
category: basic_concepts
subcategory: ''
tags:
- Speech Recognition
- openai
- Practical AI
difficulty: 2
weight: 1
slug: whisper
date: '2026-07-18T11:38:19.941052Z'
lastmod: '2026-07-18T11:44:44.999773Z'
draft: false
source: agnes_llm
status: published
language: de
description: Ein automatisches Spracherkennungssystem (ASR) von OpenAI, das auf einem
  großen Datensatz mit vielfältigen Audiodaten trainiert wurde.
---
## Definition

Whisper ist ein universelles Spracherkennungsmodell, das für verschiedene Sprachen, Dialekte und Akzente ausgelegt ist. Es wurde mit Hunderttausenden von Stunden multilingualer und multitask-überwachter Daten trainiert...

### Summary

Ein automatisches Spracherkennungssystem (ASR) von OpenAI, das auf einem großen Datensatz mit vielfältigen Audiodaten trainiert wurde.

## Key Concepts

- Automatische Spracherkennung
- Mehrsprachige Unterstützung
- Robustheit gegenüber Störgeräuschen
- Transformer-Architektur

## Use Cases

- Untertitelung und Captioning von Videos
- Transkription von Meetings oder Vorlesungen
- Verarbeitung von Sprachbefehlen

## Code Example

```python
import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

## Related Terms

- [Speech-to-text (Sprache-zu-Text)](/en/terms/speech-to-text-sprache-zu-text/)
- [Natural Language Processing (Natürliche Sprachverarbeitung)](/en/terms/natural-language-processing-natürliche-sprachverarbeitung/)
- [OpenAI (Entwickler des Modells)](/en/terms/openai-entwickler-des-modells/)
- [Audio classification (Audiodatenklassifizierung)](/en/terms/audio-classification-audiodatenklassifizierung/)
