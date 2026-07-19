---
title: "Model Index"
term_id: "model_index"
category: "basic_concepts"
subcategory: ""
tags: ["Configuration", "Hub", "Data Structure"]
difficulty: 2
weight: 1
slug: "model_index"
date: "2026-07-18T10:07:39.942993Z"
lastmod: "2026-07-18T11:44:44.700980Z"
draft: false
source: "agnes_llm"
status: "published"
language: "en"
description: "A Model Index is a metadata file used by the Hugging Face Hub to describe and organize model components and configurations."
---
## Definition

The index file, typically named 'model_index.json', contains structured information about a model's architecture, including pipeline type, sub-models, and configuration paths. It enables the Hub to correctly load and instantiate complex pipelines by mapping abstract identifiers to specific model files, ensuring interoperability between different libraries and versions within the ecosystem.

### Summary

A Model Index is a metadata file used by the Hugging Face Hub to describe and organize model components and configurations.

## Key Concepts

- Metadata
- Pipeline Configuration
- Model Loading
- Interoperability

## Use Cases

- Defining multi-component pipelines
- Uploading complex models to the Hub
- Automated model discovery and loading

## Related Terms

- [Config JSON](/en/terms/config-json/)
- [Pipeline](/en/terms/pipeline/)
- [Hugging Face Hub](/en/terms/hugging-face-hub/)
- [Serialization](/en/terms/serialization/)
