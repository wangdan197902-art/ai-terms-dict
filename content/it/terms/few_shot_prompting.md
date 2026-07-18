---
title: "Prompting Few-Shot"
term_id: "few_shot_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["prompting", "llm", "technique"]
difficulty: 2
weight: 1
slug: "few_shot_prompting"
aliases:
  - /it/terms/few_shot_prompting/
date: "2026-07-18T15:35:33.417414Z"
lastmod: "2026-07-18T17:15:08.585777Z"
draft: false
source: "agnes_llm"
status: "published"
language: "it"
description: "Il prompting few-shot è una tecnica in cui i modelli linguistici di grandi dimensioni (LLM) ricevono un piccolo numero di esempi input-output all'interno del prompt per guidarne il comportamento."
---

## Definition

Questo metodo sfrutta le capacità di apprendimento contestuale dei grandi modelli linguistici fornendo alcuni esempi illustrativi direttamente nel prompt. A differenza del fine-tuning, che richiede l'aggiornamento dei pesi del modello, questa tecnica modifica solo l'input per ottenere prestazioni migliori su compiti specifici.

### Summary

Il prompting few-shot è una tecnica in cui i modelli linguistici di grandi dimensioni (LLM) ricevono un piccolo numero di esempi input-output all'interno del prompt per guidarne il comportamento.

## Key Concepts

- Apprendimento contestuale
- Ingegneria del prompt
- Guida basata sugli esempi
- Confronto zero-shot

## Use Cases

- Formattazione dell'analisi del sentiment
- Adattamento dello stile di codifica
- Estrazione di dati strutturati

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

- [zero_shot (senza esempi)](/en/terms/zero_shot-senza-esempi/)
- [prompt_engineering (ingegneria del prompt)](/en/terms/prompt_engineering-ingegneria-del-prompt/)
- [in_context_learning (apprendimento contestuale)](/en/terms/in_context_learning-apprendimento-contestuale/)
- [llm (modelli linguistici di grandi dimensioni)](/en/terms/llm-modelli-linguistici-di-grandi-dimensioni/)
