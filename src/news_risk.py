"""Convert aggregated news into a conservative trading-risk context."""

def risk_context(analyses):
    if not analyses:
        return {"risk_level":"unknown","direction_bias":0.0,"trade_allowed":False}
    scores=[x["score"] for x in analyses]
    avg=sum(scores)/len(scores)
    negative=sum(x["sentiment"]=="negative" for x in analyses)
    positive=sum(x["sentiment"]=="positive" for x in analyses)
    if negative >= max(5, positive*2):
        level="high"
    elif negative > positive:
        level="elevated"
    else:
        level="normal"
    return {
        "risk_level":level,
        "direction_bias":round(max(-1.0,min(1.0,avg/3)),3),
        "trade_allowed":level != "high",
    }
