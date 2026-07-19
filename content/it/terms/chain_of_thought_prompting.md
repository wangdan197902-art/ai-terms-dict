---
title: "Prompting del pensiero concatenato"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
date: "2026-07-18T15:34:52.481581Z"
lastmod: "2026-07-18T17:15:08.583743Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Il prompting del pensiero concatenato è una tecnica che incoraggia i modelli linguistici di grandi dimensioni (LLM) a generare passaggi di ragionamento intermedi prima di produrre una risposta finale."
---
## Definition

Il prompting del pensiero concatenato (CoT) migliora le prestazioni dei modelli linguistici di grandi dimensioni su compiti di ragionamento complesso chiedendo esplicitamente al modello di articolare la sua logica passo dopo passo. Invece di saltare direttamente

### Summary

Il prompting del pensiero concatenato è una tecnica che incoraggia i modelli linguistici di grandi dimensioni (LLM) a generare passaggi di ragionamento intermedi prima di produrre una risposta finale.

## Key Concepts

- Ragionamento passo dopo passo
- Apprendimento few-shot
- Deduzione logica
- Passaggi intermedi

## Use Cases

- Risoluzione di problemi matematici complessi
- Compiti di ragionamento logico complesso
- Debug degli errori nella generazione di codice

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Prompting zero-shot (Senza esempi)](/en/terms/prompting-zero-shot-senza-esempi/)
- [Prompting few-shot (Con pochi esempi)](/en/terms/prompting-few-shot-con-pochi-esempi/)
- [Auto-consistenza (Verifica della coerenza delle risposte)](/en/terms/auto-consistenza-verifica-della-coerenza-delle-risposte/)
- [Ragionamento (Processo cognitivo di deduzione)](/en/terms/ragionamento-processo-cognitivo-di-deduzione/)
