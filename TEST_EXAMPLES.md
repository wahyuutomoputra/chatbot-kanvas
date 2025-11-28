# 🧪 Contoh Test Chatbot Kanvas Store

Kumpulan test cases untuk mencoba chatbot Kanvas Store via Swagger UI.

## 🚀 Cara Test

1. **Jalankan server**: `./dev.sh`
2. **Buka Swagger**: http://localhost:8000/docs
3. **Klik** `POST /chat/`
4. **Klik** **"Try it out"**
5. **Copy-paste** salah satu JSON di bawah
6. **Klik** **"Execute"**
7. **Lihat response** dengan confidence score!

## 📋 Test Cases

### 🏢 Tentang Platform

#### Test 1: Pertanyaan Dasar
```json
{
  "message": "Apa itu Kanvas Store?"
}
```
**Expected**: Confidence ~1.0, Penjelasan lengkap tentang Kanvas Store

#### Test 2: Different Phrasing
```json
{
  "message": "Kanvas Store itu apa sih?"
}
```
**Expected**: Confidence ~0.9, Match dengan FAQ "Apa itu Kanvas Store?"

#### Test 3: Informal
```json
{
  "message": "jelasin dong tentang kanvas"
}
```
**Expected**: Confidence ~0.7, Tetap match dengan FAQ yang relevan

#### Test 4: S2B2C Explanation
```json
{
  "message": "Apa yang dimaksud dengan S2B2C?"
}
```
**Expected**: Confidence ~1.0, Penjelasan model bisnis S2B2C

#### Test 5: Target Users
```json
{
  "message": "Siapa yang bisa pakai platform ini?"
}
```
**Expected**: Match dengan "Siapa yang bisa menggunakan Kanvas Store?"

### 💼 Layanan & Fitur

#### Test 6: Services Overview
```json
{
  "message": "Layanan apa saja yang tersedia?"
}
```
**Expected**: Penjelasan 3 layanan utama

#### Test 7: One-Stop Service
```json
{
  "message": "Apa maksudnya one-stop service?"
}
```
**Expected**: Penjelasan layanan terintegrasi

#### Test 8: Display Management
```json
{
  "message": "Apa itu display management?"
}
```
**Expected**: Penjelasan tentang display management service

#### Test 9: Advantages
```json
{
  "message": "Apa keunggulan menggunakan Kanvas Store?"
}
```
**Expected**: List keunggulan platform

### 🚚 Logistik & Supplier

#### Test 10: Logistics
```json
{
  "message": "Bagaimana sistem pengiriman barangnya?"
}
```
**Expected**: Match dengan FAQ tentang logistik

#### Test 11: Cross-Border
```json
{
  "message": "Apakah ada supplier dari luar negeri?"
}
```
**Expected**: Konfirmasi tentang supplier cross-border

#### Test 12: Supplier Quality
```json
{
  "message": "Bagaimana kualitas supplier di platform ini?"
}
```
**Expected**: Informasi tentang supplier terverifikasi

### 📞 Kontak & Registrasi

#### Test 13: Contact Info
```json
{
  "message": "Bagaimana cara menghubungi Kanvas Store?"
}
```
**Expected**: Email, telepon, dan website

#### Test 14: Registration
```json
{
  "message": "Gimana cara daftar jadi member?"
}
```
**Expected**: Match dengan FAQ bergabung

#### Test 15: Location
```json
{
  "message": "Kanvas Store ada di kota mana?"
}
```
**Expected**: Informasi lokasi Jakarta

### 🎯 Edge Cases

#### Test 16: Greeting
```json
{
  "message": "Halo!"
}
```
**Expected**: Greeting response dengan pengenalan chatbot

#### Test 17: No Match
```json
{
  "message": "Cuaca hari ini bagaimana?"
}
```
**Expected**: No match response dengan suggestions FAQ yang relevan

#### Test 18: Similar Topics
```json
{
  "message": "Apa bedanya dengan marketplace biasa?"
}
```
**Expected**: Confidence sedang, bisa match dengan FAQ tentang S2B2C atau keunggulan

#### Test 19: Very Specific
```json
{
  "message": "Berapa lama waktu pengiriman ke Surabaya?"
}
```
**Expected**: Confidence rendah, suggestions tentang logistik

#### Test 20: Multi-Question
```json
{
  "message": "Apa itu Kanvas Store dan bagaimana cara bergabung?"
}
```
**Expected**: Match dengan salah satu pertanyaan (biasanya yang pertama)

## 📊 Expected Results Summary

| Test Type | Expected Confidence | Notes |
|-----------|-------------------|-------|
| Exact Match | 0.95 - 1.0 | Perfect wording |
| Different Phrasing | 0.75 - 0.95 | Same meaning |
| Related Topic | 0.60 - 0.75 | Relevant but not exact |
| Greeting | N/A | Special handling |
| No Match | < 0.5 | Suggestions provided |

## 🎨 Response Analysis

### High Confidence (0.8 - 1.0)

```json
{
  "response": "Kanvas Store adalah platform...",
  "status": "success",
  "matched_question": "Apa itu Kanvas Store?",
  "method": "semantic_similarity",
  "confidence": 0.98,
  "suggestions": null
}
```

✅ **Interpretation**: Chatbot sangat yakin dengan jawaban

### Medium Confidence (0.6 - 0.8)

```json
{
  "response": "...",
  "confidence": 0.73,
  "matched_question": "Apa layanan yang ditawarkan...",
  "suggestions": [
    {
      "question": "Apa itu Display Management...",
      "similarity": 0.65
    }
  ]
}
```

⚠️ **Interpretation**: Match cukup baik, dengan suggestions alternatif

### Low Confidence (< 0.5)

```json
{
  "response": "Maaf, saya tidak menemukan jawaban yang tepat...",
  "method": "no_match",
  "confidence": 0.35,
  "suggestions": [
    {
      "question": "Bagaimana sistem logistik...",
      "similarity": 0.35
    }
  ]
}
```

❌ **Interpretation**: No match, memberikan saran pertanyaan lain

## 🔍 Testing Semantic Similarity

Test dengan variasi kata yang berbeda:

### Variasi 1: Formal vs Informal

```json
{"message": "Apa itu Kanvas Store?"}           // Formal
{"message": "Kanvas Store itu apa?"}           // Informal
{"message": "jelasin tentang kanvas dong"}     // Very informal
```

### Variasi 2: Question Style

```json
{"message": "Bagaimana cara bergabung?"}       // How
{"message": "Gimana cara join?"}               // Informal how
{"message": "Cara daftar gimana?"}             // Different word order
```

### Variasi 3: Synonym Usage

```json
{"message": "Layanan apa yang ditawarkan?"}    // ditawarkan
{"message": "Layanan apa yang tersedia?"}      // tersedia
{"message": "Apa saja fitur yang ada?"}        // fitur
```

## 💡 Tips Testing

1. **Start Simple**: Mulai dengan exact match questions
2. **Try Variations**: Test dengan phrasing berbeda
3. **Check Confidence**: Perhatikan confidence score
4. **Read Suggestions**: Jika confidence rendah, lihat suggestions
5. **Test Edge Cases**: Coba greeting, no match, dll

## 🆘 Troubleshooting

### Confidence Terlalu Rendah

**Problem**: Pertanyaan relevan tapi confidence < 0.5

**Solution**:
1. Cek FAQ di `/similarity/faqs`
2. Tambah FAQ baru yang lebih specific
3. Adjust threshold di `chat_service.py`

### Wrong Match

**Problem**: Match dengan FAQ yang salah

**Solution**:
1. Perbaiki wording FAQ
2. Tambah FAQ yang lebih spesifik
3. Test dengan `/similarity/search` untuk debug

### Slow Response

**Problem**: Response lambat

**Solution**:
1. Model loading pertama kali butuh waktu
2. Subsequent requests harusnya cepat (~50ms)
3. Check server logs untuk errors

## 📈 Advanced Testing

### Batch Testing dengan Similarity Search

```bash
curl -X POST http://localhost:8000/similarity/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "cara bergabung dengan platform",
    "candidates": [
      "Apa itu Kanvas Store?",
      "Bagaimana cara bergabung dengan Kanvas Store?",
      "Di mana lokasi Kanvas Store?"
    ],
    "top_k": 3
  }'
```

### Search All FAQs

```bash
curl "http://localhost:8000/similarity/faqs/search?query=layanan&top_k=5"
```

### Get Model Info

```bash
curl http://localhost:8000/similarity/model-info
```

## 🎯 Test Checklist

Gunakan checklist ini untuk comprehensive testing:

- [ ] Test all 12 FAQ exact matches (confidence ~1.0)
- [ ] Test 5+ different phrasings per topic
- [ ] Test informal language
- [ ] Test greeting
- [ ] Test no match scenarios
- [ ] Test very long questions
- [ ] Test questions with typos
- [ ] Test multi-language (if supported)
- [ ] Test special characters
- [ ] Test empty message (should error)
- [ ] Check response time (should be < 100ms)
- [ ] Verify all contact info correct
- [ ] Test via cURL
- [ ] Test via Swagger
- [ ] Test via Python client

## 📚 Resources

- **Swagger UI**: http://localhost:8000/docs
- **Knowledge Base**: [KNOWLEDGE_BASE.md](KNOWLEDGE_BASE.md)
- **Swagger Guide**: [SWAGGER_GUIDE.md](SWAGGER_GUIDE.md)
- **AI Model Docs**: [AI_MODEL.md](AI_MODEL.md)

---

**Happy Testing! 🚀**

Jika menemukan bug atau confidence yang tidak sesuai, update FAQ di `app/services/knowledge_base.py`

