def detect_regime(returns, volatility_threshold=0.02):
    if not returns:
        return "unknown"
    avg=sum(returns)/len(returns)
    vol=(sum((x-avg)**2 for x in returns)/len(returns))**0.5
    if vol >= volatility_threshold:
        return "high_volatility"
    if avg > 0.001:
        return "bullish"
    if avg < -0.001:
        return "bearish"
    return "sideways"
