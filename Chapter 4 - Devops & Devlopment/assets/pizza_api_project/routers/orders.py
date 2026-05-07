
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
    pizza_order: PizzaOrder = PizzaOrder(order)
    if pizza_order.the_items_list_is_empty():
        raise HTTPException(status_code=400, detail="Items list is empty")
    else:
        pizza_order.save_order()
        print(pizza_order.return_success_msg())
        return order
