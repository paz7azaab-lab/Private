def confidence(signal_score, news_score=0.0, regime_alignment=0.0):
    """Return a bounded 0..1 confidence score; it is not a profit guarantee."""
    raw=0.6*signal_score + 0.2*news_score + 0.2*regime_alignment
    return max(0.0, min(1.0, (raw+1)/2))
