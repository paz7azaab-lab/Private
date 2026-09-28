def ensemble(signals, weights=None):
    if not signals:
        return 0.0
    if weights is None:
        weights=[1/len(signals)]*len(signals)
    total=sum(weights)
    if total<=0 or len(weights)!=len(signals):
        raise ValueError("invalid weights")
    return sum(s*w for s,w in zip(signals,weights))/total
