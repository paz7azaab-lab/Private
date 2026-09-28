"""Command-line entry point for the unified paper-trading agent."""
from .agent_core import TradingAgent

def run(returns=None, signal_scores=None):
    agent=TradingAgent()
    result=agent.decide(returns or [0.001,0.002,-0.0005], signal_scores or [0.2,0.4,0.3])
    print("Trading agent initialized in PAPER mode.")
    print(result)
    return result

if __name__ == "__main__":
    run()
