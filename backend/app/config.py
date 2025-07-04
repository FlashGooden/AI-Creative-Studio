from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    app_name: str = "CreativeFlow AI"
    debug: bool = False

    # Database
    database_url: str

    # Redis
    redis_url: str

    # Security
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # AI Services
    openai_api_key: str
    elevenlabs_api_key: str
    stability_api_key: str

    # AWS S3
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_bucket_name: str
    aws_region: str = "us-east-1"

    # CORS
    cors_origins: List[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"


settings = Settings()
