#!/bin/bash

# Script untuk menjalankan aplikasi dalam mode development (auto-reload)

echo "🔧 Starting Kanvas Chatbot API in Development Mode..."

# Cek apakah virtual environment sudah ada
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment tidak ditemukan!"
    echo "ℹ️  Jalankan ./setup.sh terlebih dahulu"
    exit 1
fi

# Aktifkan virtual environment
source venv/bin/activate

# Jalankan aplikasi dengan auto-reload
echo "✅ Starting development server di http://localhost:8000"
echo "🔄 Auto-reload aktif - perubahan code akan otomatis reload server"
echo "📚 Dokumentasi API: http://localhost:8000/docs"
echo "💡 Tekan Ctrl+C untuk stop server"
echo ""

uvicorn main:app --reload --host 0.0.0.0 --port 8000

