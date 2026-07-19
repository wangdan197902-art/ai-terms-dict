# AI Terms Dictionary / AI 术语词典

> 🌐 **官网 / Website**: [terms.ai-term-hub.com](https://terms.ai-term-hub.com/)
>
> 🌍 多语种 AI 术语词典 | Multilingual AI Terminology Dictionary
>
> 📊 1000+ 术语 × 26 语种 = 26,000+ 页面

[![Website](https://img.shields.io/badge/Website-terms.ai--term--hub.com-blue)](https://terms.ai-term-hub.com/)
[![Languages](https://img.shields.io/badge/Languages-26-green)](https://terms.ai-term-hub.com/)
[![Terms](https://img.shields.io/badge/Terms-1000%2B-orange)](https://terms.ai-term-hub.com/en/terms/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

## 🌍 官网链接 / Website Links

| Language | URL |
|----------|-----|
| English | https://terms.ai-term-hub.com/en/ |
| 中文 | https://terms.ai-term-hub.com/zh/ |
| 日本語 | https://terms.ai-term-hub.com/ja/ |
| 한국어 | https://terms.ai-term-hub.com/ko/ |
| Español | https://terms.ai-term-hub.com/es/ |
| Deutsch | https://terms.ai-term-hub.com/de/ |
| Français | https://terms.ai-term-hub.com/fr/ |
| Русский | https://terms.ai-term-hub.com/ru/ |
| Português | https://terms.ai-term-hub.com/pt/ |
| Italiano | https://terms.ai-term-hub.com/it/ |
| العربية | https://terms.ai-term-hub.com/ar/ |
| 其他 15 种语言 | https://terms.ai-term-hub.com/ |

## 📖 项目介绍 / Introduction

**中文**：

AI 术语词典是一个多语种 AI 术语知识库，覆盖人工智能、机器学习、深度学习、自然语言处理、计算机视觉等领域。项目旨在为全球开发者和学习者提供准确、统一、多语种的 AI 术语参考。

- 收录 1004 个核心 AI 术语，涵盖从基础概念到前沿技术
- 支持 26 种语言，覆盖全球主要语种
- 每个术语页面包含定义、示例、相关术语、标签分类
- 静态生成，CDN 分发，全球极速访问

**English**:

AI Terms Dictionary is a multilingual AI terminology knowledge base covering artificial intelligence, machine learning, deep learning, natural language processing, computer vision, and more. The project aims to provide accurate, consistent, and multilingual AI terminology references for developers and learners worldwide.

- 1004 core AI terms, from foundational concepts to cutting-edge technologies
- 26 languages covering major global languages
- Each term page includes definition, examples, related terms, and tags
- Static generation with CDN distribution for fast global access

## ✨ 主要功能 / Features

- 🔍 **全文搜索 / Full-text Search**：基于 Pagefind 的静态搜索，支持 CJK 分词
- 🌐 **26 种语言 / 26 Languages**：英文、中文、日语、韩语、西语、法语、德语、俄语等
- 🏷️ **标签系统 / Tag System**：1000+ 标签聚合页，方便发现相关术语
- 📚 **分类浏览 / Category Browse**：6 大分类（基础概念、机器学习、深度学习、NLP、计算机视觉、应用）
- 📱 **响应式设计 / Responsive Design**：移动端友好
- ⚡ **极速加载 / Fast Loading**：Hugo 静态生成 + CDN 分发
- 🔗 **SEO 优化 / SEO Optimized**：Schema.org 结构化数据 + hreflang 多语种标注

## 🛠️ 技术栈 / Tech Stack

- **Static Site Generator**: Hugo v0.164+
- **Search**: Pagefind
- **Hosting**: Netlify
- **CI/CD**: GitHub Actions
- **Domain**: terms.ai-term-hub.com (Netlify DNS + SSL)
- **Analytics**: Google Analytics 4
- **SEO**: Schema.org Structured Data + hreflang

## 🌐 支持的语言 / Supported Languages

| Code | Language | Code | Language |
|------|----------|------|----------|
| en | English | ar | العربية |
| zh | 中文 | it | Italiano |
| ja | 日本語 | nl | Nederlands |
| ko | 한국어 | pl | Polski |
| es | Español | pt | Português |
| de | Deutsch | ru | Русский |
| fr | Français | tr | Türkçe |
| vi | Tiếng Việt | th | ไทย |
| id | Bahasa Indonesia | sv | Svenska |
| cs | Čeština | da | Dansk |
| fi | Suomi | no | Norsk |
| he | עברית | ro | Română |
| hu | Magyar | el | Ελληνικά |

## 📂 项目结构 / Project Structure

```
aiterms-dictionary/
├── content/           # Markdown content (1000+ terms × 26 languages)
├── layouts/           # Hugo templates
├── static/            # Static assets (images, CSS)
├── assets/            # Hugo asset pipelines (CSS, JS)
├── data/              # JSON data files
├── archetypes/        # Content templates
├── scripts/           # Python utility scripts
├── config/            # Hugo configuration
├── hugo.toml          # Hugo config
└── .github/workflows/ # CI/CD (Netlify auto-deploy)
```

## 🚀 部署 / Deployment

- **Production URL**: https://terms.ai-term-hub.com/
- **GitHub Repo**: https://github.com/wangdan197902-art/ai-terms-dict
- **Hosting**: Netlify (via GitHub Actions auto-deploy, custom domain: terms.ai-term-hub.com)

自动部署：push 到 `main` 分支即触发 GitHub Actions 构建 → Netlify 部署。

## 💻 本地开发 / Local Development

```bash
# Install Hugo (macOS)
brew install hugo

# Run dev server
hugo server -D

# Build for production
hugo --minify --baseURL "https://terms.ai-term-hub.com/"
```

## 📊 数据统计 / Statistics

- 术语总数 / Total Terms: 1004
- 语种数 / Languages: 26
- HTML 页面 / HTML Pages: ~52,000
- GitHub 仓库 / Repository: [ai-terms-dict](https://github.com/wangdan197902-art/ai-terms-dict)

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🔗 Links

- 🌐 **Website**: https://terms.ai-term-hub.com/
- 🐙 **GitHub**: https://github.com/wangdan197902-art/ai-terms-dict
- 📧 **Contact**: wangdan197902@gmail.com
