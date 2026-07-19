---
title: PagedAttention
term_id: pagedattention
category: training_techniques
subcategory: ''
tags:
- inference
- Optimization
- Memory Management
difficulty: 4
weight: 1
slug: pagedattention
date: '2026-07-18T11:26:43.375946Z'
lastmod: '2026-07-18T11:44:45.129978Z'
draft: false
source: agnes_llm
status: published
language: ja
description: PagedAttentionは、仮想メモリのページング概念を適応させて、トランスフォーマーモデルにおけるキーバリュー（KV）キャッシュの保存とアクセスを最適化するメモリ管理アルゴリズムです。
---
## Definition

PagedAttentionは、vLLMプロジェクトによって導入された技術で、大規模言語モデル（LLM）の推論効率を向上させることを目的としています。従来のKVキャッシュ管理におけるメモリ断片化とオーバーヘッドの問題に対処し、メモリを非連続的なブロックに分割して割り当てることで、GPUメモリの使用量を大幅に削減し、スループットを向上させます。

### Summary

PagedAttentionは、仮想メモリのページング概念を適応させて、トランスフォーマーモデルにおけるキーバリュー（KV）キャッシュの保存とアクセスを最適化するメモリ管理アルゴリズムです。

## Key Concepts

- KVキャッシュ管理
- メモリ断片化
- 推論最適化
- 仮想メモリページング

## Use Cases

- 高スループットなLLMサービング
- GPUメモリ使用量の削減
- 本番環境でのバッチ処理の最適化

## Related Terms

- [vLLM (vLLMライブラリ)](/en/terms/vllm-vllmライブラリ/)
- [Key-Value Cache (キーバリューキャッシュ)](/en/terms/key-value-cache-キーバリューキャッシュ/)
- [Transformer Architecture (トランスフォーマーアーキテクチャ)](/en/terms/transformer-architecture-トランスフォーマーアーキテクチャ/)
- [GPU Memory Optimization (GPUメモリ最適化)](/en/terms/gpu-memory-optimization-gpuメモリ最適化/)
