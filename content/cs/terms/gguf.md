---
title: "GGUF"
term_id: "gguf"
category: "basic_concepts"
subcategory: ""
tags: ["format", "optimization", "local_llm"]
difficulty: 3
weight: 1
slug: "gguf"
aliases:
  - /cs/terms/gguf/
date: "2026-07-18T15:58:30.730063Z"
lastmod: "2026-07-18T17:15:09.132069Z"
draft: false
source: "agnes_llm"
status: "published"
language: "cs"
description: "Formát souboru vyvinutý společnostígger.ai pro efektivní ukládání a načítání kvantizovaných velkých jazykových modelů na lokálním hardwaru."
---

## Definition

GGUF (GPT-Generated Unified Format) je binární formát souboru navržený specificky pro běh velkých jazykových modelů na spotřebitelském hardwaru. Podporuje různé techniky kvantizace, což umožňuje zmenšit velikost modelů a snížit nároky na paměť bez výrazné ztráty přesnosti, čímž činí pokročilou AI dostupnou pro běžné uživatele na notebooku nebo stolním počítači.

### Summary

Formát souboru vyvinutý společnostígger.ai pro efektivní ukládání a načítání kvantizovaných velkých jazykových modelů na lokálním hardwaru.

## Key Concepts

- Kvantizace
- Serializace modelů
- Lokální inferenční zpracování
- Optimalizace paměti

## Use Cases

- Spouštění LLM lokálně na noteboocích nebo stolních počítačích
- Nasazování modelů na okrajových zařízeních s omezenými zdroji
- Sdílení optimalizovaných vah modelů ve komunitě open source

## Related Terms

- [LLAMA.cpp (knihovna pro běh modelů LLAMA)](/en/terms/llama-cpp-knihovna-pro-běh-modelů-llama/)
- [Quantization (kvantizace)](/en/terms/quantization-kvantizace/)
- [ONNX (Open Neural Network Exchange)](/en/terms/onnx-open-neural-network-exchange/)
- [Model Weights (váhy modelu)](/en/terms/model-weights-váhy-modelu/)
