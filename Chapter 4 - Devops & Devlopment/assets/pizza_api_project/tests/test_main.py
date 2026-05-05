from fastapi.testclient import TestClient
from unittest.mock import patch

from pizza_api_project.main import app

client = TestClient(app)

def test_get_menu():
    response = client.get("/menu")
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]["name"] == "Margherita"

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

def test_create_order_empty_list():
    """TODO: Test that sending an order with no pizzas returns a 400 error."""
    pass
