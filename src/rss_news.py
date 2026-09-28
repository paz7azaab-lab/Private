"""API-key-free RSS news collector for the trading agent."""
import time
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass

DEFAULT_FEEDS = {
    "BBC World": "https://feeds.bbci.co.uk/news/world/rss.xml",
    "CNBC": "https://www.cnbc.com/id/100003114/device/rss/rss.html",
    "Yahoo Finance": "https://finance.yahoo.com/news/rssindex",
    "ECB": "https://www.ecb.europa.eu/rss/press.html",
}

@dataclass
class NewsItem:
    source: str
    title: str
    url: str
    published: str = ""

def fetch_feed(source, url, timeout=10):
    req = urllib.request.Request(url, headers={"User-Agent": "TradingAgent/1.0 RSS reader"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        root = ET.fromstring(response.read())
    items=[]
    for node in root.findall(".//item"):
        items.append(NewsItem(
            source=source,
            title=(node.findtext("title") or "").strip(),
            url=(node.findtext("link") or "").strip(),
            published=(node.findtext("pubDate") or "").strip(),
        ))
    return items

def collect_all(feeds=None):
    feeds = feeds or DEFAULT_FEEDS
    result=[]
    for source,url in feeds.items():
        try:
            result.extend(fetch_feed(source,url))
        except Exception as exc:
            result.append(NewsItem(source, f"FEED_ERROR: {exc}", ""))
    return result
