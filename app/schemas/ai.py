from pydantic import BaseModel, Field

class StockPredictRequest(BaseModel):
    symbol: str = Field(..., example="AAPL")
    news: str = Field(..., example="Apple reports strong iPhone sales...")

class StockPredictResponse(BaseModel):
    symbol: str
    trend: str  # UP | DOWN | NEUTRAL
    confidence: float  # 0 → 1
    reasoning: str
