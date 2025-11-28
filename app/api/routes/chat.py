"""
Chat Routes - Controller Layer
"""

from fastapi import APIRouter, HTTPException, status
from app.schemas.chat import (
    ChatRequest, 
    ChatResponse, 
    SimilarityRequest, 
    SimilarityResponse,
    FAQResponse
)
from app.services.chat_service import chat_service
from app.services.embedding_service import embedding_service
from app.services.knowledge_base import knowledge_base
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def send_message(request: ChatRequest):
    """
    Endpoint untuk mengirim pesan ke chatbot.
    Menggunakan semantic similarity dengan model all-MiniLM-L6-v2.
    
    Args:
        request: ChatRequest dengan message, user_id, dan session_id
        
    Returns:
        ChatResponse: Response dari chatbot dengan confidence score
    """
    try:
        logger.info(f"Received chat request from user: {request.user_id}")
        
        # Panggil service untuk memproses message (business logic)
        result = await chat_service.process_message(
            message=request.message,
            user_id=request.user_id,
            session_id=request.session_id
        )
        
        # Optional: Simpan chat ke database
        if request.user_id:
            await chat_service.save_chat(
                user_id=request.user_id,
                message=request.message,
                response=result["response"],
                session_id=request.session_id
            )
        
        return ChatResponse(
            response=result["response"],
            status="success",
            matched_question=result.get("matched_question"),
            method=result.get("method"),
            confidence=result.get("confidence"),
            suggestions=result.get("suggestions")
        )
        
    except Exception as e:
        logger.error(f"Error processing chat: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Terjadi kesalahan saat memproses pesan: {str(e)}"
        )


@router.get("/history/{user_id}", response_model=list)
async def get_chat_history(user_id: str, limit: int = 10):
    """
    Endpoint untuk mendapatkan riwayat chat user
    
    Args:
        user_id: ID user
        limit: Jumlah maksimal history yang diambil (default: 10)
        
    Returns:
        list: List of chat history
    """
    try:
        logger.info(f"Getting chat history for user: {user_id}")
        
        history = await chat_service.get_chat_history(
            user_id=user_id,
            limit=limit
        )
        
        return history
        
    except Exception as e:
        logger.error(f"Error getting chat history: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Terjadi kesalahan saat mengambil riwayat chat: {str(e)}"
        )

