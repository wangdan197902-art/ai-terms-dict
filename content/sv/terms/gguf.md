---
title: GGUF
term_id: gguf
category: basic_concepts
subcategory: ''
tags:
- format
- Optimization
- Local LLM
difficulty: 3
weight: 1
slug: gguf
date: '2026-07-18T15:58:53.191381Z'
lastmod: '2026-07-18T17:15:09.005415Z'
draft: false
source: agnes_llm
status: published
language: sv
description: Ett filformat utvecklat avgger.ai för att lagra och läsa in kvantifierade
  stora språkmodeller effektivt på lokal hårdvara.
---
## Definition

GGUF (GPT-Generated Unified Format) är ett binärt filformat utformat specifikt för att köra stora språkmodeller på konsumentnivåhårdvara. Det stöder olika kvantificeringstekniker, vilket möjliggör körning av modeller med minskat minnesutrymme och beräkningskrav utan att tappa för mycket prestanda.

### Summary

Ett filformat utvecklat avgger.ai för att lagra och läsa in kvantifierade stora språkmodeller effektivt på lokal hårdvara.

## Key Concepts

- Kvantifiering
- Modellserialisering
- Lokal inferens
- Minnesoptimering

## Use Cases

- Körning av LLMs lokalt på bärbara datorer eller stationära datorer
- Distribution av modeller i resursbegränsade enheter vid kanten (edge devices)
- Delning av optimerade modellvikter i öppen källkodesgemenskapen

## Related Terms

- [LLAMA.cpp (ett populärt bibliotek för GGUF)](/en/terms/llama-cpp-ett-populärt-bibliotek-för-gguf/)
- [Kvantifiering (minskning av modellprecision)](/en/terms/kvantifiering-minskning-av-modellprecision/)
- [ONNX (Open Neural Network Exchange-format)](/en/terms/onnx-open-neural-network-exchange-format/)
- [Modellvikter (parametrarna i en AI-modell)](/en/terms/modellvikter-parametrarna-i-en-ai-modell/)
