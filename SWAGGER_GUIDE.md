# 📖 Panduan Menggunakan Swagger UI

Panduan lengkap untuk menggunakan Swagger UI (OpenAPI Documentation) untuk testing Kanvas Chatbot API.

## 🚀 Langkah 1: Jalankan Server

Pertama, pastikan server sudah berjalan:

```bash
# Jalankan development server
./dev.sh

# Atau
./start.sh

# Atau manual
source venv/bin/activate
python main.py
```

Tunggu sampai muncul:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

## 🌐 Langkah 2: Buka Swagger UI

Buka browser dan akses:

```
http://localhost:8000/docs
```

Atau alternatif dokumentasi (ReDoc):
```
http://localhost:8000/redoc
```

## 📋 Tampilan Swagger UI

Anda akan melihat dokumentasi API yang terbagi dalam beberapa section:

```
┌─────────────────────────────────────────┐
│  Kanvas Chatbot API - v1.0.0           │
│  API untuk chatbot Kanvas dengan        │
│  arsitektur modular                     │
├─────────────────────────────────────────┤
│  Servers                                │
│  • http://localhost:8000                │
├─────────────────────────────────────────┤
│  📁 Health                              │
│    GET  /                               │
│    GET  /health                         │
├─────────────────────────────────────────┤
│  📁 Chat                                │
│    POST /chat/                          │
│    GET  /chat/history/{user_id}         │
├─────────────────────────────────────────┤
│  📁 Semantic Similarity                 │
│    POST /similarity/search              │
│    GET  /similarity/faqs                │
│    GET  /similarity/faqs/search         │
│    GET  /similarity/model-info          │
└─────────────────────────────────────────┘
```

## 🧪 Langkah 3: Test Endpoint

### Test 1: Health Check (Paling Mudah)

1. **Klik** pada `GET /health`
2. Akan muncul detail endpoint
3. **Klik** tombol **"Try it out"** (pojok kanan)
4. **Klik** tombol **"Execute"** (biru)
5. Lihat response di bawah:

**Response yang diharapkan:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2024-11-28T13:30:00"
}
```

### Test 2: Chat dengan AI (Main Feature)

1. **Klik** pada `POST /chat/`
2. **Klik** tombol **"Try it out"**
3. Anda akan melihat **Request body** editor
4. Edit JSON request:

```json
{
  "message": "Bagaimana cara menggunakan Kanvas?",
  "user_id": "user123",
  "session_id": "session456"
}
```

5. **Klik** tombol **"Execute"**
6. Scroll ke bawah untuk melihat **Response**

**Response yang diharapkan:**
```json
{
  "response": "Anda bisa menggunakan Kanvas dengan mengirim pesan melalui API endpoint /chat/. Cukup kirim JSON dengan field 'message' berisi pertanyaan Anda.",
  "status": "success",
  "timestamp": "2024-11-28T13:30:00",
  "matched_question": "Bagaimana cara menggunakan Kanvas?",
  "method": "semantic_similarity",
  "confidence": 0.98,
  "suggestions": null
}
```

**Perhatikan:**
- ✅ `confidence: 0.98` - Sangat tinggi (exact match)
- ✅ `matched_question` - Pertanyaan yang cocok dari FAQ
- ✅ `method: semantic_similarity` - Menggunakan AI

### Test 3: Chat dengan Pertanyaan Berbeda

Coba pertanyaan yang berbeda kata-kata tapi makna sama:

```json
{
  "message": "gimana cara pakai aplikasi ini?"
}
```

**Response:**
```json
{
  "response": "Anda bisa menggunakan Kanvas dengan mengirim pesan...",
  "matched_question": "Bagaimana cara menggunakan Kanvas?",
  "confidence": 0.75,
  "suggestions": null
}
```

**Perhatikan:**
- Pertanyaan berbeda ("gimana cara pakai" vs "bagaimana cara menggunakan")
- Tapi tetap match dengan FAQ yang benar!
- Confidence lebih rendah (0.75) karena phrasing berbeda

### Test 4: Pertanyaan yang Tidak Ada di FAQ

```json
{
  "message": "apakah mendukung bahasa Jawa?"
}
```

**Response:**
```json
{
  "response": "Maaf, saya tidak menemukan jawaban yang tepat untuk pertanyaan Anda. Mungkin Anda bisa coba pertanyaan berikut?",
  "method": "no_match",
  "confidence": 0.35,
  "suggestions": [
    {
      "question": "Bahasa apa yang didukung?",
      "similarity": 0.35
    }
  ]
}
```

**Perhatikan:**
- Confidence rendah (< 0.5)
- Memberikan suggestions pertanyaan lain yang mungkin relevan

### Test 5: Similarity Search

1. **Klik** pada `POST /similarity/search`
2. **Klik** **"Try it out"**
3. Edit request:

```json
{
  "query": "cara login",
  "candidates": [
    "Bagaimana cara login?",
    "Lupa password",
    "Registrasi akun baru",
    "Apa itu Kanvas?"
  ],
  "top_k": 3
}
```

4. **Klik** **"Execute"**

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
      "similarity": 0.68,
      "index": 1
    },
    {
      "text": "Registrasi akun baru",
      "similarity": 0.42,
      "index": 2
    }
  ],
  "status": "success"
}
```

### Test 6: Search FAQs

1. **Klik** pada `GET /similarity/faqs/search`
2. **Klik** **"Try it out"**
3. Isi parameters:
   - **query**: `cara pakai`
   - **top_k**: `3`
4. **Klik** **"Execute"**

**Response:**
```json
{
  "results": [
    {
      "question": "Bagaimana cara menggunakan Kanvas?",
      "answer": "Anda bisa menggunakan Kanvas dengan...",
      "similarity": 0.85
    },
    {
      "question": "Bagaimana cara integrasi dengan aplikasi saya?",
      "answer": "Integrasi sangat mudah!...",
      "similarity": 0.72
    }
  ],
  "total": 2
}
```

### Test 7: Get All FAQs

1. **Klik** pada `GET /similarity/faqs`
2. **Klik** **"Try it out"**
3. **Klik** **"Execute"**

**Response:**
```json
{
  "faqs": [
    {
      "question": "Apa itu Kanvas?",
      "answer": "Kanvas adalah platform chatbot..."
    },
    {
      "question": "Bagaimana cara menggunakan Kanvas?",
      "answer": "Anda bisa menggunakan Kanvas dengan..."
    }
    // ... 8 more FAQs
  ],
  "total": 10
}
```

### Test 8: Model Info

1. **Klik** pada `GET /similarity/model-info`
2. **Klik** **"Try it out"**
3. **Klik** **"Execute"**

**Response:**
```json
{
  "model_name": "sentence-transformers/all-MiniLM-L6-v2",
  "model_type": "sentence-transformers",
  "description": "all-MiniLM-L6-v2 adalah model untuk sentence embeddings dan semantic similarity",
  "embedding_dimension": 384,
  "max_sequence_length": 256
}
```

## 📊 Memahami Response

### Response Code

Swagger menampilkan response code di bagian **Responses**:

```
✅ 200 - Success (OK)
✅ 201 - Created
⚠️  400 - Bad Request (Invalid input)
⚠️  404 - Not Found
❌ 500 - Internal Server Error
```

### Response Body

Setiap response ditampilkan dalam format JSON dengan syntax highlighting:

```json
{
  "response": "...",      // ← Jawaban dari chatbot
  "status": "success",    // ← Status response
  "confidence": 0.89,     // ← Confidence score (0-1)
  "matched_question": "..." // ← FAQ yang cocok
}
```

### Response Headers

Klik tab **"Headers"** untuk melihat HTTP headers:

```
content-type: application/json
content-length: 234
date: Thu, 28 Nov 2024 06:30:00 GMT
```

## 🎯 Tips Menggunakan Swagger

### 1. Eksplorasi Schema

Klik **"Schema"** di setiap endpoint untuk melihat:
- Required fields (tanda *)
- Field types (string, number, etc)
- Field descriptions
- Example values

### 2. Copy cURL Command

Setelah execute, scroll ke bawah ke bagian **"Curl"**:

```bash
curl -X 'POST' \
  'http://localhost:8000/chat/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "message": "Bagaimana cara menggunakan Kanvas?"
}'
```

Copy command ini untuk digunakan di terminal!

### 3. Download Response

Klik **"Download"** untuk save response sebagai JSON file.

### 4. Test Multiple Scenarios

Buat beberapa test case:

**Scenario 1: Exact Match**
```json
{"message": "Apa itu Kanvas?"}
// Expected: confidence ~0.95+
```

**Scenario 2: Similar Question**
```json
{"message": "Kanvas itu apa sih?"}
// Expected: confidence ~0.7-0.85
```

**Scenario 3: Different Phrasing**
```json
{"message": "bisa jelasin tentang kanvas?"}
// Expected: confidence ~0.6-0.75
```

**Scenario 4: No Match**
```json
{"message": "cuaca hari ini gimana?"}
// Expected: confidence <0.5, suggestions provided
```

## 🔍 Debugging dengan Swagger

### Jika Response Error

1. **Periksa Request Body**
   - Apakah JSON valid?
   - Apakah required fields sudah diisi?
   - Apakah format data benar?

2. **Periksa Response Code**
   - 400: Input tidak valid
   - 500: Server error (lihat logs)

3. **Periksa Server Logs**
   
   Di terminal yang menjalankan server, lihat logs:
   ```
   INFO:     Processing message: Bagaimana cara...
   ERROR:    Error in similarity search: ...
   ```

### Jika Confidence Terlalu Rendah

1. **Cek FAQ di Knowledge Base**
   ```bash
   curl http://localhost:8000/similarity/faqs
   ```

2. **Test Similarity Langsung**
   ```bash
   POST /similarity/search
   {
     "query": "your question",
     "candidates": ["FAQ 1", "FAQ 2"],
     "top_k": 3
   }
   ```

3. **Adjust Threshold** di `app/services/chat_service.py`

## 📱 Alternative: ReDoc

Jika lebih suka tampilan berbeda, akses:

```
http://localhost:8000/redoc
```

**Keuntungan ReDoc:**
- Tampilan lebih clean
- Better untuk reading documentation
- One-page scroll

**Keuntungan Swagger:**
- Interactive testing
- Try it out feature
- Better untuk development

## 🎬 Quick Start Testing

Copy-paste test cases ini langsung di Swagger:

### Test Case 1: Basic Chat
```json
{
  "message": "Apa itu Kanvas?"
}
```

### Test Case 2: Different Phrasing
```json
{
  "message": "bisa jelasin soal kanvas?"
}
```

### Test Case 3: With User ID
```json
{
  "message": "Bagaimana cara menggunakan Kanvas?",
  "user_id": "user123"
}
```

### Test Case 4: Similarity Test
```json
{
  "query": "cara pakai aplikasi",
  "candidates": [
    "Bagaimana cara menggunakan Kanvas?",
    "Apa itu Kanvas?",
    "Apakah Kanvas gratis?"
  ],
  "top_k": 3
}
```

## 💡 Pro Tips

1. **Bookmark URL**: `http://localhost:8000/docs`
2. **Keep Terminal Open**: Untuk lihat logs real-time
3. **Use Network Tab**: Browser DevTools → Network untuk debug
4. **Test Edge Cases**: Empty strings, very long text, special characters
5. **Compare Confidence**: Test berbagai phrasing, bandingkan confidence scores

## 🆘 Troubleshooting

### Server Tidak Bisa Diakses

```bash
# Cek apakah server running
curl http://localhost:8000/health

# Jika error, restart server
./dev.sh
```

### Port Already in Use

```bash
# Kill process di port 8000
lsof -ti:8000 | xargs kill -9

# Atau ganti port di .env
PORT=8001
```

### Model Loading Error

```bash
# Re-install dependencies
./setup.sh

# Atau manual
pip install sentence-transformers==3.3.1
```

## 📚 Resources

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json
- **AI Model Docs**: [AI_MODEL.md](AI_MODEL.md)

---

**Selamat Testing! 🚀**

Jika ada pertanyaan atau issue, check logs di terminal atau baca dokumentasi lengkap di `AI_MODEL.md`.

