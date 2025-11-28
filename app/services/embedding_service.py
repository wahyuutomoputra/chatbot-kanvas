"""
Embedding Service - Handle sentence embeddings dan similarity
"""

from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Tuple, Optional
import logging
import os

logger = logging.getLogger(__name__)


class EmbeddingService:
    """Service untuk handle embeddings menggunakan all-MiniLM-L6-v2"""
    
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        """
        Inisialisasi EmbeddingService dengan model (lazy loading untuk Vercel)
        
        Args:
            model_name: Nama model dari Hugging Face
        """
        self.model_name = model_name
        self._model: Optional[SentenceTransformer] = None
        logger.info(f"EmbeddingService initialized (model: {model_name})")
        # Model akan di-load saat pertama kali digunakan (lazy loading)
    
    @property
    def model(self) -> SentenceTransformer:
        """
        Lazy load model - hanya load saat pertama kali digunakan
        Ini membantu mengurangi cold start time di Vercel
        """
        if self._model is None:
            logger.info(f"Loading model: {self.model_name}")
            # Set cache directory untuk Vercel (/tmp)
            cache_dir = os.environ.get("TRANSFORMERS_CACHE", "/tmp/.cache")
            os.makedirs(cache_dir, exist_ok=True)
            
            self._model = SentenceTransformer(
                self.model_name,
                cache_folder=cache_dir
            )
            logger.info("Model loaded successfully")
        return self._model
    
    def encode(self, texts: List[str]) -> np.ndarray:
        """
        Encode teks menjadi embeddings
        
        Args:
            texts: List of texts to encode
            
        Returns:
            numpy array of embeddings
        """
        logger.info(f"Encoding {len(texts)} texts")
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings
    
    def encode_single(self, text: str) -> np.ndarray:
        """
        Encode single text menjadi embedding
        
        Args:
            text: Text to encode
            
        Returns:
            numpy array of embedding
        """
        return self.encode([text])[0]
    
    def cosine_similarity(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        """
        Hitung cosine similarity antara dua embeddings
        
        Args:
            embedding1: First embedding
            embedding2: Second embedding
            
        Returns:
            Similarity score (0-1)
        """
        similarity = np.dot(embedding1, embedding2) / (
            np.linalg.norm(embedding1) * np.linalg.norm(embedding2)
        )
        return float(similarity)
    
    def find_most_similar(
        self, 
        query: str, 
        candidates: List[str], 
        top_k: int = 1
    ) -> List[Tuple[int, str, float]]:
        """
        Find most similar text from candidates
        
        Args:
            query: Query text
            candidates: List of candidate texts
            top_k: Number of top results to return
            
        Returns:
            List of (index, text, similarity_score)
        """
        logger.info(f"Finding similar texts for query: {query[:50]}...")
        
        # Encode query and candidates
        query_embedding = self.encode_single(query)
        candidate_embeddings = self.encode(candidates)
        
        # Calculate similarities
        similarities = []
        for idx, (candidate, candidate_embedding) in enumerate(zip(candidates, candidate_embeddings)):
            similarity = self.cosine_similarity(query_embedding, candidate_embedding)
            similarities.append((idx, candidate, similarity))
        
        # Sort by similarity (descending)
        similarities.sort(key=lambda x: x[2], reverse=True)
        
        return similarities[:top_k]
    
    def batch_similarity(self, query: str, candidates: List[str]) -> List[float]:
        """
        Calculate similarity scores untuk semua candidates
        
        Args:
            query: Query text
            candidates: List of candidate texts
            
        Returns:
            List of similarity scores
        """
        query_embedding = self.encode_single(query)
        candidate_embeddings = self.encode(candidates)
        
        similarities = [
            self.cosine_similarity(query_embedding, emb)
            for emb in candidate_embeddings
        ]
        
        return similarities


# Singleton instance
embedding_service = EmbeddingService()

