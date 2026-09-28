from dataclasses import dataclass

@dataclass
class BacktestResult:
    final_balance: float
    return_pct: float
    max_drawdown: float
    trades: int


def run_backtest(returns, starting_balance=10000.0, fee_rate=0.0, slippage_rate=0.0):
    balance = starting_balance
    peak = balance
    max_dd = 0.0
    trades = 0
    for r in returns:
        trades += 1
        net = r - fee_rate - slippage_rate
        balance *= 1 + net
        peak = max(peak, balance)
        max_dd = max(max_dd, 1 - balance / peak)
    return BacktestResult(balance, balance / starting_balance - 1, max_dd, trades)
