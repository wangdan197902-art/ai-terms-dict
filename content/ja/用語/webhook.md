---
title: "ウェブフック"
term_id: "webhook"
category: "engineering_practice"
subcategory: ""
tags: ["Integration", "APIs", "Automation"]
difficulty: 3
weight: 1
slug: "webhook"
aliases:
  - /ja/terms/webhook/
date: "2026-07-18T11:36:28.698513Z"
lastmod: "2026-07-18T11:44:45.155273Z"
draft: false
source: "agnes_llm"
status: "published"
language: "ja"
description: "特定のイベントによってトリガーされるユーザー定義のHTTPコールバックであり、システムが他のアプリケーションにリアルタイム通知を送信することを可能にします。"
---

## Definition

ウェブフックは、あるサービスがイベント発生時に別のサービスにリアルタイム情報を提供するためのメカニズムです。変更を定期的に確認するポーリングの代わりに、ソースシステムは特定のURLに対してHTTP POSTリクエストを送信してデータをプッシュします。

### Summary

特定のイベントによってトリガーされるユーザー定義のHTTPコールバックであり、システムが他のアプリケーションにリアルタイム通知を送信することを可能にします。

## Key Concepts

- イベント駆動
- HTTP POST
- コールバックURL
- プッシュ通知

## Use Cases

- 自動化されたCI/CDデプロイメント
- 決済ゲートウェイからの通知
- Slackボットとの連携

## Related Terms

- [API (API)](/en/terms/api-api/)
- [イベント駆動アーキテクチャ (Event-driven architecture)](/en/terms/イベント駆動アーキテクチャ-event-driven-architecture/)
- [REST (REST)](/en/terms/rest-rest/)
- [インテグレーション (Integration)](/en/terms/インテグレーション-integration/)
