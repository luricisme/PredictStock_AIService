from pydantic import BaseModel
from typing import Literal

class LLMTrendOutput(BaseModel):
    direction: Literal["BULLISH", "BEARISH", "NEUTRAL"]
    confidence: float  # 0–1
    reasoning: str
