"""Live-news provider adapters.

Finnhub is supported as the initial provider. API credentials must be supplied
through the runtime environment; they are never committed to GitHub.
"""

import os
from dataclasses import asdict
from typing import List
from .news_engine import NewsItem

try:
    import requests
except ImportError:
    requests = None


class FinnhubNewsProvider:
    BASE_URL = "https://finnhub.io/api/v1"

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.getenv("FINNHUB_API_KEY")

    def fetch_general_news(self, category: str = "general", limit: int = 50) -> List[NewsItem]:
        if requests is None:
            raise RuntimeError("Install requests before using the live provider.")
        if not self.api_key:
            raise RuntimeError("FINNHUB_API_KEY is not configured.")

        response = requests.get(
            f"{self.BASE_URL}/news",
            params={"category": category, "token": self.api_key},
            timeout=10,
        )
        response.raise_for_status()

        items = []
        for item in response.json()[:limit]:
            items.append(
                NewsItem(
                    title=item.get("headline", ""),
                    source=item.get("source", ""),
                    published_at=str(item.get("datetime", "")),
                    region="global",
                    category=category,
                )
            )
        return items
