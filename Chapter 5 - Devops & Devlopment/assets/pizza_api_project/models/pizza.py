from pydantic import BaseModel
from typing import List

class PizzaItem(BaseModel):
    name: str
    price: float

class OrderRequest(BaseModel):
    customer_name: str
    pizzas: List[PizzaItem]
