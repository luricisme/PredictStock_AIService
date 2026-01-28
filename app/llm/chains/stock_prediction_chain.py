from langchain_core.output_parsers import PydanticOutputParser
from app.llm.prompts.stock_prompt import STOCK_PROMPT
from app.llm.models.llm import get_llm
from app.schemas.llm import LLMTrendOutput

parser = PydanticOutputParser(
    pydantic_object=LLMTrendOutput
)

prompt = STOCK_PROMPT.partial(
    format_instructions=parser.get_format_instructions()
)

llm = get_llm()

stock_prediction_chain = prompt | llm | parser