#!/bin/bash

# Script untuk testing aplikasi

echo "🧪 Testing Kanvas Chatbot API..."

# Cek apakah virtual environment sudah ada
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment tidak ditemukan!"
    echo "ℹ️  Jalankan ./setup.sh terlebih dahulu"
    exit 1
fi

# Aktifkan virtual environment
source venv/bin/activate

# Test import aplikasi
echo "📦 Testing imports..."
python -c "from main import app; print('✓ Import berhasil!')"

if [ $? -eq 0 ]; then
    echo "✅ Import test passed"
else
    echo "❌ Import test failed"
    exit 1
fi

# Test health endpoint (jika server sedang berjalan)
echo ""
echo "🔍 Testing health endpoint..."
response=$(curl -s http://localhost:8000/health 2>/dev/null)

if [ $? -eq 0 ]; then
    echo "✅ Health check passed"
    echo "Response: $response"
else
    echo "⚠️  Server tidak berjalan (jalankan ./start.sh di terminal lain)"
fi

echo ""
echo "✅ Basic tests completed!"

