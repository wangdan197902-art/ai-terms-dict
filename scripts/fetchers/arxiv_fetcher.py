#!/usr/bin/env python3
"""arXiv AI术语抓取器。

从arxiv.org的cs.AI分类抓取近期论文，从标题和摘要中提取AI术语。

API: https://export.arxiv.org/api/query?search_query=cat:cs.AI&start=0&max_results=N&sortBy=submittedDate&sortOrder=descending
返回Atom XML格式。
"""
import re
import time
import xml.etree.ElementTree as ET
from typing import List, Dict, Any

from scripts.fetchers.base import BaseFetcher, fetch_url


# arXiv命名空间
NAMESPACES = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
    "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
}


class ArxivFetcher(BaseFetcher):
    """arXiv抓取器。"""

    name = "arxiv"

    # 要抓取的arXiv分类
    ARXIV_CATEGORIES = [
        "cs.AI",   # Artificial Intelligence
        "cs.LG",   # Machine Learning
        "cs.CL",   # Computation and Language (NLP)
        "cs.CV",   # Computer Vision
        "cs.MA",   # Multi-Agent Systems
        "cs.RO",   # Robotics
        "stat.ML", # Machine Learning (Stats)
    ]

    # 要忽略的非术语词（高频但非术语）
    STOPWORDS = {
        "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
        "of", "with", "by", "from", "as", "is", "are", "was", "were", "be",
        "been", "being", "have", "has", "had", "do", "does", "did", "will",
        "would", "could", "should", "may", "might", "must", "can", "shall",
        "this", "that", "these", "those", "i", "you", "he", "she", "it",
        "we", "they", "what", "which", "who", "when", "where", "why", "how",
        "all", "each", "every", "both", "few", "more", "most", "other",
        "some", "such", "no", "nor", "not", "only", "own", "same", "so",
        "than", "too", "very", "just", "now", "also", "well", "here",
        "there", "out", "up", "down", "off", "over", "under", "again",
        "further", "then", "once", "very", "via", "using", "based",
        "approach", "method", "methods", "model", "models", "results",
        "result", "study", "studies", "paper", "research", "work",
        "proposed", "novel", "new", "existing", "previous", "recent",
        "show", "shown", "shows", "demonstrate", "demonstrates",
        "present", "presents", "presented", "introduce", "introduces",
        "introduced", "describe", "describes", "described", "discuss",
        "discusses", "discussed", "analyze", "analyzes", "analyzed",
        "evaluate", "evaluates", "evaluated", "compare", "compares",
        "compared", "however", "although", "though", "while", "whereas",
        "because", "since", "therefore", "thus", "hence", "consequently",
        "data", "dataset", "datasets", "training", "testing", "validation",
        "performance", "accuracy", "efficiency", "effective", "effectively",
        "better", "best", "good", "bad", "high", "low", "large", "small",
        "problem", "problems", "solution", "solutions", "task", "tasks",
        "framework", "frameworks", "system", "systems", "network",
        "networks", "architecture", "architectures", "algorithm",
        "algorithms", "learning", "deep", "neural", "artificial",
        "intelligence", "machine", "computer", "human", "humans",
        "real", "world", "applications", "application", "use", "uses",
        "used", "using", "able", "ability", "different", "similar",
        "various", "many", "much", "one", "two", "three", "first",
        "second", "third", "last", "final", "initial", "current",
        "previous", "next", "following", "above", "below", "et", "al",
    }

    def fetch_papers(self, category: str, max_results: int = 100) -> List[Dict[str, Any]]:
        """抓取指定分类的论文。"""
        papers = []
        batch_size = 50

        for start in range(0, max_results, batch_size):
            url = (
                f"https://export.arxiv.org/api/query?"
                f"search_query=cat:{category}&start={start}&max_results={batch_size}&"
                f"sortBy=submittedDate&sortOrder=descending"
            )
            print(f"  抓取: {category} (start={start})")
            content = fetch_url(url, timeout=25, retries=3, delay=3.0)

            if not content:
                break

            try:
                root = ET.fromstring(content)
                entries = root.findall("atom:entry", NAMESPACES)
                if not entries:
                    break

                for entry in entries:
                    title = entry.findtext("atom:title", "", NAMESPACES)
                    summary = entry.findtext("atom:summary", "", NAMESPACES)

                    # 清理空白
                    title = " ".join(title.split())
                    summary = " ".join(summary.split())

                    papers.append({
                        "title": title,
                        "summary": summary,
                        "category": category,
                    })
                print(f"    ✓ 获取 {len(entries)} 篇论文")
            except ET.ParseError as e:
                print(f"  ✗ XML解析失败: {e}")
                break

            time.sleep(3.0)  # arXiv要求3秒间隔

            if len(papers) >= max_results:
                break

        return papers[:max_results]

    def extract_terms_from_papers(self, papers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """从论文标题和摘要中提取术语。

        策略：
        1. 提取所有名词短语（Capitalized words或全小写）
        2. 过滤停用词
        3. 保留长度3-50的术语
        4. 频次过滤（出现≥2次）
        """
        from collections import Counter

        term_freq = Counter()

        for paper in papers:
            text = paper["title"] + " " + paper["summary"]

            # 提取候选术语：连续的Capitalized词组
            # 匹配: "Large Language Model", "Reinforcement Learning", etc.
            patterns = [
                r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\b',  # 多个Capitalized词
                r'\b([A-Z][a-z]{3,})\b',  # 单个Capitalized词（≥4字符）
                r'\b([a-z]+(?:[-_][a-z]+)+)\b',  # 连字符词组
            ]

            for pattern in patterns:
                matches = re.findall(pattern, text)
                for m in matches:
                    term = m.strip()
                    if len(term) < 3 or len(term) > 60:
                        continue
                    # 跳过纯停用词
                    if term.lower() in self.STOPWORDS:
                        continue
                    # 跳过包含数字的（通常是引用编号）
                    if re.search(r'\d', term):
                        continue
                    term_freq[term] += 1

        # 频次过滤：出现≥2次
        terms = []
        for term, freq in term_freq.most_common():
            if freq < 2:
                break

            term_name = self.normalize_term(term)
            if not term_name or len(term_name) < 3:
                continue

            term_id = self.slugify(term_name)
            if not term_id:
                continue

            # 跳过停用词
            if term_name.lower() in self.STOPWORDS:
                continue

            category = self.categorize(term_name)

            terms.append({
                "term_id": term_id,
                "english": term_name,
                "category": category,
                "subcategory": "",
                "source": "arxiv",
                "source_url": "https://arxiv.org/list/cs.AI/recent",
                "aliases": [],
                "importance": min(5, 2 + freq),  # 频次越高重要性越高
                "first_seen_year": None,
                "frequency": freq,
            })

        return terms

    def fetch_terms(self, limit: int = 200) -> List[Dict[str, Any]]:
        """抓取arXiv术语。"""
        print(f"[ArxivFetcher] 开始抓取，目标: {limit} 术语")

        all_papers = []
        for cat in self.ARXIV_CATEGORIES:
            papers = self.fetch_papers(cat, max_results=80)
            all_papers.extend(papers)
            print(f"  ✓ {cat}: 共 {len(all_papers)} 篇论文")
            time.sleep(2.0)

        print(f"  ✓ 共抓取论文: {len(all_papers)}")

        terms = self.extract_terms_from_papers(all_papers)
        print(f"  ✓ 提取唯一术语: {len(terms)}")

        return terms[:limit]


if __name__ == "__main__":
    fetcher = ArxivFetcher()
    terms = fetcher.fetch_terms(limit=200)
    filepath = fetcher.save_raw(terms, "arxiv_terms.json")
    print(f"✓ 保存到: {filepath}")
    from collections import Counter
    cat_counts = Counter(t["category"] for t in terms)
    print(f"分类分布: {dict(cat_counts)}")
