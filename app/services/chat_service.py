"""
Chat Service - Business Logic untuk Chat
"""

from typing import Optional, Dict
import logging
from app.services.embedding_service import embedding_service
from app.services.knowledge_base import knowledge_base

logger = logging.getLogger(__name__)


class ChatService:
    """Service untuk menangani logika bisnis chat dengan semantic similarity"""
    
    def __init__(self):
        """Inisialisasi ChatService"""
        self.embedding_service = embedding_service
        self.knowledge_base = knowledge_base
        self.similarity_threshold = 0.5  # Minimum similarity untuk match
        logger.info("ChatService initialized with semantic similarity")
    
    async def process_message(
        self, 
        message: str, 
        user_id: Optional[str] = None,
        session_id: Optional[str] = None
    ) -> Dict[str, any]:
        """
        Memproses pesan dari user dan mengembalikan response
        Menggunakan semantic similarity untuk mencari jawaban dari knowledge base
        
        Args:
            message: Pesan dari user
            user_id: ID user (opsional)
            session_id: ID session (opsional)
            
        Returns:
            Dict: Response dari chatbot dengan metadata
        """
        logger.info(f"Processing message: {message[:50]}...")
        
        # Simple greeting detection
        message_lower = message.lower()
        if any(word in message_lower for word in ["halo", "hai", "hello", "hi"]):
            return {
                "response": "Halo! Selamat datang di Kanvas Chatbot. Saya menggunakan AI untuk menjawab pertanyaan Anda. Silakan tanya apa saja!",
                "method": "greeting",
                "confidence": 1.0
            }
        
        # Find similar question from knowledge base
        questions = self.knowledge_base.get_all_questions()
        
        if not questions:
            return {
                "response": "Maaf, knowledge base masih kosong. Silakan tambahkan FAQ terlebih dahulu.",
                "method": "no_data",
                "confidence": 0.0
            }
        
        # Find most similar question
        results = self.embedding_service.find_most_similar(
            query=message,
            candidates=questions,
            top_k=3  # Get top 3 results
        )
        
        best_match_idx, best_match_question, similarity_score = results[0]
        
        logger.info(f"Best match: '{best_match_question}' (similarity: {similarity_score:.3f})")
        
        # Check if similarity is above threshold
        if similarity_score >= self.similarity_threshold:
            answer = self.knowledge_base.get_answer(best_match_idx)
            
            # Add suggestions if similarity is not very high
            suggestions = []
            if similarity_score < 0.8 and len(results) > 1:
                suggestions = [
                    {
                        "question": q,
                        "similarity": float(s)
                    }
                    for _, q, s in results[1:3] if s >= self.similarity_threshold
                ]
            
            return {
                "response": answer,
                "matched_question": best_match_question,
                "method": "semantic_similarity",
                "confidence": float(similarity_score),
                "suggestions": suggestions if suggestions else None
            }
        else:
            # No good match found, provide top suggestions
            suggestions = [
                {
                    "question": q,
                    "similarity": float(s)
                }
                for _, q, s in results[:3]
            ]
            
            return {
                "response": "Maaf, saya tidak menemukan jawaban yang tepat untuk pertanyaan Anda. Mungkin Anda bisa coba pertanyaan berikut?",
                "method": "no_match",
                "confidence": float(similarity_score),
                "suggestions": suggestions
            }
    
    async def get_chat_history(self, user_id: str, limit: int = 10) -> list:
        """
        Mendapatkan riwayat chat user
        
        Args:
            user_id: ID user
            limit: Jumlah maksimal history yang diambil
            
        Returns:
            list: List of chat history
        """
        # TODO: Implementasi get history dari database
        logger.info(f"Getting chat history for user: {user_id}")
        return []
    
    async def save_chat(
        self, 
        user_id: str, 
        message: str, 
        response: str,
        session_id: Optional[str] = None
    ) -> bool:
        """
        Menyimpan chat ke database
        
        Args:
            user_id: ID user
            message: Pesan dari user
            response: Response dari chatbot
            session_id: ID session (opsional)
            
        Returns:
            bool: True jika berhasil disimpan
        """
        # TODO: Implementasi save ke database
        logger.info(f"Saving chat for user: {user_id}")
        return True


# Singleton instance
chat_service = ChatService()

