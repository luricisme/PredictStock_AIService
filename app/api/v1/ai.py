# app/api/v1/ai.py
from fastapi import APIRouter
from app.schemas.ai import StockPredictResponse
from app.services.ai_service import AIService

router = APIRouter(tags=["AI"])

ai_service = AIService()

@router.get(
    "/predict/{symbol}",
    response_model=StockPredictResponse
)
async def predict_stock_api(symbol: str):
    return await ai_service.predict_stock(symbol)
