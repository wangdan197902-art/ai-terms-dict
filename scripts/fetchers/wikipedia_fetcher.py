#!/usr/bin/env python3
"""Wikipedia AI术语抓取器。

从en.wikipedia.org的Category:Artificial_intelligence及其子分类递归抓取术语列表。

API: https://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:XXX&cmlimit=500&format=json
"""
import json
import time
import urllib.parse
from typing import List, Dict, Any

from scripts.fetchers.base import BaseFetcher, fetch_url


# AI相关的Wikipedia分类（精选15个，避免限流）
AI_CATEGORIES = [
    "Category:Artificial_intelligence",
    "Category:Machine_learning",
    "Category:Deep_learning",
    "Category:Neural_networks",
    "Category:Natural_language_processing",
    "Category:Computer_vision",
    "Category:Reinforcement_learning",
    "Category:Large_language_models",
    "Category:Transformers (machine learning)",
    "Category:Generative artificial intelligence",
    "Category:Prompt engineering",
    "Category:Machine learning algorithms",
    "Category:Convolutional neural networks",
    "Category:Recurrent neural networks",
    "Category:Generative models",
]


class WikipediaFetcher(BaseFetcher):
    """Wikipedia抓取器。"""

    name = "wikipedia"

    def fetch_category_members(self, category: str, depth: int = 0) -> List[Dict[str, Any]]:
        """抓取一个分类下的所有页面（递归到子分类）。

        Args:
            category: 分类名（如 "Category:Artificial_intelligence"）
            depth: 当前递归深度（最大1层避免爆炸和限流）

        Returns:
            页面列表
        """
        if depth > 1:
            return []

        results = []
        cmcontinue = None
        max_pages = 500 if depth == 0 else 100  # 顶层多抓，子层少抓
        request_count = 0

        while True:
            params = {
                "action": "query",
                "list": "categorymembers",
                "cmtitle": category,
                "cmlimit": "200",
                "cmtype": "page|subcat",
                "format": "json",
            }
            if cmcontinue:
                params["cmcontinue"] = cmcontinue

            url = "https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(params)
            content = fetch_url(url, timeout=20, retries=3, delay=3.0)
            request_count += 1

            if not content:
                break

            try:
                data = json.loads(content)
            except json.JSONDecodeError:
                print(f"  ✗ JSON解析失败: {category}")
                break

            query = data.get("query", {})
            members = query.get("categorymembers", [])

            for m in members:
                ns = m.get("ns")
                title = m.get("title", "")

                if ns == 0:  # 普通页面
                    # 过滤掉"List of..."等非术语页面
                    if title.startswith("List of ") or title.startswith("Index of "):
                        continue
                    if " (disambiguation)" in title:
                        continue
                    results.append({
                        "title": title,
                        "pageid": m.get("pageid"),
                        "category_source": category,
                    })
                elif ns == 14 and depth == 0:  # 子分类（仅顶层递归1次）
                    # 不递归，只记录子分类
                    pass

            # 检查是否还有更多
            if len(results) >= max_pages:
                break

            cmcontinue = data.get("continue", {}).get("cmcontinue")
            if not cmcontinue:
                break

            # Wikipedia限流：每次请求间隔2秒
            time.sleep(2.0)

        return results

    def fetch_page_summary(self, title: str) -> Dict[str, Any]:
        """抓取页面摘要（用于推断分类）。"""
        params = {
            "action": "query",
            "prop": "extracts",
            "exintro": "1",
            "explaintext": "1",
            "titles": title,
            "format": "json",
        }
        url = "https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(params)
        content = fetch_url(url, timeout=15, retries=2, delay=1.0)
        if not content:
            return {}

        try:
            data = json.loads(content)
            pages = data.get("query", {}).get("pages", {})
            for pid, page in pages.items():
                extract = page.get("extract", "")
                return {"extract": extract[:500]}
        except Exception:
            pass
        return {}

    def fetch_terms(self, limit: int = 500) -> List[Dict[str, Any]]:
        """抓取AI相关术语。"""
        print(f"[WikipediaFetcher] 开始抓取，目标: {limit} 术语", flush=True)

        all_pages = {}
        for i, cat in enumerate(AI_CATEGORIES):
            print(f"  [{i+1}/{len(AI_CATEGORIES)}] 抓取分类: {cat}", flush=True)
            pages = self.fetch_category_members(cat, depth=0)
            for p in pages:
                # 用title去重
                key = p["title"].lower()
                if key not in all_pages:
                    all_pages[key] = p
            print(f"    ✓ 累计唯一页面: {len(all_pages)}", flush=True)
            time.sleep(2.0)  # 分类间间隔

            if len(all_pages) >= limit * 2:
                break

        print(f"  ✓ 共抓取唯一页面: {len(all_pages)}", flush=True)

        # 保存原始数据
        self.save_raw(list(all_pages.values()), "wikipedia_raw_pages.json")

        # 转换为术语格式（不抓摘要，加快速度，靠分类名推断）
        terms = []
        for page in list(all_pages.values())[:limit]:
            title = self.normalize_term(page["title"])
            if not title or len(title) < 2:
                continue

            term_id = self.slugify(title)
            if not term_id:
                continue

            # 用category_source推断分类（不调用API）
            description = page.get("category_source", "").replace("Category:", "").replace("_", " ")
            category = self.categorize(title, description)

            terms.append({
                "term_id": term_id,
                "english": title,
                "category": category,
                "subcategory": "",
                "source": "wikipedia",
                "source_url": f"https://en.wikipedia.org/wiki/{page['title'].replace(' ', '_')}",
                "aliases": [],
                "importance": 3,
                "first_seen_year": None,
            })

        print(f"  ✓ 转换为术语格式: {len(terms)}", flush=True)
        return terms


if __name__ == "__main__":
    fetcher = WikipediaFetcher()
    terms = fetcher.fetch_terms(limit=400)
    filepath = fetcher.save_raw(terms, "wikipedia_terms.json")
    print(f"✓ 保存到: {filepath}")
    # 分类统计
    from collections import Counter
    cat_counts = Counter(t["category"] for t in terms)
    print(f"分类分布: {dict(cat_counts)}")
