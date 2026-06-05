#!/bin/bash
# TubeMind AI - One-Click Deploy to Railway + Netlify
set -e

echo "🚀 TubeMind AI Deployment"
echo "========================="
echo ""
echo "This script helps you deploy:"
echo "  1. Backend → Railway"
echo "  2. Frontend → Netlify"
echo ""

# Check git
git status >/dev/null 2>&1 || { echo "❌ Not a git repo"; exit 1; }

echo "📤 Pushing to GitHub..."
git add -A
git commit -m "🚀 Deploy: $(date +\'%Y-%m-%d %H:%M\')" --allow-empty
git push origin main

echo ""
echo "✅ Code pushed to GitHub!"
echo ""
echo "🔗 Next steps:"
echo "  1. Railway will auto-deploy Backend in 2-3 minutes"
echo "  2. Netlify will auto-deploy Frontend in 2-3 minutes"
echo ""
echo "📊 Monitor at:"
echo "  • Railway: https://railway.app/dashboard"
echo "  • Netlify: https://app.netlify.com"
