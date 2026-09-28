"""Conservative automatic analysis of RSS headlines."""
import re

POSITIVE = {"growth","beats","surge","strong","approval","record","recovery","upgrade"}
NEGATIVE = {"drop","crisis","warning","lawsuit","sanctions","war","recession","downgrade","default"}

def analyze(item):
    words=set(re.findall(r"[a-z]+", item.title.lower()))
    pos=len(words & POSITIVE)
    neg=len(words & NEGATIVE)
    score=pos-neg
    sentiment="neutral" if score==0 else ("positive" if score>0 else "negative")
    return {
        "source":item.source,
        "title":item.title,
        "url":item.url,
        "sentiment":sentiment,
        "score":score,
        "confidence":min(1.0,(pos+neg)/3),
    }

def analyze_all(items):
    return [analyze(x) for x in items if not x.title.startswith("FEED_ERROR:")]
