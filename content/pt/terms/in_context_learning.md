---
title: "Aprendizado em Contexto"
term_id: "in_context_learning"
category: "application_paradigms"
subcategory: ""
tags: ["Prompting", "Adaptation", "LLM Techniques"]
difficulty: 3
weight: 1
slug: "in_context_learning"
date: "2026-07-18T14:33:04.326056Z"
lastmod: "2026-07-18T15:51:59.424366Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Uma técnica na qual os modelos aprendem a realizar tarefas observando exemplos fornecidos no prompt."
---
## Definition

O aprendizado em contexto (ICL) permite que grandes modelos de linguagem se adaptem a novas tarefas sem atualizar seus pesos. Ao fornecer pares de entrada-saída dentro do contexto do prompt, o modelo infere o padrão e realiza a tarefa.

### Summary

Uma técnica na qual os modelos aprendem a realizar tarefas observando exemplos fornecidos no prompt.

## Key Concepts

- Aprendizado com Poucos Exemplos (Few-Shot Learning)
- Zero-Shot
- Design de Prompt
- Adaptação Sem Atualização de Pesos (Weight-Free Adaptation)

## Use Cases

- Teste rápido das capacidades do modelo em novos conjuntos de dados
- Alternância dinâmica de tarefas em agentes conversacionais
- Prototipagem de aplicações de IA sem retreinamento

## Code Example

```python
prompt = "Translate English to French:\nEnglish: Hello\nFrench: Bonjour\nEnglish: Cat\nFrench:"
response = model.generate(prompt)
```

## Related Terms

- [Engenharia de Prompt (Prompt Engineering)](/en/terms/engenharia-de-prompt-prompt-engineering/)
- [Few-Shot (Com Poucos Exemplos)](/en/terms/few-shot-com-poucos-exemplos/)
- [Zero-Shot (Sem Exemplos)](/en/terms/zero-shot-sem-exemplos/)
- [Meta-Aprendizado (Meta-Learning)](/en/terms/meta-aprendizado-meta-learning/)
