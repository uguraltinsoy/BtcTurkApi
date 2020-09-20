# BtcTurkApi

[![Build versiyon](https://img.shields.io/badge/pypi-0.0.4-brightgreen.svg)](https://pypi.org/project/BtcTurkApi)

[![Build versiyon](https://img.shields.io/badge/license-mit-lightgrey.svg)](https://pypi.org/project/BtcTurkApi)

[![Build versiyon](https://img.shields.io/badge/python-2.7%2C3.5%2C3.6-blue.svg)](https://pypi.org/project/BtcTurkApi)

## Installation

```
pip install BtcTurkApi
```
## Usage

### BtcTurk Symbols
	- TRY
	- USDT
	- BTC

### BtcTurk Pair Symbols

	- BTC_TRY
	- DASH_TRY
	- EOS_TRY
	- ETH_TRY
	- LINK_TRY
	- LTC_TRY
	- NEO_TRY
	- USDT_TRY
	- XLM_TRY
	- XRP_TRY
	- ATOM_TRY
	- XTZ_TRY
	- BTC_USDT
	- DASH_USDT
	- EOS_USDT
	- ETH_USDT
	- LINK_USDT
	- LTC_USDT
	- NEO_USDT
	- XLM_USDT
	- XRP_USDT
	- XTZ_USDT
	- ATOM_USDT
	- DASH_BTC
	- EOS_BTC
	- ETH_BTC
	- LINK_BTC
	- LTC_BTC
	- NEO_BTC
	- XLM_BTC
	- XRP_BTC
	- XTZ_BTC
	- ATOM_BTC

### Public Endpoint Methods
```python
from btcturkapi import BtcTurk

client = BtcTurk()
```

### Ticker
```python
client.ticker()
```

### Ticker Currency
```python
client.ticker_currency("USDT")
```

### Get Order Book
```python
client.get_order_book("BTC_TRY")
```

### Get All Trades
```python
client.get_all_trades("BTC_TRY")
```

### Get Last Trades
```python
client.get_last_trades("BTC_TRY","10")
```

### Get Last Ohcl
```python
client.get_all_ohcl("BTC_TRY")
```

### Private Endpoint Methods
```python
from btcturkapi import BtcTurk

client = BtcTurk("Your Api Key","Your Secret Key")
```

### Get Balances
```python
client.get_balances()
```

### Get Transactions
```python
client.get_transactions()
```

### Get Open Order
```python
client.get_open_order(pair_symbol)
```

### Cancel Order
```python
client.cancel_order(order_id)
```

### Market Sell
```python
client.market_sell(pair_symbol, quantity)
```

### Market Buy
```python
client.market_buy(pair_symbol, quantity)
```

### Limit Sell
```python
client.limit_sell(pair_symbol, quantity, price)
```

### Limit Buy
```python
client.limit_buy(pair_symbol, quantity, price)
```

### Stop Sell
```python
client.stop_sell(pair_symbol, quantity, price, stop_price)
```

### Stop Buy
```python
client.stop_buy(pair_symbol, quantity, price, stop_price)
```