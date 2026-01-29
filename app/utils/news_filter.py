from app.llm.chains.analyze_news_chain import analyze_news_chain


class NewsAIFilter:

    def filter(self, news_list, symbol):

        if not news_list:
            return []

        formatted_news = "\n".join([
            f"{i+1}. {n.get('title')} | {n.get('summary')}"
            for i, n in enumerate(news_list)
        ])

        result = analyze_news_chain.invoke({
            "symbol": symbol,
            "news_list": formatted_news
        })

        return result

