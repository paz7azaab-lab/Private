from src.agent_core import TradingAgent

def test_agent_decision_and_audit():
    a=TradingAgent(10000)
    r=a.decide([0.01,0.012,0.009],[0.7,0.8,0.6],news_items=[])
    assert r["mode"]=="paper"
    assert r["decision"]=="HOLD"  # unknown/empty news blocks the decision
    assert len(a.state.audit)==1

def test_status():
    a=TradingAgent()
    s=a.status()
    assert s["mode"]=="paper"
