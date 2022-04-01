from .endpoints import *
from .utils import *


class Firi:
    def get_time(self) -> dict:
        return get_request(TIME).get("time")

    def get_all_markets(self) -> dict:
        return get_request(MARKETS)

    def get_tickers(self) -> dict:
        return self.get_markets()

    @types(object, str)
    def get_market(self, market: str) -> dict:
        return get_request(MARKET, market)

    @types(object, str)
    def get_prices(self, market: str) -> dict:
        return self.get_market(market)

    @types(object, str, int)
    def get_market_history(self, market: str, count: int = 0) -> dict:
        payload = {"count": count} if count else {}
        return get_request(HISTORY, market, payload=payload)

    @types(object, str)
    def get_orderbook(self, market: str) -> dict:
        return get_request(ORDERBOOKS, market)

    def get_orderbooks(self, market: str) -> dict:
        return self.get_orderbook(market)

    @types(object, str)
    def get_market_ticker(self, market: str) -> dict:
        return get_request(TICKER, market)

    def get_values(self, market: str, *args) -> list:
        data = self.get_market(market)
        return [data.get(arg) for arg in args]

    @types(object, str, str)
    def get_value(self, market: str, value: str) -> str:
        return self.get_market(market).get(value)

    def get_markets(self, *args) -> list:
        data = self.get_all_markets()
        return [i for i in data if i["id"] in args]

    @staticmethod
    def get_single_value(method, market: str, value: str):
        return method(market).get(value)