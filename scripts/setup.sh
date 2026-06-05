#!/bin/bash
# TubeMind AI - One-Click Setup Script
set -e

echo "🚀 TubeMind AI Setup"
echo "===================="

# Check requirements
command -v python3 >/dev/null || { echo "❌ Python 3 required"; exit 1; }
command -v node >/dev/null || { echo "❌ Node.js required"; exit 1; }

# Backend setup
echo "⚙️ Setting up Backend..."
cd code/backend
[ ! -f .env ] && cp .env.example .env && echo "📝 Created .env - fill in your API keys!"
python3 -m pip install -r requirements.txt -q
echo "✅ Backend ready"

# Frontend setup
echo "🌐 Setting up Frontend..."
cd ../frontend
[ ! -f .env.local ] && cp .env.example .env.local
npm install -q
echo "✅ Frontend ready"

cd ../..
echo ""
echo "✅ Setup Complete!"
echo ""
echo "Next steps:"
echo "1. Fill in code/backend/.env with your API keys"
echo "2. Run: cd code/backend && uvicorn main:app --reload"
echo "3. Run: cd code/frontend && npm run dev"
echo "4. Open: http://localhost:3000"
