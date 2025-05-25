import requests
from pytest import mark
from testing_api.data_test_objects.templates.examples.orders import OrdersTemplates
from testing_api.tests.examples.examples_config_allure import ExampleOrders


class TestOrdersApi(ExampleOrders):
        @mark.critical
        @mark.smoke
        def test_create_order_success(self):
                url = f"{BASE_URL}/orders"
                payload = OrdersTemplates
                response = requests.post(url, json=payload)

                assert response.status_code == 201
                data = response.json()

                assert data.get("orderId") == payload["orderId"]
                assert data.get("items") == payload["items"]
                assert data.get("customerEmail") == payload["customerEmail"]
                assert data.get("deliveryAddress") == payload["deliveryAddress"]