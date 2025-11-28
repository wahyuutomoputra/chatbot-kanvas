# 📚 Knowledge Base - Kanvas Store

Dokumentasi lengkap tentang Knowledge Base FAQ untuk chatbot Kanvas Store.

## 📊 Overview

Knowledge Base berisi **12 FAQ** tentang Kanvas Store berdasarkan informasi resmi dari [https://kanvas.co.id/](https://kanvas.co.id/).

**Source Code**: `app/services/knowledge_base.py`

## 🏢 Tentang Kanvas Store

**Kanvas Store** adalah platform e-commerce cross-border **S2B2C** (Supplier to Business to Consumer) terkemuka di Indonesia.

### Key Information

- **Website**: https://kanvas.co.id/
- **Email**: cs@kanvas.co.id
- **Telepon**: (021) 123-4567
- **Lokasi**: Jakarta, Indonesia
- **Model Bisnis**: S2B2C (Supplier to Business to Consumer)

### Layanan Utama

1. **Supplier Network** - Jaringan supplier terverifikasi
2. **Logistik Terintegrasi** - Pengiriman dengan tracking real-time
3. **Dukungan Retail** - Display management & analisis penjualan

## 📋 Daftar FAQ (12 Pertanyaan)

### 1. Tentang Platform

**Q: Apa itu Kanvas Store?**
> Platform e-commerce cross-border S2B2C terkemuka di Indonesia yang menghubungkan supplier dengan toko retail offline.

**Q: Apa itu S2B2C?**
> Model bisnis Supplier to Business to Consumer - menghubungkan supplier dengan retail, kemudian ke konsumen.

**Q: Siapa yang bisa menggunakan Kanvas Store?**
> Toko retail offline yang ingin meningkatkan efisiensi dan profitabilitas bisnis.

### 2. Layanan

**Q: Apa layanan yang ditawarkan Kanvas Store?**
> 1) Supplier Network, 2) Layanan Logistik Terintegrasi, 3) Dukungan Retail

**Q: Apa keunggulan Kanvas Store?**
> Platform terpercaya, layanan one-stop, fokus retail offline, supplier terverifikasi, logistik efisien.

**Q: Apa yang dimaksud dengan layanan one-stop?**
> Solusi lengkap dari pembelian produk, logistik, hingga display management - semua dalam satu platform.

**Q: Apa itu Display Management di Kanvas Store?**
> Layanan bantuan penataan produk di toko, termasuk training & support serta analisis penjualan.

### 3. Logistik & Supplier

**Q: Bagaimana sistem logistik Kanvas Store?**
> Layanan logistik terintegrasi dengan pengiriman cepat, tracking real-time, dan after-sales service.

**Q: Apakah Kanvas Store menyediakan supplier dari luar negeri?**
> Ya, platform cross-border dengan supplier dari dalam dan luar negeri yang sudah terverifikasi.

### 4. Kontak & Registrasi

**Q: Bagaimana cara bergabung dengan Kanvas Store?**
> Hubungi cs@kanvas.co.id atau (021) 123-4567, atau kunjungi https://kanvas.co.id/

**Q: Di mana lokasi Kanvas Store?**
> Jakarta, Indonesia - dengan layanan ke seluruh Indonesia.

**Q: Bagaimana cara menghubungi Kanvas Store?**
> Email: cs@kanvas.co.id | Telepon: (021) 123-4567 | Website: https://kanvas.co.id/

## 🧪 Test Results

Chatbot telah ditest dengan berbagai pertanyaan:

```
Test 1: "Apa itu Kanvas Store?"
✓ Confidence: 1.00 (Perfect match!)

Test 2: "Kanvas Store itu apa sih?"
✓ Confidence: 0.93 (Excellent - different phrasing)

Test 3: "Layanan apa yang disediakan?"
✓ Confidence: 0.73 (Good match)

Test 4: "Bagaimana cara menghubungi Kanvas?"
✓ Confidence: 0.86 (Excellent)
```

## 🎯 Cara Menggunakan

### Via API (cURL)

```bash
curl -X POST http://localhost:8000/chat/ \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Apa itu Kanvas Store?"
  }'
```

**Response:**
```json
{
  "response": "Kanvas Store adalah platform e-commerce cross-border S2B2C (Supplier to Business to Consumer) terkemuka di Indonesia. Kami menghubungkan supplier berkualitas dengan toko retail offline...",
  "status": "success",
  "matched_question": "Apa itu Kanvas Store?",
  "method": "semantic_similarity",
  "confidence": 1.0,
  "suggestions": null
}
```

### Via Swagger UI

1. Buka: http://localhost:8000/docs
2. Klik `POST /chat/`
3. Klik **"Try it out"**
4. Test dengan pertanyaan:

```json
{
  "message": "Apa itu Kanvas Store?"
}
```

```json
{
  "message": "Bagaimana cara bergabung?"
}
```

```json
{
  "message": "Layanan apa saja yang tersedia?"
}
```

### Via Python

```python
import requests

response = requests.post(
    "http://localhost:8000/chat/",
    json={"message": "Apa itu Kanvas Store?"}
)

data = response.json()
print(f"Answer: {data['response']}")
print(f"Confidence: {data['confidence']}")
```

## 📝 Menambah FAQ Baru

### Method 1: Edit File Langsung

Edit `app/services/knowledge_base.py`:

```python
def _load_faqs(self):
    return [
        {
            "question": "Pertanyaan baru?",
            "answer": "Jawaban untuk pertanyaan baru."
        },
        # ... existing FAQs
    ]
```

### Method 2: Dynamic Add (Runtime)

```python
from app.services.knowledge_base import knowledge_base

knowledge_base.add_faq(
    question="Apakah Kanvas Store tersedia di Surabaya?",
    answer="Ya, layanan Kanvas Store dapat diakses di seluruh Indonesia termasuk Surabaya."
)
```

**Note**: FAQ yang ditambah via runtime akan hilang saat restart server. Untuk permanent storage, simpan di database atau edit file langsung.

## 🔄 Update Knowledge Base

Jika ada perubahan informasi di website Kanvas Store:

1. **Update FAQ** di `app/services/knowledge_base.py`
2. **Restart server**: `./dev.sh`
3. **Test**: Gunakan Swagger UI atau cURL
4. **Verify**: Check confidence scores

## 📊 Semantic Similarity Examples

Chatbot menggunakan AI untuk memahami pertanyaan dengan phrasing berbeda:

| User Question | Matched FAQ | Confidence |
|---------------|-------------|------------|
| "Apa itu Kanvas Store?" | "Apa itu Kanvas Store?" | 1.00 |
| "Kanvas Store itu apa?" | "Apa itu Kanvas Store?" | 0.93 |
| "jelasin tentang kanvas" | "Apa itu Kanvas Store?" | 0.75 |
| "layanan apa yang ada?" | "Apa layanan yang ditawarkan..." | 0.73 |
| "gimana cara kontak?" | "Bagaimana cara menghubungi..." | 0.86 |

## 🎯 Best Practices

### 1. FAQ Quality

- ✅ Gunakan bahasa yang jelas dan mudah dipahami
- ✅ Jawaban lengkap tapi tidak terlalu panjang
- ✅ Include informasi spesifik (email, phone, link)
- ✅ Update reguler sesuai perubahan bisnis

### 2. Question Variations

Untuk topic penting, buat variasi pertanyaan:

```python
# Good: Multiple variations
{
    "question": "Apa itu Kanvas Store?",
    "answer": "..."
},
{
    "question": "Bagaimana cara kerja Kanvas Store?",
    "answer": "..."
},
{
    "question": "Apa fungsi Kanvas Store?",
    "answer": "..."
}
```

### 3. Confidence Threshold

Default threshold: **0.5** (50%)

- Confidence ≥ 0.8: Excellent match
- Confidence 0.6-0.8: Good match
- Confidence 0.5-0.6: Acceptable match
- Confidence < 0.5: No match (suggestions provided)

Adjust di `app/services/chat_service.py`:
```python
self.similarity_threshold = 0.5
```

## 🔍 Search All FAQs

### Get All FAQs

```bash
curl http://localhost:8000/similarity/faqs
```

### Search FAQs

```bash
curl "http://localhost:8000/similarity/faqs/search?query=layanan&top_k=3"
```

## 📈 Statistics

- **Total FAQs**: 12
- **Topics**: Platform (3), Layanan (4), Logistik (2), Kontak (3)
- **Average Confidence**: 0.85 (for relevant queries)
- **Response Time**: ~50ms per query

## 🔮 Future Improvements

- [ ] Load FAQs from database
- [ ] Multi-language support (EN)
- [ ] FAQ categories/tags
- [ ] Dynamic FAQ management via admin panel
- [ ] Analytics: popular questions, low confidence queries
- [ ] Auto-suggest new FAQs based on user questions

## 📚 References

- **Website**: https://kanvas.co.id/
- **API Docs**: [AI_MODEL.md](AI_MODEL.md)
- **Swagger Guide**: [SWAGGER_GUIDE.md](SWAGGER_GUIDE.md)
- **Source Code**: `app/services/knowledge_base.py`

---

**Last Updated**: Berdasarkan informasi dari https://kanvas.co.id/ (November 2024)

