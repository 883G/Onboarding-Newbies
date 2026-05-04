
from fastapi import FastAPI
import uvicorn
from pizza_api_project.models.pizza import PizzaItem, OrderRequest
from pizza_api_project.routers import orders
from pizza_api_project.routers.orders import create_order

app = FastAPI(title="Pizza Delivery API")
app.include_router(orders.router)

def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    item = {"name": "cornpizza", "price": "4.5"}
    items: PizzaItem = []
    pizzaitem1 = PizzaItem(**item)
    pizzaitem2 = PizzaItem(**item)
    items.append(pizzaitem1)
    items.append(pizzaitem2)
    order_data = {"customer_name": "ofek", "pizzas": items}
    order_request: OrderRequest = OrderRequest(**order_data)
    create_order(order_request)


if __name__ == "__main__":
    main()

@app.get("/")
def root():
    return {"message": "Welcome to the Pizza API"}

