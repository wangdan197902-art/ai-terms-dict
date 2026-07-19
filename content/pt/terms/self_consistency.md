---
title: "Autoconsistência"
term_id: "self_consistency"
category: "training_techniques"
subcategory: ""
tags: ["LLM", "inference", "technique"]
difficulty: 4
weight: 1
slug: "self_consistency"
date: "2026-07-18T15:20:39.725801Z"
lastmod: "2026-07-18T15:51:59.530846Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "A autoconsistência é uma estratégia de decodificação na qual múltiplos caminhos de raciocínio são amostrados e a resposta mais frequente é selecionada como saída final."
---
## Definition

Principalmente utilizada com Grandes Modelos de Linguagem (LLMs), esta técnica melhora a precisão gerando várias respostas diversas para um prompt por meio de amostragem. Em vez de depender da decodificação gulosa (greedy), ela agrega os resultados para determinar a resposta mais provável.

### Summary

A autoconsistência é uma estratégia de decodificação na qual múltiplos caminhos de raciocínio são amostrados e a resposta mais frequente é selecionada como saída final.

## Key Concepts

- Votação por maioria
- Estratégia de decodificação
- Raciocínio em LLMs
- Redução de alucinações

## Use Cases

- Problemas matemáticos em texto
- Dedução lógica complexa
- Tarefas de síntese de código

## Related Terms

- [Chain-of-thought (Cadeia de pensamento)](/en/terms/chain-of-thought-cadeia-de-pensamento/)
- [Temperature sampling (Amostragem por temperatura)](/en/terms/temperature-sampling-amostragem-por-temperatura/)
- [Ensemble methods (Métodos de conjunto)](/en/terms/ensemble-methods-métodos-de-conjunto/)
- [Prompt engineering (Engenharia de prompts)](/en/terms/prompt-engineering-engenharia-de-prompts/)
