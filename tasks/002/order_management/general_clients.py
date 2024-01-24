import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import abs_persons as persons
from sales_management.abs_purchaser import Purcheser
from order_management.general_orders import Order
from order_management.orderer_mixins import OrderCreator, OrderManager, OrderViewer
from sales_management.sales_exceptions import NotEnoghtFundsError
from order_management.order_exceptions import MissigOrderError

class Orderer(OrderCreator, OrderManager, OrderViewer):
    ...

class Client(persons.PersonWithConacts, Orderer, Purcheser):
    role = 'client'
    def _get_item(self, item, _list):
        res = super()._get_item(item, _list)
        if not res:
            raise MissigOrderError
        return res
    
    def __init__(self, name: str, phone: str, email: str, budget = 0,currency = 'AMD') -> None:
        super().__init__(name, phone, email)
        if budget:
            self.increase_budget(budget)
        if currency:
            self.set_curreccy(currency)
            
    def _check_payability(self, item):
        if self.request_fund(item.total_price):
            return True
        raise NotEnoghtFundsError
    
    def __str__(self):
        return f'{self.role}: {self.name}'
    
    def view(self) -> str:
        return super().view() + self.view_budget() + '\n'
    
    def pay(self, order): 
        res =  super().pay(order)
        self.add_purchase(res)

    @property
    def order_class(self):
        return Order
    
    
if __name__=="__main__":
    client1 = Client('Anna', '099887766', 'aaa@gmail.com', budget = 120000)
    print(client1.__class__.__mro__)