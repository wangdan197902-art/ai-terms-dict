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
  - /pt/terms/whisper/
date: "2026-07-18T15:27:07.254518Z"
lastmod: "2026-07-18T15:51:59.542480Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Um sistema de reconhecimento automático de fala (ASR) desenvolvido pela OpenAI, treinado em um grande conjunto de dados diversificado de áudio."
---

## Definition

Whisper é um modelo de reconhecimento de fala de propósito geral projetado para lidar com vários idiomas, dialetos e sotaques. Ele é treinado em centenas de milhares de horas de supervisão multilíngue e multitarefa, tornando-o robusto contra ruído e variações de áudio.

### Summary

Um sistema de reconhecimento automático de fala (ASR) desenvolvido pela OpenAI, treinado em um grande conjunto de dados diversificado de áudio.

## Key Concepts

- Reconhecimento Automático de Fala
- Suporte multilíngue
- Robustez a ruídos
- Arquitetura Transformer

## Use Cases

- Legendagem e geração de legendas para vídeos
- Transcrição de reuniões ou palestras
- Processamento de comandos de voz

## Code Example

```python
import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

## Related Terms

- [Fala-para-texto (Conversão de áudio em texto)](/en/terms/fala-para-texto-conversão-de-áudio-em-texto/)
- [Processamento de Linguagem Natural](/en/terms/processamento-de-linguagem-natural/)
- [OpenAI (Organização desenvolvedora)](/en/terms/openai-organização-desenvolvedora/)
- [Classificação de Áudio](/en/terms/classificação-de-áudio/)
