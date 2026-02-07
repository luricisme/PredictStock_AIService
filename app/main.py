from fastapi import FastAPI
from app.api.v1 import router as v1_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.cors import setup_cors

def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
    )

    setup_cors(app)
    app.include_router(v1_router, prefix="/api/v1")

    return app

app = create_app()