from typing import Literal
from pydantic import BaseModel, Field

class TrendPrediction(BaseModel):
    direction: Literal["BULLISH", "BEARISH", "NEUTRAL"]
    confidence: int = Field(ge=0, le=100)

class FearGreed(BaseModel):
    score: int = Field(ge=0, le=100)
    label: Literal["Fear", "Neutral", "Greed"]
    
class StockPredictResponse(BaseModel):
    symbol: str
    trend: TrendPrediction
    fear_greed: FearGreed
    causal_analysis: str
