---
title: "Thế giới nhỏ có thể điều hướng phân cấp"
term_id: "hierarchical_navigable_small_world"
category: "basic_concepts"
subcategory: ""
tags: ["algorithms", "search", "data_structures"]
difficulty: 4
weight: 1
slug: "hierarchical_navigable_small_world"
aliases:
  - /vi/terms/hierarchical_navigable_small_world/
date: "2026-07-18T15:56:40.760991Z"
lastmod: "2026-07-18T16:38:07.765502Z"
draft: false
source: "agnes_llm"
status: "published"
language: "vi"
description: "Một cấu trúc dữ liệu dựa trên đồ thị cho phép tìm kiếm láng giềng gần nhất xấp xỉ hiệu quả trong không gian nhiều chiều."
---

## Definition

Thuật toán Thế giới nhỏ có thể điều hướng phân cấp (HNSW) xây dựng một đồ thị đa lớp, trong đó mỗi lớp chứa một tập hợp con các nút từ lớp bên dưới. Quá trình điều hướng bắt đầu từ lớp trên cùng (ít nút nhất) để nhanh chóng tiếp cận vùng lân cận của mục tiêu, sau đó di chuyển xuống các lớp chi tiết hơn để tinh chỉnh kết quả. Phương pháp này đạt được tốc độ tìm kiếm nhanh và độ chính xác cao với độ phức tạp thời gian logarit.

### Summary

Một cấu trúc dữ liệu dựa trên đồ thị cho phép tìm kiếm láng giềng gần nhất xấp xỉ hiệu quả trong không gian nhiều chiều.

## Key Concepts

- Tìm kiếm trên đồ thị
- Láng giềng gần nhất xấp xỉ (Approximate Nearest Neighbor)
- Đồ thị đa lớp
- Độ phức tạp logarit

## Use Cases

- Tìm kiếm vector
- Công cụ gợi ý (Recommendation engines)
- Tìm kiếm hình ảnh

## Related Terms

- [K láng giềng gần nhất (K-Nearest Neighbors)](/en/terms/k-láng-giềng-gần-nhất-k-nearest-neighbors/)
- [Faiss (Thư viện tìm kiếm vector của Facebook)](/en/terms/faiss-thư-viện-tìm-kiếm-vector-của-facebook/)
- [Annoy (Thư viện tìm kiếm vector của Spotify)](/en/terms/annoy-thư-viện-tìm-kiếm-vector-của-spotify/)
