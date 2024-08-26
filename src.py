import asyncio

import ccxt
from ccxt import Exchange

from utils import logger


async def place_order(exchange: Exchange, symbol: str, amount: float, price: float) -> None:
    try:
        order = exchange.create_limit_sell_order(symbol, amount, price)
        print(f'Order placed: {order}')
    except ccxt.NetworkError as e:
        logger.error(f'Network error while placing order: {e}')
    except ccxt.ExchangeError as e:
        logger.error(f'Exchange error while placing order: {e}')
    except Exception as e:
        logger.error(f'Unexpected error: {e}')


async def main(exchange: Exchange, symbol: str, amount: float, price: float) -> None:
    while True:
        await place_order(exchange, symbol, amount, price)
        await asyncio.sleep(0.01)  # set delay


def initialize_exchange(exchange_name: str, api_key: str, api_secret: str, api_password: str = None) -> Exchange:
    exchange_class = getattr(ccxt, exchange_name)
    exchange = exchange_class({
        'apiKey': api_key,
        'secret': api_secret,
        'password': api_password
    })
    return exchange
