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
date: '2026-07-18T11:43:05.960127Z'
lastmod: '2026-07-18T11:44:45.358714Z'
draft: false
source: agnes_llm
status: published
language: fr
description: Un système de reconnaissance automatique de la parole (ASR) développé
  par OpenAI, entraîné sur un vaste ensemble de données audio diversifié.
---
## Definition

Whisper est un modèle de reconnaissance vocale polyvalent conçu pour gérer diverses langues, dialectes et accents. Il est entraîné sur des centaines de milliers d'heures de données audio multilingues et multitâches supervisées, ce qui lui confère une grande robustesse face au bruit et aux variations linguistiques.

### Summary

Un système de reconnaissance automatique de la parole (ASR) développé par OpenAI, entraîné sur un vaste ensemble de données audio diversifié.

## Key Concepts

- Reconnaissance automatique de la parole
- Support multilingue
- Robustesse au bruit
- Architecture Transformer

## Use Cases

- Génération de sous-titres et légendes vidéo
- Transcription de réunions ou de conférences
- Traitement des commandes vocales

## Code Example

```python
import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

## Related Terms

- [Parole en texte (conversion de l'audio parlé en texte écrit)](/en/terms/parole-en-texte-conversion-de-l-audio-parlé-en-texte-écrit/)
- [Traitement automatique des langues (analyse et génération du langage humain)](/en/terms/traitement-automatique-des-langues-analyse-et-génération-du-langage-humain/)
- [OpenAI (organisme de recherche en IA ayant développé Whisper)](/en/terms/openai-organisme-de-recherche-en-ia-ayant-développé-whisper/)
- [Classification audio (catégorisation de sons non vocaux ou vocaux)](/en/terms/classification-audio-catégorisation-de-sons-non-vocaux-ou-vocaux/)
