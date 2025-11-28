"""
Configuration Settings
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Konfigurasi aplikasi"""
    
    # App Settings
    APP_NAME: str = "Kanvas Chatbot API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "API untuk chatbot Kanvas dengan arsitektur modular"
    DEBUG: bool = True
    
    # Server Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # CORS Settings
    ALLOWED_ORIGINS: list = ["*"]  # Dalam production, ganti dengan domain spesifik
    
    # Database Settings (untuk future use)
    DATABASE_URL: Optional[str] = None
    
    # API Keys (untuk future use)
    API_KEY: Optional[str] = None
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Singleton instance
settings = Settings()

