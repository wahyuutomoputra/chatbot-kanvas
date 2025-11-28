"""
Similarity Routes - Endpoints untuk semantic similarity
"""

from fastapi import APIRouter, HTTPException, status
from app.schemas.chat import SimilarityRequest, SimilarityResponse, FAQResponse
from app.services.embedding_service import embedding_service
from app.services.knowledge_base import knowledge_base
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/similarity", tags=["Semantic Similarity"])


@router.post("/search", response_model=SimilarityResponse)
async def similarity_search(request: SimilarityRequest):
    """
    Endpoint untuk mencari text yang paling mirip dari candidates.
    Menggunakan model all-MiniLM-L6-v2 untuk semantic similarity.
    
    Args:
        request: SimilarityRequest dengan query dan candidates
        
    Returns:
        SimilarityResponse: List of similar texts dengan score
    """
    try:
        logger.info(f"Similarity search for: {request.query[:50]}...")
        
        # Find most similar texts
        results = embedding_service.find_most_similar(
            query=request.query,
            candidates=request.candidates,
            top_k=request.top_k
        )
        
        # Format results
        formatted_results = [
            {
                "text": text,
                "similarity": float(similarity),
                "index": idx
            }
            for idx, text, similarity in results
        ]
        
        return SimilarityResponse(
            results=formatted_results,
            status="success"
        )
        
    except Exception as e:
        logger.error(f"Error in similarity search: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Terjadi kesalahan saat mencari similarity: {str(e)}"
        )


@router.get("/faqs", response_model=FAQResponse)
async def get_all_faqs():
    """
    Endpoint untuk mendapatkan semua FAQ dari knowledge base
    
    Returns:
        FAQResponse: List of all FAQs
    """
    try:
        faqs = knowledge_base.get_all_faqs()
        
        return FAQResponse(
            faqs=faqs,
            total=len(faqs)
        )
        
    except Exception as e:
        logger.error(f"Error getting FAQs: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Terjadi kesalahan saat mengambil FAQs: {str(e)}"
        )


@router.get("/faqs/search")
async def search_faqs(query: str, top_k: int = 3):
    """
    Endpoint untuk mencari FAQ yang paling relevan dengan query
    
    Args:
        query: Query text
        top_k: Number of top results (default: 3)
        
    Returns:
        List of relevant FAQs dengan similarity score
    """
    try:
        logger.info(f"Searching FAQs for: {query[:50]}...")
        
        # Get all questions
        questions = knowledge_base.get_all_questions()
        
        if not questions:
            return {
                "results": [],
                "message": "Knowledge base kosong"
            }
        
        # Find most similar questions
        results = embedding_service.find_most_similar(
            query=query,
            candidates=questions,
            top_k=min(top_k, len(questions))
        )
        
        # Format results with full FAQ
        formatted_results = []
        for idx, question, similarity in results:
            faq = knowledge_base.get_faq(idx)
            if faq:
                formatted_results.append({
                    "question": faq["question"],
                    "answer": faq["answer"],
                    "similarity": float(similarity)
                })
        
        return {
            "results": formatted_results,
            "total": len(formatted_results)
        }
        
    except Exception as e:
        logger.error(f"Error searching FAQs: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Terjadi kesalahan saat mencari FAQs: {str(e)}"
        )


@router.get("/model-info")
async def get_model_info():
    """
    Endpoint untuk mendapatkan informasi model yang digunakan
    
    Returns:
        Model information
    """
    return {
        "model_name": embedding_service.model_name,
        "model_type": "sentence-transformers",
        "description": "all-MiniLM-L6-v2 adalah model untuk sentence embeddings dan semantic similarity",
        "embedding_dimension": 384,
        "max_sequence_length": 256
    }

