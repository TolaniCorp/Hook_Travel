# 🚀 HOOK Travel – Deployment Guide

This guide explains how to deploy the HOOK Travel Dev Portal using **Netlify + GitHub Actions** for static site delivery and CI automation.

---

## 🧭 Deployment Flow

1. Developer pushes to `main`
2. GitHub Actions triggers `.github/workflows/static.yml`
3. The site is deployed via `netlify deploy --prod`

---

## 🔐 Required GitHub Secrets

Set the following in your GitHub repo:

| Secret Key | Description |
|------------|-------------|
| `NETLIFY_AUTH_TOKEN` | Your Netlify personal access token |
| `NETLIFY_SITE_ID` | The unique ID of your Netlify site |

To find your **Site ID**, go to Netlify → Site Settings → General → Site Information.

To get your **Auth Token**, go to [Netlify User Settings → Applications](https://app.netlify.com/user/applications)

---

## 📁 Directory Structure

| Folder | Purpose |
|--------|---------|
| `/public` | Static site files (HTML, CSS, JS) |
| `/netlify/functions` | Serverless API endpoints |
| `.github/workflows/static.yml` | CI/CD workflow for Netlify deployment |

---

## 🛠 Manual Deployment (Optional)

If you want to deploy manually:

```bash
npm install -g netlify-cli
netlify deploy --dir=public --prod --site=<your-site-id>
```

---

Let’s deploy the future of intelligent travel.  
— HOOK Web Ops 🌍✈️
