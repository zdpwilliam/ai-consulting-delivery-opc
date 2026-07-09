"""Application settings and configuration"""

from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings"""
    
    # API Keys
    openai_api_key: str
    claude_api_key: str
    
    # Environment
    app_env: str = "development"
    debug: bool = True
    log_level: str = "INFO"
    
    # Default settings
    default_industry: str = "ecommerce"
    default_currency: str = "USD"
    default_timezone: str = "UTC"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
