from langchain_core.output_parsers import PydanticOutputParser
from app.schemas.ai import StockPredictResponse
from app.llm.prompts.stock_prompt import STOCK_PROMPT
from app.llm.models.llm import get_llm

parser = PydanticOutputParser(pydantic_object=StockPredictResponse)

prompt = STOCK_PROMPT.partial(
    format_instructions=parser.get_format_instructions()
)

llm = get_llm()

stock_sentiment_chain = prompt | llm | parser