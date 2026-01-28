import httpx
from app.core.config import Settings
from app.utils.date_utils import get_today, get_days_before_today

class MarketService:
    BASE_URL = Settings().MARKET_SERVICE_API

    async def get_last_24h_candles(
        self,
        symbol: str,
        interval: str = "1h",
        limit: int = 48
    ):
        from_date = get_days_before_today(1)
        to_date = get_today()
        
        url = f"{self.BASE_URL}/market/candles/{symbol}/history"
        params = {
            "interval": interval,
            "from": from_date,
            "to": to_date,
            "limit": limit
        }
        
        async with httpx.AsyncClient(timeout=10) as client:
            res = await client.get(url, params=params)
            res.raise_for_status()
            return res.json()["data"]