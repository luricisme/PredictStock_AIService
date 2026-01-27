from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # =========================
    # APP INFO
    # =========================
    APP_NAME: str = "Predict Stock - AI Service"
    APP_VERSION: str = "1.0.0"
    ENV: str = "dev"  # dev | staging | prod
    DEBUG: bool = True

    # =========================
    # SERVER (uvicorn)
    # =========================
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # =========================
    # LLM / AI
    # =========================
    GOOGLE_API_KEY: str | None = None
    LLM_MODEL: str = "gemini-2.5-flash"
    LLM_TEMPERATURE: float = 0.2
    LLM_MAX_TOKENS: int = 1024

    # =========================
    # LOGGING
    # =========================
    LOG_LEVEL: str = "INFO"

    # =========================
    # SECURITY
    # =========================
    SECRET_KEY: str = "change-me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # =========================
    # Pydantic Settings Config
    # =========================
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
