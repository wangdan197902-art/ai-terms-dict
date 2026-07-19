---
title: フィ係数
term_id: phi_coefficient
category: basic_concepts
subcategory: ''
tags:
- statistics
- Evaluation Metrics
- Binary Classification
difficulty: 3
weight: 1
slug: phi_coefficient
date: '2026-07-18T11:28:02.045986Z'
lastmod: '2026-07-18T11:44:45.131878Z'
draft: false
source: agnes_llm
status: published
language: ja
description: 2つの二値変数の間の関連性を測る統計指標。
---
## Definition

フィ係数（φ）は、2つの二値変数の間の関連性を測る指標であり、二分変数に対するピアソン相関係数として機能します。-1から+1の範囲を取り、0は無相関を意味します。

### Summary

2つの二値変数の間の関連性を測る統計指標。

## Key Concepts

- 二値変数
- 相関
- 分割表
- 関連の強さ

## Use Cases

- 精度以外のバイナリ分類器のパフォーマンス評価
- Yes/No回答を含む調査データの関係性分析
- カテゴリカル入力を持つデータセットにおける特徴量選択

## Code Example

```python
import numpy as np
from scipy.stats import chi2_contingency
# Example: Calculate phi coefficient from a 2x2 confusion matrix
tn, fp, fn, tp = 90, 10, 5, 95
matrix = [[tn, fp], [fn, tp]]
chi2, p, dof, expected = chi2_contingency(matrix)
phi = np.sqrt(chi2 / (tn + fp + fn + tp))
print(f'Phi coefficient: {phi:.3f}')
```

## Related Terms

- [クレイマーV (カテゴリカル変数の相関強度)](/en/terms/クレイマーv-カテゴリカル変数の相関強度/)
- [ピアソン相関係数 (線形相関の指標)](/en/terms/ピアソン相関係数-線形相関の指標/)
- [混同行列 (分類結果の集計表)](/en/terms/混同行列-分類結果の集計表/)
- [相互情報量 (変数間の依存性の測定)](/en/terms/相互情報量-変数間の依存性の測定/)
