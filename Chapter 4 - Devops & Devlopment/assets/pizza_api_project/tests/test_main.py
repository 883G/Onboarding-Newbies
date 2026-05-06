from unittest import mock

from fastapi.testclient import TestClient
from unittest.mock import patch
from pizza_api_project.main import app
from pizza_api_project.models.pizza import OrderRequest
from pizza_api_project.models.pizza_order import PizzaOrder

client = TestClient(app)


# Arrange
@patch('pizza_api_project.db_handler.database_orm.save_order_to_db', return_value=True)
def test_success_save_order_func(mock_save_order_to_db_func):
    order_data = {'customer_name': 'ofek', 'pizzas': [{"name": "Margherita", "price": 10.0}]}
    order_request: OrderRequest = OrderRequest(**order_data)
    pizza_order: PizzaOrder = PizzaOrder(order_request)
    # Assert
    assert pizza_order.save_order() is True


# Arrange
@patch('pizza_api_project.models.pizza_order.PizzaOrder.the_items_list_is_empty', return_value=True)
def test_fail_post_order_endpoint(mock_order) -> None:
    # Act
    response = client.post("/orders", json={'customer_name': 'ofek', 'pizzas': []})
    # Assert
    assert response.status_code == 400


# Arrange
@patch('pizza_api_project.models.pizza_order.PizzaOrder.the_items_list_is_empty', return_value=False)
def test_success_post_order_endpoint(mock_order) -> None:
    # Act
    response = client.post("/orders", json={'customer_name': 'ofek', 'pizzas': [{"name": "Margherita", "price": 10.0}]})
    # Assert
    assert response.status_code == 200


def test_get_menu() -> None:
    # Act
    response = client.get("/menu")
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]["name"] == "Margherita"

