from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

exchange_name = os.getenv('EXCHANGE_NAME').lower()
api_key = os.getenv('API_KEY')
api_secret = os.getenv('SECRET_KEY')
api_password = os.getenv('PASSWORD', '')

symbol = os.getenv('PAIR_SYMBOL', '')
amount = float(os.getenv('AMOUNT', ''))
price = float(os.getenv('PRICE', ''))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
