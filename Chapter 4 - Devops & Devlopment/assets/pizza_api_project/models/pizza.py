from pydantic import BaseModel, validator, model_validator
from typing import List

class PizzaItem(BaseModel):
    name: str
    price: float

    @validator("name")
    def name_cannot_contain_non_alphabetic_characters(cls, name: str):
        if not name.isalpha():
            raise ValueError("name cannot contain non alphabetic characters")
        return name.title()

    @validator("price")
    def name_cannot_contain_non_alphabetic_characters(cls, price: float):
        if price <= 0.0:
            raise ValueError("the price most be bigger than 0")
        return price


class OrderRequest(BaseModel):
    customer_name: str
    pizzas: List[PizzaItem]
