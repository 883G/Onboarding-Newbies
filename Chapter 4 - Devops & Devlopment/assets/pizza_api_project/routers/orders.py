from typing import List

import uvicorn
from fastapi import APIRouter, HTTPException
from pizza_api_project.models.pizza import PizzaItem, OrderRequest
from pizza_api_project.models.pizza_order import PizzaOrder

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
    if len(order.pizzas).__eq__(0):
        raise HTTPException(status_code=400, detail="Items list id empty")
    else:
        pizza_order: PizzaOrder = PizzaOrder(order)
        pizza_order.save_order()
        print(pizza_order.return_success_msg())
        return order
