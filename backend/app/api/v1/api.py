from fastapi import APIRouter
from app.api.v1.endpoints import test

api_router = APIRouter()

# Include test endpoints
api_router.include_router(test.router, prefix="/test", tags=["test"])


@api_router.get("/status")
async def api_status():
    return {"status": "API v1 is running"}