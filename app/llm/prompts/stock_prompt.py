from langchain_core.prompts import PromptTemplate

STOCK_PROMPT = PromptTemplate(
    template="""
You are a crypto market analyst.

Symbol: {symbol}

Technical summary (last 24h):
{technical_summary}

Your task:
1. Predict short-term trend direction.
2. Provide a concise causal analysis (2–3 sentences).

Rules:
- Trend must be one of: BULLISH, BEARISH, NEUTRAL
- Do NOT mention indicators explicitly.
- Focus on price action, momentum, volatility.

{format_instructions}
""",
    input_variables=["symbol", "technical_summary"],
)
