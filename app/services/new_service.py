import httpx
from app.core.config import Settings

class NewsService:

    async def get_latest_news(self, limit: int = 20):
        BASE_URL = Settings().CRAWLER_SERVICE_API
        async with httpx.AsyncClient() as client:
            res = await client.get(f"{BASE_URL}/user-service/news")

            res.raise_for_status()

            data = res.json()
            return data.get("data", [])
