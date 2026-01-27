from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings

def get_llm():
    return ChatGoogleGenerativeAI(
        model=settings.LLM_MODEL,
        temperature=settings.LLM_TEMPERATURE,
        max_output_tokens=settings.LLM_MAX_TOKENS,
        google_api_key=settings.GOOGLE_API_KEY,
    )

