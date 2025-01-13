# Trading Simulation Repository

This repository contains tools designed to assist with investments using the Korea Investment & Securities API. It includes scripts for stock analysis, backtesting, and automated trading simulation.

## File Descriptions

- **`backtest.ipynb`**: A Jupyter Notebook that generates and analyzes the 20-day (SMA20) and 60-day (SMA60) Simple Moving Averages (SMA) for a given stock. The simulation buys the stock when the SMA20 crosses above SMA60 (Golden Cross) and sells it when SMA20 crosses below SMA60 (Dead Cross).
  
- **`get_stock_info.py`**: This file uses the Korea Investment & Securities API to request and retrieve intraday stock data (minute-by-minute) for a specified stock, which is used for analysis in other parts of the project.

- **`get_token.py`**: A script that retrieves an access token from the Korea Investment & Securities API to authenticate requests and gain access to the API.

- **`stock_info(sample).json`**: A sample file containing 330 minutes of stock data (1-minute intervals). This is used to run simulations in `backtest.ipynb`. In real-world usage, the `get_stock_info.py` script should be run to generate this file dynamically from the Korea Investment & Securities API.

## Reference

- The tools in this repository are developed using the Korea Investment & Securities API, which helps automate investment processes and provides access to real-time stock data for analysis.
