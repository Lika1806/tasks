import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mixins.list_viewer import ListViewer
from order_management.order_exceptions import MissigOrderError
from abc import ABC, abstractmethod
from mixins.item_getter import ItemGetterByID

    
class OrderOwner():
    def __init__(self) -> None:
        super().__init__()
        self._order_list = []
    
    def get_order_list(self):
        return self._order_list[:]
        
class OrderViewer(ListViewer, ItemGetterByID):
    _order_list = list()

    def view_order(self, order):
        order = self._get_item(order, self._order_list)
        if not order:
            raise MissigOrderError
        return f'order{order.item_id}\n{order.view_order_list()}'

    def view_orders(self):
        res = self.view_list(self._order_list, 'order list')
        return res
        
    
class OrderCreator(ABC):
    _order_list = list()
    def creat_order(self, *items):
        new_order = self.order_class(self, items)
        self._order_list.append(new_order)
        return new_order
    
    @property
    @abstractmethod
    def order_class(self):
        ...

class OrderManager(ABC,OrderOwner,ItemGetterByID):

    def add_to_order(self, order, *items):
        order = self._get_item(order, self._order_list)
        order.add_to_order(*items)

    def remove_from_order(self, order, *items):
        order = self._get_item(order,self._order_list)
        order.remove_from_order(*items)

    def cancel_order(self,order):
        order = self._get_item(order, self._order_list)
        order._cancel()
        self._remove_order(order)
    
    def _remove_order(self,order):
        self._order_list.remove(order)

    def pay(self, order):
        order = self._get_item(order, self._order_list)
        if not self._check_payability(order):
            raise  
        new_purchase = order.pay()
        self._remove_order(order)
        return new_purchase
    
    @abstractmethod
    def _check_payability(self, value):
        ...

