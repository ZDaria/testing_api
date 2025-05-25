from allure import epic, feature
from pytest import mark

from testing_api.config.config import Config
from testing_api.tests.base_test import BaseTest


@mark.examples
@epic("")
class Examples(BaseTest):
    pass


@mark.example_orders
@feature("")
class ExampleOrders(Examples):
    examples_config = Config.get_example_orders_config()
