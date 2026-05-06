from unittest import mock

from fastapi.testclient import TestClient
from unittest.mock import patch, Mock

import pizza_api_project.db_handler.database_orm
import pizza_api_project.models.pizza
from pizza_api_project.main import app
from pizza_api_project.models.pizza import OrderRequest
from pizza_api_project.models.pizza_order import PizzaOrder

client = TestClient(app)


def test_save_order_to_db():
    with patch.object(PizzaOrder, 'save_order', return_value=True):
        order_data = {'customer_name': 'ofek', 'pizzas': [{"name": "Margherita", "price": 10.0}]}
        assert pizza_api_project.db_handler.database_orm.save_order_to_db(order_data) is True


# ==========================================
# TODO: WRITE TESTS FOR THE POST ENDPOINT
# ==========================================

# Example of what is needed:
# @patch('main.save_order_to_db')
# def test_create_order_success(mock_save_db):
#     # 1. Arrange: setup mock return value and payload
#     # 2. Act: send POST request to /orders
#     # 3. Assert: check status code, response data, and that mock was called
#     pass

def test_create_order_empty_list(mocker):
    # mock_send_order = mocker.Mock()
    # mock_send_order.
    # order_request: OrderRequest = OrderRequest(customer_name='ofek', pizzas=[])
    # assert len(order_request.pizzas) == 0
    # asser
    """TODO: Test that sending an order with no pizzas returns a 400 error."""
    pass
