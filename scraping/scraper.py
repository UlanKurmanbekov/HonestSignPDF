import httpx

from scraping.authenticator import Authenticator
from core.config import PRODUCT_URL, PRODUCT_TOKEN_TYPE


class ProductScraper:
    def __init__(self, authenticator: Authenticator):
        self.authenticator = authenticator

    def scrape(self, gtin: str) -> dict[str, any]:
        access_token = self.authenticator.authenticate()

        headers = {
            "Authorization": f"{PRODUCT_TOKEN_TYPE} {access_token}",
            "Content-Type": "application/json"
        }

        params = {
            "page": 0,
            "size": 10,
            "gtin": gtin,
            "gtinMatchType": "EQUAL"
        }

        response = httpx.get(PRODUCT_URL, headers=headers, params=params)
        response.raise_for_status()
        print(response)
        return response.json()
