from fastapi import APIRouter
from app.api.v1.ai import router as ai_router
from app.api.v1.test import router as test_router

router = APIRouter()

router.include_router(ai_router, prefix="/ai", tags=["AI"])
router.include_router(test_router, prefix="/test", tags=["Test"])