---
title: Long Context
term_id: long_context
category: basic_concepts
subcategory: ''
tags:
- NLP
- transformers
- architecture
difficulty: 2
weight: 1
slug: long_context
date: '2026-07-18T10:05:43.261513Z'
lastmod: '2026-07-18T11:44:44.694079Z'
draft: false
source: agnes_llm
status: published
language: en
description: The ability of a language model to process and retain information from
  input sequences containing thousands or millions of tokens.
---
## Definition

Long context refers to the capacity of transformer-based models to handle extensive input lengths, often exceeding standard limits like 2k or 4k tokens. This capability allows models to analyze entire documents, codebases, or lengthy conversations in a single pass. Achieving this requires architectural innovations such as efficient attention mechanisms (e.g., FlashAttention) or positional encoding adjustments to maintain coherence and memory over vast distances within the sequence.

### Summary

The ability of a language model to process and retain information from input sequences containing thousands or millions of tokens.

## Key Concepts

- Context window
- Token limit
- Attention mechanism
- Positional encoding

## Use Cases

- Summarizing full legal contracts
- Analyzing complete source code repositories
- Processing long-form audio transcripts

## Related Terms

- [Context Window](/en/terms/context-window/)
- [Transformer Architecture](/en/terms/transformer-architecture/)
- [RoPE (Rotary Positional Embeddings)](/en/terms/rope-rotary-positional-embeddings/)
- [KV Cache](/en/terms/kv-cache/)
