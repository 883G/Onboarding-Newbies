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


class OrderRequest(BaseModel):
    customer_name: str
    pizzas: List[PizzaItem]
