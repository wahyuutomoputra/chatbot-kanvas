# 🔧 Optimasi untuk Vercel - Mengatasi "data is too long"

Panduan mengatasi error "data is too long" saat deploy ke Vercel.

## 🚨 Masalah

Error: **"data is too long"**

**Penyebab:**
- Torch library terlalu besar (~385MB)
- Model sentence-transformers (~80MB)
- Total dependencies melebihi limit Vercel (250MB uncompressed)

## ✅ Solusi yang Sudah Diterapkan

### 1. CPU-Only Torch

Menggunakan `torch==2.5.1+cpu` yang lebih kecil (~150MB vs 385MB):

```txt
--extra-index-url https://download.pytorch.org/whl/cpu
torch==2.5.1+cpu
```

**Penghematan**: ~235MB

### 2. Lazy Loading Model

Model hanya di-load saat pertama kali digunakan, bukan saat import:

```python
@property
def model(self) -> SentenceTransformer:
    if self._model is None:
        self._model = SentenceTransformer(self.model_name)
    return self._model
```

**Keuntungan**:
- Faster cold start
- Model di-cache di `/tmp`
- Tidak load jika tidak digunakan

### 3. Cache Directory untuk Vercel

Set cache ke `/tmp` (writable di Vercel):

```python
cache_dir = os.environ.get("TRANSFORMERS_CACHE", "/tmp/.cache")
```

### 4. Vercel Configuration

Updated `vercel.json` dengan:
- Memory: 3008MB (Pro plan)
- Max duration: 60s
- Cache directory setting

### 5. .vercelignore

Exclude files yang tidak perlu dari build.

## 📊 Perbandingan Ukuran

| Item | Sebelum | Sesudah | Penghematan |
|------|---------|---------|-------------|
| Torch | ~385MB | ~150MB | ~235MB |
| Model (first load) | ~80MB | ~80MB* | - |
| **Total** | **~465MB** | **~230MB** | **~235MB** |

*Model di-download ke `/tmp` saat first request

## 🚀 Deploy Steps

### 1. Update Requirements

Pastikan `requirements.txt` sudah update:

```bash
# Check requirements
cat requirements.txt
```

### 2. Test Local (Optional)

```bash
# Install CPU-only torch
pip install torch==2.5.1+cpu --extra-index-url https://download.pytorch.org/whl/cpu

# Test
python -c "from app.services.embedding_service import embedding_service; print('OK')"
```

### 3. Deploy ke Vercel

```bash
# Via CLI
vercel --prod

# Atau via Dashboard
# Push to Git → Auto deploy
```

### 4. Monitor Build

Check build logs di Vercel Dashboard:
- Ukuran function harus < 250MB
- Build time mungkin lebih lama (first time)

## 🔍 Troubleshooting

### Masih Error "data is too long"

**Solusi 1: Exclude More Files**

Update `.vercelignore`:

```
# Tambahkan
*.md
docs/
examples/
```

**Solusi 2: Split Functions**

Pisahkan endpoints yang tidak butuh model:

```python
# api/index.py - Main handler
from main import app

# api/chat.py - Chat handler (with model)
from app.services.embedding_service import embedding_service
# ... chat logic
```

**Solusi 3: Use External Model Service**

Jika masih terlalu besar, consider:
- Deploy model di service terpisah (Hugging Face Inference API)
- Use API call instead of local model
- Use lighter model

### Model Loading Slow

**Problem**: Cold start lambat karena download model

**Solution**:
1. Model akan di-cache di `/tmp` setelah first load
2. Use Vercel Pro untuk keep functions warm
3. Pre-warm dengan cron job

### Memory Limit

**Problem**: Out of memory error

**Solution**:
1. Upgrade ke Vercel Pro (3GB memory)
2. Optimize model usage
3. Clear cache jika perlu

## 📝 Alternative Solutions

### Option 1: Hugging Face Inference API

Gunakan API instead of local model:

```python
import requests

def encode_with_api(texts):
    response = requests.post(
        "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2",
        json={"inputs": texts}
    )
    return response.json()
```

**Pros**: No model size issue
**Cons**: API cost, latency

### Option 2: Lighter Model

Gunakan model yang lebih kecil:

```python
# Model lebih kecil (~20MB)
model_name = "sentence-transformers/paraphrase-MiniLM-L3-v2"
```

### Option 3: Pre-compute Embeddings

Pre-compute FAQ embeddings dan simpan di database:

```python
# Pre-compute saat build
faq_embeddings = compute_embeddings(all_faqs)
# Save to database/JSON
```

**Pros**: No model needed at runtime
**Cons**: Less flexible

## 🎯 Recommended Approach

Untuk production, recommended:

1. **Use CPU-only torch** ✅ (sudah diterapkan)
2. **Lazy loading** ✅ (sudah diterapkan)
3. **Cache model** ✅ (sudah diterapkan)
4. **Monitor size** - Check build logs
5. **Optimize further** - Jika masih perlu

## 📊 Expected Results

Setelah optimasi:

- ✅ Build size: < 250MB
- ✅ Cold start: ~5-10s (first request)
- ✅ Warm start: ~100-200ms
- ✅ Memory usage: ~500-800MB
- ✅ Function timeout: 60s (Pro plan)

## 🔗 Resources

- **Vercel Limits**: https://vercel.com/docs/functions/serverless-functions/runtimes/python
- **Torch CPU**: https://pytorch.org/get-started/locally/
- **Sentence Transformers**: https://www.sbert.net/

## ⚠️ Important Notes

1. **First Deploy**: Akan lebih lama karena download dependencies
2. **Cold Start**: Model download saat first request (~5-10s)
3. **Cache**: Model cached di `/tmp` (ephemeral, reset per deploy)
4. **Memory**: Pro plan recommended untuk model loading
5. **Timeout**: Set maxDuration ke 60s untuk model loading

---

**Setelah optimasi ini, deploy seharusnya berhasil! 🚀**

Jika masih ada masalah, check build logs atau consider alternative solutions di atas.

