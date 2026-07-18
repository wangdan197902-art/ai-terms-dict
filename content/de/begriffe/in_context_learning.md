---
title: "In-Context-Lernen"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
aliases:
  - /de/terms/in_context_learning/
date: "2026-07-18T07:41:20.132455Z"
lastmod: "2026-07-18T11:44:44.584728Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Eine Technik, bei der Modelle Aufgaben durch Beobachtung von Beispielen lernen, die in der Eingabeaufforderung bereitgestellt werden."
---

## Definition

In-Context-Lernen (ICL) ermöglicht es Large Language Models, sich an neue Aufgaben anzupassen, ohne ihre Gewichte zu aktualisieren. Durch die Bereitstellung von Input-Output-Paaren innerhalb des Prompt-Kontexts leitet das Modell das Muster ab und...

### Summary

Eine Technik, bei der Modelle Aufgaben durch Beobachtung von Beispielen lernen, die in der Eingabeaufforderung bereitgestellt werden.

## Key Concepts

- Few-Shot-Lernen
- Zero-Shot
- Prompt-Design
- Gewichtsfreie Anpassung

## Use Cases

- Schnelles Testen von Modellfähigkeiten auf neuen Datensätzen
- Dynamisches Aufgabenswitching in Konversationsagenten
- Prototyping von KI-Anwendungen ohne Neutrainierung

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Prompt Engineering (Strukturierung von Eingabeaufforderungen)](/en/terms/prompt-engineering-strukturierung-von-eingabeaufforderungen/)
- [Few-Shot (Beispiele im Prompt)](/en/terms/few-shot-beispiele-im-prompt/)
- [Zero-Shot (Keine Beispiele im Prompt)](/en/terms/zero-shot-keine-beispiele-im-prompt/)
- [Meta-Lernen](/en/terms/meta-lernen/)
