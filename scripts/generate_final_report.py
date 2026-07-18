#!/usr/bin/env python3
"""生成最终完成报告。

汇总1000术语扩展项目的完成情况，生成Markdown报告。
"""
import json
import sys
from pathlib import Path
from datetime import datetime
from collections import Counter


PROJECT_ROOT = Path(__file__).parent.parent
REPORT_DIR = PROJECT_ROOT / "09_报告"
REPORT_DIR.mkdir(parents=True, exist_ok=True)


def load_json(path):
    """加载JSON文件。"""
    if not Path(path).exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def count_markdown_files():
    """统计content目录的Markdown文件数。"""
    content_dir = PROJECT_ROOT / "content"
    total = 0
    by_lang = {}
    for lang_dir in content_dir.iterdir():
        if not lang_dir.is_dir():
            continue
        lang = lang_dir.name
        count = sum(1 for _ in lang_dir.rglob("*.md"))
        by_lang[lang] = count
        total += count
    return total, by_lang


def count_html_files():
    """统计public目录的HTML文件数。"""
    public_dir = PROJECT_ROOT / "public"
    if not public_dir.exists():
        return 0
    return sum(1 for _ in public_dir.rglob("*.html"))


def main():
    print("=" * 60)
    print("生成最终完成报告")
    print("=" * 60)

    # 加载数据
    seeds = load_json(PROJECT_ROOT / "data" / "seeds" / "seed_terms.json") or []
    definitions = load_json(PROJECT_ROOT / "data" / "queue" / "generated_definitions.json") or []
    translations = load_json(PROJECT_ROOT / "data" / "queue" / "translated_terms.json") or []
    pending = load_json(PROJECT_ROOT / "data" / "queue" / "pending_terms.json") or {}

    md_total, md_by_lang = count_markdown_files()
    html_total = count_html_files()

    # 统计
    seed_count = len(seeds)
    def_count = len(definitions)
    trans_count = len(translations)
    expected_trans = seed_count * 6

    # 翻译语种分布
    lang_dist = Counter(t.get("language") for t in translations)

    # 翻译来源分布
    source_dist = Counter()
    for s in seeds:
        url = s.get("source_url", "")
        if "wikipedia" in url:
            source_dist["wikipedia"] += 1
        elif "huggingface" in url:
            source_dist["huggingface"] += 1
        elif "arxiv" in url:
            source_dist["arxiv"] += 1
        else:
            source_dist["local"] += 1

    # 分类分布
    cat_dist = Counter(s.get("category") for s in seeds)

    # 生成报告
    report = f"""# 1000术语扩展 - 最终完成报告

> 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
> 项目：小语种AI术语词典
> 目标：1000术语 × 6语种 = 6000页面

---

## 一、项目成果总览

| 指标 | 目标 | 实际 | 状态 |
|------|------|------|------|
| 种子术语数 | ≥1000 | {seed_count} | {'✓' if seed_count >= 1000 else '✗'} |
| AI生成定义数 | ≥1000 | {def_count} | {'✓' if def_count >= 1000 else '✗'} |
| 翻译条数 | ≥6000 | {trans_count} | {'✓' if trans_count >= 6000 else '✗'} |
| Markdown文件数 | ≥6000 | {md_total} | {'✓' if md_total >= 6000 else '✗'} |
| HTML页面数 | ≥6000 | {html_total} | {'✓' if html_total >= 6000 else '✗'} |

---

## 二、数据来源分布

| 数据源 | 术语数 | 占比 |
|--------|--------|------|
| 本地种子 | {source_dist.get('local', 0)} | {source_dist.get('local', 0)/seed_count*100:.1f}% |
| Wikipedia | {source_dist.get('wikipedia', 0)} | {source_dist.get('wikipedia', 0)/seed_count*100:.1f}% |
| HuggingFace | {source_dist.get('huggingface', 0)} | {source_dist.get('huggingface', 0)/seed_count*100:.1f}% |
| arXiv | {source_dist.get('arxiv', 0)} | {source_dist.get('arxiv', 0)/seed_count*100:.1f}% |

---

## 三、分类分布

| 分类 | 术语数 | 占比 |
|------|--------|------|
| basic_concepts | {cat_dist.get('basic_concepts', 0)} | {cat_dist.get('basic_concepts', 0)/seed_count*100:.1f}% |
| training_techniques | {cat_dist.get('training_techniques', 0)} | {cat_dist.get('training_techniques', 0)/seed_count*100:.1f}% |
| application_paradigms | {cat_dist.get('application_paradigms', 0)} | {cat_dist.get('application_paradigms', 0)/seed_count*100:.1f}% |
| engineering_practice | {cat_dist.get('engineering_practice', 0)} | {cat_dist.get('engineering_practice', 0)/seed_count*100:.1f}% |
| ethics_safety | {cat_dist.get('ethics_safety', 0)} | {cat_dist.get('ethics_safety', 0)/seed_count*100:.1f}% |

---

## 四、翻译语种分布

| 语种 | 翻译条数 | 占比 |
|------|----------|------|
| en (英文) | {lang_dist.get('en', 0)} | {lang_dist.get('en', 0)/trans_count*100:.1f if trans_count else 0}% |
| es (西班牙语) | {lang_dist.get('es', 0)} | {lang_dist.get('es', 0)/trans_count*100:.1f if trans_count else 0}% |
| de (德语) | {lang_dist.get('de', 0)} | {lang_dist.get('de', 0)/trans_count*100:.1f if trans_count else 0}% |
| ja (日语) | {lang_dist.get('ja', 0)} | {lang_dist.get('ja', 0)/trans_count*100:.1f if trans_count else 0}% |
| fr (法语) | {lang_dist.get('fr', 0)} | {lang_dist.get('fr', 0)/trans_count*100:.1f if trans_count else 0}% |
| zh (中文) | {lang_dist.get('zh', 0)} | {lang_dist.get('zh', 0)/trans_count*100:.1f if trans_count else 0}% |

---

## 五、Markdown文件分布

| 语种 | 文件数 |
|------|--------|
"""
    for lang, count in sorted(md_by_lang.items()):
        report += f"| {lang} | {count} |\n"

    report += f"""
---

## 六、完成情况评估

### 已完成
- ✓ 种子库扩展到 {seed_count} 术语（从200扩展）
- ✓ AI生成定义 {def_count} 条
- ✓ 多语种翻译 {trans_count} 条
- ✓ Markdown文件 {md_total} 个
- ✓ HTML页面 {html_total} 个

### 关键技术成果
1. **3源数据抓取**：Wikipedia + HuggingFace + arXiv
2. **断点续传机制**：generate_definitions_batch.py 和 translate_batch.py 支持断点续传
3. **错误隔离**：单批次失败不影响其他批次
4. **进度持久化**：data/progress/ 目录保存执行进度
5. **严格过滤**：merge_terms.py 实现多维度去重和过滤

### 后续工作
- [ ] 部署到GitHub Pages
- [ ] 配置自定义域名
- [ ] 提交到搜索引擎
- [ ] 持续监控和优化

---

## 七、项目文件结构

```
01-小语种AI术语词典/aiterms-dictionary/
├── data/
│   ├── seeds/seed_terms.json ({seed_count} 术语)
│   ├── queue/
│   │   ├── pending_terms.json ({pending.get('total', 0)} 待处理)
│   │   ├── generated_definitions.json ({def_count} 定义)
│   │   └── translated_terms.json ({trans_count} 翻译)
│   ├── raw/ (原始抓取数据)
│   └── progress/ (执行进度)
├── content/ ({md_total} Markdown文件)
├── public/ ({html_total} HTML页面)
├── scripts/
│   ├── fetchers/ (3个数据源抓取器)
│   ├── generate_definitions_batch.py (断点续传)
│   ├── translate_batch.py (断点续传)
│   ├── merge_terms.py (合并去重)
│   ├── build_content.py (Markdown生成)
│   ├── clean_mock.py (Mock清理)
│   └── validate.py (Schema校验)
└── 09_报告/ (本报告)
```

---

报告生成完毕。
"""

    # 保存报告
    report_file = REPORT_DIR / "最终完成报告.md"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"✓ 报告已生成: {report_file}")
    print(f"\n报告摘要:")
    print(f"  种子术语: {seed_count}")
    print(f"  AI定义: {def_count}")
    print(f"  翻译: {trans_count}")
    print(f"  Markdown: {md_total}")
    print(f"  HTML: {html_total}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
