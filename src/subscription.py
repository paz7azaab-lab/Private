"""Subscription and usage-plan logic for the trading-agent SaaS.

This module only manages access and simulated fee accounting.
It does not move money or execute real trades.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from decimal import Decimal


@dataclass(frozen=True)
class Plan:
    name: str
    monthly_price_usd: Decimal
    fee_rate: Decimal
    trial_days: int = 0


PLANS = {
    "free": Plan("free", Decimal("0"), Decimal("0")),
    "basic": Plan("basic", Decimal("9.99"), Decimal("0")),
    "pro": Plan("pro", Decimal("24.99"), Decimal("0")),
    "advanced": Plan("advanced", Decimal("49.99"), Decimal("0")),
    "fee": Plan("fee", Decimal("0"), Decimal("0.02")),
}


def trial_ends_at(started_at: datetime, days: int = 7) -> datetime:
    return started_at + timedelta(days=days)


def subscription_due(plan_name: str) -> Decimal:
    return PLANS[plan_name].monthly_price_usd


def calculate_platform_fee(trade_value: Decimal, plan_name: str) -> Decimal:
    """Calculate the platform fee for the fee-based plan only."""
    plan = PLANS[plan_name]
    if plan.fee_rate <= 0:
        return Decimal("0")
    if trade_value < 0:
        raise ValueError("trade_value cannot be negative")
    return (trade_value * plan.fee_rate).quantize(Decimal("0.01"))


def entitlement(plan_name: str) -> dict:
    if plan_name not in PLANS:
        raise ValueError(f"Unknown plan: {plan_name}")
    return {
        "plan": plan_name,
        "monthly_price_usd": str(PLANS[plan_name].monthly_price_usd),
        "fee_rate": str(PLANS[plan_name].fee_rate),
    }
