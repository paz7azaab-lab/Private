def apply_costs(return_rate, fee_rate=0.0, slippage_rate=0.0):
    return return_rate - abs(fee_rate) - abs(slippage_rate)


def effective_fill(price, side, slippage_rate):
    return price*(1+slippage_rate) if side.lower()=="buy" else price*(1-slippage_rate)
