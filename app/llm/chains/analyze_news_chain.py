from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.llm.models.llm import get_llm

llm = get_llm()

prompt = PromptTemplate(
    template="""
You are a crypto news relevance classifier.

Symbol: {symbol}

News List:
{news_list}

Task:
Return ONLY a JSON array of numbers representing relevant news indexes.

Rules:
- Index starts from 1
- If none relevant → return []
- Only return JSON, nothing else

Relevant if:
- Mentions token symbol
- Mentions project name
- Mentions blockchain ecosystem
- Affects sentiment or price of this asset

Example Output:
[1,3,5]

Answer:
""",
    input_variables=["symbol", "news_list"]
)

analyze_news_chain = prompt | llm | StrOutputParser()