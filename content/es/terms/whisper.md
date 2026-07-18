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
  - /es/terms/whisper/
date: "2026-07-18T11:13:45.019619Z"
lastmod: "2026-07-18T11:44:44.866338Z"
draft: false
source: "agnes_llm"
status: "published"
language: "es"
description: "Un sistema de reconocimiento automático de voz (ASR) desarrollado por OpenAI, entrenado con un gran conjunto de datos de audio diverso."
---

## Definition

Whisper es un modelo de reconocimiento de voz de propósito general diseñado para manejar varios idiomas, dialectos y acentos. Está entrenado con cientos de miles de horas de supervisión multilingüe y multitarea, lo que le permite transcribir audio con alta precisión incluso en entornos ruidosos.

### Summary

Un sistema de reconocimiento automático de voz (ASR) desarrollado por OpenAI, entrenado con un gran conjunto de datos de audio diverso.

## Key Concepts

- Reconocimiento automático de voz
- Soporte multilingüe
- Robustez ante el ruido
- Arquitectura Transformer

## Use Cases

- Generación de subtítulos y leyendas para videos
- Transcripción de reuniones o conferencias
- Procesamiento de comandos de voz

## Code Example

```python
import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

## Related Terms

- [Texto a partir de voz (Conversión de audio hablado a texto escrito)](/en/terms/texto-a-partir-de-voz-conversión-de-audio-hablado-a-texto-escrito/)
- [Procesamiento del lenguaje natural (Tecnología para entender el lenguaje humano)](/en/terms/procesamiento-del-lenguaje-natural-tecnología-para-entender-el-lenguaje-humano/)
- [OpenAI (Organización creadora del modelo)](/en/terms/openai-organización-creadora-del-modelo/)
- [Clasificación de audio (Identificación de tipos de sonido)](/en/terms/clasificación-de-audio-identificación-de-tipos-de-sonido/)
