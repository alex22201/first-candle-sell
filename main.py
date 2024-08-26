import asyncio

from src import initialize_exchange, main
from utils import (
    exchange_name,
    api_key,
    api_secret,
    api_password,
    symbol,
    amount,
    price,
    logger
)


def run_main():
    try:
        exchange = initialize_exchange(exchange_name, api_key, api_secret, api_password)
        asyncio.run(main(exchange, symbol, amount, price))
    except KeyboardInterrupt:
        logger.info('Script interrupted by user.')
    finally:
        logger.info('Script finished.')


if __name__ == "__main__":
    run_main()
