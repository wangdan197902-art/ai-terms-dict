---
title: "Prompting de Pensamento em Cadeia"
term_id: "chain_of_thought_prompting"
category: "application_paradigms"
subcategory: ""
tags: ["Prompt Engineering", "Reasoning", "LLM Techniques"]
difficulty: 4
weight: 1
slug: "chain_of_thought_prompting"
aliases:
  - /pt/terms/chain_of_thought_prompting/
date: "2026-07-18T14:43:42.123735Z"
lastmod: "2026-07-18T15:51:59.447924Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "O Prompting de Pensamento em Cadeia é uma técnica que incentiva os LLMs a gerar etapas intermediárias de raciocínio antes de produzir uma resposta final."
---

## Definition

O prompting de Pensamento em Cadeia (CoT) melhora o desempenho dos grandes modelos de linguagem em tarefas complexas de raciocínio, solicitando explicitamente ao modelo que articule sua lógica passo a passo. Em vez de pular diretamente para a conclusão, o modelo é guiado a expor seu processo de dedução.

### Summary

O Prompting de Pensamento em Cadeia é uma técnica que incentiva os LLMs a gerar etapas intermediárias de raciocínio antes de produzir uma resposta final.

## Key Concepts

- Raciocínio Passo a Passo
- Aprendizado com Poucos Exemplos (Few-Shot Learning)
- Dedução Lógica
- Etapas Intermediárias

## Use Cases

- Resolução de problemas matemáticos verbais
- Tarefas complexas de raciocínio lógico
- Depuração de erros na geração de código

## Code Example

```python
prompt = "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. If each can has 3 balls, how many does he have?\nA: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."
print(prompt)
```

## Related Terms

- [Prompting Zero-Shot (Prompting sem exemplos)](/en/terms/prompting-zero-shot-prompting-sem-exemplos/)
- [Prompting Few-Shot (Prompting com poucos exemplos)](/en/terms/prompting-few-shot-prompting-com-poucos-exemplos/)
- [Autoconsistência](/en/terms/autoconsistência/)
- [Raciocínio](/en/terms/raciocínio/)
