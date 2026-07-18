---
title: "Code-Generierung"
term_id: "code_generation"
category: "application_paradigms"
subcategory: ""
tags: ["development", "automation", "programming"]
difficulty: 3
weight: 1
slug: "code_generation"
aliases:
  - /de/terms/code_generation/
date: "2026-07-18T07:41:06.457082Z"
lastmod: "2026-07-18T11:44:44.583786Z"
draft: false
source: "agnes_llm"
status: "published"
language: "de"
description: "Der Prozess der Nutzung künstlicher Intelligenz, um automatisch Quellcode aus natürlichen Sprachbeschreibungen oder vorhandenen Code-Snippets zu erstellen."
---

## Definition

Die Code-Generierung nutzt große Sprachmodelle, die auf umfangreichen Repositories von Programmiersprachen trainiert wurden, um funktionale Software-Artefakte zu erzeugen. Sie interpretiert menschenlesbare Eingaben, wie Kommentare oder Beschreibungen, und wandelt diese in ausführbaren Code um.

### Summary

Der Prozess der Nutzung künstlicher Intelligenz, um automatisch Quellcode aus natürlichen Sprachbeschreibungen oder vorhandenen Code-Snippets zu erstellen.

## Key Concepts

- Natural Language Processing
- Quellcodesynthese
- Große Sprachmodelle
- Automatisierte Refaktorierung

## Use Cases

- Automatisierung der Erstellung von Boilerplate-Code
- Umwandlung von Pseudocode in ausführbare Skripte
- Unterstützung von Entwicklern beim Debuggen und Optimieren

## Code Example

```python
import openai
# Example prompt for generating a function
def generate_sort_function():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Write a Python function to sort a list of integers."}]
    )
    return response.choices[0].message.content
```

## Related Terms

- [LLM (Large Language Model)](/en/terms/llm-large-language-model/)
- [IDE-Integration (Integration in Entwicklungsumgebungen)](/en/terms/ide-integration-integration-in-entwicklungsumgebungen/)
- [Program Synthesis (Programmgenerierung)](/en/terms/program-synthesis-programmgenerierung/)
- [Copilot (KI-Assistent)](/en/terms/copilot-ki-assistent/)
