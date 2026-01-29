def filter_news_for_symbol(news_list: list[dict], symbol: str) -> list[str]:
    """
    Return list news text relevant to symbol
    """

    base_symbol = symbol.replace("USDT", "").lower()

    relevant_news = []

    for news in news_list:
        text = f"{news.get('title', '')} {news.get('summary', '')}".lower()

        if base_symbol in text:
            relevant_news.append(
                f"- {news.get('title')} | {news.get('summary')}"
            )

    return relevant_news[:5]  # limit max 5 news
