# Kanvas Chatbot API

API backend untuk chatbot Kanvas menggunakan FastAPI dengan arsitektur modular.

⚡ **[Quick Start Guide](QUICKSTART.md)** - Langsung mulai coding!  
📚 **[Knowledge Base](KNOWLEDGE_BASE.md)** - FAQ tentang Kanvas Store

## 🏗️ Arsitektur

Project ini menggunakan **Clean Architecture** dengan pemisahan yang jelas antara:
- **Routes (Controller)**: Menangani HTTP requests/responses
- **Services (Business Logic)**: Memproses logika bisnis
- **Schemas (Models)**: Validasi data dengan Pydantic
- **Core (Config)**: Konfigurasi aplikasi

## 🤖 AI-Powered Chat

Chatbot ini menggunakan **all-MiniLM-L6-v2** untuk semantic similarity:
- ✅ Semantic search untuk FAQ matching
- ✅ Confidence scoring untuk setiap jawaban
- ✅ Intelligent suggestions jika tidak ada exact match
- ✅ Fast inference (~50ms per query)

📖 **[Dokumentasi AI Model](AI_MODEL.md)** - Penjelasan lengkap tentang model AI

## 📁 Struktur Project

```
kanvas-chatbot/
├── app/                        # Main application package
│   ├── api/routes/            # Controllers (HTTP handlers)
│   │   ├── health.py          # Health check endpoints
│   │   └── chat.py            # Chat endpoints
│   ├── services/              # Business logic layer
│   │   └── chat_service.py    # Chat processing logic
│   ├── schemas/               # Data models (Pydantic)
│   │   └── chat.py            # Request/response models
│   └── core/                  # Configuration
│       └── config.py          # App settings
├── venv/                      # Virtual environment
├── main.py                    # Application entry point
├── requirements.txt           # Dependencies
├── *.sh                       # Shell scripts
└── *.md                       # Documentation files
```

📖 **Dokumentasi lengkap struktur**: Lihat [STRUCTURE.md](STRUCTURE.md)

## 🚀 Quick Start

### Setup Otomatis (Recommended)

```bash
# 1. Setup project (buat venv & install dependencies)
./setup.sh

# 2. Jalankan aplikasi
./start.sh
```

### Manual Setup

#### 1. Aktifkan Virtual Environment

```bash
# MacOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Konfigurasi Environment (Opsional)

Buat file `.env` untuk custom configuration:

```bash
APP_NAME="Kanvas Chatbot API"
DEBUG=True
HOST="0.0.0.0"
PORT=8000
LOG_LEVEL="INFO"
```

#### 4. Jalankan Server

```bash
# Menggunakan script (recommended)
./start.sh

# Atau mode development (auto-reload)
./dev.sh

# Atau manual
uvicorn main:app --reload

# Atau jalankan file main.py
python main.py
```

Server akan berjalan di `http://localhost:8000`

## 🛠️ Shell Scripts

Project ini dilengkapi dengan shell scripts untuk memudahkan development:

| Script | Fungsi | Usage |
|--------|--------|-------|
| `./setup.sh` | Setup awal project | Pertama kali / update deps |
| `./start.sh` | Jalankan aplikasi | Production mode |
| `./dev.sh` | Development mode | Auto-reload aktif |
| `./test.sh` | Testing aplikasi | Validasi setup |

📖 **Dokumentasi lengkap**: Lihat [SCRIPTS.md](SCRIPTS.md)

## 📚 API Endpoints

### 🏥 Health Check

**GET** `/` - Status API  
**GET** `/health` - Health check dengan timestamp

### 💬 Chat (AI-Powered dengan Semantic Similarity)

**POST** `/chat/` - Chat dengan AI menggunakan all-MiniLM-L6-v2

**Request:**
```bash
curl -X POST http://localhost:8000/chat/ \
  -H "Content-Type: application/json" \
  -d '{"message": "Bagaimana cara menggunakan aplikasi ini?"}'
```

**Response dengan Confidence Score:**
```json
{
  "response": "Anda bisa menggunakan Kanvas dengan mengirim pesan...",
  "status": "success",
  "matched_question": "Bagaimana cara menggunakan Kanvas?",
  "method": "semantic_similarity",
  "confidence": 0.89,
  "suggestions": null
}
```

**GET** `/chat/history/{user_id}` - Riwayat chat user

### 🔍 Semantic Similarity

**POST** `/similarity/search` - Similarity search  
**GET** `/similarity/faqs` - Get all FAQs  
**GET** `/similarity/faqs/search?query={query}` - Search FAQs  
**GET** `/similarity/model-info` - Info model AI

**Example:**
```bash
curl -X POST http://localhost:8000/similarity/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "cara login",
    "candidates": ["login page", "forgot password"],
    "top_k": 2
  }'
```

📖 **[API Documentation](AI_MODEL.md)** - Dokumentasi lengkap endpoints & AI model

## 📖 Dokumentasi API Interaktif

Setelah server berjalan, akses dokumentasi interaktif di:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

📘 **[Panduan Swagger UI](SWAGGER_GUIDE.md)** - Tutorial lengkap cara test API via Swagger

## 🧩 Penjelasan Arsitektur

### 1. Routes (Controller Layer)
File: `app/api/routes/chat.py`

Bertanggung jawab untuk:
- Menerima HTTP requests
- Validasi input via Pydantic schemas
- Memanggil service layer
- Mengembalikan HTTP responses

### 2. Services (Business Logic Layer)
File: `app/services/chat_service.py`

Bertanggung jawab untuk:
- Logika bisnis aplikasi
- Pemrosesan data
- Integrasi dengan external services (database, AI/ML models, dll)

### 3. Schemas (Data Models)
File: `app/schemas/chat.py`

Bertanggung jawab untuk:
- Definisi struktur data
- Validasi input/output
- Dokumentasi API otomatis

### 4. Core (Configuration)
File: `app/core/config.py`

Bertanggung jawab untuk:
- Konfigurasi aplikasi
- Environment variables
- Settings management

## 🔧 Development

### Menambah Endpoint Baru

1. **Buat Schema** di `app/schemas/`
2. **Buat Service** di `app/services/`
3. **Buat Route** di `app/api/routes/`
4. **Register Router** di `main.py`

### Contoh: Menambah Fitur User Management

```python
# 1. Schema (app/schemas/user.py)
class UserCreate(BaseModel):
    username: str
    email: str

# 2. Service (app/services/user_service.py)
class UserService:
    async def create_user(self, user: UserCreate):
        # Business logic here
        pass

# 3. Route (app/api/routes/user.py)
@router.post("/users/")
async def create_user(user: UserCreate):
    return await user_service.create_user(user)

# 4. Register (main.py)
from app.api.routes import user
app.include_router(user.router)
```

## 🧪 Testing

```bash
# Install testing dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest
```

## 📦 Dependencies

### Core Framework
- **FastAPI 0.115.0** - Web framework modern & cepat
- **Uvicorn 0.34.0** - ASGI server
- **Pydantic 2.10.0** - Data validation
- **Pydantic-Settings 2.6.1** - Configuration management
- **Python-dotenv 1.0.1** - Environment variables

### AI/ML
- **sentence-transformers 3.3.1** - Semantic similarity model
- **torch 2.9.1** - PyTorch for deep learning
- **numpy 2.2.0** - Numerical computing

## 🎯 Next Steps

- [ ] Implementasi AI/ML model untuk chatbot
- [ ] Integrasi dengan database (PostgreSQL/MongoDB)
- [ ] Autentikasi & authorization (JWT)
- [ ] Rate limiting
- [ ] Caching (Redis)
- [ ] WebSocket untuk real-time chat
- [ ] Unit & integration tests
- [ ] Docker containerization
- [ ] CI/CD pipeline

## 📝 License

MIT License

