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
date: '2026-07-18T16:21:24.432884Z'
lastmod: '2026-07-18T16:38:07.058280Z'
draft: false
source: agnes_llm
status: published
language: 'no'
description: Et automatisk talegjenkjennelsessystem (ASR) utviklet av OpenAI, trent
  på et stort datasett med variert lyd.
---
## Definition

Whisper er en allment brukbar talegjenkjennelsesmodell designet for å håndtere ulike språk, dialekter og aksenter. Den er trent på hundretusener av timer med flerspråklig og multitask overvåket...

### Summary

Et automatisk talegjenkjennelsessystem (ASR) utviklet av OpenAI, trent på et stort datasett med variert lyd.

## Key Concepts

- Automatisk talegjenkjenning
- Flerspråklig støtte
- Robusthet mot støy
- Transformer-arkitektur

## Use Cases

- Underteksting og bildetekster for video
- Transkribering av møter eller forelesninger
- Behandling av stemmekommandoer

## Code Example

```python
import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

## Related Terms

- [Tale-til-tekst (Konvertering av tale til skriftlig tekst)](/en/terms/tale-til-tekst-konvertering-av-tale-til-skriftlig-tekst/)
- [Naturlig språkbehandling (Teknologi for forståelse av menneskelig språk)](/en/terms/naturlig-språkbehandling-teknologi-for-forståelse-av-menneskelig-språk/)
- [OpenAI (Utvikleren av modellen)](/en/terms/openai-utvikleren-av-modellen/)
- [Lydklassifisering (Identifisering av lydtype)](/en/terms/lydklassifisering-identifisering-av-lydtype/)
