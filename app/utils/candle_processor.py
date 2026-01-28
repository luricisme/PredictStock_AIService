from app.schemas.candle import Candle

def summarize_candles(candles: list[Candle]) -> dict:
    closes = [c.close for c in candles]
    highs = [c.high for c in candles]
    lows = [c.low for c in candles]

    price_change = closes[-1] - closes[0]
    percent_change = round((price_change / closes[0]) * 100, 2)

    trend = (
        "bullish" if percent_change > 0.5
        else "bearish" if percent_change < -0.5
        else "sideways"
    )

    return {
        "trend": trend,
        "percent_change": percent_change,
        "high_24h": max(highs),
        "low_24h": min(lows),
        "last_close": closes[-1],
        "volatility": round(max(highs) - min(lows), 2),
        "candle_count": len(candles)
    }