from abc import ABC, abstractmethod
import uuid
from typing import List, Any

from pizza_api_project.models.pizza import OrderRequest


class CreateOrder(ABC):
    @abstractmethod
    def calc_total_price(self):
        pass

    @abstractmethod
    def save_order(self, order_data: dict):
        pass

    @abstractmethod
    def print_success_msg(self):
        pass


class Order(CreateOrder, ABC):
    order_id: uuid
    customer_name: str
    items: List[Any]

