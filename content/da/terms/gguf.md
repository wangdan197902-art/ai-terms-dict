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
date: '2026-07-18T15:56:40.320465Z'
lastmod: '2026-07-18T17:15:09.290475Z'
draft: false
source: agnes_llm
status: published
language: da
description: Et filformat udviklet afgger.ai til effektiv lagring og indlæsning af
  kvantificerede store sprogmodeller på lokalt hardware.
---
## Definition

GGUF (GPT-Generated Unified Format) er et binært filformat designet specifikt til at køre store sprogmodeller på forbrugerhardware. Det understøtter forskellige kvantificeringsteknikker, hvilket gør det muligt at reducere modellens hukommelsesbehov betydeligt uden at ofre for meget præcision, hvilket muliggør drift på maskiner uden dedikeret GPU.

### Summary

Et filformat udviklet afgger.ai til effektiv lagring og indlæsning af kvantificerede store sprogmodeller på lokalt hardware.

## Key Concepts

- Kvantificering (Quantization)
- Modelserialisering
- Lokal Inferens
- Hukommelsesoptimering

## Use Cases

- Kørsel af LLM'er lokalt på bærbarcomputer eller desktop
- Udrulning af modeller på ressourcerestricted edge-enheder
- Deling af optimerede modelvægte i open-source-miljøet

## Related Terms

- [LLAMA.cpp (En populær C++-bibliotek til GGUF)](/en/terms/llama-cpp-en-populær-c-bibliotek-til-gguf/)
- [Quantization (Kvantificering)](/en/terms/quantization-kvantificering/)
- [ONNX (Open Neural Network Exchange)](/en/terms/onnx-open-neural-network-exchange/)
- [Model Weights (Modelvægte)](/en/terms/model-weights-modelvægte/)
