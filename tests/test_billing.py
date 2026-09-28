from decimal import Decimal

from src.billing import record_fee
from src.subscription import calculate_platform_fee


def test_two_percent_fee():
    assert calculate_platform_fee(Decimal("1000"), "fee") == Decimal("20.00")


def test_record_fee():
    record = record_fee("user-1", "trade-1", Decimal("250"))
    assert record.platform_fee == Decimal("5.00")
