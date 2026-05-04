from abc import ABC, abstractmethod
import uuid
from typing import List, Any


class CreateOrder(ABC):
    @abstractmethod
    def calc_total_price(self):
        pass

    @abstractmethod
    def save_order(self):
        pass

    @abstractmethod
    def return_success_msg(self):
        pass


class Order(CreateOrder, ABC):
    customer_name: str
    items: List[Any]
    order_id: uuid

    def __init__(self, customer_name: str, items: List[Any]):
        self.customer_name = customer_name
        self.items = items
        self.order_id = uuid.uuid4()
