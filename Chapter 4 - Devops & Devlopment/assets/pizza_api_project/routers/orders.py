from typing import List

from fastapi import APIRouter, HTTPException
from models.pizza import OrderRequest
from db_handler.database_orm import save_order_to_db

from pizza_api_project.models.pizza import PizzaItem

router = APIRouter()

@router.get("/menu")
def get_menu():
    return [
        {"name": "Margherita", "price": 10.0},
        {"name": "Pepperoni", "price": 12.5},
        {"name": "Vegan", "price": 11.0}
    ]

@router.post("/orders")
def create_order(order: OrderRequest):
    return order
    """
    TODO: INCOMPLETE ENDPOINT!
    1. Calculate total price.
    2. Call 'save_order_to_db(order_data)' to save it.
    3. Return a success message with the total price and an order ID.
    4. Handle cases where the pizza list is empty (raise 400 exception).
    """
    pass

def calc_total_price(pizzas: List[PizzaItem]) -> float:
    total_price: float = 0
    for pizza in pizzas:
        total_price += pizza.price
    return total_price
