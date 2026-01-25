from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Predict Stock AI Service"
    APP_VERSION: str = "1.0.0"
    
    # LLM
    GOOGLE_API_KEY: str | None = None
    
    class Config:
        env_file = ".env"
        
settings = Settings()