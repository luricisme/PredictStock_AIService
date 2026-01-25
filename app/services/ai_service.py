from app.schemas.ai import StockPredictRequest, StockPredictResponse
from app.llm.chains.stock_sentiment_chain import stock_sentiment_chain

def predict_stock(request: StockPredictRequest) -> StockPredictResponse:
    result = stock_sentiment_chain.invoke({
        "news": request.news
    })

    return StockPredictResponse(
        symbol=request.symbol,
        trend=result.trend,
        confidence=result.confidence,
        reasoning=result.reasoning
    )

