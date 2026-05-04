from typing import List

from pizza_api_project.models.order import Order
from pizza_api_project.models.pizza import PizzaItem


class PizzaOrder(Order):

    def __init__(self, customer_name: str, pizzas: List[PizzaItem]):
        super().__init__(customer_name, pizzas)

    def save_order(self, order_data: dict):
        pass

    def print_success_msg(self):
        pass

    def calc_total_price(self):
        total_price: float = 0
        for pizza in self.items:
            total_price += pizza.price
        return total_price

