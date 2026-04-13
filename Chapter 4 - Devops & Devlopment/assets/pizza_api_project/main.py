from fastapi import FastAPI
from routers import orders

app = FastAPI(title="Pizza Delivery API")

app.include_router(orders.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Pizza API"}
