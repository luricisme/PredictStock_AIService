from langchain_core.prompts import PromptTemplate

STOCK_PROMPT = PromptTemplate(
    template="""
You are a financial analyst.

Based on the following company news, predict the stock trend.

Company news:
{news}

Return:
- trend: UP, DOWN, or NEUTRAL
- confidence: number between 0 and 1
- reasoning: short explanation
""",
    input_variables=["news"],
)

