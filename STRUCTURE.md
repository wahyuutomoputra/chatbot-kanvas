# 📁 Struktur Project

Dokumentasi lengkap struktur folder dan file dalam project Kanvas Chatbot API.

## 🌳 File Tree

```
kanvas-chatbot/
│
├── 📄 Shell Scripts (Automation)
│   ├── setup.sh              # Setup awal project
│   ├── start.sh              # Jalankan aplikasi
│   ├── dev.sh                # Development mode (auto-reload)
│   └── test.sh               # Testing aplikasi
│
├── 📄 Configuration Files
│   ├── requirements.txt      # Python dependencies
│   ├── .env                  # Environment variables (user-created)
│   ├── .gitignore           # Git ignore rules
│   └── main.py              # Application entry point
│
├── 📄 Documentation
│   ├── README.md            # Main documentation
│   ├── SCRIPTS.md           # Shell scripts guide
│   └── STRUCTURE.md         # This file
│
├── 📁 app/                  # Main application package
│   ├── __init__.py
│   │
│   ├── 📁 api/              # API Layer
│   │   ├── __init__.py
│   │   └── routes/          # HTTP Routes (Controllers)
│   │       ├── __init__.py
│   │       ├── health.py    # Health check endpoints
│   │       └── chat.py      # Chat endpoints
│   │
│   ├── 📁 services/         # Business Logic Layer
│   │   ├── __init__.py
│   │   └── chat_service.py  # Chat business logic
│   │
│   ├── 📁 schemas/          # Data Models (Pydantic)
│   │   ├── __init__.py
│   │   └── chat.py          # Chat request/response models
│   │
│   └── 📁 core/             # Core Configuration
│       ├── __init__.py
│       └── config.py        # App settings & config
│
└── 📁 venv/                 # Virtual environment (auto-generated)
    └── ...
```

## 📂 Penjelasan Folder

### `/` (Root Directory)

File-file utama project:

| File | Deskripsi |
|------|-----------|
| `main.py` | Entry point aplikasi, setup FastAPI |
| `requirements.txt` | Daftar dependencies Python |
| `.gitignore` | File yang diabaikan Git |
| `README.md` | Dokumentasi utama |
| `SCRIPTS.md` | Dokumentasi shell scripts |
| `STRUCTURE.md` | Dokumentasi struktur (file ini) |

### Shell Scripts

| File | Fungsi |
|------|--------|
| `setup.sh` | Setup awal: buat venv, install deps |
| `start.sh` | Jalankan aplikasi production mode |
| `dev.sh` | Jalankan dengan auto-reload |
| `test.sh` | Testing aplikasi |

### `app/` - Main Application

Package utama aplikasi dengan struktur modular.

#### `app/api/routes/` - Controllers

**Tanggung Jawab:**
- Handle HTTP requests/responses
- Routing endpoints
- Validasi input via schemas
- Call services untuk business logic

**Files:**

| File | Endpoints | Deskripsi |
|------|-----------|-----------|
| `health.py` | `GET /`, `GET /health` | Health check & status |
| `chat.py` | `POST /chat/`, `GET /chat/history/{user_id}` | Chat functionality |

**Contoh Flow:**
```
HTTP Request → Route (Controller) → Service → Route → HTTP Response
```

#### `app/services/` - Business Logic

**Tanggung Jawab:**
- Logika bisnis aplikasi
- Data processing
- Integrasi external services
- Database operations (future)
- AI/ML integration (future)

**Files:**

| File | Class | Deskripsi |
|------|-------|-----------|
| `chat_service.py` | `ChatService` | Handle chat logic, processing messages |

**Contoh Methods:**
- `process_message()` - Proses pesan dari user
- `get_chat_history()` - Ambil riwayat chat
- `save_chat()` - Simpan chat ke database

#### `app/schemas/` - Data Models

**Tanggung Jawab:**
- Definisi struktur data (Pydantic models)
- Validasi input/output
- Type hints
- Auto-generate OpenAPI docs

**Files:**

| File | Models | Deskripsi |
|------|--------|-----------|
| `chat.py` | `ChatRequest`, `ChatResponse`, `HealthResponse` | Chat-related models |

**Contoh Model:**
```python
class ChatRequest(BaseModel):
    message: str
    user_id: Optional[str]
    session_id: Optional[str]
```

#### `app/core/` - Configuration

**Tanggung Jawab:**
- App configuration
- Environment variables
- Settings management
- Constants

**Files:**

| File | Class | Deskripsi |
|------|-------|-----------|
| `config.py` | `Settings` | App settings via Pydantic Settings |

## 🔄 Request Flow

```
┌─────────────┐
│ HTTP Client │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────┐
│         main.py (FastAPI)           │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│    app/api/routes/ (Controller)     │
│  - Receive request                  │
│  - Validate with schemas            │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│    app/services/ (Business Logic)   │
│  - Process data                     │
│  - Business rules                   │
│  - External integrations            │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│    app/api/routes/ (Controller)     │
│  - Format response                  │
│  - Return to client                 │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────┐
│ HTTP Client │
└─────────────┘
```

## 📋 Naming Conventions

### Files
- **Routes**: `{resource}.py` (e.g., `chat.py`, `user.py`)
- **Services**: `{resource}_service.py` (e.g., `chat_service.py`)
- **Schemas**: `{resource}.py` (e.g., `chat.py`)

### Classes
- **Schemas**: `{Resource}{Type}` (e.g., `ChatRequest`, `UserResponse`)
- **Services**: `{Resource}Service` (e.g., `ChatService`, `UserService`)

### Functions
- **Routes**: `{verb}_{resource}()` (e.g., `get_chat_history()`, `create_user()`)
- **Services**: `{action}_{resource}()` (e.g., `process_message()`, `validate_user()`)

## 🎯 Best Practices

### 1. Separation of Concerns
- **Routes**: Hanya HTTP logic
- **Services**: Semua business logic
- **Schemas**: Data validation saja

### 2. Single Responsibility
Setiap file/class punya satu tanggung jawab utama.

### 3. Dependency Injection
Services sebagai singleton untuk reusability.

### 4. Type Hints
Gunakan type hints untuk semua functions.

### 5. Documentation
Setiap function punya docstring yang jelas.

## 🔧 Menambah Fitur Baru

### Contoh: Menambah User Management

1. **Buat Schema** (`app/schemas/user.py`):
```python
class UserCreate(BaseModel):
    username: str
    email: str
```

2. **Buat Service** (`app/services/user_service.py`):
```python
class UserService:
    async def create_user(self, user: UserCreate):
        # Business logic here
        pass
```

3. **Buat Route** (`app/api/routes/user.py`):
```python
@router.post("/users/")
async def create_user(user: UserCreate):
    return await user_service.create_user(user)
```

4. **Register Router** (di `main.py`):
```python
from app.api.routes import user
app.include_router(user.router)
```

## 📊 File Statistics

```
Total Files: ~20 (excluding venv)
Lines of Code: ~500 (excluding comments)

Breakdown:
- Routes: 2 files
- Services: 1 file
- Schemas: 1 file
- Core: 1 file
- Config: 1 file
- Scripts: 4 files
- Docs: 3 files
```

## 🔗 Related Documentation

- [README.md](README.md) - Main documentation
- [SCRIPTS.md](SCRIPTS.md) - Shell scripts guide
- API Docs: http://localhost:8000/docs

