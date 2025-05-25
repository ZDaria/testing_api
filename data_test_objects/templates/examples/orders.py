import uuid
from testing_api.config.config import Config


class OrdersTemplates:
    @staticmethod
    def get_order_template() -> dict:
        """Метод для получения тела запроса о заказе"""
        return {
            "orderId": uuid.uuid4(),
            "items": [],
            "customerEmail": "test@example.com",
            "deliveryAddress": "123 Test St, Test City"
        }

    @staticmethod
    def get_order_item_template() -> dict:
        """Метод для получения тела запроса о продукте"""
        return {
            "productId":
                Config.get_example_orders_config()[Config.stand]["PRODUCT_ID"],
            "quantity": 1
        }
