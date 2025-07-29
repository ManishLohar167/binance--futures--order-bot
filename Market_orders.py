import logging
from binance.client import Client
from binance.enums import *

# Initialize logger
logging.basicConfig(filename='../bot.log', level=logging.INFO)

class MarketOrder:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"Market order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing market order: {e}")
            return None
