---
title: "Self-Consistency"
term_id: "self_consistency"
category: "training_techniques"
subcategory: ""
tags: ["LLM", "inference", "technique"]
difficulty: 4
weight: 1
slug: "self_consistency"
aliases:
  - /en/terms/self_consistency/
date: "2026-07-18T10:14:51.879133Z"
lastmod: "2026-07-18T11:44:44.719626Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "Self-consistency is a decoding strategy where multiple reasoning paths are sampled and the most frequent answer is selected as the final output."
---

## Definition

Primarily used with Large Language Models (LLMs), this technique improves accuracy by generating several diverse responses to a prompt via sampling. Instead of relying on greedy decoding, it aggregates these outputs and applies majority voting to determine the most consistent result. This method effectively reduces hallucinations and enhances logical reasoning capabilities in complex tasks like mathematical problem-solving or code generation.

### Summary

Self-consistency is a decoding strategy where multiple reasoning paths are sampled and the most frequent answer is selected as the final output.

## Key Concepts

- Majority voting
- Decoding strategy
- LLM reasoning
- Hallucination reduction

## Use Cases

- Mathematical word problems
- Complex logical deduction
- Code synthesis tasks

## Related Terms

- [Chain-of-thought](/en/terms/chain-of-thought/)
- [Temperature sampling](/en/terms/temperature-sampling/)
- [Ensemble methods](/en/terms/ensemble-methods/)
- [Prompt engineering](/en/terms/prompt-engineering/)
