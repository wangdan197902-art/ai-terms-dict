---
title: "Engenharia de Prompt"
term_id: "prompt_engineering"
category: "application_paradigms"
subcategory: ""
tags: ["LLM", "UX", "Optimization"]
difficulty: 2
weight: 1
slug: "prompt_engineering"
date: "2026-07-18T13:43:28.034998Z"
lastmod: "2026-07-18T15:51:59.422301Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "A prática de projetar e otimizar textos de entrada para orientar grandes modelos de linguagem em direção a saídas desejadas."
---
## Definition

A engenharia de prompt envolve a criação de entradas específicas, conhecidas como prompts, para elicitar respostas precisas, relevantes e de alta qualidade de modelos de IA generativa. Requer compreender como os modelos interpretam o contexto e as instruções fornecidas.

### Summary

A prática de projetar e otimizar textos de entrada para orientar grandes modelos de linguagem em direção a saídas desejadas.

## Key Concepts

- Enquadramento contextual
- Aprendizado few-shot
- Ajuste por instrução
- Otimização de tokens

## Use Cases

- Chatbots de atendimento ao cliente automatizados
- Assistentes de geração de código
- Auxiliares de escrita criativa

## Code Example

```python
prompt = "Translate the following English text to French: 'Hello world'"
response = llm.generate(prompt)
```

## Related Terms

- [LLM (Modelo de Linguagem de Grande Escala)](/en/terms/llm-modelo-de-linguagem-de-grande-escala/)
- [Chain-of-Thought (Cadeia de Pensamento)](/en/terms/chain-of-thought-cadeia-de-pensamento/)
- [RAG (Recuperação Aumentada por Geração)](/en/terms/rag-recuperação-aumentada-por-geração/)
- [Fine-tuning (Ajuste Fino)](/en/terms/fine-tuning-ajuste-fino/)
