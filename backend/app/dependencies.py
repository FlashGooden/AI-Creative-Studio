from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.redis import get_redis
from fastapi import Depends


def get_database() -> Session:
    """Get database session dependency."""
    return next(get_db())


def get_redis_client():
    """Get Redis client dependency."""
    return get_redis()