import requests

from testing_api.config.config import Config


class OrdersApi:

    def __init__(self):
        self.url = f"{Config.get_example_orders_config()[
            Config.stand
        ]['BASE_URL']}/orders"

    def post_orders(self, cookies, json):
        requests.post(cookies=cookies, url=self.url, json=json)
