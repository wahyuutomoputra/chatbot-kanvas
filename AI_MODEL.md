# 🤖 AI Model Documentation

Dokumentasi lengkap tentang model AI yang digunakan dalam Kanvas Chatbot API.

## 📊 Model Overview

### all-MiniLM-L6-v2

**Jenis**: Sentence Transformer (Embedding Model)  
**Publisher**: Microsoft / Sentence Transformers  
**Task**: Semantic Similarity & Sentence Embeddings  
**Dimensi Embedding**: 384  
**Max Sequence Length**: 256 tokens

#### Karakteristik Model

- ✅ **Cepat**: Inference time ~10-20ms per sentence
- ✅ **Ringan**: Model size ~80MB, cocok untuk production
- ✅ **Akurat**: Performance bagus untuk semantic similarity
- ✅ **Multi-bahasa**: Support Bahasa Indonesia dan Inggris
- ✅ **Open Source**: Gratis dan bisa digunakan komersial

## 🎯 Use Cases

### 1. FAQ Matching
Mencari jawaban paling relevan dari knowledge base berdasarkan pertanyaan user.

```python
# User bertanya: "Gimana cara pakai aplikasi ini?"
# System mencari FAQ yang paling mirip:
# - "Bagaimana cara menggunakan Kanvas?" (similarity: 0.89) ✓
# - "Apa itu Kanvas?" (similarity: 0.45)
```

### 2. Semantic Search
Mencari dokumen/teks yang paling relevan dengan query.

```python
# Query: "login bermasalah"
# Results:
# - "Bagaimana cara reset password?" (similarity: 0.76)
# - "Tidak bisa login ke akun saya" (similarity: 0.82) ✓
```

### 3. Question Similarity
Mendeteksi pertanyaan yang sama meskipun phrasing berbeda.

```python
# "Berapa harganya?" ≈ "Apakah gratis?"
# "Bagaimana cara daftar?" ≈ "Cara membuat akun baru"
```

## 🔧 Implementasi

### Architecture

```
User Question
    ↓
[Embedding Service]
    ↓
all-MiniLM-L6-v2 Model
    ↓
Vector Embedding (384 dimensions)
    ↓
Cosine Similarity dengan Knowledge Base
    ↓
Best Match Answer
```

### Services

#### 1. Embedding Service
**File**: `app/services/embedding_service.py`

**Fungsi Utama**:
- `encode()` - Convert text ke vector embeddings
- `cosine_similarity()` - Hitung similarity score (0-1)
- `find_most_similar()` - Cari teks paling mirip

#### 2. Knowledge Base
**File**: `app/services/knowledge_base.py`

**Fungsi**:
- Menyimpan FAQ (question + answer)
- Manage knowledge base
- Add/Get FAQ

#### 3. Chat Service
**File**: `app/services/chat_service.py`

**Logic**:
1. Terima pertanyaan user
2. Encode pertanyaan ke embedding
3. Compare dengan semua FAQ
4. Return jawaban dengan confidence score tertinggi

## 📡 API Endpoints

### 1. Chat Endpoint (Main)

**POST** `/chat/`

Endpoint utama untuk chat dengan semantic similarity.

**Request:**
```json
{
  "message": "Bagaimana cara menggunakan aplikasi ini?",
  "user_id": "user123"
}
```

**Response:**
```json
{
  "response": "Anda bisa menggunakan Kanvas dengan mengirim pesan melalui API endpoint /chat/...",
  "status": "success",
  "matched_question": "Bagaimana cara menggunakan Kanvas?",
  "method": "semantic_similarity",
  "confidence": 0.89,
  "suggestions": null
}
```

### 2. Similarity Search

**POST** `/similarity/search`

Mencari teks paling mirip dari candidates.

**Request:**
```json
{
  "query": "cara login",
  "candidates": [
    "Bagaimana cara login?",
    "Lupa password",
    "Registrasi akun baru"
  ],
  "top_k": 3
}
```

**Response:**
```json
{
  "results": [
    {
      "text": "Bagaimana cara login?",
      "similarity": 0.95,
      "index": 0
    },
    {
      "text": "Lupa password",
      "similarity": 0.67,
      "index": 1
    }
  ],
  "status": "success"
}
```

### 3. FAQ Search

**GET** `/similarity/faqs/search?query={query}&top_k={k}`

Mencari FAQ paling relevan.

**Example:**
```bash
GET /similarity/faqs/search?query=cara%20pakai&top_k=3
```

**Response:**
```json
{
  "results": [
    {
      "question": "Bagaimana cara menggunakan Kanvas?",
      "answer": "Anda bisa menggunakan Kanvas dengan...",
      "similarity": 0.92
    }
  ],
  "total": 1
}
```

### 4. Get All FAQs

**GET** `/similarity/faqs`

Mendapatkan semua FAQ.

**Response:**
```json
{
  "faqs": [
    {
      "question": "Apa itu Kanvas?",
      "answer": "Kanvas adalah platform..."
    }
  ],
  "total": 10
}
```

### 5. Model Info

**GET** `/similarity/model-info`

Informasi model yang digunakan.

**Response:**
```json
{
  "model_name": "sentence-transformers/all-MiniLM-L6-v2",
  "model_type": "sentence-transformers",
  "description": "all-MiniLM-L6-v2 adalah model untuk sentence embeddings",
  "embedding_dimension": 384,
  "max_sequence_length": 256
}
```

## 🎚️ Configuration

### Similarity Threshold

Default: `0.5` (50%)

Ubah di `app/services/chat_service.py`:

```python
self.similarity_threshold = 0.5  # Minimum similarity untuk match
```

**Rekomendasi**:
- `0.3-0.5`: Lebih permissive, banyak hasil
- `0.6-0.7`: Balanced
- `0.8-1.0`: Strict, hanya exact matches

### Model Loading

Model di-load saat aplikasi startup (singleton pattern).

**First Load**: ~3-5 detik (download model)  
**Subsequent Loads**: ~1-2 detik (dari cache)

Model disimpan di:
```
~/.cache/torch/sentence_transformers/
```

## 📈 Performance

### Inference Speed

| Operation | Time |
|-----------|------|
| Single encode | ~10-20ms |
| Batch encode (10 texts) | ~30-50ms |
| Similarity calculation | <1ms |
| Full FAQ search (10 FAQs) | ~50ms |

### Accuracy

Cosine similarity scores:

| Score | Interpretasi |
|-------|-------------|
| 0.9 - 1.0 | Sangat mirip / identical |
| 0.7 - 0.9 | Mirip / relevant |
| 0.5 - 0.7 | Agak mirip / possibly relevant |
| 0.3 - 0.5 | Kurang mirip |
| 0.0 - 0.3 | Tidak mirip |

## 🔄 Extending the System

### Menambah FAQ Baru

Edit `app/services/knowledge_base.py`:

```python
def _load_faqs(self):
    return [
        {
            "question": "Pertanyaan baru?",
            "answer": "Jawaban untuk pertanyaan baru"
        },
        # ... more FAQs
    ]
```

### Load dari Database

Ganti method `_load_faqs()` untuk load dari database:

```python
def _load_faqs(self):
    # Load from database
    faqs = database.query("SELECT * FROM faqs")
    return faqs
```

### Multiple Languages

Model sudah support multi-bahasa, tapi untuk hasil optimal:

1. Pisahkan FAQ per bahasa
2. Detect bahasa user input
3. Search di FAQ dengan bahasa yang sama

### Custom Model

Ganti model di `app/services/embedding_service.py`:

```python
# Contoh: model lebih besar untuk accuracy lebih tinggi
embedding_service = EmbeddingService(
    model_name="sentence-transformers/all-mpnet-base-v2"
)
```

## 🧪 Testing

### Test Similarity

```python
from app.services.embedding_service import embedding_service

# Test similarity
similarity = embedding_service.find_most_similar(
    query="cara login",
    candidates=[
        "Bagaimana cara login?",
        "Lupa password",
        "Apa itu Kanvas?"
    ],
    top_k=3
)

print(similarity)
# [(0, 'Bagaimana cara login?', 0.95), ...]
```

### Test via API

```bash
# Test chat
curl -X POST http://localhost:8000/chat/ \
  -H "Content-Type: application/json" \
  -d '{"message": "gimana cara pakai?"}'

# Test similarity
curl -X POST http://localhost:8000/similarity/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "cara login",
    "candidates": ["login page", "forgot password", "register"],
    "top_k": 2
  }'
```

## 📚 References

- [Sentence Transformers Documentation](https://www.sbert.net/)
- [all-MiniLM-L6-v2 Model Card](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [Cosine Similarity Explained](https://en.wikipedia.org/wiki/Cosine_similarity)

## 💡 Tips & Best Practices

1. **Cache Embeddings**: Pre-compute embeddings untuk FAQ agar lebih cepat
2. **Batch Processing**: Encode multiple texts sekaligus lebih efisien
3. **Threshold Tuning**: Adjust similarity threshold sesuai use case
4. **Quality FAQs**: Kualitas FAQ sangat mempengaruhi hasil
5. **Regular Updates**: Update knowledge base secara berkala

## 🔮 Future Improvements

- [ ] Cache pre-computed FAQ embeddings
- [ ] Add re-ranking model untuk accuracy lebih tinggi
- [ ] Support conversational context
- [ ] Multi-turn conversations
- [ ] Intent classification
- [ ] Named Entity Recognition (NER)
- [ ] Sentiment analysis

