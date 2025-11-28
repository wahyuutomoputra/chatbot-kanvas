"""
Health Check Routes
"""

from fastapi import APIRouter
from app.schemas.chat import HealthResponse
from app.core.config import settings

router = APIRouter(tags=["Health"])


@router.get("/", response_model=dict)
async def root():
    """Endpoint root untuk mengecek status API"""
    return {
        "message": f"Selamat datang di {settings.APP_NAME}",
        "status": "running",
        "version": settings.APP_VERSION
    }


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Endpoint untuk health check"""
    return HealthResponse(
        status="healthy",
        version=settings.APP_VERSION
    )

