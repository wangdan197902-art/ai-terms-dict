#!/usr/bin/env python3
"""
AI Terms Dictionary - 本地验收清单
检查7项关键功能是否可用
"""
import json
import os
import re
import sys
import urllib.request
import urllib.parse
from pathlib import Path

BASE_URL = os.environ.get("HUGO_BASE_URL", "http://localhost:1313")
TIMEOUT = 10

# 验收项颜色
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"


def fetch(url, timeout=TIMEOUT):
    """获取URL内容，返回(status_code, content)"""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "AcceptanceCheck/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return 0, str(e)


def check_url(url, expected=200):
    """检查URL是否返回预期状态码"""
    status, _ = fetch(url)
    return status == expected, status


def acceptance_01_homepage():
    """验收1: 首页可访问"""
    print(f"\n{BOLD}[1/7] 首页可访问{RESET}")
    ok, status = check_url(f"{BASE_URL}/")
    if ok:
        print(f"  {GREEN}✓{RESET} 首页 HTTP {status}")
        return True
    print(f"  {RED}✗{RESET} 首页 HTTP {status}")
    return False


def acceptance_02_term_pages():
    """验收2: 术语页可访问"""
    print(f"\n{BOLD}[2/7] 术语页可访问{RESET}")
    # 检查各语种术语列表页
    lang_paths = [
        ("en", "terms"), ("es", "terminos"), ("de", "begriffe"),
        ("ja", "用語"), ("fr", "termes"), ("zh", "术语")
    ]
    all_ok = True
    for lang, folder in lang_paths:
        url = f"{BASE_URL}/{lang}/{urllib.parse.quote(folder)}/"
        ok, status = check_url(url)
        if ok:
            print(f"  {GREEN}✓{RESET} /{lang}/{folder}/ HTTP {status}")
        else:
            print(f"  {RED}✗{RESET} /{lang}/{folder}/ HTTP {status}")
            all_ok = False

    # 检查具体术语页（prompt_engineering）
    term_url = f"{BASE_URL}/en/terms/prompt_engineering/"
    ok, status = check_url(term_url)
    if ok:
        print(f"  {GREEN}✓{RESET} /en/terms/prompt_engineering/ HTTP {status}")
    else:
        print(f"  {RED}✗{RESET} /en/terms/prompt_engineering/ HTTP {status}")
        all_ok = False
    return all_ok


def acceptance_03_language_switcher():
    """验收3: 多语言切换可用"""
    print(f"\n{BOLD}[3/7] 多语言切换可用{RESET}")
    # 检查术语页是否包含hreflang标签
    url = f"{BASE_URL}/en/terms/prompt_engineering/"
    status, content = fetch(url)
    if status != 200:
        print(f"  {RED}✗{RESET} 无法访问术语页 HTTP {status}")
        return False

    hreflangs = re.findall(r'<link rel="alternate" hreflang="([^"]+)"', content)
    if len(hreflangs) >= 6:
        print(f"  {GREEN}✓{RESET} 发现 {len(hreflangs)} 个 hreflang 标签: {', '.join(hreflangs[:6])}")
        return True
    print(f"  {YELLOW}⚠{RESET} 仅发现 {len(hreflangs)} 个 hreflang 标签（预期6+）")
    return len(hreflangs) >= 2


def acceptance_04_search():
    """验收4: 搜索可用"""
    print(f"\n{BOLD}[4/7] 搜索可用{RESET}")
    # 检查搜索页
    search_url = f"{BASE_URL}/en/search/"
    ok, status = check_url(search_url)
    if not ok:
        print(f"  {RED}✗{RESET} 搜索页 HTTP {status}")
        return False
    print(f"  {GREEN}✓{RESET} 搜索页 HTTP {status}")

    # 检查Pagefind索引
    pf_url = f"{BASE_URL}/pagefind/pagefind.js"
    ok, status = check_url(pf_url)
    if ok:
        print(f"  {GREEN}✓{RESET} Pagefind索引 HTTP {status}")
        return True
    print(f"  {RED}✗{RESET} Pagefind索引 HTTP {status}（请运行: make search-index）")
    return False


def acceptance_05_jsonld():
    """验收5: JSON-LD结构化数据有效"""
    print(f"\n{BOLD}[5/7] JSON-LD结构化数据{RESET}")
    # 检查术语页的JSON-LD
    url = f"{BASE_URL}/en/terms/prompt_engineering/"
    status, content = fetch(url)
    if status != 200:
        print(f"  {RED}✗{RESET} 无法访问术语页 HTTP {status}")
        return False

    jsonld_blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    if not jsonld_blocks:
        print(f"  {RED}✗{RESET} 未找到JSON-LD块")
        return False

    valid_count = 0
    for block in jsonld_blocks:
        try:
            data = json.loads(block.strip())
            if "@type" in data:
                valid_count += 1
        except json.JSONDecodeError:
            pass

    if valid_count > 0:
        print(f"  {GREEN}✓{RESET} 发现 {valid_count} 个有效JSON-LD块")
        return True
    print(f"  {RED}✗{RESET} JSON-LD块存在但无效")
    return False


def acceptance_06_responsive():
    """验收6: 响应式CSS存在"""
    print(f"\n{BOLD}[6/7] 响应式CSS{RESET}")
    url = f"{BASE_URL}/css/style.css"
    status, content = fetch(url)
    if status != 200:
        print(f"  {RED}✗{RESET} CSS文件 HTTP {status}")
        return False

    checks = [
        ("media (max-width: 1024px)", "1024px断点"),
        ("media (max-width: 768px)", "768px断点"),
        ("media (max-width: 480px)", "480px断点"),
        ("data-theme=\"dark\"", "深色模式"),
        ("prefers-reduced-motion", "无障碍偏好"),
    ]
    all_ok = True
    for pattern, name in checks:
        if pattern in content:
            print(f"  {GREEN}✓{RESET} {name}")
        else:
            print(f"  {RED}✗{RESET} {name} 缺失")
            all_ok = False
    return all_ok


def acceptance_07_sitemap():
    """验收7: sitemap.xml可访问"""
    print(f"\n{BOLD}[7/7] Sitemap & SEO{RESET}")
    checks = [
        (f"{BASE_URL}/sitemap.xml", "sitemap.xml"),
        (f"{BASE_URL}/robots.txt", "robots.txt"),
        (f"{BASE_URL}/llms.txt", "llms.txt"),
        (f"{BASE_URL}/og-image.svg", "og-image.svg"),
        (f"{BASE_URL}/site.webmanifest", "webmanifest"),
    ]
    all_ok = True
    for url, name in checks:
        ok, status = check_url(url)
        if ok:
            print(f"  {GREEN}✓{RESET} {name} HTTP {status}")
        else:
            print(f"  {RED}✗{RESET} {name} HTTP {status}")
            all_ok = False
    return all_ok


def main():
    print(f"{BOLD}{'='*50}{RESET}")
    print(f"{BOLD}AI Terms Dictionary - 本地验收清单{RESET}")
    print(f"{BOLD}{'='*50}{RESET}")
    print(f"目标: {BASE_URL}")

    results = []
    results.append(("首页", acceptance_01_homepage()))
    results.append(("术语页", acceptance_02_term_pages()))
    results.append(("语言切换", acceptance_03_language_switcher()))
    results.append(("搜索", acceptance_04_search()))
    results.append(("JSON-LD", acceptance_05_jsonld()))
    results.append(("响应式", acceptance_06_responsive()))
    results.append(("Sitemap/SEO", acceptance_07_sitemap()))

    print(f"\n{BOLD}{'='*50}{RESET}")
    print(f"{BOLD}验收结果汇总{RESET}")
    print(f"{BOLD}{'='*50}{RESET}")
    passed = 0
    for name, ok in results:
        icon = f"{GREEN}✓{RESET}" if ok else f"{RED}✗{RESET}"
        print(f"  {icon} {name}")
        if ok:
            passed += 1

    total = len(results)
    print(f"\n{BOLD}通过: {passed}/{total}{RESET}")
    if passed == total:
        print(f"{GREEN}{BOLD}✓ 全部验收通过！{RESET}")
        return 0
    print(f"{YELLOW}⚠ 部分验收未通过，请检查上述输出{RESET}")
    return 1 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
