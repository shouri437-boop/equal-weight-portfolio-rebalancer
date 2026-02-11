# equal-weight-portfolio-rebalancer
Python based backtesting engine comparing buy and  hold and equal weight portfolio rebalancing strategies with time series visualization.

# Equal-Weight Portfolio Rebalancer (Python)

## Overview
This project implements a Python-based portfolio backtesting system that compares a **Buy & Hold** strategy with an **Equal-Weight Rebalancing** strategy across multiple assets.

The system simulates price movements, tracks portfolio state (cash and shares), performs periodic rebalancing using current prices, and visualizes portfolio value over time.

---

## Key Features
- Synthetic multi-asset price generation (random walk)
- Buy & Hold baseline strategy
- Equal-weight portfolio rebalancing at fixed intervals
- Cash-aware trading (sell first, then buy)
- Integer share constraints with leftover cash handling
- Time-series portfolio valuation
- Side-by-side performance visualization

---

## Methodology

1. **Price Simulation**
   - Generated daily prices for 5 assets over 60 days
   - Prices evolve using small random percentage changes

2. **Buy & Hold Strategy**
   - Initial capital split equally across all assets
   - No rebalancing after initial allocation

3. **Equal-Weight Rebalancing Strategy**
   - Portfolio rebalanced at Day 20 and Day 40
   - Uses current-day prices
   - Sells overweight assets first, then buys underweight assets
   - Maintains integer share constraints

4. **Evaluation**
   - Portfolio value tracked daily
   - Final values and full performance curves compared

---

## Results
In the simulated environment, the equal-weight rebalancing strategy produced materially different outcomes compared to buy-and-hold, demonstrating the impact of systematic reallocation and risk control.

> Note: Since prices are randomly generated, absolute returns vary per run. The focus is on **strategy mechanics**, not prediction accuracy.

---

## Tech Stack
- Python
- Matplotlib
- Core Python data structures (lists, dictionaries)

---


