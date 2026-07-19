---
title: Prompting com Poucos Exemplos
term_id: few_shot_prompting
category: application_paradigms
subcategory: ''
tags:
- prompting
- LLM
- technique
difficulty: 2
weight: 1
slug: few_shot_prompting
date: '2026-07-18T14:44:21.676958Z'
lastmod: '2026-07-18T15:51:59.450057Z'
draft: false
source: agnes_llm
status: published
language: pt
description: O prompting com poucos exemplos é uma técnica na qual os LLMs recebem
  um pequeno número de pares entrada-saída dentro do prompt para orientar seu comportamento.
---
## Definition

Este método aproveita as capacidades de aprendizado no contexto de grandes modelos de linguagem, fornecendo alguns exemplos ilustrativos diretamente no prompt. Ao contrário do ajuste fino (fine-tuning), que requer a atualização dos parâmetros do modelo...

### Summary

O prompting com poucos exemplos é uma técnica na qual os LLMs recebem um pequeno número de pares entrada-saída dentro do prompt para orientar seu comportamento.

## Key Concepts

- Aprendizado no contexto
- Engenharia de prompt
- Orientação baseada em exemplos
- Comparação com zero-shot

## Use Cases

- Formatação de análise de sentimento
- Adaptação de estilo de código
- Extração de dados estruturados

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

- [zero_shot (aprendizado sem exemplos)](/en/terms/zero_shot-aprendizado-sem-exemplos/)
- [prompt_engineering (engenharia de prompt)](/en/terms/prompt_engineering-engenharia-de-prompt/)
- [in_context_learning (aprendizado no contexto)](/en/terms/in_context_learning-aprendizado-no-contexto/)
- [llm (grandes modelos de linguagem)](/en/terms/llm-grandes-modelos-de-linguagem/)
