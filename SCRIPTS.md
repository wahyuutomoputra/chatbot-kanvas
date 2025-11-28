# 🚀 Shell Scripts Documentation

Dokumentasi lengkap untuk shell scripts yang tersedia dalam project ini.

## 📋 Daftar Scripts

| Script | Fungsi | Kapan Digunakan |
|--------|--------|-----------------|
| `setup.sh` | Setup awal project | Pertama kali clone/download project |
| `start.sh` | Jalankan aplikasi (production mode) | Menjalankan server normal |
| `dev.sh` | Jalankan aplikasi (development mode) | Development dengan auto-reload |
| `test.sh` | Testing aplikasi | Cek apakah aplikasi berjalan dengan baik |

## 🔧 setup.sh

### Fungsi
- Check Python version
- Membuat virtual environment (jika belum ada)
- Upgrade pip
- Install semua dependencies dari `requirements.txt`

### Kapan Digunakan
- Pertama kali setup project
- Setelah update `requirements.txt`
- Setelah clone project baru

### Cara Menggunakan
```bash
./setup.sh
```

### Output
```
🔧 Setup Kanvas Chatbot API...

📌 Checking Python version...
Python 3.13.0

📦 Membuat virtual environment...
✅ Virtual environment berhasil dibuat

🔄 Mengaktifkan virtual environment...
⬆️  Upgrading pip...
📥 Installing dependencies...

✅ Setup selesai!

📝 Langkah selanjutnya:
   1. (Opsional) Buat file .env untuk konfigurasi
   2. Jalankan: ./start.sh
```

## 🚀 start.sh

### Fungsi
- Validasi virtual environment ada
- Validasi dependencies terinstall
- Aktifkan virtual environment
- Jalankan aplikasi via `main.py`

### Kapan Digunakan
- Menjalankan aplikasi dalam production mode
- Testing aplikasi sebelum deployment
- Demonstrasi aplikasi

### Cara Menggunakan
```bash
./start.sh
```

### Output
```
🚀 Starting Kanvas Chatbot API...
✅ Starting server di http://localhost:8000
📚 Dokumentasi API: http://localhost:8000/docs
💡 Tekan Ctrl+C untuk stop server

INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Stop Server
Tekan `Ctrl+C` untuk menghentikan server.

## 🔧 dev.sh

### Fungsi
- Validasi virtual environment ada
- Aktifkan virtual environment
- Jalankan aplikasi dengan `uvicorn` dan **auto-reload**
- Cocok untuk development

### Kapan Digunakan
- Development aktif
- Testing perubahan code real-time
- Debugging

### Cara Menggunakan
```bash
./dev.sh
```

### Fitur Auto-Reload
Server akan otomatis restart ketika:
- Ada perubahan file `.py`
- Save file di editor

### Output
```
🔧 Starting Kanvas Chatbot API in Development Mode...
✅ Starting development server di http://localhost:8000
🔄 Auto-reload aktif - perubahan code akan otomatis reload server
📚 Dokumentasi API: http://localhost:8000/docs
💡 Tekan Ctrl+C untuk stop server

INFO:     Will watch for changes in these directories: ['/path/to/project']
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Stop Server
Tekan `Ctrl+C` untuk menghentikan server.

## 🧪 test.sh

### Fungsi
- Test import aplikasi
- Test health check endpoint (jika server berjalan)
- Validasi basic functionality

### Kapan Digunakan
- Sebelum commit code
- Setelah perubahan besar
- Validasi setup berhasil

### Cara Menggunakan
```bash
./test.sh
```

### Output (Server Tidak Berjalan)
```
🧪 Testing Kanvas Chatbot API...
📦 Testing imports...
✓ Import berhasil!
✅ Import test passed

🔍 Testing health endpoint...
⚠️  Server tidak berjalan (jalankan ./start.sh di terminal lain)

✅ Basic tests completed!
```

### Output (Server Berjalan)
```
🧪 Testing Kanvas Chatbot API...
📦 Testing imports...
✓ Import berhasil!
✅ Import test passed

🔍 Testing health endpoint...
✅ Health check passed
Response: {"status":"healthy","version":"1.0.0","timestamp":"..."}

✅ Basic tests completed!
```

## 🔄 Workflow Development

### Pertama Kali Setup
```bash
# 1. Clone/download project
git clone <repo-url>
cd kanvas-chatbot

# 2. Setup project
./setup.sh

# 3. Jalankan development server
./dev.sh
```

### Daily Development
```bash
# 1. Jalankan development server
./dev.sh

# 2. Edit code di editor favorit
# 3. Save file → server auto-reload
# 4. Test di browser/API client

# 5. Sebelum commit
./test.sh
```

### Setelah Update Dependencies
```bash
# 1. Update requirements.txt
# 2. Jalankan setup lagi
./setup.sh

# 3. Test
./test.sh
```

## ❓ Troubleshooting

### Permission Denied
```bash
chmod +x *.sh
```

### Virtual Environment Tidak Ditemukan
```bash
./setup.sh
```

### Dependencies Belum Terinstall
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Port 8000 Sudah Digunakan
Edit `.env` atau ubah di `app/core/config.py`:
```bash
PORT=8001
```

## 💡 Tips

1. **Gunakan `dev.sh` untuk development** - Auto-reload sangat membantu
2. **Gunakan `start.sh` untuk demo/testing** - Lebih stable
3. **Jalankan `test.sh` sebelum commit** - Hindari broken code
4. **Setup.sh hanya perlu dijalankan sekali** - Kecuali ada update dependencies

## 🔗 Links

- **Dokumentasi API**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

