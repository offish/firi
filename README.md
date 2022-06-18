# Firi
[![Version](https://img.shields.io/pypi/v/firi.svg)](https://pypi.org/project/firi)
[![Stars](https://img.shields.io/github/stars/offish/firi.svg)](https://github.com/offish/firi/stargazers)
[![Issues](https://img.shields.io/github/issues/offish/firi.svg)](https://github.com/offish/firi/issues)
[![Size](https://img.shields.io/github/repo-size/offish/firi.svg)](https://github.com/offish/firi)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python package for interacting with [Firi](https://firi.com/affiliate/?referral=01f67b69)'s [API](https://developers.firi.com/#/).

Non-refferal link [here](https://firi.com).

**THIS PACKAGE DOES NOT CURRENTLY SUPPORT PRIVATE ENDPOINTS.**

## Installation
Install and update using pip
```text
pip install --upgrade firi
```

## Usage
```python
>>> from firi import Firi, floatify, BITCOIN, XRP

>>> firi = Firi()

>>> firi.get_market(BITCOIN) # or get_prices(BTC) or "BTCNOK". Predefined tickers can be found in markets.py
{'last': '480408.40', 'high': '533400.00', 'change': '-7.77', 'low': '460000.00', 'volume': '46.86'}

>>> firi.get_markets() # or get_tickers()
[{'id': 'BTCNOK', 'last': '473000.20', 'high': '533400.00', 'change': '-9.25', 'low': '460000.00', 'volume': '47.21'}, ...]

>>> floatify(firi.get_market(XRP))
{'last': 9.4, 'high': 10.95, 'change': -14.16, 'low': 7.44, 'volume': 1291258.8}
```

## Documentation
Firi's official documentation can be found [here](https://developers.firi.com/#/README).

## Donate
BTC: 37hb1eSbodHcKBdH2RbVenbFhkVVGXG2z5

ETH: 0x7862b653d13f2e08df6ee129041511d01a3a0f59
