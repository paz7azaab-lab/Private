"""News -> analysis pipeline for the paper-trading agent."""

from .news_engine import NewsItem, NewsSignal, analyze_news
from .news_providers import FinnhubNewsProvider


class NewsPipeline:
    def __init__(self, provider=None):
        self.provider = provider or FinnhubNewsProvider()

    def update(self) -> NewsSignal:
        items = self.provider.fetch_general_news()
        return analyze_news(items)
