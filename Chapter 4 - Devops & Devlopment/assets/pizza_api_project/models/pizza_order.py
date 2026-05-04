
from pizza_api_project.db_handler.database_orm import save_order_to_db
from pizza_api_project.models.order import Order
from pizza_api_project.models.pizza import PizzaItem, OrderRequest


class PizzaOrder(Order):

    def __init__(self, order_request: OrderRequest):
        super().__init__(order_request.customer_name, order_request.pizzas)

    def save_order(self):
        save_order_to_db(self.__dict__)

    def return_success_msg(self) -> str:
        return "the order: ", self.order_id, "is success! ", "the total price is: ", self.calc_total_price()

    def calc_total_price(self):
        total_price: float = sum(pizza.price for pizza in self.items)
        return total_price
