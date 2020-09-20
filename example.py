from btcturkapi import BtcTurk

#Public Methods
client = BtcTurk()
print(client.ticker())
print(client.ticker_currency("USDT"))
print(client.get_order_book("BTC_TRY"))
print(client.get_all_trades("BTC_TRY"))
print(client.get_last_trades("BTC_TRY","10"))
print(client.get_all_ohcl("BTC_TRY"))

#Private Method
client = BtcTurk("Your Api Key","Your Secret Key")
print(client.get_balances())
print(client.get_transactions())
print(client.get_open_order("BTC_TRY"))
print(client.cancel_order("orderID"))
print(client.market_sell("BTC_TRY","001"))
print(client.market_buy("BTC_TRY","001"))
print(client.limit_sell("BTC_TRY","001","19000"))
print(client.limit_buy("BTC_TRY","001","19000"))
print(client.stop_sell("BTC_TRY","001","19000","19010"))
print(client.stop_buy("BTC_TRY","001","19000","19110"))

