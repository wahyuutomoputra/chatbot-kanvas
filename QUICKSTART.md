# ⚡ Quick Start Guide

Panduan cepat untuk mulai menggunakan Kanvas Chatbot API.

## 🚀 Instalasi Cepat (3 Langkah)

```bash
# 1. Setup project
./setup.sh

# 2. Jalankan aplikasi
./start.sh

# 3. Buka browser
# http://localhost:8000/docs
```

## 📋 Common Commands

### Development
```bash
# Mode development (auto-reload)
./dev.sh

# Mode production
./start.sh

# Testing
./test.sh
```

### Manual Commands
```bash
# Aktifkan virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Jalankan server
python main.py
# atau
uvicorn main:app --reload

# Deaktivasi venv
deactivate
```

## 🌐 URL Penting

| URL | Deskripsi |
|-----|-----------|
| http://localhost:8000 | Homepage API |
| http://localhost:8000/docs | Swagger UI (Interactive API Docs) |
| http://localhost:8000/redoc | ReDoc (Alternative API Docs) |
| http://localhost:8000/health | Health Check |

## 🧪 Test API

### Via Browser (Swagger UI) - RECOMMENDED

Buka: **http://localhost:8000/docs**

📘 **[Panduan Lengkap Swagger UI](SWAGGER_GUIDE.md)** - Tutorial step-by-step cara test API  
🧪 **[Test Examples](TEST_EXAMPLES.md)** - 20+ test cases siap pakai

**Quick Test:**
1. Buka http://localhost:8000/docs
2. Klik `POST /chat/`
3. Klik **"Try it out"**
4. Test dengan pertanyaan tentang Kanvas Store:
   ```json
   {
     "message": "Apa itu Kanvas Store?"
   }
   ```
5. Klik **"Execute"**
6. Lihat response dengan confidence score!

### Via cURL

**Health Check:**
```bash
curl http://localhost:8000/health
```

**Chat dengan AI (Semantic Similarity):**
```bash
curl -X POST http://localhost:8000/chat/ \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Bagaimana cara menggunakan aplikasi ini?"
  }'
```

**Similarity Search:**
```bash
curl -X POST http://localhost:8000/similarity/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "cara login",
    "candidates": ["login page", "forgot password", "register"],
    "top_k": 2
  }'
```

**Search FAQs:**
```bash
curl "http://localhost:8000/similarity/faqs/search?query=cara%20pakai&top_k=3"
```

**Get All FAQs:**
```bash
curl http://localhost:8000/similarity/faqs
```

### Via Python
```python
import requests

# Health check
response = requests.get("http://localhost:8000/health")
print(response.json())

# Send message
response = requests.post(
    "http://localhost:8000/chat/",
    json={
        "message": "Halo, apa kabar?",
        "user_id": "user123"
    }
)
print(response.json())
```

### Via JavaScript
```javascript
// Health check
fetch('http://localhost:8000/health')
  .then(res => res.json())
  .then(data => console.log(data));

// Send message
fetch('http://localhost:8000/chat/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    message: 'Halo, apa kabar?',
    user_id: 'user123'
  })
})
  .then(res => res.json())
  .then(data => console.log(data));
```

## 🔧 Konfigurasi

### Environment Variables (Optional)

Buat file `.env`:
```bash
APP_NAME="My Custom Chatbot"
DEBUG=True
HOST="0.0.0.0"
PORT=8080
LOG_LEVEL="DEBUG"
```

### Default Settings
Jika tidak ada `.env`, akan menggunakan default:
- Port: 8000
- Host: 0.0.0.0
- Debug: True
- Log Level: INFO

## 📝 File Struktur Singkat

```
kanvas-chatbot/
├── *.sh                 # Shell scripts
├── app/                 # Source code
│   ├── api/routes/     # Controllers
│   ├── services/       # Business logic
│   ├── schemas/        # Data models
│   └── core/           # Config
└── main.py             # Entry point
```

## 🎯 Workflow Harian

### Pertama Kali
```bash
git clone <repo-url>
cd kanvas-chatbot
./setup.sh
./dev.sh
```

### Development
```bash
# Start server
./dev.sh

# Edit code...
# Save → Auto reload!

# Test
./test.sh
```

## ❓ Troubleshooting

### Port sudah digunakan
```bash
# Cek process yang menggunakan port 8000
lsof -ti:8000

# Kill process
kill -9 $(lsof -ti:8000)
```

### Dependencies error
```bash
./setup.sh
```

### Permission denied
```bash
chmod +x *.sh
```

### Python version error
```bash
# Cek Python version
python3 --version

# Minimal: Python 3.8+
# Recommended: Python 3.11+
```

## 📚 Dokumentasi Lengkap

- **README.md** - Overview & dokumentasi utama
- **SCRIPTS.md** - Dokumentasi shell scripts
- **STRUCTURE.md** - Struktur project & arsitektur
- **QUICKSTART.md** - Quick reference (file ini)

## 💡 Tips

1. **Gunakan `./dev.sh` saat development** - Auto-reload sangat membantu!
2. **Check `/docs` endpoint** - Dokumentasi interaktif lengkap
3. **Lihat logs** - Semua request/error tercatat di terminal
4. **Test via Swagger UI** - Paling mudah untuk testing manual

## 🎉 Next Steps

Setelah berhasil menjalankan aplikasi, coba:

1. ✅ Test semua endpoints di `/docs`
2. ✅ Baca `STRUCTURE.md` untuk memahami arsitektur
3. ✅ Modify `chat_service.py` untuk custom logic
4. ✅ Tambah endpoint baru (lihat `STRUCTURE.md`)
5. ✅ Integrasikan dengan frontend/mobile app

---

**Happy Coding! 🚀**

