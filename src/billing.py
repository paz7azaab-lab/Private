"""Paper billing ledger.

Records what would be owed to the platform without charging cards,
moving funds, or connecting to a brokerage.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal


@dataclass
class FeeRecord:
    user_id: str
    trade_id: str
    trade_value: Decimal
    fee_rate: Decimal
    platform_fee: Decimal
    created_at: str


def record_fee(user_id: str, trade_id: str, trade_value: Decimal, fee_rate: Decimal = Decimal("0.02")) -> FeeRecord:
    if trade_value < 0:
        raise ValueError("trade_value cannot be negative")
    fee = (trade_value * fee_rate).quantize(Decimal("0.01"))
    return FeeRecord(
        user_id=user_id,
        trade_id=trade_id,
        trade_value=trade_value,
        fee_rate=fee_rate,
        platform_fee=fee,
        created_at=datetime.now(timezone.utc).isoformat(),
    )
