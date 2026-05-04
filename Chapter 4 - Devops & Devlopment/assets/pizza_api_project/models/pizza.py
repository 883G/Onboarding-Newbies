from pydantic import BaseModel
from typing import List
import uuid
class PizzaItem(BaseModel):
    name: str
    price: float

class OrderRequest(BaseModel):
    customer_name: str
    pizzas: List[PizzaItem]
    order_id: uuid = uuid.uuid4()
