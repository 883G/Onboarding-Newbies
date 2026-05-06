from pydantic import BaseModel, validator, model_validator
from typing import List

from conf import special_characters


class PizzaItem(BaseModel):
    name: str
    price: float

    @validator("name")
    def name_cannot_contain_non_alphabetic_characters(cls, name: str):
        if any(char in special_characters for char in name):
            raise ValueError("name cannot contain special characters")
        return name.title()

    @validator("price")
    def price_is_bigger_then_zero(cls, price: float):
        if price <= 0.0:
            raise ValueError("the price most be bigger than 0")
        return price


class OrderRequest(BaseModel):
    customer_name: str
    pizzas: List[PizzaItem]
