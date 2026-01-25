from fastapi import FastAPI
from app.api.v1.ai import router as ai_router
from app.core.config import settings
from app.core.logging import setup_logging

def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
    )

    app.include_router(ai_router, prefix="/api/v1")

    return app

app = create_app()