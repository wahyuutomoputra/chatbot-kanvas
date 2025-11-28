#!/bin/bash

# Script untuk setup awal project

echo "🔧 Setup Kanvas Chatbot API..."
echo ""

# Cek versi Python
echo "📌 Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "❌ Python3 tidak ditemukan!"
    echo "ℹ️  Install Python3 terlebih dahulu"
    exit 1
fi

# Buat virtual environment jika belum ada
if [ ! -d "venv" ]; then
    echo "📦 Membuat virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment berhasil dibuat"
else
    echo "✅ Virtual environment sudah ada"
fi

# Aktifkan virtual environment
echo "🔄 Mengaktifkan virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip --quiet

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Setup selesai!"
    echo ""
    echo "📝 Langkah selanjutnya:"
    echo "   1. (Opsional) Buat file .env untuk konfigurasi"
    echo "   2. Jalankan: ./start.sh"
    echo ""
else
    echo ""
    echo "❌ Setup gagal!"
    echo "ℹ️  Periksa error di atas"
    exit 1
fi

