from unittest.mock import patch

import pizza_api_project
import pizza_api_project.db_handler.database_orm
from pizza_api_project.models.pizza_order import PizzaOrder
from pizza_api_project.tests.test_main import client


def test_post_order() -> None:
    #response = client.post("/orders")
    #assert response.status_code == 400
    pass
def test_get_menu() -> None:
    response = client.get("/menu")
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]["name"] == "Margherita"

@patch('pizza_order.PizzaOrder')
def test_save_order_to_db_func(mock_save_order_to_db):
    mock_save_order_to_db.return_value = True
    order_data = {'customer_name': 'ofek', 'pizzas': [{"name": "Margherita", "price": 10.0}]}
    assert pizza_api_project.db_handler.database_orm.save_order_to_db(order_data) is True