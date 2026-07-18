---
title: "高速公路网络"
term_id: "highway_network"
category: "basic_concepts"
subcategory: ""
tags: ["neural_networks", "deep_learning", "architecture"]
difficulty: 4
weight: 1
slug: "highway_network"
aliases:
  - /zh/terms/highway_network/
date: "2026-07-18T11:20:58.430843Z"
lastmod: "2026-07-18T11:44:45.513841Z"
draft: false
source: "agnes_llm"
status: "published"
language: "zh"
description: "一种深度神经网络架构，引入门控机制以促进梯度在极深网络中的流动。"
---

## Definition

高速公路网络旨在通过引入自适应门控来控制信息流，从而解决深度学习中的梯度消失问题。类似于LSTM单元，这些门允许网络决定保留多少原始输入信息以及多少经过变换的信息。这使得训练非常深的网络成为可能，而不会遇到传统的梯度消失或爆炸问题。

### Summary

一种深度神经网络架构，引入门控机制以促进梯度在极深网络中的流动。

## Key Concepts

- 门控机制
- 梯度消失
- 深度学习
- 信息流

## Use Cases

- 深度神经网络
- 语音识别
- 计算机视觉

## Related Terms

- [Residual Network (残差网络)](/en/terms/residual-network-残差网络/)
- [LSTM (长短期记忆网络)](/en/terms/lstm-长短期记忆网络/)
- [Skip Connection (跳跃连接)](/en/terms/skip-connection-跳跃连接/)
