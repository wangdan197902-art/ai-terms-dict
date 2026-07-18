# AI Terms Dictionary

> Multilingual AI Terms Dictionary

## Deployment

- **Production URL**: https://terms.ai-term-hub.com/
- **GitHub Repo**: https://github.com/wangdan197902-art/ai-terms-dict
- **Hosting**: Netlify (via GitHub Actions auto-deploy, custom domain: terms.ai-term-hub.com)

## Local Development

```bash
# Install Hugo (macOS)
brew install hugo

# Run dev server
hugo server -D

# Build for production
hugo --minify --baseURL "https://terms.ai-term-hub.com/"
```

## Auto Deploy

Push to `main` branch → GitHub Actions auto-deploys to Netlify.

## Project Structure

```
├── content/           # Markdown content
├── layouts/           # Hugo templates
├── static/            # Static assets (images, CSS)
├── data/              # JSON data files
├── hugo.toml          # Hugo config
└── .github/workflows/ # CI/CD (Netlify auto-deploy)
```
