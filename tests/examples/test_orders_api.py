import requests
from pytest import mark
from testing_api.data_test_objects.templates.examples.orders import (OrdersTemplates)
from testing_api.tests.examples.examples_config_allure import ExampleOrders


class TestOrdersApi(ExampleOrders):
        @mark.critical
        @mark.smoke
        def test_create_order_success(self):
                url = f"{self.examples_config["BASE_URL"]}/orders"
                payload = OrdersTemplates
                response = requests.post(url, json=payload, cookies="")

                assert response.status_code == 201
                data = response.json()

                assert data.get("orderId") == payload["orderId"]
                assert data.get("items") == payload["items"]
                assert data.get("customerEmail") == payload["customerEmail"]
                assert data.get("deliveryAddress") == payload["deliveryAddress"]

"""
import requests
import pytest

BASE_URL = "http://example.com/api"  # замени на реальный адрес API

def test_create_order_success():
    url = f"{BASE_URL}/orders"
    payload = {
        "orderId": "123e4567-e89b-12d3-a456-426614174000",
        "items": [
            {
            "productId": "987e6543-e21b-32d3-a654-426614174999", "quantity": 2
            }
        ],
        "customerEmail": "test@example.com",
        "deliveryAddress": "123 Test St, Test City"
    }
    
    response = requests.post(url, json=payload)
    
    assert response.status_code == 201
    data = response.json()
    
    assert "orderId" in data
    assert data["orderId"] == payload["orderId"]
    assert "items" in data
    assert data["items"] == payload["items"]
    assert "customerEmail" in data
    assert data["customerEmail"] == payload["customerEmail"]
    assert "deliveryAddress" in data
    assert data["deliveryAddress"] == payload["deliveryAddress"]"""