# 🚀 Panduan Deploy ke Vercel

Panduan lengkap untuk deploy Kanvas Chatbot API ke Vercel.

## 📋 Prerequisites

1. **Akun Vercel**: Daftar di [vercel.com](https://vercel.com)
2. **Vercel CLI** (opsional): `npm i -g vercel`
3. **Git Repository**: Project sudah di-push ke GitHub/GitLab/Bitbucket

## 🔧 Konfigurasi

### 1. File `vercel.json`

File `vercel.json` sudah dikonfigurasi dengan benar:

```json
{
    "version": 2,
    "builds": [
        {
            "src": "api/index.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "api/index.py"
        }
    ]
}
```

**Penjelasan:**
- `version: 2` - Menggunakan Vercel v2 configuration
- `builds` - Build `api/index.py` dengan Python runtime
- `routes` - Semua request di-route ke `api/index.py`

### 2. File `api/index.py`

Handler untuk Vercel yang meng-export FastAPI app:

```python
from main import app
__all__ = ["app"]
```

### 3. File `requirements.txt`

Pastikan semua dependencies ada di `requirements.txt`:

```txt
fastapi==0.115.0
uvicorn[standard]==0.34.0
pydantic==2.10.0
pydantic-settings==2.6.1
python-dotenv==1.0.1
sentence-transformers==3.3.1
numpy==2.2.0
torch==2.5.1
```

## 🚀 Deploy Methods

### Method 1: Via Vercel Dashboard (Recommended)

1. **Login ke Vercel**: https://vercel.com/login
2. **Import Project**:
   - Klik "Add New..." → "Project"
   - Pilih repository (GitHub/GitLab/Bitbucket)
   - Atau drag & drop folder project
3. **Configure Project**:
   - **Framework Preset**: Other
   - **Root Directory**: `./` (default)
   - **Build Command**: (kosongkan, Vercel auto-detect)
   - **Output Directory**: (kosongkan)
4. **Environment Variables** (jika ada):
   - Tambahkan di Settings → Environment Variables
   - Contoh:
     ```
     APP_NAME=Kanvas Chatbot API
     DEBUG=False
     LOG_LEVEL=INFO
     ```
5. **Deploy**: Klik "Deploy"

### Method 2: Via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel

# Deploy to production
vercel --prod
```

### Method 3: Via Git Push (Auto Deploy)

1. **Connect Repository**:
   - Di Vercel Dashboard, import project dari Git
   - Set up auto-deploy
2. **Push to Git**:
   ```bash
   git add .
   git commit -m "Deploy to Vercel"
   git push origin main
   ```
3. **Auto Deploy**: Vercel otomatis deploy setiap push

## ⚙️ Environment Variables

Tambahkan environment variables di Vercel Dashboard:

### Production Settings

```
APP_NAME=Kanvas Chatbot API
APP_VERSION=1.0.0
DEBUG=False
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=INFO
ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

### Optional (jika ada)

```
DATABASE_URL=your_database_url
API_KEY=your_api_key
```

**Cara Set:**
1. Vercel Dashboard → Project → Settings
2. Environment Variables
3. Add variable untuk Production, Preview, Development

## 📦 Build & Deploy Process

Vercel akan otomatis:

1. **Detect Python**: Auto-detect dari `requirements.txt`
2. **Install Dependencies**: Install semua packages
3. **Build**: Build `api/index.py`
4. **Deploy**: Deploy sebagai serverless functions

**Build Logs:**
```
Installing dependencies...
Collecting fastapi==0.115.0
...
Building api/index.py
Deploying...
```

## 🔍 Troubleshooting

### Error: Module not found

**Problem**: Import error saat deploy

**Solution**:
1. Pastikan semua dependencies di `requirements.txt`
2. Check `api/index.py` import path benar
3. Pastikan struktur folder benar

### Error: Build timeout

**Problem**: Build terlalu lama (khususnya saat install torch/sentence-transformers)

**Solution**:
1. Gunakan Vercel Pro untuk build time lebih lama
2. Optimize dependencies (jika mungkin)
3. Consider using lighter models

### Error: Function timeout

**Problem**: Request timeout (default 10s untuk Hobby plan)

**Solution**:
1. Optimize model loading (cache embeddings)
2. Upgrade ke Pro plan (60s timeout)
3. Use edge functions untuk faster response

### Model Loading Slow

**Problem**: Model all-MiniLM-L6-v2 loading lambat di cold start

**Solution**:
1. **Cache model**: Model akan di-cache setelah first load
2. **Warm up**: Use cron job untuk keep function warm
3. **Optimize**: Pre-compute FAQ embeddings

## 📊 Performance Tips

### 1. Optimize Cold Start

```python
# api/index.py
from main import app
import os

# Pre-load model saat cold start
if os.environ.get("VERCEL"):
    # Pre-load embedding service
    from app.services.embedding_service import embedding_service
    # Warm up dengan dummy query
    embedding_service.encode_single("test")

__all__ = ["app"]
```

### 2. Cache Embeddings

Pre-compute FAQ embeddings dan simpan:

```python
# Pre-compute saat build atau first request
faq_embeddings = embedding_service.encode(all_questions)
# Save to cache
```

### 3. Use Edge Functions (Future)

Untuk response lebih cepat, consider edge functions untuk simple endpoints.

## 🌐 Post-Deploy

### 1. Test API

Setelah deploy, test endpoint:

```bash
# Health check
curl https://your-project.vercel.app/health

# Chat endpoint
curl -X POST https://your-project.vercel.app/chat/ \
  -H "Content-Type: application/json" \
  -d '{"message": "Apa itu Kanvas Store?"}'
```

### 2. Check Logs

Vercel Dashboard → Project → Logs

### 3. Monitor Performance

Vercel Dashboard → Analytics

## 🔒 Security

### 1. CORS Settings

Update `ALLOWED_ORIGINS` di environment variables:

```
ALLOWED_ORIGINS=https://kanvas.co.id,https://www.kanvas.co.id
```

### 2. API Keys (jika perlu)

Tambahkan authentication untuk production:

```python
# app/core/config.py
API_KEY: Optional[str] = None

# app/api/routes/chat.py
from fastapi import Header, HTTPException

@router.post("/chat/")
async def send_message(
    request: ChatRequest,
    x_api_key: str = Header(None)
):
    if settings.API_KEY and x_api_key != settings.API_KEY:
        raise HTTPException(401, "Invalid API key")
    # ... rest of code
```

## 📝 Checklist Deploy

- [ ] `vercel.json` sudah benar
- [ ] `api/index.py` sudah dibuat
- [ ] `requirements.txt` lengkap
- [ ] Environment variables sudah di-set
- [ ] Test local dengan `vercel dev`
- [ ] Deploy ke Vercel
- [ ] Test production endpoints
- [ ] Check logs untuk errors
- [ ] Update CORS settings
- [ ] Monitor performance

## 🧪 Test Local dengan Vercel

Sebelum deploy, test local:

```bash
# Install Vercel CLI
npm i -g vercel

# Run local
vercel dev
```

Server akan running di `http://localhost:3000`

## 📚 Resources

- **Vercel Docs**: https://vercel.com/docs
- **FastAPI on Vercel**: https://vercel.com/docs/frameworks/backend/fastapi
- **Python Runtime**: https://vercel.com/docs/functions/serverless-functions/runtimes/python
- **Environment Variables**: https://vercel.com/docs/environment-variables

## ⚠️ Important Notes

1. **Model Size**: Model all-MiniLM-L6-v2 (~80MB) akan di-download saat cold start
2. **Cold Start**: First request mungkin lambat (~5-10s)
3. **Timeout**: Hobby plan = 10s, Pro = 60s
4. **Memory**: Hobby plan = 1GB, Pro = 3GB
5. **Storage**: Model cached di `/tmp` (ephemeral)

## 🔮 Alternative: Optimize for Production

Untuk production yang lebih optimal:

1. **Use lighter model** atau pre-compute embeddings
2. **Cache model** di external storage (S3, etc)
3. **Use edge functions** untuk simple queries
4. **Database** untuk FAQ (bukan hardcoded)
5. **CDN** untuk static assets

---

**Happy Deploying! 🚀**

Jika ada masalah, check Vercel logs atau dokumentasi resmi.

