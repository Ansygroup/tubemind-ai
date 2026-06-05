# 🔑 الخطوة 1: إعداد الحسابات

## الحسابات المطلوبة

### 1. Supabase (مجاني) - قاعدة البيانات
1. روح: https://supabase.com
2. Sign up
3. New Project → اختر اسم وكلمة مرور
4. Settings → API → انسخ URL و anon key

### 2. Anthropic (Claude AI) - الذكاء الاصطناعي
1. روح: https://console.anthropic.com
2. Sign up → API Keys → Create key
3. انسخ الـ key (sk-ant-...)

### 3. Hugging Face (مجاني + Pro $9)
1. روح: https://huggingface.co
2. Sign up → Settings → Access Tokens → New token
3. اشترك Pro لتشغيل Spaces بـ GPU

### 4. Fal.ai - توليد الفيديو
1. روح: https://fal.ai
2. Sign up → Dashboard → API Keys
3. اشحن $5-10 رصيد

### 5. Google Cloud - YouTube API
1. روح: https://console.cloud.google.com
2. New Project → "TubeMind AI"
3. Enable: YouTube Data API v3
4. Credentials → OAuth 2.0 → Create credentials
5. Redirect URI: https://YOUR-BACKEND.up.railway.app/auth/youtube/callback
