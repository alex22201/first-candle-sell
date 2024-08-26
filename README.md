# 🚀 First Candle Sell Script 🔥

## Overview

Welcome to **First Candle Sell Script**—a Python script designed to execute precise limit sell orders on the **first candle** after a new listing! Whether you're chasing early gains or looking to exit positions at peak moments, this bot leverages the power of `asyncio` and [CCXT](https://github.com/ccxt/ccxt) to ensure your trades are executed quickly and efficiently.

## Features

- **Listing Candle Strategy:** Automate your trading strategy to sell coins on the first candle immediately after a new listing.
- **Multi-Exchange Support:** Compatible with a wide range of cryptocurrency exchanges via the CCXT library.
- **Asynchronous Execution:** Uses Python's `asyncio` for fast, non-blocking operations during critical moments of a listing.
- **Highly Configurable:** Easily adjust trading parameters like symbol, amount, and price to tailor the bot to your specific needs during a listing event.

## Getting Started

### Prerequisites

Make sure you have the following installed before running the script:

- Python 3.7+
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/first-candle-sell-bot.git
    cd first-candle-sell-bot
    ```

2. **Install the required Python packages:**

    ```bash
    pip3 install -r requirements.txt
    ```

### Configuration

3. **Configure your environment:**

    Create a `.env` file in the project root and add your exchange API credentials along with the trading pair, amount, and price for the order:

    ```env
    EXCHANGE_NAME=binance
    API_KEY=your_api_key
    API_SECRET=your_api_secret
    PASSWORD=''
   

    PAIR_SYMBOL='DOGS/USDT'
    AMOUNT=50000
    PRICE=0.001
    ```

    - `EXCHANGE_NAME`: The name of the exchange you are trading on (e.g., `'binance'`).
    - `API_KEY`: Your API key for the exchange.
    - `API_SECRET`: Your API secret for the exchange.
    - `PAIR_SYMBOL`: The trading pair symbol (e.g., `'DOGS/USDT'`).
    - `AMOUNT`: The amount of the asset you wish to sell.
    - `PRICE`: The limit price at which you wish to sell the asset.

4. **Run the script:**

    Once your `.env` file is properly configured, you can run the script with:

    ```bash
    python3 main.py
    ```