from fastapi import FastAPI

from pizza_api_project.models.pizza import PizzaItem
from pizza_api_project.models.pizza_order import PizzaOrder
from pizza_api_project.routers import orders

app = FastAPI(title="Pizza Delivery API")

app.include_router(orders.router)


@app.get("/")
def root():
    return {"message": "Welcome to the Pizza API"}


def main():
    item = {"name": "cornpizza", "price": "4.5"}
    items = []
    pizzaitem1 = PizzaItem(**item)
    pizzaitem2 = PizzaItem(**item)
    items.append(pizzaitem1)
    items.append(pizzaitem2)
    pizza_order = PizzaOrder("ofek", items)
    print(str(pizza_order.order_id), pizza_order.items, pizza_order.customer_name)


if __name__ == "__main__":
    main()
