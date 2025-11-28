"""
Knowledge Base - FAQ dan data untuk chatbot
"""

from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)


class KnowledgeBase:
    """Knowledge base untuk FAQ dan informasi chatbot"""
    
    def __init__(self):
        """Inisialisasi knowledge base dengan FAQ"""
        self.faqs = self._load_faqs()
        logger.info(f"Loaded {len(self.faqs)} FAQs")
    
    def _load_faqs(self) -> List[Dict[str, str]]:
        """
        Load FAQs dari data
        Sumber: https://kanvas.co.id/
        
        Returns:
            List of FAQ dictionaries
        """
        # TODO: Load from database atau file JSON
        # Data berdasarkan informasi resmi dari https://kanvas.co.id/
        return [
            {
                "question": "Apa itu Kanvas Store?",
                "answer": "Kanvas Store adalah platform e-commerce cross-border S2B2C (Supplier to Business to Consumer) terkemuka di Indonesia. Kami menghubungkan supplier berkualitas dengan toko retail offline, menyediakan solusi terintegrasi untuk pembelian dan display produk, membantu toko retail meningkatkan efisiensi dan profitabilitas bisnis."
            },
            {
                "question": "Apa itu S2B2C?",
                "answer": "S2B2C adalah model bisnis Supplier to Business to Consumer. Kanvas Store menghubungkan supplier dengan toko retail (Business), yang kemudian menjual ke konsumen akhir (Consumer). Platform kami menjadi jembatan antara supplier dan retail melalui platform digital yang efisien."
            },
            {
                "question": "Apa layanan yang ditawarkan Kanvas Store?",
                "answer": "Kanvas Store menyediakan 3 layanan unggulan: 1) Supplier Network - Akses ke supplier terverifikasi dari dalam dan luar negeri dengan kualitas produk terjamin dan harga kompetitif. 2) Layanan Logistik Terintegrasi - Pengiriman cepat dengan tracking real-time dan layanan after-sales. 3) Dukungan Retail - Solusi lengkap termasuk display management, training & support, dan analisis penjualan."
            },
            {
                "question": "Siapa yang bisa menggunakan Kanvas Store?",
                "answer": "Kanvas Store diperuntukkan untuk toko retail offline yang ingin meningkatkan efisiensi operasional dan profitabilitas bisnis. Baik toko kecil maupun retail chain bisa bergabung dengan platform kami untuk mendapatkan akses ke supplier berkualitas dan layanan terintegrasi."
            },
            {
                "question": "Apa keunggulan Kanvas Store?",
                "answer": "Keunggulan Kanvas Store: 1) Platform S2B2C terkemuka dan 100% terpercaya, 2) Layanan One-Stop dari pembelian hingga display management, 3) Fokus pada retail offline, 4) Supplier terverifikasi dengan produk berkualitas, 5) Sistem logistik efisien dengan tracking real-time, 6) Support lengkap untuk meningkatkan penjualan."
            },
            {
                "question": "Bagaimana cara bergabung dengan Kanvas Store?",
                "answer": "Untuk bergabung dengan Kanvas Store, Anda bisa menghubungi kami melalui email di cs@kanvas.co.id atau telepon di (021) 123-4567. Tim kami akan membantu proses registrasi dan onboarding. Kunjungi website kami di https://kanvas.co.id/ untuk informasi lebih lanjut."
            },
            {
                "question": "Di mana lokasi Kanvas Store?",
                "answer": "Kanvas Store berlokasi di Jakarta, Indonesia. Namun layanan kami dapat diakses oleh toko retail di seluruh Indonesia. Kami menghubungkan supplier dari dalam dan luar negeri dengan toko retail lokal."
            },
            {
                "question": "Bagaimana sistem logistik Kanvas Store?",
                "answer": "Kanvas Store menyediakan layanan logistik terintegrasi dengan fitur pengiriman cepat, tracking real-time untuk memantau pesanan, dan layanan after-sales untuk memastikan kepuasan pelanggan. Sistem logistik kami dirancang khusus untuk efisiensi pengiriman produk ke toko retail."
            },
            {
                "question": "Apa itu Display Management di Kanvas Store?",
                "answer": "Display Management adalah layanan dukungan retail dari Kanvas Store yang membantu toko retail dalam penataan dan display produk di toko. Layanan ini termasuk training & support serta analisis penjualan untuk membantu meningkatkan performa penjualan toko retail."
            },
            {
                "question": "Bagaimana cara menghubungi Kanvas Store?",
                "answer": "Anda dapat menghubungi Kanvas Store melalui: Email: cs@kanvas.co.id, Telepon: (021) 123-4567. Kami juga memiliki website resmi di https://kanvas.co.id/. Tim customer service kami siap membantu Anda."
            },
            {
                "question": "Apakah Kanvas Store menyediakan supplier dari luar negeri?",
                "answer": "Ya, Kanvas Store adalah platform e-commerce cross-border, yang artinya kami menyediakan akses ke supplier berkualitas dari dalam dan luar negeri. Semua supplier telah melalui proses verifikasi untuk memastikan kualitas produk terjamin."
            },
            {
                "question": "Apa yang dimaksud dengan layanan one-stop?",
                "answer": "Layanan one-stop Kanvas Store berarti kami menyediakan solusi lengkap dan terintegrasi mulai dari pembelian produk, logistik pengiriman, hingga penataan display di toko retail. Toko retail tidak perlu menggunakan berbagai platform berbeda, cukup satu platform untuk semua kebutuhan."
            }
        ]
    
    def get_all_questions(self) -> List[str]:
        """
        Get semua pertanyaan dari FAQ
        
        Returns:
            List of questions
        """
        return [faq["question"] for faq in self.faqs]
    
    def get_answer(self, question_index: int) -> Optional[str]:
        """
        Get answer berdasarkan index pertanyaan
        
        Args:
            question_index: Index of the question
            
        Returns:
            Answer string atau None
        """
        if 0 <= question_index < len(self.faqs):
            return self.faqs[question_index]["answer"]
        return None
    
    def get_faq(self, question_index: int) -> Optional[Dict[str, str]]:
        """
        Get FAQ berdasarkan index
        
        Args:
            question_index: Index of the FAQ
            
        Returns:
            FAQ dictionary atau None
        """
        if 0 <= question_index < len(self.faqs):
            return self.faqs[question_index]
        return None
    
    def add_faq(self, question: str, answer: str) -> bool:
        """
        Tambah FAQ baru
        
        Args:
            question: Question text
            answer: Answer text
            
        Returns:
            True if successful
        """
        self.faqs.append({"question": question, "answer": answer})
        logger.info(f"Added new FAQ: {question}")
        return True
    
    def get_all_faqs(self) -> List[Dict[str, str]]:
        """
        Get semua FAQs
        
        Returns:
            List of all FAQs
        """
        return self.faqs


# Singleton instance
knowledge_base = KnowledgeBase()

