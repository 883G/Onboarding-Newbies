from unittest.mock import patch, Mock

from fastapi import HTTPException

import pizza_api_project
import pizza_api_project.db_handler.database_orm
from pizza_api_project.models.pizza import OrderRequest
from pizza_api_project.models.pizza_order import PizzaOrder
from pizza_api_project.routers.orders import create_order
from pizza_api_project.tests.test_main import client


def test_get_menu() -> None:
    response = client.get("/menu")
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]["name"] == "Margherita"

#def test_post_order_endpoint():
 #   mock_order_request = Mock()
  #  mock_order_request.the_items_list_is_empty = Mock(return_value=True)
   # assert create_order(mock_order_request) ==

