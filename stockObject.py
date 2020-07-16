from paper_config import *
import requests, json
import alpaca_trade_api as tradeapi

# On paper account reset it also resets Keys

BASE_URL = "https://paper-api.alpaca.markets"
# TODO: Decide when we want to buy (ceiling and floor)
# TODO: Pick an amount we want to play with (EX: $5000)
# TODO: Type of order for our sale (rn its good till end of day)
# TODO: Last Trade or Last Quote, need to decide how to set our buy limit price

# Temp ceiling and floor for the sweet spot
ceiling = 400
floor = 300

# Amount variable is the amount you are willing to spend
amount = 5000


class stock:
    def __init__(self):
        self.alpaca = tradeapi.REST(paper_id, paper_secret, BASE_URL)

    # Sends a buy
    def buy(self, symbol, qty, side, type, limit_price, time_in_force):
        self.alpaca.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type=type,
            limit_price=limit_price,
            time_in_force=time_in_force
        )

    # Sends a sell
    def sell(self, symbol, qty, side, type, time_in_force, limit_price, stop_loss):
        self.alpaca.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type=type,
            time_in_force=time_in_force,
            limit_price=limit_price,
            stop_loss=stop_loss
        )

    # Cancels the trade of a specific order
    def cancel(self, order_id):
        self.alpaca.cancel_order(order_id)

    # Cancels all outstanding trades
    def all_cancel(self):
        self.alpaca.cancel_all_orders()

    # Grabs the account buying power
    def account_balance(self):
        r = self.alpaca.get_account()
        print(r.buying_power)

    # Grabs the price of the last trade [returns float w/ 2 decimals]
    def last_trade(self, symbol):
        lt = self.alpaca.get_last_trade(symbol)
        print(lt)
        print(type(lt))
        return lt.price

    # Computes the var(qty) of shares to buy to get var(amount) of stock [returns int]
    def qty(self, amount, price):
        qty = round(amount / price)
        return qty

    def spot_check(self, symbol):
        while True:
            price = self.last_trade(symbol)
            qty = self.qty(amount, price)
            if price > floor and price < ceiling:
                r = self.buy(symbol, qty, "buy", "limit", price,
                             "fok")  # fok is fill or kill order is fully filled of cancelled
                try:
                    self.position(symbol)
                    self.sell(symbol, qty, "sell", "limit", "gtc", (price * 1.0002),
                              (price * 0.9999))  # gtc is good till close
                    break
                except requests.exceptions.HTTPError:
                    print("No Postions in" + symbol)

    def position(self, symbol):
        print(self.alpaca.get_position(symbol))


investment = stock()
investment.account_balance()
lt = investment.last_trade("WKHS")
investment.absolute_value(lt)
# investment.buy("WKHS", 100, "buy", price, "limit", "fok") #(symbol, qty, side, type, limit_price, time_in_force)
# investment.position("RCL")
print("hello world")


