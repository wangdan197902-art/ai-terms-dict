---
title: "Conexão Residual"
term_id: "residual_connection"
category: "basic_concepts"
subcategory: ""
tags: ["architecture", "optimization", "deep_learning"]
difficulty: 3
weight: 1
slug: "residual_connection"
aliases:
  - /pt/terms/residual_connection/
date: "2026-07-18T14:45:42.847462Z"
lastmod: "2026-07-18T15:51:59.454546Z"
draft: false
source: "agnes_llm"
status: "published"
language: "pt"
description: "Um mecanismo que adiciona a entrada diretamente à saída de uma camada para facilitar o fluxo de gradiente em redes profundas."
---

## Definition

As conexões residuais, também conhecidas como conexões de salto (skip connections), permitem que os gradientes fluam através da rede ao adicionar diretamente uma entrada à saída de uma camada subsequente. Essa arquitetura resolve o problema do gradiente desaparecente, possibilitando o treinamento de redes extremamente profundas.

### Summary

Um mecanismo que adiciona a entrada diretamente à saída de uma camada para facilitar o fluxo de gradiente em redes profundas.

## Key Concepts

- Conexões de Salto
- Problema do Gradiente Desaparecente
- Aprendizado Residual Profundo
- Fluxo de Gradiente

## Use Cases

- Treinamento de redes neurais convolucionais profundas
- Arquiteturas de Transformers
- Modelos de classificação de imagens

## Code Example

```python
import torch.nn as nn
class ResidualBlock(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv = nn.Conv2d(channels, channels, 3, padding=1)
    def forward(self, x):
        return x + self.conv(x)
```

## Related Terms

- [skip_connection (Conexão de salto)](/en/terms/skip_connection-conexão-de-salto/)
- [vanishing_gradient (Gradiente desaparecente)](/en/terms/vanishing_gradient-gradiente-desaparecente/)
- [deep_learning (Aprendizado profundo)](/en/terms/deep_learning-aprendizado-profundo/)
- [resnet (Rede residual)](/en/terms/resnet-rede-residual/)
