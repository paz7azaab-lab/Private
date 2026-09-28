def walk_forward(series, train_size, test_size, evaluator):
    """Evaluate each test window using only the preceding training window."""
    results=[]
    i=train_size
    while i < len(series):
        train=series[i-train_size:i]
        test=series[i:i+test_size]
        results.append(evaluator(train, test))
        i += test_size
    return results
