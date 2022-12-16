import logging

import requests

from .exceptions import CannotGetPrice

logger = logging.getLogger(__name__)


class GateIOClient:
    def __init__(self):
        self.http_session = requests.Session()

    def _get_price(self, symbol: str) -> float:
        url = f"https://api.gateio.ws/api/v4/spot/candlesticks/?interval=15m&limit=1&currency_pair={symbol}"
        try:
            response = self.http_session.get(url, timeout=10)
            api_json = response.json()
            result = api_json[0]
            price = float(result[2])
            return price
        except (ValueError, IOError) as e:
            raise CannotGetPrice from e

    def get_fra_usd_price(self) -> float:
        return self._get_price("FRA_USDT")
