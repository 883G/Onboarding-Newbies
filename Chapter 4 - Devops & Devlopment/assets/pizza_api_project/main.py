from typing import Any

from fastapi import FastAPI

from pizza_api_project.models.pizza import PizzaItem, OrderRequest
from pizza_api_project.routers import orders

app = FastAPI(title="Pizza Delivery API")

app.include_router(orders.router)


@app.get("/")
def root():
    return {"message": "Welcome to the Pizza API"}


def main():
    item = {"name": "cornpizza", "price": "4.5"}
    items: PizzaItem = []
    pizzaitem1 = PizzaItem(**item)
    pizzaitem2 = PizzaItem(**item)
    items.append(pizzaitem1)
    items.append(pizzaitem2)
    order_data = {"customer_name": "ofek", "pizzas": items}
    order_request: OrderRequest = OrderRequest(**order_data)
    print(order_request)

if __name__ == "__main__":
    main()
