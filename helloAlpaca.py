import alpaca_trade_api as tradeapi
from keys import *

api = tradeapi.REST(idKey, secretKey, api_version='v2')
account = api.get_account()
api.list_positions()
print(account.status)


#200 requests per minute
#Convert numbers to strings

'''
Ways to specify the stock (in case multiple with same symbol)
- "{symbol}"
- "{symbol}:{exchange}"
- "{symbol}:{exchange}:{asset_class}"
- "{asset_id}"
'''
