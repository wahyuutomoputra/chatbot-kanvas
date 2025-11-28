"""
Chat Schemas - Request & Response Models
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ChatRequest(BaseModel):
    """Schema untuk request chat"""
    message: str = Field(..., min_length=1, description="Pesan dari user")
    user_id: Optional[str] = Field(None, description="ID user (opsional)")
    session_id: Optional[str] = Field(None, description="ID session (opsional)")

    class Config:
        json_schema_extra = {
            "example": {
                "message": "Halo, apa kabar?",
                "user_id": "user123",
                "session_id": "session456"
            }
        }


class ChatResponse(BaseModel):
    """Schema untuk response chat"""
    response: str = Field(..., description="Respons dari chatbot")
    status: str = Field(default="success", description="Status response")
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp response")
    matched_question: Optional[str] = Field(None, description="Pertanyaan yang cocok dari knowledge base")
    method: Optional[str] = Field(None, description="Method yang digunakan (semantic_similarity, greeting, etc)")
    confidence: Optional[float] = Field(None, description="Confidence score (0-1)")
    suggestions: Optional[list] = Field(None, description="Saran pertanyaan lain")
    
    class Config:
        json_schema_extra = {
            "example": {
                "response": "Kanvas adalah platform chatbot yang menggunakan AI...",
                "status": "success",
                "timestamp": "2024-01-01T12:00:00",
                "matched_question": "Apa itu Kanvas?",
                "method": "semantic_similarity",
                "confidence": 0.92,
                "suggestions": None
            }
        }


class SimilarityRequest(BaseModel):
    """Schema untuk request similarity search"""
    query: str = Field(..., min_length=1, description="Query text untuk dicari")
    candidates: list[str] = Field(..., min_items=1, description="List of candidate texts")
    top_k: int = Field(default=3, ge=1, le=10, description="Number of top results")
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "Bagaimana cara pakai aplikasi ini?",
                "candidates": [
                    "Apa itu Kanvas?",
                    "Bagaimana cara menggunakan Kanvas?",
                    "Apakah Kanvas gratis?"
                ],
                "top_k": 3
            }
        }


class SimilarityResponse(BaseModel):
    """Schema untuk response similarity search"""
    results: list = Field(..., description="List of (text, similarity_score)")
    status: str = Field(default="success", description="Status response")
    
    class Config:
        json_schema_extra = {
            "example": {
                "results": [
                    {"text": "Bagaimana cara menggunakan Kanvas?", "similarity": 0.89},
                    {"text": "Apa itu Kanvas?", "similarity": 0.65}
                ],
                "status": "success"
            }
        }


class FAQResponse(BaseModel):
    """Schema untuk response FAQ list"""
    faqs: list = Field(..., description="List of FAQs")
    total: int = Field(..., description="Total number of FAQs")
    
    class Config:
        json_schema_extra = {
            "example": {
                "faqs": [
                    {"question": "Apa itu Kanvas?", "answer": "Kanvas adalah..."},
                    {"question": "Bagaimana cara menggunakan?", "answer": "Anda bisa..."}
                ],
                "total": 2
            }
        }


class HealthResponse(BaseModel):
    """Schema untuk health check response"""
    status: str = Field(default="healthy", description="Status aplikasi")
    version: str = Field(..., description="Versi aplikasi")
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp check")

