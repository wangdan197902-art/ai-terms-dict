---
title: "Docker"
term_id: "docker"
category: "engineering_practice"
subcategory: ""
tags: ["DevOps", "Infrastructure", "Deployment"]
difficulty: 2
weight: 1
slug: "docker"
date: "2026-07-18T10:58:50.315961Z"
lastmod: "2026-07-18T11:44:45.046503Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "Dockerは、軽量でポータブルなコンテナ内でアプリケーションを開発、配布、実行するためのプラットフォームです。"
---
## Definition

Dockerにより、開発者はアプリケーションとそのすべての依存関係をソフトウェア開発の標準化されたユニットにパッケージ化できます。これらのコンテナはソフトウェアを環境から分離し、一貫性を確保します。

### Summary

Dockerは、軽量でポータブルなコンテナ内でアプリケーションを開発、配布、実行するためのプラットフォームです。

## Key Concepts

- コンテナ化
- イメージ
- 分離
- ポータビリティ（移植性）

## Use Cases

- 学習済みMLモデルをマイクロサービスとしてデプロイする
- データサイエンスチームの開発環境を標準化する
- クラウドインフラストラクチャでの推論ワークロードをスケーリングする

## Code Example

```python
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

## Related Terms

- [Kubernetes (コンテナオーケストレーションツール)](/en/terms/kubernetes-コンテナオーケストレーションツール/)
- [Virtual Machine (仮想マシン)](/en/terms/virtual-machine-仮想マシン/)
- [CI/CD (継続的インテグレーション/継続的デリバリー)](/en/terms/ci-cd-継続的インテグレーション-継続的デリバリー/)
- [Microservices (マイクロサービス)](/en/terms/microservices-マイクロサービス/)
