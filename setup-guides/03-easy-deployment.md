# 🚀 الخطوة 3: النشر السهل (30 دقيقة)

## ⚙️ Backend على Railway

1. روح: https://railway.app
2. New Project → Deploy from GitHub repo
3. اختر: tubemind-ai
4. Root Directory: `code/backend`
5. Variables → أضف:
```
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_KEY=eyJxxx
ANTHROPIC_API_KEY=sk-ant-xxx
GOOGLE_CLIENT_ID=xxx.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=GOCSPX-xxx
HF_TOKEN=hf_xxx
FAL_KEY=xxx
SECRET_KEY=tubemind-secret-2024
```
6. اضغط Deploy
7. انسخ الـ URL → مثل: https://tubemind-backend-production.up.railway.app

## 🌐 Frontend على Netlify

1. روح: https://app.netlify.com
2. Add new site → Import existing project → GitHub
3. اختر: tubemind-ai
4. Build settings:
   - Base directory: `code/frontend`
   - Build command: `npm run build`
   - Publish directory: `code/frontend/.next`
5. Environment variables:
```
NEXT_PUBLIC_API_URL=https://tubemind-backend-production.up.railway.app
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJxxx
```
6. Deploy site

## ✅ التحقق

بعد النشر:
- Backend: https://tubemind-backend-production.up.railway.app/health
- Frontend: https://tubemind-ai.netlify.app
