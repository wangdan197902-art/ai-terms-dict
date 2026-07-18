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
  - /id/terms/whisper/
date: "2026-07-18T16:13:33.331363Z"
lastmod: "2026-07-18T16:38:07.519914Z"
draft: false
source: "agnes_llm"
status: "published"
language: "id"
description: "Sistem pengenalan ucapan otomatis (ASR) yang dikembangkan oleh OpenAI dan dilatih pada dataset audio beragam yang besar."
---

## Definition

Whisper adalah model pengenalan ucapan serbaguna yang dirancang untuk menangani berbagai bahasa, dialek, dan aksen. Model ini dilatih pada ratusan ribu jam data multilingual dan multitask yang disupervisi, membuatnya sangat robust terhadap kebisingan latar belakang dan variasi pengucapan, sehingga mampu mentranskripsi ucapan menjadi teks dengan akurasi tinggi dalam banyak konteks.

### Summary

Sistem pengenalan ucapan otomatis (ASR) yang dikembangkan oleh OpenAI dan dilatih pada dataset audio beragam yang besar.

## Key Concepts

- Pengenalan Ucapan Otomatis
- Dukungan multibahasa
- Ketahanan terhadap kebisingan
- Arsitektur Transformer

## Use Cases

- Pembuatan caption dan subtitle video
- Transkripsi rapat atau kuliah
- Pemrosesan perintah suara

## Code Example

```python
import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])
```

## Related Terms

- [Speech-to-text (Konversi ucapan ke teks)](/en/terms/speech-to-text-konversi-ucapan-ke-teks/)
- [Pemrosesan Bahasa Alami (Teknologi AI untuk memahami bahasa manusia)](/en/terms/pemrosesan-bahasa-alami-teknologi-ai-untuk-memahami-bahasa-manusia/)
- [OpenAI (Perusahaan pengembang model Whisper)](/en/terms/openai-perusahaan-pengembang-model-whisper/)
- [Klasifikasi Audio (Identifikasi jenis atau konten suara)](/en/terms/klasifikasi-audio-identifikasi-jenis-atau-konten-suara/)
