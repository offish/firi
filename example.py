from firi import Firi, RIPPLE, XRP, BITCOIN, floatify

firi = Firi()

print(firi.get_time())
print(firi.get_all_markets())
print(firi.get_tickers())
print(firi.get_market("XRPNOK"))
print(floatify(firi.get_market("xrpnok")))
print(firi.get_market_history(RIPPLE, 2))
print(firi.get_orderbook(XRP))
print(firi.get_orderbooks("BTCNOK"))
print(firi.get_market_ticker(BITCOIN))
print(firi.get_values("BTCNOK", "low", "high", "last"))
print(firi.get_markets("BTCNOK", "XRPNOK"))
print(firi.get_single_value(firi.get_market_ticker, "BTCNOK", "bid"))