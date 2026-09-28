# Trading Agent

Independent trading-agent project.

## Current scope
- Market-data analysis
- Technical indicators
- Signal generation
- Risk-management rules
- Paper-trading simulation
- Trade logging
- Subscription access control
- Paper billing ledger

## Monetization model
Users can choose either:
- Basic: $9.99/month
- Pro: $24.99/month
- Advanced: $49.99/month
- Fee-based: no monthly subscription, with a simulated 2% platform fee

A 7-day trial is configured.

## Safety and billing status
The project remains in paper-trading mode. Real-money trade execution and real-money payment collection are disabled. The billing layer currently calculates and records simulated amounts only; it does not transfer money to any account.

## Structure
- `src/` — agent logic, subscriptions, and paper billing
- `config/` — configuration and plans
- `tests/` — tests
- `data/` — local sample data
