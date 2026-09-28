from dataclasses import dataclass

@dataclass
class RiskLimits:
    max_daily_loss: float = 0.03
    max_drawdown: float = 0.10
    max_position_fraction: float = 0.20

class RiskEngine:
    def __init__(self, limits: RiskLimits | None = None):
        self.limits = limits or RiskLimits()
        self.start_balance = None
        self.peak_balance = None

    def check(self, balance: float, daily_pnl: float, position_value: float) -> dict:
        if self.start_balance is None:
            self.start_balance = balance
            self.peak_balance = balance
        self.peak_balance = max(self.peak_balance, balance)
        drawdown = 1 - balance / self.peak_balance if self.peak_balance else 0.0
        daily_loss = max(0.0, -daily_pnl / self.start_balance) if self.start_balance else 0.0
        position_fraction = abs(position_value) / balance if balance else 1.0
        blocked = daily_loss > self.limits.max_daily_loss or drawdown > self.limits.max_drawdown or position_fraction > self.limits.max_position_fraction
        return {"allowed": not blocked, "daily_loss": daily_loss, "drawdown": drawdown, "position_fraction": position_fraction}
