from src.backtest import run_backtest
from src.market_regime import detect_regime
from src.slippage import effective_fill
from src.strategy_ensemble import ensemble

def test_backtest():
    r=run_backtest([0.01,-0.005], fee_rate=0.001, slippage_rate=0.001)
    assert r.trades == 2

def test_regime():
    assert detect_regime([0.01,0.012,0.009]) == "bullish"

def test_slippage():
    assert effective_fill(100,"buy",0.01)==101

def test_ensemble():
    assert abs(ensemble([1,-1],[0.75,0.25])-0.5)<1e-9
