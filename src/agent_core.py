"""Unified paper-trading AI agent orchestrator.

The agent combines market input, RSS news context, signal scoring,
risk controls, cost simulation, anomaly checks and an audit trail.
It never places real-money orders.
"""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from .market_regime import detect_regime
from .signal_confidence import confidence
from .strategy_ensemble import ensemble
from .risk_engine import RiskEngine
from .anomaly_detector import detect_anomaly
from .slippage import apply_costs
from .news_risk import risk_context
from .news_analysis import analyze_all
from .rss_news import collect_all

@dataclass
class AgentState:
    balance: float = 10000.0
    position_value: float = 0.0
    daily_pnl: float = 0.0
    last_decision: str = "HOLD"
    audit: list = field(default_factory=list)

class TradingAgent:
    def __init__(self, starting_balance=10000.0, risk_engine=None):
        self.state=AgentState(balance=starting_balance)
        self.risk= risk_engine or RiskEngine()

    def decide(self, returns, signal_scores, position_value=0.0, news_items=None):
        returns=list(returns)
        signal_scores=list(signal_scores)
        regime=detect_regime(returns)
        market_signal=ensemble(signal_scores) if signal_scores else 0.0
        if news_items is None:
            news_items=collect_all()
        analyses=analyze_all(news_items)
        news=risk_context(analyses)
        regime_alignment=1.0 if ((regime=="bullish" and market_signal>0) or (regime=="bearish" and market_signal<0)) else 0.0
        conf=confidence(max(-1,min(1,market_signal)), news.get("direction_bias",0.0), regime_alignment)
        anomaly=detect_anomaly(returns)
        risk=self.risk.check(self.state.balance,self.state.daily_pnl,position_value)
        allowed=risk["allowed"] and news.get("trade_allowed",False) and not anomaly
        if not allowed:
            decision="HOLD"
        elif market_signal>0.25 and conf>=0.65:
            decision="WATCH_LONG"
        elif market_signal<-0.25 and conf>=0.65:
            decision="WATCH_SHORT"
        else:
            decision="HOLD"
        event={"timestamp":datetime.now(timezone.utc).isoformat(),"decision":decision,"regime":regime,"signal":market_signal,"confidence":conf,"news_risk":news.get("risk_level"),"anomaly":anomaly,"risk":risk,"mode":"paper"}
        self.state.last_decision=decision
        self.state.position_value=position_value
        self.state.audit.append(event)
        return event

    def simulate_fill(self, price, side, expected_return, fee_rate=0.0, slippage_rate=0.0):
        net=apply_costs(expected_return,fee_rate,slippage_rate)
        return {"mode":"paper","price":price,"side":side,"expected_return":expected_return,"net_return":net}

    def status(self):
        return {"mode":"paper","balance":self.state.balance,"position_value":self.state.position_value,"last_decision":self.state.last_decision,"audit_events":len(self.state.audit)}
