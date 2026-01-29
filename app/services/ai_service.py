from app.schemas.ai import StockPredictResponse
from app.services.market_service import MarketService
from app.services.new_service import NewsService
from app.utils.candle_mapper import map_raw_candle
from app.utils.candle_processor import summarize_candles
from app.utils.fear_greed import calculate_fear_greed
from app.llm.chains.stock_prediction_chain import stock_prediction_chain
from app.utils.news_filter import filter_news_for_symbol

class AIService:
    def __init__(self):
        self.market = MarketService()
        self.news = NewsService()

    async def predict_stock(self, symbol: str) -> StockPredictResponse:
        # ===== 1. Market Data =====
        raw_candles = await self.market.get_last_24h_candles(symbol)

        candles = [map_raw_candle(c) for c in raw_candles]
        technical = summarize_candles(candles)

        # ===== 2. News Data =====
        news_list = await self.news.get_latest_news()
        relevant_news = filter_news_for_symbol(news_list, symbol)
        
        news_context = "\n".join(relevant_news) if relevant_news else "No major related news"

        llm_result = stock_prediction_chain.invoke({
            "symbol": symbol,
            "technical_summary": technical,
            "news_context": news_context
        })

        fear_greed = calculate_fear_greed(
            percent_change=technical["percent_change"],
            volatility=technical["volatility"]
        )

        return StockPredictResponse(
            symbol=symbol,
            trend={
                "direction": llm_result.direction,
                "confidence": int(llm_result.confidence * 100)
            },
            fear_greed=fear_greed,
            causal_analysis=llm_result.reasoning
        )
