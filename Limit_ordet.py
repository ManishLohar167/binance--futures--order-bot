import logging
from binance.client import Client
from binance.enums import *

logging.basicConfig(filename='../bot.log', level=logging.INFO)

class LimitOrder:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logging.info(f"Limit order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing limit order: {e}")
            return None
