from fastapi import APIRouter
from app.schemas.ai import StockPredictRequest, StockPredictResponse
from app.services.ai_service import predict_stock

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/predict", response_model=StockPredictResponse)
def predict_stock_api(request: StockPredictRequest):
    return predict_stock(request)