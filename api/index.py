"""
Vercel Serverless Handler untuk FastAPI
File ini digunakan oleh Vercel untuk menjalankan aplikasi FastAPI
"""

from main import app

# Export app untuk Vercel
# Vercel akan otomatis detect app instance ini
__all__ = ["app"]

