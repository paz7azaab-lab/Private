"""Global news engine interface for the trading agent.

This module is designed for live news ingestion. It deliberately keeps
news as a risk/context signal rather than treating headlines as guaranteed
trade predictors.
"""

from dataclasses import dataclass
from typing import Iterable


@dataclass
class NewsItem:
    title: str
    source: str
    published_at: str
    region: str = ""
    category: str = ""


@dataclass
class NewsSignal:
    score: float
    confidence: float
    reason: str


def analyze_news(items: Iterable[NewsItem]) -> NewsSignal:
    items = list(items)
    if not items:
        return NewsSignal(0.0, 0.0, "No news data available.")

    # Placeholder until a verified live-news provider and NLP model are connected.
    return NewsSignal(
        score=0.0,
        confidence=0.0,
        reason=f"Received {len(items)} news item(s); live sentiment model not connected yet."
    )
