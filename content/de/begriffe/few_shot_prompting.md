---
title: "Few-Shot Prompting"
term_id: "few_shot_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["prompting", "llm", "technique"]
difficulty: 2
weight: 1
slug: "few_shot_prompting"
aliases:
  - /de/terms/few_shot_prompting/
date: "2026-07-18T10:58:15.207380Z"
lastmod: "2026-07-18T11:44:44.894871Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Few-Shot Prompting ist eine Technik, bei der Large Language Models (LLMs) im Prompt eine kleine Anzahl von Eingabe-Ausgabe-Beispielen erhalten, um ihr Verhalten zu steuern."
---

## Definition

Diese Methode nutzt die Fähigkeiten zum Lernen im Kontext großer Sprachmodelle, indem sie direkt im Prompt einige illustrative Beispiele bereitstellt. Im Gegensatz zum Fine-Tuning, das eine Aktualisierung der Modellgewichte erfordert, ändert sich hier nichts am Modell selbst, sondern nur die Eingabeaufforderung.

### Summary

Few-Shot Prompting ist eine Technik, bei der Large Language Models (LLMs) im Prompt eine kleine Anzahl von Eingabe-Ausgabe-Beispielen erhalten, um ihr Verhalten zu steuern.

## Key Concepts

- Lernen im Kontext
- Prompt Engineering
- Beispielbasierte Anleitung
- Vergleich mit Zero-Shot

## Use Cases

- Formatierung der Sentimentanalyse
- Anpassung des Code-Stils
- Extrahieren strukturierter Daten

## Code Example

```python
response = llm.generate(
    prompt="Translate English to French:\n"
           "Hello -> Bonjour\n"
           "World -> Monde\n"
           "Cat -> ?"
)
```

## Related Terms

- [zero_shot (Null-Schoten-Lernen)](/en/terms/zero_shot-null-schoten-lernen/)
- [prompt_engineering (Prompt-Engineering)](/en/terms/prompt_engineering-prompt-engineering/)
- [in_context_learning (Lernen im Kontext)](/en/terms/in_context_learning-lernen-im-kontext/)
- [llm (Large Language Model)](/en/terms/llm-large-language-model/)
