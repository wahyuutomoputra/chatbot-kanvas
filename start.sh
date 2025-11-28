#!/bin/bash

# Script untuk menjalankan Kanvas Chatbot API

echo "🚀 Starting Kanvas Chatbot API..."

# Cek apakah virtual environment sudah ada
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment tidak ditemukan!"
    echo "ℹ️  Jalankan ./setup.sh terlebih dahulu"
    exit 1
fi

# Aktifkan virtual environment
source venv/bin/activate

# Cek apakah dependencies sudah terinstall
if ! python -c "import fastapi" 2>/dev/null; then
    echo "❌ Dependencies belum terinstall!"
    echo "ℹ️  Jalankan ./setup.sh terlebih dahulu"
    exit 1
fi

# Jalankan aplikasi
echo "✅ Starting server di http://localhost:8000"
echo "📚 Dokumentasi API: http://localhost:8000/docs"
echo "💡 Tekan Ctrl+C untuk stop server"
echo ""

python main.py

